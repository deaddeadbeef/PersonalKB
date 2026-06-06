"""Audit pronunciation manifest entries against explicit romaji hints.

This is a targeted guardrail for audio authenticity. It only checks manifest
rows whose display text contains a parenthesized romaji hint, such as
``一か月 (ikkagetsu)``. Those hints are strong evidence that a kanji string
needs a specific reading, so mismatches here should be reviewed before
regenerating audio.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import jaconv
import pykakasi


AUDIO_DIR = Path(__file__).resolve().parent
VAULT_ROOT = AUDIO_DIR.parents[1]
DEFAULT_MANIFEST = AUDIO_DIR / "pronunciation_manifest.json"
DEFAULT_REPORT = VAULT_ROOT / "_ops" / "reports" / "japanese-audio-reading-hints-audit.txt"

ROMAJI_HINT_RE = re.compile(r"\(([A-Za-z][A-Za-zūōāīēŪŌĀĪĒ' -]{1,28})\)")
IGNORE_HINTS = {
    # Single-particle/counter headings are already guarded by explicit
    # pronunciation overrides in build_pronunciation_manifest.py.
    "ban",
    "chaku",
    "dai",
    "e",
    "hai",
    "hiki",
    "hon",
    "kai",
    "mai",
    "nin",
    "o",
    "satsu",
    "soku",
    "tsu",
    "wa",
}


def normalize_romaji(value: str) -> str:
    value = value.lower().strip()
    value = (
        value.replace("ō", "ou")
        .replace("ū", "uu")
        .replace("ā", "aa")
        .replace("ī", "ii")
        .replace("ē", "ee")
    )
    value = re.sub(r"[^a-z' -]", "", value)
    return value.replace("'", "").replace("-", "").replace(" ", "")


def romaji_to_hiragana(value: str) -> str:
    return jaconv.alphabet2kana(normalize_romaji(value))


def make_text_reader():
    converter = pykakasi.kakasi()

    def text_to_hiragana(value: str) -> str:
        return "".join(
            part.get("hira", part.get("kana", "")) for part in converter.convert(value)
        )

    return text_to_hiragana


def load_manifest(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as fh:
        items = json.load(fh)
    if not isinstance(items, list):
        raise ValueError(f"{path} must contain a JSON list")
    return items


def audit_rows(items: list[dict[str, Any]]) -> list[dict[str, str]]:
    text_to_hiragana = make_text_reader()
    findings: list[dict[str, str]] = []

    for item in items:
        filename = str(item.get("filename", ""))
        text = str(item.get("text", ""))
        display_text = str(item.get("display_text", ""))
        text_reading = text_to_hiragana(text)

        for match in ROMAJI_HINT_RE.finditer(display_text):
            hint = match.group(1).strip()
            if hint.lower() in IGNORE_HINTS:
                continue
            hint_reading = romaji_to_hiragana(hint)
            if not hint_reading or not text_reading:
                continue
            if hint_reading in text_reading or text_reading in hint_reading:
                continue
            findings.append(
                {
                    "filename": filename,
                    "tts_text": text,
                    "display_text": display_text,
                    "romaji_hint": hint,
                    "hint_reading": hint_reading,
                    "tts_text_reading": text_reading,
                    "note": str(item.get("pronunciation_note", "")),
                }
            )

    return findings


def write_report(path: Path, findings: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "JAPANESE AUDIO READING-HINT AUDIT",
        "=" * 80,
        "",
        "SUMMARY",
        f"  Findings: {len(findings)}",
        "",
    ]
    if findings:
        lines.extend(
            [
                "| filename | tts_text | display_text | romaji_hint | hint_reading | tts_text_reading | note |",
                "| --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for row in findings:
            lines.append(
                "| "
                + " | ".join(
                    row[key].replace("|", "\\|")
                    for key in (
                        "filename",
                        "tts_text",
                        "display_text",
                        "romaji_hint",
                        "hint_reading",
                        "tts_text_reading",
                        "note",
                    )
                )
                + " |"
            )
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--fail-on-findings", action="store_true")
    args = parser.parse_args()

    manifest = args.manifest
    if not manifest.is_absolute():
        manifest = AUDIO_DIR / manifest
    findings = audit_rows(load_manifest(manifest))
    write_report(args.report, findings)
    print(f"Wrote {len(findings)} findings to {args.report}")
    return 1 if args.fail_on_findings and findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
