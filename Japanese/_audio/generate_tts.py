import azure.cognitiveservices.speech as speechsdk
import os
import sys
import json
import time

def generate_audio(text, filename, voice, key, region):
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    if os.path.exists(output_path):
        print(f"  SKIP: {filename}")
        return True

    speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
    speech_config.set_speech_synthesis_output_format(
        speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3
    )
    speech_config.speech_synthesis_voice_name = voice
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_path)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = synthesizer.speak_text_async(text).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        size = os.path.getsize(output_path)
        print(f"  OK: {filename} ({size} bytes)")
        return True
    else:
        cancellation = result.cancellation_details
        print(f"  FAIL: {filename} - {cancellation.reason}: {cancellation.error_details}")
        return False

def generate_batch(manifest_file, key, region):
    with open(manifest_file, "r", encoding="utf-8") as f:
        items = json.load(f)

    ok = 0
    fail = 0
    for item in items:
        voice = item.get("voice", "ja-JP-NanamiNeural")
        if generate_audio(item["text"], item["filename"], voice, key, region):
            ok += 1
        else:
            fail += 1
        time.sleep(0.3)

    print(f"\nDone: {ok} ok, {fail} fail, {len(items)} total")

if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("AZURE_SPEECH_KEY")
    region = sys.argv[2] if len(sys.argv) > 2 else "japaneast"
    manifest = sys.argv[3] if len(sys.argv) > 3 else "test_manifest.json"
    if not key:
        print("ERROR: pass key as first arg or set AZURE_SPEECH_KEY")
        sys.exit(1)
    generate_batch(manifest, key, region)
