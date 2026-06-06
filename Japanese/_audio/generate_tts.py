"""Generate Japanese TTS audio clips from a manifest."""

from __future__ import annotations

import argparse
import gc
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

import azure.cognitiveservices.speech as speechsdk


AUDIO_DIR = Path(__file__).resolve().parent
DEFAULT_MANIFEST = AUDIO_DIR / "pronunciation_manifest.json"
DEFAULT_REGION = "japaneast"
DEFAULT_VOICE = "ja-JP-NanamiNeural"
BROWSER_COMPATIBLE_MP3_FORMAT = speechsdk.SpeechSynthesisOutputFormat.Audio48Khz96KBitRateMonoMp3

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def resolve_key(explicit_key: str | None) -> str:
    if explicit_key:
        return explicit_key.strip()

    env_key = os.environ.get("AZURE_SPEECH_KEY")
    if env_key:
        return env_key.strip()

    az_exe = (
        shutil.which("az")
        or shutil.which("az.cmd")
        or r"C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd"
    )
    command = [
        az_exe,
        "cognitiveservices",
        "account",
        "keys",
        "list",
        "--name",
        "tts-tester",
        "--resource-group",
        "tts-resources",
        "--query",
        "key1",
        "-o",
        "tsv",
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
    except OSError as exc:
        raise RuntimeError("Azure key missing and Azure CLI was not available") from exc

    key = result.stdout.strip()
    if not key:
        raise RuntimeError(f"Azure key lookup failed: {result.stderr.strip()}")
    return key


def load_manifest(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as fh:
        items = json.load(fh)
    if not isinstance(items, list):
        raise ValueError(f"{path} must contain a JSON list")
    return items


def make_speech_config(key: str, region: str, voice: str) -> speechsdk.SpeechConfig:
    speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
    # Obsidian/Electron rejects Azure's 16 kHz / 32 kbps MP3 output as a media
    # format error. Keep generated clips in the browser-compatible MPEG-1 range.
    speech_config.set_speech_synthesis_output_format(BROWSER_COMPATIBLE_MP3_FORMAT)
    speech_config.speech_synthesis_voice_name = voice
    return speech_config


def remove_with_retry(path: Path) -> bool:
    for _ in range(20):
        if not path.exists():
            return True
        try:
            path.unlink()
            return True
        except PermissionError:
            time.sleep(0.1)
    return not path.exists()


def synthesize_clip(
    *,
    text: str,
    filename: str,
    voice: str,
    key: str,
    region: str,
    force: bool,
    dry_run: bool,
) -> tuple[bool, str]:
    output_path = AUDIO_DIR / filename
    if output_path.exists() and not force:
        return True, "skip"

    if dry_run:
        return True, "dry-run"

    temp_path = output_path.with_name(output_path.name + ".tmp")
    if temp_path.exists():
        if not remove_with_retry(temp_path):
            return False, f"could not remove locked temp file {temp_path.name}"

    speech_config = make_speech_config(key, region, voice)
    audio_config = speechsdk.audio.AudioOutputConfig(filename=str(temp_path))
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config,
    )

    result = synthesizer.speak_text_async(text).get()
    if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
        cancellation = result.cancellation_details
        del synthesizer
        del audio_config
        gc.collect()
        remove_with_retry(temp_path)
        return False, f"{cancellation.reason}: {cancellation.error_details}"

    del synthesizer
    del audio_config
    gc.collect()

    size = temp_path.stat().st_size
    if size <= 0:
        remove_with_retry(temp_path)
        return False, "empty output"

    replace_error: PermissionError | None = None
    for _ in range(20):
        try:
            os.replace(temp_path, output_path)
            replace_error = None
            break
        except PermissionError as exc:
            replace_error = exc
            time.sleep(0.1)
    if replace_error is not None:
        return False, f"replace failed: {replace_error}"

    return True, f"ok {size} bytes"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--key", help="Azure Speech key; falls back to AZURE_SPEECH_KEY or az")
    parser.add_argument("--region", default=DEFAULT_REGION)
    parser.add_argument("--voice", default=DEFAULT_VOICE)
    parser.add_argument("--force", action="store_true", help="overwrite existing MP3 files")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--offset", type=int, default=0, help="skip the first N manifest rows")
    parser.add_argument("--limit", type=int, help="synthesize only the first N manifest rows")
    parser.add_argument("--delay", type=float, default=0.15)
    parser.add_argument("--fail-fast", action="store_true")
    args = parser.parse_args()

    manifest_path = args.manifest
    if not manifest_path.is_absolute():
        manifest_path = AUDIO_DIR / manifest_path
    items = load_manifest(manifest_path)
    if args.offset:
        items = items[args.offset :]
    if args.limit is not None:
        items = items[: args.limit]

    key = "" if args.dry_run else resolve_key(args.key)

    ok = 0
    fail = 0
    skipped = 0
    for index, item in enumerate(items, 1):
        text = item.get("text")
        filename = item.get("filename")
        if not isinstance(text, str) or not isinstance(filename, str):
            print(f"[{index}/{len(items)}] malformed item: {item!r}")
            fail += 1
            if args.fail_fast:
                return 1
            continue

        voice = item.get("voice") or args.voice
        print(f"[{index}/{len(items)}] {filename} <- {text}", flush=True)
        success, detail = synthesize_clip(
            text=text,
            filename=filename,
            voice=voice,
            key=key,
            region=args.region,
            force=args.force,
            dry_run=args.dry_run,
        )

        if success:
            ok += 1
            if detail == "skip":
                skipped += 1
            print(f"  {detail}")
        else:
            fail += 1
            print(f"  FAIL: {detail}")
            if args.fail_fast:
                return 1

        if not args.dry_run and args.delay > 0:
            time.sleep(args.delay)

    print(f"Done: {ok} ok ({skipped} skipped), {fail} fail, {len(items)} total")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
