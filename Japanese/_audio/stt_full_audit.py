import os
import re
import time
import glob
import subprocess
import tempfile
from pathlib import Path
import gc
import shutil
import winreg
import azure.cognitiveservices.speech as sdk


def refresh_windows_path() -> None:
    try:
        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
        ) as key:
            machine_path = winreg.QueryValueEx(key, "Path")[0]
    except OSError:
        machine_path = os.environ.get("Path", "")

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as key:
            user_path = winreg.QueryValueEx(key, "Path")[0]
    except OSError:
        user_path = ""

    merged = ";".join(part for part in (machine_path, user_path) if part)
    if merged:
        os.environ["Path"] = merged
        os.environ["PATH"] = merged


refresh_windows_path()

AUDIO_DIR = Path(r"D:\Vaults\PersonalKB\Japanese\_audio")
REPORT = AUDIO_DIR / "stt-spot-check-report.txt"

key = os.environ["AZURE_SPEECH_KEY"]
sc = sdk.SpeechConfig(subscription=key, region="japaneast")
sc.speech_recognition_language = "ja-JP"

# Sample clips from different categories
categories = {
    "core100": 5, "hira": 5, "kata": 5, "verb": 5,
    "greet": 3, "adj": 5, "kanjin5": 3, "gap": 5,
    "nontbl": 5, "pitch": 5, "particle": 3, "keigo": 3,
    "daily": 3, "biz": 3, "culture": 3, "onomat": 3,
}

samples = []
for prefix, count in categories.items():
    files = sorted(glob.glob(str(AUDIO_DIR / f"{prefix}-*.mp3")))
    if files:
        step = max(1, len(files) // count)
        sel = files[::step][:count]
        samples.extend(sel)
        print(f"  {prefix}: {len(sel)}/{len(files)}")

print(f"\nTotal samples: {len(samples)}")

# Create temp directory for WAV files
tmpdir = tempfile.mkdtemp()
results = []

for i, clip_path in enumerate(samples):
    clip_name = os.path.basename(clip_path)
    base = clip_name.replace(".mp3", "")

    # Parse filename for expected content
    parts = base.split("-", 1)
    prefix = parts[0]
    hint = parts[1] if len(parts) > 1 else base
    # Remove leading numbers from gap/nontbl series
    hint = re.sub(r"^\d+[-_]?", "", hint)

    try:
        # Convert MP3 to WAV using ffmpeg
        wav_path = os.path.join(tmpdir, base + ".wav")
        proc = subprocess.run(
            ["ffmpeg", "-i", clip_path, "-ar", "16000", "-ac", "1",
             "-acodec", "pcm_s16le", wav_path, "-y"],
            capture_output=True, text=True, timeout=10
        )

        if proc.returncode != 0 or not os.path.exists(wav_path):
            results.append((clip_name, prefix, hint, f"[FFMPEG_ERROR: {proc.stderr[-100:]}]", "ERROR"))
            continue

        # Run STT on WAV
        ac = sdk.audio.AudioConfig(filename=wav_path)
        rec = sdk.SpeechRecognizer(speech_config=sc, audio_config=ac)
        r = rec.recognize_once()
        del rec
        del ac
        gc.collect()

        # Clean up WAV
        os.remove(wav_path)

        if r.reason == sdk.ResultReason.RecognizedSpeech:
            transcription = r.text
            hint_lower = hint.lower()
            trans_lower = transcription.lower()

            # Check match: romaji hint in transcription
            is_match = hint_lower in trans_lower

            # Also check if any non-ASCII chars from hint appear in transcription
            if not is_match:
                is_match = any(c in transcription for c in hint if ord(c) > 127)

            status = "MATCH" if is_match else "CHECK"
        elif r.reason == sdk.ResultReason.NoMatch:
            transcription = "[NO_MATCH]"
            status = "NO_MATCH"
        else:
            transcription = f"[SDK_ERROR: {r.reason}]"
            status = "ERROR"

    except Exception as e:
        transcription = f"[EXCEPTION: {str(e)[:100]}]"
        status = "ERROR"

    results.append((clip_name, prefix, hint, transcription, status))
    print(f"  {i+1}/{len(samples)}: [{status}] {clip_name} -> {transcription[:60]}")
    time.sleep(0.2)

# Stats
match_count = sum(1 for r in results if r[4] == "MATCH")
check_count = sum(1 for r in results if r[4] == "CHECK")
error_count = sum(1 for r in results if r[4] in ("ERROR", "NO_MATCH"))
total = len(results)

# Write report
with open(REPORT, "w", encoding="utf-8") as f:
    f.write("STT SPOT-CHECK REPORT\n")
    f.write("=" * 60 + "\n")
    f.write(f"Total: {total}\n")
    f.write(f"Matched (filename hint found in transcription): {match_count}\n")
    f.write(f"Needs review (transcription doesn't match hint): {check_count}\n")
    f.write(f"Errors/No match: {error_count}\n")
    f.write(f"Match rate: {match_count/max(total,1)*100:.1f}%\n\n")

    f.write("=== NEEDS REVIEW ===\n")
    for cn, pf, h, tr, st in results:
        if st == "CHECK":
            f.write(f"  {cn}\n    hint: {h}\n    stt:  {tr}\n\n")

    f.write("\n=== ERRORS/NO_MATCH ===\n")
    for cn, pf, h, tr, st in results:
        if st in ("ERROR", "NO_MATCH"):
            f.write(f"  {cn}\n    hint: {h}\n    result: {tr}\n\n")

    f.write("\n=== ALL RESULTS ===\n")
    for cn, pf, h, tr, st in results:
        f.write(f"  [{st}] {cn}\n    hint: {h}\n    stt:  {tr}\n\n")

# Cleanup
shutil.rmtree(tmpdir, ignore_errors=True)

# Also clean up test WAV from earlier
test_wav = AUDIO_DIR / "test_watashi.wav"
if test_wav.exists():
    test_wav.unlink()

print(f"\nDone! Match={match_count}/{total} Review={check_count}/{total} Err={error_count}/{total}")
print(f"Report: {REPORT}")