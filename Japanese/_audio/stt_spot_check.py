"""Source-aware STT spot check for Japanese local audio clips.

This is a sanity check for local clip content, not a pronunciation authority.
Expected text comes from pronunciation_manifest.json, never from filenames.
Use --live only when AZURE_SPEECH_KEY is available.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


AUDIO_DIR = Path(__file__).resolve().parent
VAULT_ROOT = AUDIO_DIR.parents[1]
MANIFEST_PATH = AUDIO_DIR / "pronunciation_manifest.json"
DEFAULT_REPORT_PATH = AUDIO_DIR / "stt-spot-check-report.txt"
DEFAULT_REGION = "japaneast"

DEFAULT_CATEGORY_COUNTS = {
    "core100": 5,
    "hira": 5,
    "kata": 5,
    "verb": 5,
    "greet": 3,
    "adj": 5,
    "kanjin5": 3,
    "gap": 5,
    "nontbl": 5,
    "pitch": 5,
    "particle": 3,
    "keigo": 3,
    "daily": 3,
    "biz": 3,
    "culture": 3,
    "onomat": 3,
}

JP_PUNCTUATION = re.compile(r"[\s。、，,.!?！？・:：;；'\"“”‘’()\[\]{}<>《》「」『』ー-]+")


@dataclass(frozen=True)
class ManifestEntry:
    filename: str
    text: str
    display_text: str
    source_manifest: str
    pronunciation_note: str

    @property
    def category(self) -> str:
        return self.filename.split("-", 1)[0]

    @property
    def audio_path(self) -> Path:
        return AUDIO_DIR / self.filename

    @property
    def candidates(self) -> list[str]:
        seen: set[str] = set()
        values: list[str] = []
        for value in (self.text, self.display_text):
            cleaned = value.strip()
            if cleaned and cleaned not in seen:
                values.append(cleaned)
                seen.add(cleaned)
        return values


@dataclass
class SttResult:
    entry: ManifestEntry
    status: str
    transcription: str


def normalize_for_match(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).lower()
    return JP_PUNCTUATION.sub("", text)


def transcription_matches(transcription: str, candidates: Iterable[str]) -> bool:
    normalized_transcription = normalize_for_match(transcription)
    if not normalized_transcription:
        return False

    for candidate in candidates:
        normalized_candidate = normalize_for_match(candidate)
        if not normalized_candidate:
            continue
        if normalized_candidate in normalized_transcription:
            return True
        if normalized_transcription in normalized_candidate:
            return True
    return False


def load_manifest(path: Path) -> list[ManifestEntry]:
    raw_entries = json.loads(path.read_text(encoding="utf-8"))
    entries: list[ManifestEntry] = []
    for raw in raw_entries:
        filename = raw.get("filename", "")
        text = raw.get("text", "")
        display_text = raw.get("display_text", "")
        if not filename or not text:
            continue
        entries.append(
            ManifestEntry(
                filename=filename,
                text=text,
                display_text=display_text or text,
                source_manifest=raw.get("source_manifest", ""),
                pronunciation_note=raw.get("pronunciation_note", ""),
            )
        )
    return entries


def parse_category_counts(values: list[str]) -> dict[str, int]:
    counts = dict(DEFAULT_CATEGORY_COUNTS)
    for value in values:
        if "=" not in value:
            raise ValueError(f"category count must be PREFIX=COUNT, got {value!r}")
        prefix, raw_count = value.split("=", 1)
        prefix = prefix.strip()
        if not prefix:
            raise ValueError(f"missing prefix in {value!r}")
        counts[prefix] = int(raw_count)
    return counts


def select_entries(
    entries: list[ManifestEntry],
    counts: dict[str, int],
    seed: int,
    include_all: bool,
) -> list[ManifestEntry]:
    if include_all:
        return sorted(entries, key=lambda entry: entry.filename.lower())

    by_category: dict[str, list[ManifestEntry]] = defaultdict(list)
    for entry in entries:
        by_category[entry.category].append(entry)

    rng = random.Random(seed)
    selected: list[ManifestEntry] = []
    for category, count in sorted(counts.items()):
        group = sorted(by_category.get(category, []), key=lambda entry: entry.filename.lower())
        if not group or count <= 0:
            continue
        selected.extend(rng.sample(group, min(count, len(group))))

    return sorted(selected, key=lambda entry: (entry.category, entry.filename.lower()))


def convert_to_wav(mp3_path: Path, wav_path: Path) -> None:
    proc = subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(mp3_path),
            "-ar",
            "16000",
            "-ac",
            "1",
            "-acodec",
            "pcm_s16le",
            str(wav_path),
            "-y",
        ],
        capture_output=True,
        text=True,
        timeout=15,
    )
    if proc.returncode != 0 or not wav_path.exists():
        detail = proc.stderr.strip() or f"ffmpeg exited {proc.returncode}"
        raise RuntimeError(detail)


def recognize_once(wav_path: Path, key: str, region: str) -> str:
    import azure.cognitiveservices.speech as speechsdk

    speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
    speech_config.speech_recognition_language = "ja-JP"
    audio_config = speechsdk.audio.AudioConfig(filename=str(wav_path))
    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config,
    )
    result = recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    if result.reason == speechsdk.ResultReason.NoMatch:
        return "[NO_MATCH]"
    return f"[SDK_ERROR: {result.reason}]"


def run_live_stt(entries: list[ManifestEntry], key: str, region: str) -> list[SttResult]:
    results: list[SttResult] = []
    tmpdir = Path(tempfile.mkdtemp(prefix="japanese-stt-"))
    try:
        for index, entry in enumerate(entries, start=1):
            wav_path = tmpdir / f"{entry.audio_path.stem}.wav"
            try:
                convert_to_wav(entry.audio_path, wav_path)
                transcription = recognize_once(wav_path, key, region)
                if transcription == "[NO_MATCH]" or transcription.startswith("[SDK_ERROR:"):
                    status = "ERROR"
                elif transcription_matches(transcription, entry.candidates):
                    status = "MATCH"
                else:
                    status = "REVIEW"
            except Exception as exc:  # STT audit should report all clip failures.
                transcription = f"[ERROR: {str(exc)[:160]}]"
                status = "ERROR"
            finally:
                wav_path.unlink(missing_ok=True)

            results.append(SttResult(entry=entry, status=status, transcription=transcription))
            print(
                f"{index:>3}/{len(entries)} [{status}] {entry.filename} -> "
                f"{transcription[:80]}",
                flush=True,
            )
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
    return results


def validate_entries(entries: list[ManifestEntry]) -> tuple[list[str], Counter[str]]:
    problems: list[str] = []
    category_counts: Counter[str] = Counter()
    seen: set[str] = set()
    for entry in entries:
        category_counts[entry.category] += 1
        if entry.filename in seen:
            problems.append(f"duplicate manifest filename: {entry.filename}")
        seen.add(entry.filename)
        if not entry.audio_path.exists():
            problems.append(f"missing MP3: {entry.filename}")
        if not entry.candidates:
            problems.append(f"missing expected text: {entry.filename}")
    return problems, category_counts


def write_report(
    report_path: Path,
    *,
    mode: str,
    entries: list[ManifestEntry],
    selected: list[ManifestEntry],
    validation_problems: list[str],
    category_counts: Counter[str],
    results: list[SttResult] | None,
    seed: int,
    region: str,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = [
        "STT SPOT-CHECK REPORT",
        "=" * 80,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "Expectation source: pronunciation_manifest.json text/display_text fields",
        "Filename-derived expectations: disabled",
        "Authority: STT is a triage signal only; native/course/tutor/reference audio remains authoritative.",
        "",
        "SUMMARY",
        f"  Mode                  : {mode}",
        f"  Azure region          : {region}",
        f"  Manifest entries      : {len(entries)}",
        f"  Selected clips        : {len(selected)}",
        f"  Random seed           : {seed}",
        f"  Validation problems   : {len(validation_problems)}",
    ]

    if results is not None:
        status_counts = Counter(result.status for result in results)
        total = len(results)
        lines.extend(
            [
                f"  Matched               : {status_counts['MATCH']}/{total}",
                f"  Needs review          : {status_counts['REVIEW']}/{total}",
                f"  Errors                : {status_counts['ERROR']}/{total}",
            ]
        )
    else:
        lines.append("  Live STT run          : not run")

    lines.extend(["", "CATEGORY COVERAGE"])
    for category, count in sorted(category_counts.items()):
        selected_count = sum(1 for entry in selected if entry.category == category)
        if selected_count:
            lines.append(f"  {category:12s} selected {selected_count:3d} / manifest {count:3d}")

    if validation_problems:
        lines.extend(["", "VALIDATION PROBLEMS"])
        lines.extend(f"  {problem}" for problem in validation_problems)

    lines.extend(["", "SELECTED CLIPS"])
    for entry in selected:
        lines.append(
            f"  {entry.filename} | expected={entry.text} | "
            f"display={entry.display_text} | source={entry.source_manifest}"
        )

    if results is not None:
        review = [result for result in results if result.status == "REVIEW"]
        errors = [result for result in results if result.status == "ERROR"]
        if review:
            lines.extend(["", "NEEDS REVIEW"])
            for result in review:
                lines.extend(
                    [
                        f"  {result.entry.filename}",
                        f"    Expected    : {' / '.join(result.entry.candidates)}",
                        f"    Transcribed : {result.transcription}",
                    ]
                )
        if errors:
            lines.extend(["", "ERRORS"])
            for result in errors:
                lines.extend(
                    [
                        f"  {result.entry.filename}",
                        f"    Expected    : {' / '.join(result.entry.candidates)}",
                        f"    Result      : {result.transcription}",
                    ]
                )

        lines.extend(["", "ALL LIVE RESULTS"])
        for result in results:
            lines.extend(
                [
                    f"  [{result.status}] {result.entry.filename}",
                    f"    Expected    : {' / '.join(result.entry.candidates)}",
                    f"    Transcribed : {result.transcription}",
                ]
            )

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="Run Azure Speech-to-Text.")
    parser.add_argument("--all", action="store_true", help="Select every manifest entry.")
    parser.add_argument("--seed", type=int, default=42, help="Random sample seed.")
    parser.add_argument("--region", default=DEFAULT_REGION, help="Azure Speech region.")
    parser.add_argument(
        "--category-count",
        action="append",
        default=[],
        metavar="PREFIX=COUNT",
        help="Override default balanced sample counts.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=DEFAULT_REPORT_PATH,
        help="Report path.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    counts = parse_category_counts(args.category_count)
    entries = load_manifest(MANIFEST_PATH)
    validation_problems, category_counts = validate_entries(entries)
    selected = select_entries(entries, counts, args.seed, args.all)

    results: list[SttResult] | None = None
    mode = "dry-run-source-plan"
    if args.live:
        key = os.environ.get("AZURE_SPEECH_KEY")
        if not key:
            write_report(
                args.report,
                mode="live-requested-but-missing-azure-key",
                entries=entries,
                selected=selected,
                validation_problems=validation_problems,
                category_counts=category_counts,
                results=None,
                seed=args.seed,
                region=args.region,
            )
            print("AZURE_SPEECH_KEY is not set; wrote source-aware dry-run report.", file=sys.stderr)
            return 2
        mode = "live-stt"
        results = run_live_stt(selected, key, args.region)

    write_report(
        args.report,
        mode=mode,
        entries=entries,
        selected=selected,
        validation_problems=validation_problems,
        category_counts=category_counts,
        results=results,
        seed=args.seed,
        region=args.region,
    )

    print(f"Report saved to: {args.report}")
    return 1 if validation_problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
