"""Build the canonical pronunciation-safe Japanese audio manifest.

The source manifests are partly harvested from Markdown tables. Some table
cells contain learning rules, placeholders, romanization hints, or OCR errors
that should not be sent directly to text-to-speech. This script keeps those
source manifests intact and emits a single manifest whose ``text`` field is the
exact Japanese string used for synthesis.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


AUDIO_DIR = Path(__file__).resolve().parent
VAULT_ROOT = AUDIO_DIR.parents[1]
OUTPUT_MANIFEST = AUDIO_DIR / "pronunciation_manifest.json"
REPORT_PATH = VAULT_ROOT / "_ops" / "reports" / "japanese-audio-pronunciation-audit.txt"

ROMANIZATION_PARENS = re.compile(r"\s*\([A-Za-z0-9ūōāīēŪŌĀĪĒ' -]+\)")
ASCII_PROBLEM = re.compile(r"[A-Za-z\[\]{}~+/]")

PRONUNCIATION_OVERRIDES: dict[str, tuple[str, str]] = {
    # Counter suffixes and particles where the intended reading is not the default kanji name.
    "gap-024-phrase.mp3": ("わ", "topic particle reading"),
    "gap-026-phrase.mp3": ("お", "object particle reading"),
    "gap-029-phrase.mp3": ("え", "direction particle reading"),
    "gap-049-(nin).mp3": ("にん", "counter suffix reading"),
    "gap-050-(hon).mp3": ("ほん", "counter suffix reading"),
    "gap-051-(mai).mp3": ("まい", "counter suffix reading"),
    "gap-052-(hai).mp3": ("はい", "counter suffix reading"),
    "gap-053-(satsu).mp3": ("さつ", "counter suffix reading"),
    "gap-054-(dai).mp3": ("だい", "counter suffix reading"),
    "gap-055-(hiki).mp3": ("ひき", "counter suffix reading"),
    "gap-058-(ikkagetsu).mp3": ("いっかげつ", "force duration counter reading"),
    "gap-089-(wa).mp3": ("わ", "counter suffix reading"),
    "gap-090-(kai).mp3": ("かい", "counter suffix reading"),
    "gap-091-(kai).mp3": ("かい", "counter suffix reading"),
    "gap-092-(ban).mp3": ("ばん", "counter suffix reading"),
    "gap-093-(soku).mp3": ("そく", "counter suffix reading"),
    "gap-094-(chaku).mp3": ("ちゃく", "counter suffix reading"),
    "particle-001-wa.mp3": ("わ", "topic particle reading"),
    "particle-007-o.mp3": ("お", "object particle reading"),
    "particle-018-e.mp3": ("え", "direction particle reading"),
    "hira-101-particle-wa.mp3": ("わ", "topic particle reading"),
    "hira-102-particle-e.mp3": ("え", "direction particle reading"),
    "writing-006-particle-wa.mp3": ("わ", "topic particle reading"),
    "writing-009-particle-o.mp3": ("お", "object particle reading"),

    # Reading disambiguation and remaining extraction repairs.
    "gap-184-(akeru)-open.mp3": ("あける", "force transitive open reading"),
    "listen-010-koe-no-katachi.mp3": ("こえの形", "force title reading"),
}

EXPECTED_READING_OVERRIDE_REASONS = {
    "topic particle reading",
    "object particle reading",
    "direction particle reading",
    "counter suffix reading",
    "force duration counter reading",
    "force transitive open reading",
    "force title reading",
}


def source_manifest_paths() -> list[Path]:
    return [
        path
        for path in sorted(AUDIO_DIR.glob("*_manifest.json"))
        if path.name != OUTPUT_MANIFEST.name
    ]


def contains_japanese(text: str) -> bool:
    return any(
        "\u3040" <= ch <= "\u30ff" or "\u3400" <= ch <= "\u9fff"
        for ch in text
    )


def normalize_text(text: str) -> str:
    text = text.strip()
    if contains_japanese(text):
        text = ROMANIZATION_PARENS.sub("", text)
        text = re.sub(r"\s+[A-Za-z][A-Za-z -]+$", "", text)
    text = text.replace(" / ", "、").replace("/", "、")
    text = text.replace("→", "、")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_expected_reading_override(entry: dict[str, Any]) -> bool:
    return entry["pronunciation_note"] in EXPECTED_READING_OVERRIDE_REASONS


def build_entries() -> tuple[list[dict[str, Any]], Counter[str], list[str], list[str]]:
    entries_by_filename: dict[str, dict[str, Any]] = {}
    duplicate_notes: list[str] = []
    invalid_notes: list[str] = []
    stats: Counter[str] = Counter()

    for manifest_path in source_manifest_paths():
        with manifest_path.open("r", encoding="utf-8") as fh:
            raw_items = json.load(fh)
        if not isinstance(raw_items, list):
            invalid_notes.append(f"{manifest_path.name}: expected a list")
            continue

        for item in raw_items:
            filename = item.get("filename")
            source_text = item.get("text")
            if not filename or not isinstance(source_text, str):
                invalid_notes.append(f"{manifest_path.name}: malformed item {item!r}")
                continue

            override = PRONUNCIATION_OVERRIDES.get(filename)
            if override:
                tts_text, reason = override
                stats["overrides"] += 1
            else:
                tts_text = normalize_text(source_text)
                reason = "normalized" if tts_text != source_text else "unchanged"
                stats[reason] += 1

            entry = {
                "filename": filename,
                "text": tts_text,
                "display_text": source_text,
                "source_manifest": manifest_path.name,
                "voice": item.get("voice", "ja-JP-NanamiNeural"),
                "pronunciation_note": reason,
            }

            existing = entries_by_filename.get(filename)
            if existing:
                if existing["text"] != entry["text"]:
                    duplicate_notes.append(
                        f"{filename}: {existing['source_manifest']}={existing['text']} | "
                        f"{manifest_path.name}={entry['text']}"
                    )
                existing.setdefault("duplicate_source_manifests", []).append(manifest_path.name)
                stats["duplicates"] += 1
                continue

            entries_by_filename[filename] = entry
            stats[f"source:{manifest_path.name}"] += 1

            if not tts_text:
                invalid_notes.append(f"{filename}: empty TTS text")
            elif ASCII_PROBLEM.search(tts_text):
                invalid_notes.append(f"{filename}: ASCII/control text remains in {tts_text!r}")

    entries = sorted(entries_by_filename.values(), key=lambda row: row["filename"].lower())
    return entries, stats, duplicate_notes, invalid_notes


def write_report(
    entries: list[dict[str, Any]],
    stats: Counter[str],
    duplicate_notes: list[str],
    invalid_notes: list[str],
    report_path: Path,
) -> None:
    mp3s = sorted(AUDIO_DIR.glob("*.mp3"))
    manifest_names = {entry["filename"] for entry in entries}
    missing_mp3 = sorted(name for name in manifest_names if not (AUDIO_DIR / name).exists())
    mp3_not_in_manifest = sorted(path.name for path in mp3s if path.name not in manifest_names)

    changed_entries = [
        entry for entry in entries if entry["text"] != entry["display_text"]
    ]
    expected_reading_entries = [
        entry for entry in changed_entries if is_expected_reading_override(entry)
    ]
    source_repair_entries = [
        entry for entry in changed_entries if not is_expected_reading_override(entry)
    ]

    lines = [
        "JAPANESE AUDIO PRONUNCIATION AUDIT",
        "=" * 80,
        "",
        "SUMMARY",
        f"  Source manifests          : {len(source_manifest_paths())}",
        f"  Pronunciation entries     : {len(entries)}",
        f"  MP3 files                 : {len(mp3s)}",
        f"  Entries changed for TTS   : {len(changed_entries)}",
        f"  Explicit overrides        : {stats['overrides']}",
        f"  Expected reading overrides: {len(expected_reading_entries)}",
        f"  Source repair overrides   : {len(source_repair_entries)}",
        f"  Duplicate manifest rows   : {stats['duplicates']}",
        f"  Missing MP3 files         : {len(missing_mp3)}",
        f"  MP3 files not in manifest : {len(mp3_not_in_manifest)}",
        f"  Invalid TTS inputs        : {len(invalid_notes)}",
        "",
        "SOURCE COVERAGE",
    ]

    for key, value in sorted(stats.items()):
        if key.startswith("source:"):
            lines.append(f"  {key.removeprefix('source:'):28s} {value}")

    if expected_reading_entries:
        lines.extend(["", "EXPECTED READING OVERRIDES"])
        for entry in expected_reading_entries:
            lines.append(
                f"  {entry['filename']}: {entry['display_text']} -> "
                f"{entry['text']} ({entry['pronunciation_note']})"
            )

    if source_repair_entries:
        lines.extend(["", "SOURCE REPAIR OVERRIDES"])
        for entry in source_repair_entries:
            lines.append(
                f"  {entry['filename']}: {entry['display_text']} -> "
                f"{entry['text']} ({entry['pronunciation_note']})"
            )

    if changed_entries:
        lines.extend(["", "CHANGED TTS INPUTS"])
        for entry in changed_entries:
            lines.append(
                f"  {entry['filename']}: {entry['display_text']} -> "
                f"{entry['text']} ({entry['pronunciation_note']})"
            )

    if duplicate_notes:
        lines.extend(["", "DUPLICATE NOTES"])
        lines.extend(f"  {note}" for note in duplicate_notes)

    if missing_mp3:
        lines.extend(["", "MISSING MP3 FILES"])
        lines.extend(f"  {name}" for name in missing_mp3)

    if mp3_not_in_manifest:
        lines.extend(["", "MP3 FILES NOT IN MANIFEST"])
        lines.extend(f"  {name}" for name in mp3_not_in_manifest)

    if invalid_notes:
        lines.extend(["", "INVALID TTS INPUTS"])
        lines.extend(f"  {note}" for note in invalid_notes)

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT_MANIFEST)
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    parser.add_argument("--check", action="store_true", help="fail if output is stale")
    args = parser.parse_args()

    entries, stats, duplicate_notes, invalid_notes = build_entries()
    serialized = json.dumps(entries, ensure_ascii=False, indent=2) + "\n"

    if args.check:
        current = args.output.read_text(encoding="utf-8") if args.output.exists() else ""
        if current != serialized:
            print(f"ERROR: {args.output} is stale")
            return 1
    else:
        args.output.write_text(serialized, encoding="utf-8")

    args.report.parent.mkdir(parents=True, exist_ok=True)
    write_report(entries, stats, duplicate_notes, invalid_notes, args.report)

    if invalid_notes:
        print(f"ERROR: {len(invalid_notes)} invalid TTS inputs remain")
        for note in invalid_notes[:20]:
            print(f"  {note}")
        return 1

    print(f"Wrote {len(entries)} entries to {args.output}")
    print(f"Wrote audit report to {args.report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
