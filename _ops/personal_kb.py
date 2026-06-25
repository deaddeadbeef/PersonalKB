#!/usr/bin/env python3
"""Maintenance utilities for the PersonalKB Obsidian vault."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "_ops" / "reports"

EXCLUDED_SCAN_PARTS = {".git"}
EXCLUDED_CONTENT_PARTS = {".git", ".tasks", "_ops"}
NON_WIKI_PARTS = {
    ".git",
    ".tasks",
    ".obsidian",
    "_ops",
    "_raw",
    "_chunks",
    "_templates",
    "_queries",
    "_audio",
}
ROOT_NON_ARTICLES = {"AGENTS.md", "index.md", "log.md", "Untitled.base"}
WIKI_QUALITY_DASHBOARD = "PersonalKB Wiki Quality Dashboard.md"
ROOT_NON_ARTICLES.add(WIKI_QUALITY_DASHBOARD)
PLACEHOLDER_RE = re.compile(
    r"\b(TBD|TODO|FIXME)\b|"
    r"Pending chunk extraction|"
    r"To be populated as chunks are created|"
    r"\{(?:Topic Name|What this is and why it matters|One sentence|Real-world comparison|Step-by-step description)\}"
)
WIKILINK_RE = re.compile(r"(!)?\[\[([^\]]+)\]\]")
WORD_RE = re.compile(r"\b[\w'-]+\b", re.UNICODE)
AUDIO_EMBED_RE = re.compile(r"!\[\[[^\]]+\.mp3(?:[#|][^\]]*)?\]\]", re.IGNORECASE)
AUDIO_EMBED_PAGE_LIMIT = 250
EMBED_RE = re.compile(r"!\[\[[^\]]+\]\]")
WIKILINK_INLINE_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")


@dataclass(frozen=True)
class Note:
    path: Path
    rel: str
    title: str
    text: str


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def all_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and not any(part in EXCLUDED_SCAN_PARTS for part in path.parts)
    ]


def markdown_files() -> list[Path]:
    return [path for path in all_files() if path.suffix.lower() == ".md"]


def content_markdown_files() -> list[Path]:
    return [
        path
        for path in markdown_files()
        if path.name != WIKI_QUALITY_DASHBOARD
        and set(path.relative_to(ROOT).parts).isdisjoint(EXCLUDED_CONTENT_PARTS)
    ]


def is_wiki_article(path: Path) -> bool:
    if path.name in ROOT_NON_ARTICLES:
        return False
    rel_parts = path.relative_to(ROOT).parts
    parts = set(rel_parts)
    return (
        path.suffix.lower() == ".md"
        and parts.isdisjoint(NON_WIKI_PARTS)
        and not any(part.startswith("_") for part in rel_parts)
    )


def strip_frontmatter(text: str) -> str:
    match = re.match(r"\A---\s*\r?\n.*?\r?\n---\s*\r?\n", text, flags=re.DOTALL)
    return text[match.end() :] if match else text


def frontmatter(text: str) -> str:
    match = re.match(r"\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|$)", text, flags=re.DOTALL)
    if not match:
        return ""
    return match.group(1).strip()


def first_heading(path: Path, text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return clean_index_text(line[2:])
    return path.stem


def one_line_summary(text: str) -> str:
    body = strip_frontmatter(text)
    for line in body.splitlines():
        cleaned = line.strip()
        if cleaned.startswith(">"):
            cleaned = cleaned.lstrip("> ").strip()
            cleaned = re.sub(r"\*\*One-line summary\*\*:?", "", cleaned).strip()
            if cleaned:
                return truncate(clean_index_text(cleaned))
    for line in body.splitlines():
        cleaned = line.strip()
        if not cleaned or cleaned in {"---", "***"}:
            continue
        if cleaned.startswith("#") or cleaned.startswith("|") or cleaned.startswith("```"):
            continue
        if cleaned.startswith("- ") or cleaned.startswith("* "):
            continue
        return truncate(clean_index_text(cleaned))
    return ""


def clean_index_text(value: str) -> str:
    value = AUDIO_EMBED_RE.sub("", value)
    value = EMBED_RE.sub("", value)

    def replace_link(match: re.Match[str]) -> str:
        target = match.group(1).replace("\\", "/").strip()
        display = match.group(2)
        if display:
            return display.strip()
        return target.rsplit("/", 1)[-1].strip()

    value = WIKILINK_INLINE_RE.sub(replace_link, value)
    return re.sub(r"\s+", " ", value).strip(" -")


def truncate(value: str, limit: int = 180) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "..."


def word_count(text: str) -> int:
    return len(WORD_RE.findall(strip_frontmatter(text)))


def wikilink_targets(text: str) -> Iterable[tuple[str, bool]]:
    for match in WIKILINK_RE.finditer(text):
        raw = match.group(2)
        target = raw.split("|", 1)[0].strip()
        if target:
            yield target, bool(match.group(1))


def build_link_index(files: list[Path]) -> tuple[set[str], set[str], dict[str, Path]]:
    note_keys: set[str] = set()
    file_keys: set[str] = set()
    note_key_to_path: dict[str, Path] = {}
    note_keys.add(Path(WIKI_QUALITY_DASHBOARD).stem.lower())
    note_keys.add(Path(WIKI_QUALITY_DASHBOARD).with_suffix("").as_posix().lower())
    for path in files:
        file_keys.add(path.name.lower())
        if path.suffix.lower() != ".md":
            continue
        base = path.stem.lower()
        note_keys.add(base)
        note_key_to_path.setdefault(base, path)
        path_key = rel(path)[:-3].lower()
        note_keys.add(path_key)
        note_key_to_path.setdefault(path_key, path)
    return note_keys, file_keys, note_key_to_path


def resolve_wikilink(target: str, note_keys: set[str], file_keys: set[str]) -> bool:
    normalized = target.replace("\\", "/").strip().lower()
    if normalized in note_keys:
        return True
    if Path(normalized).name in note_keys:
        return True
    if "#" in normalized:
        anchorless = normalized.split("#", 1)[0].strip()
        if anchorless in note_keys:
            return True
        if Path(anchorless).name in note_keys:
            return True
    suffix = Path(target).suffix.lower()
    if suffix:
        if file_keys.__contains__(Path(target).name.lower()):
            return True
        return (ROOT / target).exists()
    return False


def obsidian_link(path: Path, title: str | None = None) -> str:
    target = rel(path)
    if target.lower().endswith(".md"):
        target = target[:-3]
    display = title or path.stem
    if target == display:
        return f"[[{target}]]"
    return f"[[{target}|{display}]]"


def load_notes(paths: Iterable[Path]) -> list[Note]:
    notes = []
    for path in paths:
        text = read_text(path)
        notes.append(Note(path=path, rel=rel(path), title=first_heading(path, text), text=text))
    return notes


def audit() -> dict[str, object]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    files = all_files()
    md_files = markdown_files()
    content_md_files = content_markdown_files()
    article_paths = [path for path in md_files if is_wiki_article(path)]
    articles = load_notes(article_paths)
    note_keys, file_keys, note_key_to_path = build_link_index(files)

    by_extension = Counter(path.suffix.lower() or "(none)" for path in files)
    empty_notes = [note for note in articles if not note.text.strip()]
    stubs = [note for note in articles if note.text.strip() and len(note.text.encode("utf-8")) < 1500]
    missing_up = [note for note in articles if "up:" not in frontmatter(note.text)]
    missing_confidence = [note for note in articles if "confidence:" not in frontmatter(note.text)]
    missing_references = [
        note
        for note in articles
        if not re.search(r"^## References\s*$", note.text, flags=re.MULTILINE)
    ]

    placeholder_hits = []
    for note in load_notes(content_md_files):
        for line_no, line in enumerate(note.text.splitlines(), start=1):
            if PLACEHOLDER_RE.search(line):
                placeholder_hits.append({"file": note.rel, "line": line_no, "text": line.strip()})

    reader_placeholder_hits = []
    for note in articles:
        for line_no, line in enumerate(note.text.splitlines(), start=1):
            if PLACEHOLDER_RE.search(line):
                reader_placeholder_hits.append({"file": note.rel, "line": line_no, "text": line.strip()})

    heavy_audio_embed_pages = []
    for note in load_notes(content_md_files):
        audio_embeds = len(AUDIO_EMBED_RE.findall(note.text))
        if audio_embeds > AUDIO_EMBED_PAGE_LIMIT:
            heavy_audio_embed_pages.append(
                {"file": note.rel, "audio_embeds": audio_embeds, "limit": AUDIO_EMBED_PAGE_LIMIT}
            )

    broken_links = []
    inbound = Counter()
    for note in load_notes(content_md_files):
        for target, embedded in wikilink_targets(note.text):
            if not resolve_wikilink(target, note_keys, file_keys):
                broken_links.append({"file": note.rel, "target": target, "embedded": embedded})
                continue
            key = target.replace("\\", "/").split("/")[-1].lower()
            inbound[key] += 1
            full_key = target.replace("\\", "/").lower()
            inbound[full_key] += 1

    reader_broken_links = []
    for note in articles:
        for target, embedded in wikilink_targets(note.text):
            if not resolve_wikilink(target, note_keys, file_keys):
                reader_broken_links.append({"file": note.rel, "target": target, "embedded": embedded})

    orphans = []
    for note in articles:
        base = note.path.stem.lower()
        full = rel(note.path)[:-3].lower()
        if inbound[base] == 0 and inbound[full] == 0:
            orphans.append(note)

    summary = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "root": str(ROOT),
        "files_total": len(files),
        "by_extension": dict(sorted(by_extension.items())),
        "markdown_files": len(md_files),
        "candidate_articles": len(articles),
        "empty_notes": len(empty_notes),
        "stubs_under_1500_bytes": len(stubs),
        "missing_up": len(missing_up),
        "missing_confidence": len(missing_confidence),
        "missing_references": len(missing_references),
        "placeholder_hits": len(placeholder_hits),
        "reader_placeholder_hits": len(reader_placeholder_hits),
        "heavy_audio_embed_pages": len(heavy_audio_embed_pages),
        "broken_link_occurrences": len(broken_links),
        "reader_broken_link_occurrences": len(reader_broken_links),
        "orphan_articles": len(orphans),
    }

    write_json(REPORT_DIR / "audit-summary.json", summary)
    write_json(REPORT_DIR / "wiki-quality-summary.json", summary)
    write_note_list(REPORT_DIR / "audit-empty-notes.md", "Empty Notes", empty_notes)
    write_note_list(REPORT_DIR / "audit-stubs.md", "Stubs Under 1500 Bytes", stubs)
    write_note_list(REPORT_DIR / "audit-missing-up.md", "Missing up Frontmatter", missing_up)
    write_note_list(REPORT_DIR / "audit-missing-confidence.md", "Missing confidence Frontmatter", missing_confidence)
    write_note_list(REPORT_DIR / "audit-missing-references.md", "Missing References Section", missing_references)
    write_rows(REPORT_DIR / "audit-placeholder-hits.md", "Placeholder Hits", placeholder_hits, ["file", "line", "text"])
    write_rows(
        REPORT_DIR / "wiki-placeholder-hits.md",
        "Reader-Facing Placeholder Hits",
        reader_placeholder_hits,
        ["file", "line", "text"],
    )
    write_rows(
        REPORT_DIR / "audit-heavy-audio-embed-pages.md",
        "Heavy Audio Embed Pages",
        heavy_audio_embed_pages,
        ["file", "audio_embeds", "limit"],
    )
    write_rows(REPORT_DIR / "audit-broken-links.md", "Broken Wiki Links", broken_links, ["file", "target", "embedded"])
    write_rows(
        REPORT_DIR / "wiki-broken-links.md",
        "Reader-Facing Broken Wiki Links",
        reader_broken_links,
        ["file", "target", "embedded"],
    )
    write_note_list(REPORT_DIR / "audit-orphans.md", "Orphan Articles", orphans)
    write_wiki_quality_dashboard(
        summary=summary,
        missing_up=missing_up,
        missing_confidence=missing_confidence,
        missing_references=missing_references,
        reader_placeholder_hits=reader_placeholder_hits,
        reader_broken_links=reader_broken_links,
        stubs=stubs,
        orphans=orphans,
    )

    return summary


def wiki_quality_verdict(summary: dict[str, object]) -> str:
    reader_broken = int(summary["reader_broken_link_occurrences"])
    reader_placeholders = int(summary["reader_placeholder_hits"])
    missing_refs = int(summary["missing_references"])
    missing_confidence = int(summary["missing_confidence"])
    if reader_broken == 0 and reader_placeholders == 0 and missing_refs == 0 and missing_confidence == 0:
        return "Ready as a clean reference wiki."
    if reader_broken == 0 and reader_placeholders == 0:
        return "Good enough for guided reading, but not yet clean enough to call finished."
    return "Readable with the new book spines, but not yet good enough as a polished wiki."


def report_link(path: str, label: str) -> str:
    return f"[{label}](<{path}>)"


def write_wiki_quality_dashboard(
    *,
    summary: dict[str, object],
    missing_up: list[Note],
    missing_confidence: list[Note],
    missing_references: list[Note],
    reader_placeholder_hits: list[dict[str, object]],
    reader_broken_links: list[dict[str, object]],
    stubs: list[Note],
    orphans: list[Note],
) -> None:
    verdict = wiki_quality_verdict(summary)
    lines = [
        "---",
        "type: generated-quality-dashboard",
        "tags: [vault-index, quality, audit, navigation]",
        'up: "[[PersonalKB Book Reading Guide]]"',
        "confidence: verified",
        "tier-coverage: [core, practice]",
        "---",
        "# PersonalKB Wiki Quality Dashboard",
        "",
        "## Verdict",
        "",
        verdict,
        "",
        "The wiki is now navigable as a reading shelf because every committed top-level topic has a book-style spine. It is not yet clean as a finished reference set because reader-facing pages still have unresolved links, placeholder lines, and incomplete provenance metadata.",
        "",
        "## Reader-Facing Wiki Health",
        "",
        "| Check | Count | Meaning |",
        "| --- | ---: | --- |",
        f"| Candidate reader-facing articles | {summary['candidate_articles']} | Wiki pages outside raw, chunk, query, template, audio, task, and ops layers |",
        f"| Broken links in reader-facing articles | {summary['reader_broken_link_occurrences']} | Navigation defects that affect normal reading |",
        f"| Placeholder lines in reader-facing articles | {summary['reader_placeholder_hits']} | Draft markers visible to readers |",
        f"| Missing references sections | {summary['missing_references']} | Pages that still need a source/provenance footer |",
        f"| Missing confidence frontmatter | {summary['missing_confidence']} | Pages without confidence classification |",
        f"| Missing up frontmatter | {summary['missing_up']} | Pages without explicit parent navigation |",
        f"| Stubs under 1500 bytes | {summary['stubs_under_1500_bytes']} | Thin pages that may not carry their topic yet |",
        f"| Empty notes | {summary['empty_notes']} | Notes with no body text |",
        f"| Orphan articles | {summary['orphan_articles']} | Reader-facing pages with no inbound wikilinks |",
        "",
        "## Maintenance-Layer Noise",
        "",
        "These counts are still useful, but they include chunks, templates, queries, schema examples, and operational notes. Do not use them alone to judge reading quality.",
        "",
        "| Check | Count |",
        "| --- | ---: |",
        f"| All broken wikilink occurrences | {summary['broken_link_occurrences']} |",
        f"| All placeholder hits | {summary['placeholder_hits']} |",
        f"| Heavy audio embed pages | {summary['heavy_audio_embed_pages']} |",
        "",
        "## Next Housekeeping Order",
        "",
        "1. Fix reader-facing broken links first; they interrupt reading and graph traversal.",
        "2. Remove visible placeholder lines from reader-facing LLM and SpaceX pages.",
        "3. Add references sections and confidence frontmatter to high-traffic book-spine targets.",
        "4. Only then spend time on chunk/query/template noise.",
        "",
        "## Top Reader-Facing Broken Links",
        "",
    ]
    if reader_broken_links:
        for row in reader_broken_links[:25]:
            lines.append(f"- `{row['file']}` -> `{row['target']}`")
    else:
        lines.append("- None.")

    lines.extend(["", "## Top Reader-Facing Placeholder Hits", ""])
    if reader_placeholder_hits:
        for row in reader_placeholder_hits[:25]:
            lines.append(f"- `{row['file']}:{row['line']}` -> {row['text']}")
    else:
        lines.append("- None.")

    lines.extend(
        [
            "",
            "## Report Files",
            "",
            f"- {report_link('_ops/reports/wiki-quality-summary.json', 'Reader-facing quality summary JSON')}",
            f"- {report_link('_ops/reports/wiki-broken-links.md', 'Reader-facing broken links')}",
            f"- {report_link('_ops/reports/wiki-placeholder-hits.md', 'Reader-facing placeholder hits')}",
            f"- {report_link('_ops/reports/audit-summary.json', 'Full audit summary JSON')}",
            f"- {report_link('_ops/reports/audit-broken-links.md', 'Full broken-link report')}",
            f"- {report_link('_ops/reports/audit-placeholder-hits.md', 'Full placeholder report')}",
            "",
            "## References",
            "",
            "- [[PersonalKB Book Reading Guide]]",
            "- [[index|PersonalKB Index]]",
            "- [[log|PersonalKB Maintenance Log]]",
            f"- {report_link('_ops/reports/wiki-quality-summary.json', 'Generated wiki quality summary')}",
            f"- {report_link('_ops/reports/audit-summary.json', 'Generated full audit summary')}",
            "",
            f"Generated: {summary['generated_at']}",
            "",
        ]
    )
    (ROOT / WIKI_QUALITY_DASHBOARD).write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_note_list(path: Path, title: str, notes: list[Note]) -> None:
    lines = [f"# {title}", "", f"Count: {len(notes)}", ""]
    for note in sorted(notes, key=lambda item: item.rel.lower()):
        lines.append(f"- {obsidian_link(note.path, note.title)} (`{note.rel}`)")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_rows(path: Path, title: str, rows: list[dict[str, object]], columns: list[str]) -> None:
    lines = [f"# {title}", "", f"Count: {len(rows)}", ""]
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for row in rows:
        values = [str(row.get(column, "")).replace("|", "\\|") for column in columns]
        lines.append("| " + " | ".join(values) + " |")
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_index() -> None:
    articles = load_notes(path for path in markdown_files() if is_wiki_article(path))
    grouped: dict[str, list[Note]] = defaultdict(list)
    for note in articles:
        first = note.path.relative_to(ROOT).parts[0]
        group = "Root" if note.path.parent == ROOT else first
        grouped[group].append(note)

    lines = [
        "---",
        "type: generated-index",
        "tags: [vault-index, generated]",
        "---",
        "# PersonalKB Index",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "This file is generated by `_ops/personal_kb.py index`. Use it as the first navigation stop for agent queries.",
        "",
    ]
    for group in sorted(grouped):
        notes = sorted(grouped[group], key=lambda item: item.rel.lower())
        lines.extend([f"## {group}", ""])
        for note in notes:
            summary = one_line_summary(note.text)
            wc = word_count(note.text)
            suffix = f" - {summary}" if summary else ""
            lines.append(f"- {obsidian_link(note.path, note.title)} ({wc} words){suffix}")
        lines.append("")

    (ROOT / "index.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def init_log() -> None:
    path = ROOT / "log.md"
    if path.exists():
        return
    lines = [
        "---",
        "type: maintenance-log",
        "tags: [vault-log, generated]",
        "---",
        "# PersonalKB Maintenance Log",
        "",
        "Append-only record of ingest, query, lint, and refinement operations.",
        "",
        f"## [{datetime.now().date()}] setup | LLM wiki operating loop",
        "",
        "Scope: initialized agent schema, audit tooling, generated index, and maintenance log.",
        "",
        "Changed files:",
        "- `AGENTS.md`",
        "- `_ops/`",
        "- `index.md`",
        "- `log.md`",
        "",
        "Verification:",
        "- `python _ops/personal_kb.py audit`",
        "- `python _ops/personal_kb.py index`",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("audit", help="write audit reports to _ops/reports")
    subparsers.add_parser("index", help="regenerate root index.md")
    subparsers.add_parser("init-log", help="create log.md if it does not exist")
    args = parser.parse_args()

    if args.command == "audit":
        print(json.dumps(audit(), indent=2, ensure_ascii=False))
    elif args.command == "index":
        write_index()
        print(f"wrote {ROOT / 'index.md'}")
    elif args.command == "init-log":
        init_log()
        print(f"ready {ROOT / 'log.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
