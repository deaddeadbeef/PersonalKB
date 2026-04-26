import os, re, time, glob, subprocess, tempfile, shutil, requests
from pathlib import Path

AUDIO_DIR = Path(r"D:\Vaults\PersonalKB\Japanese\_audio")
REPORT = AUDIO_DIR / "stt-spot-check-report.txt"
key = os.environ["AZURE_SPEECH_KEY"]
region = "japaneast"
STT_URL = f"https://{region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=ja-JP"

cats = {"core100":5,"hira":5,"kata":5,"verb":5,"greet":3,"adj":5,"kanjin5":3,"gap":5,"nontbl":5,"pitch":5,"particle":3,"daily":3}
samples = []
for pfx, cnt in cats.items():
    fs = sorted(glob.glob(str(AUDIO_DIR / f"{pfx}-*.mp3")))
    if fs:
        step = max(1, len(fs)//cnt)
        sel = fs[::step][:cnt]
        samples.extend(sel)
        print(f"  {pfx}: {len(sel)}/{len(fs)}")

print(f"Total: {len(samples)}")
tmpdir = tempfile.mkdtemp()
results = []

headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "audio/wav; codecs=audio/pcm; samplerate=16000",
    "Accept": "application/json",
}

for i, cp in enumerate(samples):
    cn = os.path.basename(cp)
    base = cn.replace(".mp3","")
    parts = base.split("-",1)
    pfx = parts[0]
    hint = parts[1] if len(parts)>1 else base
    hint = re.sub(r"^\d+[-_]?","",hint)
    try:
        # Convert MP3 to WAV in memory via ffmpeg
        wp = os.path.join(tmpdir, base+".wav")
        proc = subprocess.run(
            ["ffmpeg","-i",cp,"-ar","16000","-ac","1","-acodec","pcm_s16le",wp,"-y"],
            capture_output=True, timeout=10
        )
        if not os.path.exists(wp):
            results.append((cn,pfx,hint,"[FFMPEG_FAIL]","ERROR"))
            continue

        # Read WAV bytes and delete file immediately
        with open(wp, "rb") as f:
            wav_bytes = f.read()
        os.remove(wp)

        # Send to Azure REST API
        resp = requests.post(STT_URL, headers=headers, data=wav_bytes, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get("RecognitionStatus") == "Success":
                tr = data.get("DisplayText", "")
                m = hint.lower() in tr.lower() or any(c in tr for c in hint if ord(c)>127)
                st = "MATCH" if m else "CHECK"
            else:
                tr = f"[{data.get('RecognitionStatus','Unknown')}]"
                st = "NO_MATCH" if "NoMatch" in str(data.get("RecognitionStatus","")) else "ERROR"
        else:
            tr = f"[HTTP {resp.status_code}: {resp.text[:80]}]"
            st = "ERROR"
    except Exception as e:
        tr = f"[EXC:{str(e)[:80]}]"
        st = "ERROR"
    results.append((cn,pfx,hint,tr,st))
    print(f"  {i+1}/{len(samples)}: [{st}] {cn} -> {tr[:60]}")
    time.sleep(0.3)

mc = sum(1 for r in results if r[4]=="MATCH")
cc = sum(1 for r in results if r[4]=="CHECK")
ec = sum(1 for r in results if r[4] in ("ERROR","NO_MATCH"))
t = len(results)

with open(REPORT,"w",encoding="utf-8") as f:
    f.write(f"STT SPOT-CHECK REPORT\n{'='*60}\n")
    f.write(f"Total: {t}, Match: {mc}, NeedsReview: {cc}, Errors: {ec}\n")
    f.write(f"Rate: {mc/max(t,1)*100:.1f}%\n\n")
    f.write("=== NEEDS REVIEW ===\n")
    for cn,pf,h,tr,st in results:
        if st=="CHECK": f.write(f"  {cn} | hint={h} | stt={tr}\n")
    f.write("\n=== ERRORS ===\n")
    for cn,pf,h,tr,st in results:
        if st in ("ERROR","NO_MATCH"): f.write(f"  {cn} | hint={h} | {tr}\n")
    f.write("\n=== ALL ===\n")
    for cn,pf,h,tr,st in results:
        f.write(f"  [{st}] {cn} | hint={h} | stt={tr}\n")

shutil.rmtree(tmpdir, ignore_errors=True)
print(f"\nDone! Match={mc}/{t} Review={cc}/{t} Err={ec}/{t}")
print(f"Report: {REPORT}")
