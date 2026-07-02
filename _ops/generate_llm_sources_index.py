#!/usr/bin/env python3
"""Regenerate the LLM source index from raw-note metadata."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "LLM" / "_raw"
TARGET = ROOT / "LLM" / "Sources" / "Sources Index.md"


@dataclass(frozen=True)
class RawSource:
    number: int
    path: Path
    title: str
    authors: str
    year: str
    source_type: str


SECTIONS = (
    ("Foundational Papers", range(1, 11)),
    ("Architecture and Training", range(11, 21)),
    ("Methods and Applications", range(21, 31)),
    ("Extended Catalog", range(31, 61)),
    ("Reasoning and Agents", range(61, 76)),
)


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|$)", text, flags=re.DOTALL)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def normalize_authors(value: str) -> str:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        value = value[1:-1].strip()
    return value or "Unknown"


def note_target(path: Path) -> str:
    return path.relative_to(ROOT).with_suffix("").as_posix()


def wikilink(path: Path, label: str) -> str:
    return f"[[{note_target(path)}|{label}]]"


def load_sources() -> list[RawSource]:
    sources: list[RawSource] = []
    for path in sorted(RAW_ROOT.glob("raw-llm-*.md")):
        match = re.match(r"raw-llm-(\d{3})", path.name)
        if not match:
            continue
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        number = int(match.group(1))
        title = meta.get("title") or meta.get("source_title") or first_heading(text, path.stem)
        authors = normalize_authors(meta.get("author") or meta.get("authors") or "Unknown")
        year = meta.get("year") or "Unknown"
        source_type = meta.get("source_type") or "paper"
        sources.append(
            RawSource(
                number=number,
                path=path,
                title=title,
                authors=authors,
                year=year,
                source_type=source_type,
            )
        )
    return sorted(sources, key=lambda source: source.number)


def section_for(number: int) -> str:
    for section, numbers in SECTIONS:
        if number in numbers:
            return section
    return "Other Sources"


def build() -> str:
    sources = load_sources()
    grouped: dict[str, list[RawSource]] = {section: [] for section, _ in SECTIONS}
    grouped["Other Sources"] = []
    for source in sources:
        grouped[section_for(source.number)].append(source)

    lines = [
        "---",
        "tags: [index, llm, sources]",
        'up: "[[LLM/LLM]]"',
        "confidence: verified",
        "freshness: stable",
        "tier-coverage: [core, deep-dive, provenance]",
        "---",
        "",
        "# Sources Index - LLM",
        "",
        "> **One-line summary** A provenance map for the LLM wiki, generated from the raw source notes so every paper link points to an existing note.",
        "",
        "This note anchors the sources used in the LLM knowledge base. Each row links to a raw source note; use the article pages and book spine for normal reading, and use this index when you need provenance.",
        "",
        f"Total raw source notes: **{len(sources)}**",
        "",
        "## How To Use Sources",
        "",
        "| Need | Use | Evidence habit |",
        "|---|---|---|",
        "| Verify an architecture or training claim | Start with the relevant paper row, then return to [[LLM/LLM Book Reading Spine|LLM Book Reading Spine]] | Capture claim, paper, year, mechanism, limitation, and the article that reused it |",
        "| Connect papers to local inference | Pair this index with [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] | State the local implication and the run sheet, benchmark, or evaluation that could test it |",
        "| Compare model families or eras | Use the paper groups below, then read the matching era overview | Keep chronology explicit so later models are not used as evidence for earlier claims |",
        "| Reuse a current model or vendor claim | Check the raw note date and treat product claims as freshness-sensitive | Add an as-of date before using the claim in deployment or model-selection notes |",
        "",
    ]

    for section, _ in SECTIONS:
        rows = grouped.get(section, [])
        if not rows:
            continue
        lines.extend(
            [
                f"## {section}",
                "",
                "| # | Title | Authors | Year | Type | Raw Note |",
                "|---:|---|---|---:|---|---|",
            ]
        )
        for source in rows:
            lines.append(
                f"| {source.number:03d} | {source.title} | {source.authors} | {source.year} | {source.source_type} | {wikilink(source.path, f'raw-llm-{source.number:03d}')} |"
            )
        lines.append("")

    other = grouped.get("Other Sources", [])
    if other:
        lines.extend(
            [
                "## Other Sources",
                "",
                "| # | Title | Authors | Year | Type | Raw Note |",
                "|---:|---|---|---:|---|---|",
            ]
        )
        for source in other:
            lines.append(
                f"| {source.number:03d} | {source.title} | {source.authors} | {source.year} | {source.source_type} | {wikilink(source.path, f'raw-llm-{source.number:03d}')} |"
            )
        lines.append("")

    lines.extend(
        [
            "## References",
            "",
            "- [[LLM/LLM|Large Language Models - A Chronicle]]",
            "- [[LLM/LLM Corpus Index]]",
            "- [[LLM/LLM Book Reading Spine]]",
            "",
            "Refresh with `python _ops\\generate_llm_sources_index.py` after adding or renaming raw LLM source notes.",
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    TARGET.write_text(build(), encoding="utf-8")
    print(f"wrote {TARGET}")


if __name__ == "__main__":
    main()
