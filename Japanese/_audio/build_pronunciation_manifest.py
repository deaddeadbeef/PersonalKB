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
    # Table rules and examples where the audio should read the example, not the rule.
    "gap-005-Plain-().mp3": ("タメ口", "removed English register label"),
    "gap-006-.mp3": ("行く、来る", "read both verbs without slash"),
    "gap-007-(oishii).mp3": ("おいしい", "removed romanization"),
    "gap-008-Drop-,-add.mp3": ("おいしくない", "read adjective form example"),
    "gap-009-Drop-,-add.mp3": ("おいしかった", "read adjective form example"),
    "gap-010-Drop-,-add.mp3": ("おいしくなかった", "read adjective form example"),
    "gap-011-Drop-,-add.mp3": ("おいしく", "read adjective form example"),
    "gap-012-Add.mp3": ("おいしいです", "read polite adjective example"),
    "gap-013-+.mp3": ("元気な人", "read na-adjective example"),
    "gap-014-+.mp3": ("元気です", "read na-adjective example"),
    "gap-015-+.mp3": ("元気じゃない", "read na-adjective example"),
    "gap-016-+.mp3": ("元気でした", "read na-adjective example"),
    "gap-017-+.mp3": ("元気じゃなかった", "read na-adjective example"),
    "gap-018-+.mp3": ("元気に", "read na-adjective example"),
    "gap-019-adj.mp3": ("安くておいしい", "read conjunction example"),
    "gap-020-adj.mp3": ("静かできれい", "read conjunction example"),
    "gap-021-A-B-~.mp3": ("犬は猫より大きいです", "read comparison example"),
    "gap-022-A-~.mp3": ("富士山が一番高いです", "read superlative example"),
    "gap-023-~.mp3": ("どちらが安いですか", "read question example"),
    "gap-060-(kakimasu).mp3": ("書きます", "read conjugated form"),
    "gap-061-Drop-,-add.mp3": ("食べます", "read conjugated form"),
    "gap-062-,.mp3": ("します、きます", "read both irregular forms"),
    "gap-066-.mp3": ("ぶ、む、ぬ", "read endings without slash"),
    "gap-067-.mp3": ("つ、る、う", "read endings without slash"),
    "gap-068-Exception.mp3": ("行く", "removed English exception label"),
    "gap-069-(kakanai).mp3": ("書かない", "read conjugated form"),
    "gap-070-Drop-,-add.mp3": ("食べない", "read conjugated form"),
    "gap-071-,.mp3": ("しない、こない", "read both irregular forms"),
    "gap-072-(NOT-).mp3": ("ない", "removed English warning"),
    "gap-084-phrase.mp3": ("私はそう思います", "expanded ellipsis to a pronounceable sentence"),
    "gap-125-.mp3": ("彼、彼女", "read both pronouns without slash"),

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
    "nontbl-040-wa-ha-particle.mp3": ("これは本です", "expanded placeholder pattern"),

    # Placeholder examples.
    "nontbl-002-desu.mp3": ("田中です", "expanded placeholder"),
    "nontbl-003-kara-kimashita.mp3": ("アメリカから来ました", "expanded placeholder"),
    "nontbl-004-shumi-wa-desu.mp3": ("趣味は音楽です", "expanded placeholder"),
    "nontbl-006-to-moushimasu.mp3": ("田中と申します", "expanded placeholder"),
    "nontbl-007-hataraiteorimasu.mp3": ("山田商事の営業部で働いております", "expanded placeholder"),
    "selfintro2-010-kaisha-de-hataraitemasu.mp3": (
        "山田商事の営業部で働いております。",
        "removed Latin company placeholder",
    ),

    # Clips that were generated from English notes or malformed harvested text.
    "adj-038-describe-things-around-you-using-both-i-na-adjectives.mp3": (
        "身の回りのものを、い形容詞とな形容詞の両方を使って説明しましょう。",
        "translated English practice instruction",
    ),
    "n4give-018-ageru-kureru.mp3": ("あげる、くれる", "repaired harvested contrast"),
    "n4give-019-ageru-sashiageru.mp3": ("あげる、さしあげる", "repaired harvested contrast"),

    # OCR and table extraction errors.
    "gap-194-phrase.mp3": ("寝る", "repaired OCR error"),
    "gap-208-phrase.mp3": ("卵", "repaired OCR error"),
    "gap-212-phrase.mp3": ("醤油", "normalized common kanji form"),
    "gap-213-phrase.mp3": ("朝ごはん", "repaired OCR error"),
    "gap-214-phrase.mp3": ("昼ごはん", "repaired OCR error"),
    "gap-229-phrase.mp3": ("救急車", "repaired OCR error"),
    "gap-257-phrase.mp3": ("涼しい", "repaired OCR error"),
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
