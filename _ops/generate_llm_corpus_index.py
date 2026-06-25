from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LLM_ROOT = ROOT / "LLM"
TARGET = LLM_ROOT / "LLM Corpus Index.md"


ORDER = [
    "_root",
    "Pre-2017 — Before Transformers",
    "2017 — The Transformer",
    "2018–2019 — Pretrained Language Models",
    "2020–2021 — The Scaling Era",
    "2022 — Alignment and Chat",
    "2023 — Open Models and Agents",
    "2024–2025 — Frontier and Efficiency",
    "2026 — Reasoning and Agents",
    "Architecture Variants",
    "Study",
    "Sources",
    "_queries",
    "_raw",
    "_chunks",
    "_templates",
]

FAST_ROUTES = [
    ("Start here", "LLM/LLM", "Chronological MOC and era overview."),
    ("Learning path", "LLM/LLM — Learning Path", "Guided study sequence."),
    ("Complete corpus", "LLM/LLM Corpus Index", "This all-links map."),
    ("Study index", "LLM/Study/LLM Study Index", "Study notes, runners, labs, and drills."),
    ("Mastery dashboard", "LLM/Study/LLM Mastery Dashboard", "Daily navigation and next proof route."),
    ("Local hosting lab", "LLM/Study/Local LLM Hosting and Inference Lab", "Practical local model serving route."),
    ("Command cookbook", "LLM/Study/Local LLM Command Cookbook", "Copyable local inference commands."),
    ("End-to-end mental model", "LLM/Study/Local LLM End-to-End Mental Model", "From model artifact to response."),
    ("Mechanism bridge", "LLM/Study/LLM Mechanism-to-Inference Bridge Map", "Academic mechanisms to local controls."),
    ("Sources", "LLM/Sources/Sources Index", "Paper/source bibliography."),
]


def wikilink(path: str, label: str | None = None) -> str:
    clean_path = path.replace("\\", "/")
    clean_label = label or Path(path).stem
    if clean_label == clean_path:
        return f"[[{clean_path}]]"
    return f"[[{clean_path}|{clean_label}]]"


def note_target(path: Path) -> str:
    return path.relative_to(ROOT).with_suffix("").as_posix()


def top_group(path: Path) -> str:
    rel = path.relative_to(LLM_ROOT)
    parts = rel.parts
    return parts[0] if len(parts) > 1 else "_root"


def sort_key(path: Path) -> tuple[int, str]:
    group = top_group(path)
    group_index = ORDER.index(group) if group in ORDER else len(ORDER)
    return group_index, path.relative_to(LLM_ROOT).as_posix().casefold()


def collect_files() -> list[Path]:
    files = [p for p in LLM_ROOT.rglob("*.md") if p != TARGET]
    files.append(TARGET)
    return sorted(files, key=sort_key)


def section_title(group: str) -> str:
    if group == "_root":
        return "Root Navigation"
    if group.startswith("_"):
        return f"Evidence Layer: `{group}`"
    return group


def build() -> str:
    files = collect_files()
    grouped: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        grouped[top_group(path)].append(path)

    counts = Counter(top_group(path) for path in files)
    ordered_groups = [g for g in ORDER if g in grouped]
    ordered_groups.extend(sorted(g for g in grouped if g not in ORDER))

    lines: list[str] = [
        "---",
        "tags: [llm, index, corpus, navigation]",
        'up: "[[LLM/LLM]]"',
        "confidence: verified",
        "tier-coverage: [intuition, core, deep-dive, practice]",
        "---",
        "",
        "# LLM Corpus Index",
        "",
        "> **One-line summary** A complete linked map of every Markdown note in the LLM corpus, grouped for navigation instead of scattered across era, study, source, query, raw, and chunk layers.",
        "",
        f"Generated on {date.today().isoformat()} from `LLM/**/*.md` by `_ops/generate_llm_corpus_index.py`.",
        "",
        "This page is intentionally exhaustive. Use the fast routes first, then drop into the complete link map when you need to find a specific page, runner, paper note, chunk, or query.",
        "",
        "## Fast Routes",
        "",
    ]

    for label, target, description in FAST_ROUTES:
        lines.append(f"- **{label}:** {wikilink(target, Path(target).name)} — {description}")

    lines.extend(
        [
            "",
            "## Corpus Counts",
            "",
            f"- Total linked Markdown notes under `LLM/`: **{len(files)}**",
            "- Scope includes wiki articles, study notes, runners, labs, source indexes, raw paper notes, chunk evidence, queries, and templates.",
            "- Protected source layers are linked for navigation only; this index does not rewrite `_raw`, `_chunks`, or `_templates`.",
            "",
            "| Section | Linked notes |",
            "|---|---:|",
        ]
    )

    for group in ordered_groups:
        lines.append(f"| {section_title(group)} | {counts[group]} |")

    lines.extend(
        [
            "",
            "## How To Use This Index",
            "",
            "1. Use [[LLM/LLM|Large Language Models — A Chronicle]] when you want the story by era.",
            "2. Use [[LLM/Study/LLM Study Index|LLM Study Index]] when you want labs, runners, drills, and local hosting proof artifacts.",
            "3. Use this page when search fails, when a note is buried, or when you need to verify that a page exists somewhere in the corpus.",
            "4. Treat `_raw`, `_chunks`, and `_queries` as evidence layers, not the normal reading path.",
            "",
            "## Complete Link Map",
            "",
        ]
    )

    for group in ordered_groups:
        group_files = grouped[group]
        lines.extend([f"### {section_title(group)}", ""])
        for path in group_files:
            rel = path.relative_to(LLM_ROOT)
            label = path.stem
            suffix = ""
            if group != "_root":
                suffix = f" <small>`{rel.as_posix()}`</small>"
            lines.append(f"- {wikilink(note_target(path), label)}{suffix}")
        lines.append("")

    lines.extend(
        [
            "## Refresh Procedure",
            "",
            "Run this after adding, moving, or deleting LLM notes:",
            "",
            "```powershell",
            "python _ops\\generate_llm_corpus_index.py",
            "python _ops\\personal_kb.py index",
            "python _ops\\personal_kb.py audit",
            "```",
            "",
            "## References",
            "",
            "- [[LLM/Sources/Sources Index]]",
            "- [[LLM/LLM]]",
            "- [[LLM/Study/LLM Study Index]]",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> None:
    TARGET.write_text(build(), encoding="utf-8")
    print(f"wrote {TARGET}")


if __name__ == "__main__":
    main()
