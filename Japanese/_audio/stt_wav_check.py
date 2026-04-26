import os, re, time, glob as g, tempfile
from pathlib import Path
from pydub import AudioSegment
import azure.cognitiveservices.speech as sdk

AUDIO_DIR = Path(r"D:\Vaults\PersonalKB\Japanese\_audio")
REPORT = AUDIO_DIR / "stt-spot-check-report.txt"
key = os.environ["AZURE_SPEECH_KEY"]
sc = sdk.SpeechConfig(subscription=key, region="japaneast")
sc.speech_recognition_language = "ja-JP"

cats = {"core100":5,"hira":5,"kata":5,"verb":5,"greet":3,"adj":5,"kanjin5":3,"gap":5,"nontbl":5,"pitch":5}
samples = []
for prefix, count in cats.items():
    files = sorted(g.glob(str(AUDIO_DIR / f"{prefix}-*.mp3")))
    if files:
        step = max(1, len(files)//count)
        sel = files[::step][:count]
        samples.extend(sel)
        print(f"  {prefix}: {len(sel)}/{len(files)}")

print(f"Total: {len(samples)}")
results = []
tmpdir = tempfile.mkdtemp()

for i, cp in enumerate(samples):
    cn = os.path.basename(cp)
    base = cn.replace(".mp3","")
    parts = base.split("-",1)
    prefix = parts[0]
    hint = parts[1] if len(parts)>1 else base
    hint = re.sub(r"^\d+[-_]?","",hint)
    try:
        wav_path = os.path.join(tmpdir, base + ".wav")
        audio = AudioSegment.from_mp3(cp)
        audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
        audio.export(wav_path, format="wav")
        ac = sdk.audio.AudioConfig(filename=wav_path)
        rec = sdk.SpeechRecognizer(speech_config=sc, audio_config=ac)
        r = rec.recognize_once()
        os.remove(wav_path)
        if r.reason == sdk.ResultReason.RecognizedSpeech:
            tr = r.text
            hl = hint.lower()
            tl = tr.lower()
            m = hl in tl or any(c in tr for c in hint if ord(c)>127)
            st = "MATCH" if m else "CHECK"
        elif r.reason == sdk.ResultReason.NoMatch:
            tr = "[NO_MATCH]"
            st = "NO_MATCH"
        else:
            tr = f"[ERR:{r.reason}]"
            st = "ERROR"
    except Exception as e:
        tr = f"[EXC:{e}]"
        st = "ERROR"
    results.append((cn,prefix,hint,tr,st))
    print(f"  {i+1}/{len(samples)}: [{st}] {cn} -> {tr[:50]}")
    time.sleep(0.2)

mc = sum(1 for r in results if r[4]=="MATCH")
cc = sum(1 for r in results if r[4]=="CHECK")
ec = sum(1 for r in results if r[4] in ("ERROR","NO_MATCH"))
t = len(results)

with open(REPORT,"w",encoding="utf-8") as f:
    f.write(f"STT SPOT-CHECK REPORT\n" + "="*60 + f"\nTotal: {t}, Match: {mc}, NeedsReview: {cc}, Errors: {ec}\nRate: {mc/max(t,1)*100:.1f}%\n\n")
    f.write("=== NEEDS REVIEW ===\n")
    for cn,pf,h,tr,st in results:
        if st=="CHECK": f.write(f"  {cn} | hint={h} | stt={tr}\n")
    f.write("\n=== ERRORS/NO_MATCH ===\n")
    for cn,pf,h,tr,st in results:
        if st in ("ERROR","NO_MATCH"): f.write(f"  {cn} | hint={h} | {tr}\n")
    f.write("\n=== ALL RESULTS ===\n")
    for cn,pf,h,tr,st in results:
        f.write(f"  [{st}] {cn} | hint={h} | stt={tr}\n")

import shutil
shutil.rmtree(tmpdir, ignore_errors=True)
print(f"\nDone! Match={mc}/{t} Review={cc}/{t} Err={ec}/{t}")
print(f"Report: {REPORT}")
