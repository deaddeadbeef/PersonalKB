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
PROTECTED_CONTENT_PARTS = {"_raw", "_chunks", "_templates"}
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
    r"\bPlaceholder for\b|"
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
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
DIAGRAM_DIRECTIVE_RE = re.compile(
    r"^(?:flowchart|graph)\s+(?:TD|TB|BT|LR|RL)\b|"
    r"^(?:sequenceDiagram|classDiagram|stateDiagram-v2|erDiagram|journey|gantt|pie|mindmap|timeline|gitGraph)\b"
)
GENERIC_SUMMARY_RE = re.compile(
    r"(?:The Core Idea:\s*)?Understanding .* is fundamental|"
    r"(?:Analogy:\s*)?Each concept in Japanese has parallels|"
    r"(?:Why It Matters:\s*)?You'll encounter this in everyday Japanese"
)
SUMMARY_LABEL_RE = re.compile(
    r"^(?:One-line summary:?|The Core Idea:|Analogy:|Why It Matters:|Philosophy:|Best For:|Who Uses It:)\s*",
    re.IGNORECASE,
)
ROUTE_SUMMARY_SKIP_RE = re.compile(
    r"^(?:\d+\.\s|Use sources in this order:|Every .* needs three things:|Pick exactly one|Create a dated copy|Do this once:|"
    r"Use this path|Navigation table|This note is|"
    r"(?:Author|Designer|Paradigm|Typing|Memory|Compiled|Executed|Publisher|Level|Source):)"
)
TITLE_FIRST_SUMMARY_RE = re.compile(
    r"\b(?:DS Review|Review Drill|Audio Assignment Ladder|Weekly Review|Audio Coverage Map|"
    r"Authentic Audio Spine|Keigo and Register Production Checklist|Pitch Accent Practice Path|"
    r"Study Plan|Learning Path|Study Index|Sources Index|Chapter Index|Language Profile|"
    r"Algorithms Unlocked|Modern Operating Systems|Priority Queues and Heaps)\b",
    re.IGNORECASE,
)
SUMMARY_ABBREVIATIONS = {
    "al.",
    "ch.",
    "dr.",
    "e.g.",
    "ed.",
    "eds.",
    "etc.",
    "fig.",
    "i.e.",
    "jr.",
    "mr.",
    "mrs.",
    "ms.",
    "no.",
    "prof.",
    "sr.",
    "st.",
    "vs.",
}
GENERATED_SUMMARY_NOISE_PATTERN = (
    r"(?: -|—) (?:flowchart|graph|sequenceDiagram|classDiagram|stateDiagram-v2|"
    r"erDiagram|journey|gantt|pie|mindmap|timeline|gitGraph)\b|"
    r"(?: -|—) (?:The Core Idea:\s*)?Understanding .* is fundamental|"
    r"(?: -|—) (?:One-line summary|The Core Idea|Analogy|Why It Matters):|"
    r"(?: -|—) (?:私|これは|お世話|乾杯|はじめまして|いらっしゃいませ|らりるれろ|Staff:|→ Sources Index|\[!)|"
    r"(?: -|—) (?:\d+\.\s|Use sources in this order:|Every .* needs three things:|Pick exactly one|Create a dated copy|Do this once:)|"
    r"(?: -|—) (?:Use this path|Navigation table|This note is|"
    r"(?:Author|Designer|Paradigm|Typing|Memory|Compiled|Executed|Publisher|Level|Source):)|"
    r"(?: -|—) .*\.{3}$|"
    r"^- \[\[[^\]\n]+\]\](?: \(\d+ words\))?[ \t]*(?:-|—)[ \t]*[^.!?\n]+$|"
    r"^- \[\[LLM/(?!Sources/Sources Index(?:\|[^\]]+)?\]\]|LLM Corpus Index(?:\|[^\]]+)?\]\]|Study/LLM Study Index(?:\|[^\]]+)?\]\])"
    r"[^\]]+\]\]\s*$"
)
FRESHNESS_REVIEW_MARKER_RE = re.compile(
    r"(?im)^(?:last[-_]verified|as[-_]of|source[-_]date)\s*:|"
    r"\b(?:last verified|last checked|as of)\b"
)


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


def has_any_part(path_or_rel: Path | str, parts: set[str]) -> bool:
    if isinstance(path_or_rel, Path):
        path_parts = path_or_rel.relative_to(ROOT).parts
    else:
        path_parts = Path(path_or_rel).parts
    return any(part in parts for part in path_parts)


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
    text = text.lstrip("\ufeff")
    match = re.match(r"\A---\s*\r?\n.*?\r?\n---\s*\r?\n", text, flags=re.DOTALL)
    return text[match.end() :] if match else text


def frontmatter(text: str) -> str:
    text = text.lstrip("\ufeff")
    match = re.match(r"\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|$)", text, flags=re.DOTALL)
    if not match:
        return ""
    return match.group(1).strip()


def frontmatter_field(text: str, field: str) -> str:
    match = re.search(rf"(?im)^{re.escape(field)}\s*:\s*(.+?)\s*$", frontmatter(text))
    if not match:
        return ""
    return match.group(1).strip().strip("\"'")


def freshness_value(text: str) -> str:
    return frontmatter_field(text, "freshness").lower()


def has_freshness_review_marker(text: str) -> bool:
    return bool(FRESHNESS_REVIEW_MARKER_RE.search(text))


def references_body(text: str) -> str | None:
    match = re.search(r"^## References\s*$", text, flags=re.MULTILINE)
    if not match:
        return None
    body = text[match.end() :]
    next_heading = re.search(r"^##\s+", body, flags=re.MULTILINE)
    if next_heading:
        body = body[: next_heading.start()]
    return body.strip()


def strip_code_fences(text: str) -> str:
    text = text.lstrip("\ufeff")
    return re.sub(r"^```.*?^```\s*", "", text, flags=re.MULTILINE | re.DOTALL)


def first_heading(path: Path, text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return clean_index_text(line[2:])
    return path.stem


def fallback_summary_for_title(title: str) -> str:
    title = clean_index_text(title)
    if not title:
        return ""
    if title == "Algorithms Unlocked":
        return "Primary algorithms textbook route through correctness, growth rates, sorting, graphs, strings, cryptography, compression, and complexity."
    if title == "Modern Operating Systems":
        return "Primary operating-systems textbook route through processes, memory, file systems, I/O, virtualization, multiprocessors, security, and case studies."
    if title == "Priority Queues and Heaps":
        return "Navigation guide for choosing the right heap or priority-queue implementation."
    if "Language Profile" in title:
        topic = re.sub(r"\s*[—-]\s*Language Profile\b", "", title, flags=re.IGNORECASE).strip(" -—")
        return f"Language profile for {topic}, covering philosophy, runtime model, strengths, tradeoffs, and ecosystem." if topic else "Language profile covering philosophy, runtime model, strengths, tradeoffs, and ecosystem."
    if "Learning Path" in title:
        topic = re.sub(r"\s*[—-]\s*Learning Path\b", "", title, flags=re.IGNORECASE).strip(" -—")
        return f"Pass-based learning path for {topic}." if topic else "Pass-based learning path."
    if "Study Index" in title:
        topic = re.sub(r"\s*Study Index\b", "", title, flags=re.IGNORECASE).strip(" -—")
        return f"Study router for {topic} drills, labs, proof artifacts, and review sessions." if topic else "Study router for drills, labs, proof artifacts, and review sessions."
    if "Sources Index" in title or "Recipe Sources Index" in title:
        topic = re.sub(r"\s*(?:Recipe )?Sources Index\b", "", title, flags=re.IGNORECASE).strip(" -—")
        return f"Source and provenance map for {topic}." if topic else "Source and provenance map."
    if "Chapter Index" in title:
        topic = re.sub(r"^Chapter Index\s*[—-]?\s*", "", title, flags=re.IGNORECASE).strip(" -—")
        return f"Chapter-by-chapter route through {topic}." if topic else "Chapter-by-chapter route through the source text."
    if title.startswith("DS Review"):
        topic = re.sub(r"^DS Review\s*[—-]\s*", "", title).strip(" -—")
        return f"Data structures review drill for {topic}." if topic else "Data structures review drill."
    if re.search(r"\bReview Drill\b", title, flags=re.IGNORECASE):
        topic = re.sub(r"\s*[—-]\s*Review Drill\b", "", title, flags=re.IGNORECASE)
        topic = re.sub(r"^Review Drill\s*[—-]\s*", "", topic, flags=re.IGNORECASE).strip(" -—")
        return f"Review drill for {topic}." if topic else "Review drill for active recall."
    if "Audio Assignment Ladder" in title:
        topic = title.replace("Audio Assignment Ladder", "").strip(" -—")
        return f"Audio assignment ladder for {topic}." if topic else "Audio assignment ladder."
    if "Weekly Review" in title:
        topic = title.replace("Weekly Review", "").strip(" -—")
        return f"Weekly review checklist for {topic}." if topic else "Weekly review checklist."
    if "Audio Coverage Map" in title:
        topic = title.replace("Audio Coverage Map", "").strip(" -—")
        return f"Audio coverage map for {topic}." if topic else "Audio coverage map."
    if "Authentic Audio Spine" in title:
        topic = title.replace("Authentic Audio Spine", "").strip(" -—")
        return f"Authentic-audio route for {topic}." if topic else "Authentic-audio route."
    if "Keigo and Register Production Checklist" in title:
        return "Production checklist for keigo and register-sensitive output."
    if "Pitch Accent Practice Path" in title:
        return "Practice path for pitch-accent awareness and correction."
    if "Study Plan" in title:
        topic = title.replace("Japanese Study Plan", "").replace("Study Plan", "").strip(" -—")
        return f"Study plan for {topic}." if topic else "Study plan."
    return ""


def prefer_title_summary(title: str) -> bool:
    return bool(TITLE_FIRST_SUMMARY_RE.search(title))


def one_line_summary_blocks(text: str) -> list[str]:
    blocks: list[str] = []
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        cleaned = lines[index].strip()
        if cleaned.startswith(">") and re.search(r"\bOne-line summary\b", cleaned, flags=re.IGNORECASE):
            block: list[str] = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                block.append(lines[index].strip().lstrip("> ").strip())
                index += 1
            value = " ".join(block)
            value = re.sub(r"\*\*One-line summary:?\*\*:?", "", value, flags=re.IGNORECASE).strip()
            if value:
                blocks.append(value)
            continue
        index += 1
    return blocks


def paragraph_summary_candidates(text: str) -> list[str]:
    candidates: list[str] = []
    block: list[str] = []

    def flush() -> None:
        if block:
            candidates.append(" ".join(block).strip())
            block.clear()

    for line in text.splitlines():
        cleaned = line.strip()
        if not cleaned or cleaned in {"---", "***"}:
            flush()
            continue
        if (
            cleaned.startswith("#")
            or cleaned.startswith("|")
            or cleaned.startswith(">")
            or cleaned.startswith("→")
            or cleaned.startswith("```")
            or cleaned.startswith("- ")
            or cleaned.startswith("* ")
            or DIAGRAM_DIRECTIVE_RE.match(cleaned)
            or ROUTE_SUMMARY_SKIP_RE.match(cleaned)
            or GENERIC_SUMMARY_RE.search(cleaned)
            or GENERIC_SUMMARY_RE.search(clean_index_text(cleaned))
        ):
            flush()
            continue
        block.append(cleaned)
    flush()
    return candidates


def one_line_summary(text: str, title: str = "") -> str:
    body = strip_code_fences(strip_frontmatter(text))
    for cleaned in one_line_summary_blocks(body):
        return truncate(clean_index_text(cleaned))
    fallback = fallback_summary_for_title(title)
    if fallback and prefer_title_summary(title):
        return truncate(fallback)
    for candidate in paragraph_summary_candidates(body):
        cleaned_text = clean_index_text(candidate)
        if (
            not cleaned_text
            or ROUTE_SUMMARY_SKIP_RE.match(cleaned_text)
            or GENERIC_SUMMARY_RE.search(cleaned_text)
        ):
            continue
        if cleaned_text:
            return truncate(cleaned_text)
    return truncate(fallback)


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
    value = value.replace("**", "").replace("__", "").replace("*", "")
    value = value.replace("`", "")
    value = SUMMARY_LABEL_RE.sub("", value)
    return re.sub(r"\s+", " ", value).strip(" -")


def finish_summary(value: str) -> str:
    value = value.strip().rstrip(" ,;:—-")
    if not value:
        return value
    if re.search(r'[.!?][)"\']?$', value):
        return value
    return f"{value}."


def truncate(value: str, limit: int = 220) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= limit:
        return finish_summary(value)
    minimum = min(80, max(40, limit // 3))
    sentence_ends = [
        match.start()
        for match in re.finditer(r"(?<=[.!?])\s+", value)
        if minimum <= match.start() <= limit and is_sentence_boundary(value, match.start())
    ]
    if sentence_ends:
        return finish_summary(value[: sentence_ends[-1]])
    for delimiter in ("; ", ": ", " — ", " - ", ", "):
        boundary = value.rfind(delimiter, 0, limit + 1)
        if boundary >= minimum:
            return finish_summary(value[:boundary])
    boundary = value.rfind(" ", 0, limit + 1)
    if boundary >= minimum:
        return finish_summary(value[:boundary])
    return finish_summary(value[:limit])


def is_sentence_boundary(value: str, boundary: int) -> bool:
    token = value[:boundary].strip().rsplit(" ", 1)[-1]
    bare = token.rstrip(".!?")
    if re.fullmatch(r"[A-Z]", bare):
        return False
    return token.lower() not in SUMMARY_ABBREVIATIONS


def word_count(text: str) -> int:
    return len(WORD_RE.findall(strip_frontmatter(text)))


def wikilink_targets(text: str) -> Iterable[tuple[str, bool]]:
    for match in WIKILINK_RE.finditer(strip_code_fences(text)):
        raw = match.group(2)
        target = raw.split("|", 1)[0].strip()
        if target:
            yield target, bool(match.group(1))


def wikilink_targets_with_lines(text: str) -> Iterable[tuple[int, str, bool]]:
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), start=1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in WIKILINK_RE.finditer(line):
            raw = match.group(2)
            target = raw.split("|", 1)[0].strip()
            if target:
                yield line_no, target, bool(match.group(1))


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


def normalize_anchor(value: str) -> str:
    value = value.replace("%20", " ").strip()
    return re.sub(r"\s+", " ", value).lower()


def heading_anchors(text: str) -> set[str]:
    anchors = set()
    for line in strip_code_fences(text).splitlines():
        match = HEADING_RE.match(line)
        if match:
            anchors.add(normalize_anchor(clean_index_text(match.group(2))))
    return anchors


def build_path_indexes(paths: list[Path]) -> tuple[dict[str, Path], dict[str, list[Path]]]:
    path_key_to_path: dict[str, Path] = {}
    stem_key_to_paths: dict[str, list[Path]] = defaultdict(list)
    for path in paths:
        if path.suffix.lower() != ".md":
            continue
        path_key_to_path[rel(path)[:-3].lower()] = path
        stem_key_to_paths[path.stem.lower()].append(path)
    return path_key_to_path, stem_key_to_paths


def resolve_wikilink_path(
    target: str,
    source_path: Path,
    path_key_to_path: dict[str, Path],
    stem_key_to_paths: dict[str, list[Path]],
) -> Path | None:
    page = target.split("#", 1)[0].replace("\\", "/").strip()
    if not page:
        return source_path
    normalized = page.lower()
    if normalized in path_key_to_path:
        return path_key_to_path[normalized]
    candidates = stem_key_to_paths.get(Path(normalized).name, [])
    if not candidates:
        return None
    source_parts = source_path.relative_to(ROOT).parts
    if source_parts:
        same_topic = [path for path in candidates if path.relative_to(ROOT).parts[:1] == source_parts[:1]]
        if len(same_topic) == 1:
            return same_topic[0]
    return candidates[0]


def is_unqualified_note_target(target: str) -> bool:
    page = target.split("#", 1)[0].replace("\\", "/").strip()
    return bool(page) and "/" not in page


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
    path_key_to_path, stem_key_to_paths = build_path_indexes(md_files)
    heading_by_path = {path: heading_anchors(read_text(path)) for path in md_files}
    article_stem_to_paths: dict[str, list[Path]] = defaultdict(list)
    for path in article_paths:
        article_stem_to_paths[path.stem.lower()].append(path)

    by_extension = Counter(path.suffix.lower() or "(none)" for path in files)
    empty_notes = [note for note in articles if not note.text.strip()]
    stubs = [note for note in articles if note.text.strip() and len(note.text.encode("utf-8")) < 1500]
    missing_up = [note for note in articles if "up:" not in frontmatter(note.text)]
    missing_confidence = [note for note in articles if "confidence:" not in frontmatter(note.text)]
    missing_freshness = [note for note in articles if not freshness_value(note.text)]
    current_sensitive_articles = [
        note for note in articles if freshness_value(note.text) == "current-sensitive"
    ]
    current_sensitive_without_review_date = [
        {
            "file": note.rel,
            "title": note.title,
            "freshness": freshness_value(note.text),
            "reason": "missing last-verified/as-of/source-date marker",
        }
        for note in current_sensitive_articles
        if not has_freshness_review_marker(note.text)
    ]
    missing_references = [
        note
        for note in articles
        if references_body(note.text) is None
    ]
    empty_references = [
        note
        for note in articles
        if references_body(note.text) == ""
    ]

    placeholder_hits = []
    for note in load_notes(content_md_files):
        for line_no, line in enumerate(note.text.splitlines(), start=1):
            if PLACEHOLDER_RE.search(line):
                placeholder_hits.append({"file": note.rel, "line": line_no, "text": line.strip()})
    template_placeholder_hits = [
        row for row in placeholder_hits if has_any_part(str(row["file"]), {"_templates"})
    ]
    operational_placeholder_hits = [
        row for row in placeholder_hits if not has_any_part(str(row["file"]), {"_templates"})
    ]

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

    reader_broken_anchor_links = []
    for note in articles:
        for line_no, target, embedded in wikilink_targets_with_lines(note.text):
            if "#" not in target:
                continue
            page, anchor = target.split("#", 1)
            if not anchor or anchor.startswith("^"):
                continue
            target_path = resolve_wikilink_path(target, note.path, path_key_to_path, stem_key_to_paths)
            if not target_path:
                continue
            if normalize_anchor(anchor) not in heading_by_path.get(target_path, set()):
                reader_broken_anchor_links.append(
                    {
                        "file": note.rel,
                        "line": line_no,
                        "target": target,
                        "target_file": rel(target_path),
                        "anchor": anchor,
                        "embedded": embedded,
                    }
                )

    reader_ambiguous_wikilinks = []
    for note in articles:
        for line_no, target, embedded in wikilink_targets_with_lines(note.text):
            if not is_unqualified_note_target(target):
                continue
            page = target.split("#", 1)[0].replace("\\", "/").strip()
            candidates = article_stem_to_paths.get(Path(page).name.lower(), [])
            if len(candidates) <= 1:
                continue
            reader_ambiguous_wikilinks.append(
                {
                    "file": note.rel,
                    "line": line_no,
                    "target": target,
                    "basename": Path(page).name,
                    "candidate_count": len(candidates),
                    "candidates": "; ".join(rel(path) for path in candidates[:8]),
                    "embedded": embedded,
                }
            )

    protected_broken_links = [
        row for row in broken_links if has_any_part(str(row["file"]), PROTECTED_CONTENT_PARTS)
    ]
    operational_broken_links = [
        row for row in broken_links if not has_any_part(str(row["file"]), PROTECTED_CONTENT_PARTS)
    ]

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
        "missing_freshness": len(missing_freshness),
        "current_sensitive_articles": len(current_sensitive_articles),
        "current_sensitive_without_review_date": len(current_sensitive_without_review_date),
        "missing_references": len(missing_references),
        "empty_references": len(empty_references),
        "placeholder_hits": len(placeholder_hits),
        "reader_placeholder_hits": len(reader_placeholder_hits),
        "template_placeholder_hits": len(template_placeholder_hits),
        "operational_placeholder_hits": len(operational_placeholder_hits),
        "heavy_audio_embed_pages": len(heavy_audio_embed_pages),
        "broken_link_occurrences": len(broken_links),
        "reader_broken_link_occurrences": len(reader_broken_links),
        "reader_broken_anchor_occurrences": len(reader_broken_anchor_links),
        "reader_ambiguous_wikilink_occurrences": len(reader_ambiguous_wikilinks),
        "protected_broken_link_occurrences": len(protected_broken_links),
        "operational_broken_link_occurrences": len(operational_broken_links),
        "orphan_articles": len(orphans),
    }
    editorial_readiness = editorial_readiness_checks()
    summary["editorial_readiness"] = editorial_readiness
    summary["editorial_readiness_ready"] = all(row["status"] == "Ready" for row in editorial_readiness)

    write_json(REPORT_DIR / "audit-summary.json", summary)
    write_json(REPORT_DIR / "wiki-quality-summary.json", summary)
    write_note_list(REPORT_DIR / "audit-empty-notes.md", "Empty Notes", empty_notes)
    write_note_list(REPORT_DIR / "audit-stubs.md", "Stubs Under 1500 Bytes", stubs)
    write_note_list(REPORT_DIR / "audit-missing-up.md", "Missing up Frontmatter", missing_up)
    write_note_list(REPORT_DIR / "audit-missing-confidence.md", "Missing confidence Frontmatter", missing_confidence)
    write_note_list(REPORT_DIR / "audit-missing-freshness.md", "Missing freshness Frontmatter", missing_freshness)
    write_note_list(REPORT_DIR / "audit-missing-references.md", "Missing References Section", missing_references)
    write_note_list(REPORT_DIR / "audit-empty-references.md", "Empty References Section", empty_references)
    write_rows(REPORT_DIR / "audit-placeholder-hits.md", "Placeholder Hits", placeholder_hits, ["file", "line", "text"])
    write_rows(
        REPORT_DIR / "audit-operational-placeholder-hits.md",
        "Operational Placeholder Hits",
        operational_placeholder_hits,
        ["file", "line", "text"],
    )
    write_rows(
        REPORT_DIR / "audit-template-placeholder-hits.md",
        "Template Placeholder Hits",
        template_placeholder_hits,
        ["file", "line", "text"],
    )
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
        REPORT_DIR / "audit-operational-broken-links.md",
        "Operational Broken Wiki Links",
        operational_broken_links,
        ["file", "target", "embedded"],
    )
    write_rows(
        REPORT_DIR / "audit-protected-broken-links.md",
        "Protected-Layer Broken Wiki Links",
        protected_broken_links,
        ["file", "target", "embedded"],
    )
    write_rows(
        REPORT_DIR / "wiki-broken-links.md",
        "Reader-Facing Broken Wiki Links",
        reader_broken_links,
        ["file", "target", "embedded"],
    )
    write_rows(
        REPORT_DIR / "wiki-broken-anchor-links.md",
        "Reader-Facing Broken Section Anchor Links",
        reader_broken_anchor_links,
        ["file", "line", "target", "target_file", "anchor", "embedded"],
    )
    write_rows(
        REPORT_DIR / "wiki-ambiguous-wikilinks.md",
        "Reader-Facing Ambiguous Wikilinks",
        reader_ambiguous_wikilinks,
        ["file", "line", "target", "basename", "candidate_count", "candidates", "embedded"],
    )
    write_rows(
        REPORT_DIR / "wiki-current-sensitive-review.md",
        "Current-Sensitive Pages Missing Dated Review Marker",
        current_sensitive_without_review_date,
        ["file", "title", "freshness", "reason"],
    )
    write_note_list(REPORT_DIR / "audit-orphans.md", "Orphan Articles", orphans)
    write_wiki_quality_dashboard(
        summary=summary,
        missing_up=missing_up,
        missing_confidence=missing_confidence,
        missing_freshness=missing_freshness,
        missing_references=missing_references,
        empty_references=empty_references,
        reader_placeholder_hits=reader_placeholder_hits,
        reader_broken_links=reader_broken_links,
        reader_broken_anchor_links=reader_broken_anchor_links,
        reader_ambiguous_wikilinks=reader_ambiguous_wikilinks,
        current_sensitive_without_review_date=current_sensitive_without_review_date,
        stubs=stubs,
        orphans=orphans,
    )

    return summary


def wiki_quality_verdict(summary: dict[str, object]) -> str:
    reader_broken = int(summary["reader_broken_link_occurrences"])
    reader_anchor_broken = int(summary["reader_broken_anchor_occurrences"])
    reader_ambiguous_links = int(summary["reader_ambiguous_wikilink_occurrences"])
    reader_placeholders = int(summary["reader_placeholder_hits"])
    missing_refs = int(summary["missing_references"])
    empty_refs = int(summary["empty_references"])
    missing_confidence = int(summary["missing_confidence"])
    missing_freshness = int(summary.get("missing_freshness", 0))
    freshness_review_queue = int(summary.get("current_sensitive_without_review_date", 0))
    editorial_ready = bool(summary.get("editorial_readiness_ready", True))
    if reader_broken == 0 and reader_anchor_broken == 0 and reader_ambiguous_links == 0 and reader_placeholders == 0 and missing_refs == 0 and empty_refs == 0 and missing_confidence == 0 and missing_freshness == 0:
        if not editorial_ready:
            return "Mechanically clean, but reader-facing structure needs review."
        if freshness_review_queue:
            return "Ready as a clean reference wiki, with a visible current-sensitive review queue."
        return "Ready as a clean reference wiki."
    if reader_broken == 0 and reader_anchor_broken == 0 and reader_ambiguous_links == 0 and reader_placeholders == 0:
        return "Good enough for guided reading, but not yet clean enough to call finished."
    return "Readable with the new book spines, but not yet good enough as a polished wiki."


def wiki_quality_explanation(summary: dict[str, object]) -> str:
    reader_broken = int(summary["reader_broken_link_occurrences"])
    reader_anchor_broken = int(summary["reader_broken_anchor_occurrences"])
    reader_ambiguous_links = int(summary["reader_ambiguous_wikilink_occurrences"])
    reader_placeholders = int(summary["reader_placeholder_hits"])
    missing_refs = int(summary["missing_references"])
    empty_refs = int(summary["empty_references"])
    missing_confidence = int(summary["missing_confidence"])
    missing_freshness = int(summary.get("missing_freshness", 0))
    freshness_review_queue = int(summary.get("current_sensitive_without_review_date", 0))
    missing_up = int(summary["missing_up"])
    stubs = int(summary["stubs_under_1500_bytes"])
    editorial_ready = bool(summary.get("editorial_readiness_ready", True))
    if reader_broken == 0 and reader_anchor_broken == 0 and reader_ambiguous_links == 0 and reader_placeholders == 0:
        remaining = []
        if missing_refs:
            remaining.append("missing source/provenance footers")
        if empty_refs:
            remaining.append("empty source/provenance footers")
        if missing_confidence:
            remaining.append("missing confidence labels")
        if missing_freshness:
            remaining.append("missing freshness classifications")
        if missing_up:
            remaining.append("missing parent navigation")
        if stubs:
            remaining.append("thin stubs")
        if remaining:
            return (
                "The wiki is navigable for normal reading: reader-facing broken links and visible draft placeholders are cleared. "
                "The remaining work is metadata and depth cleanup: " + ", ".join(remaining) + "."
            )
        if not editorial_ready:
            return "The wiki has clean reader-facing lint counts, but at least one generated editorial readiness gate needs review."
        if freshness_review_queue:
            return (
                "The wiki is navigable for normal reading, with no reader-facing broken links, broken section links, ambiguous wikilinks, placeholders, empty references, or missing provenance metadata found by the current audit. "
                "Current-sensitive pages are classified, and the remaining freshness work is now a dated review queue instead of hidden drift."
            )
        return "The wiki is navigable for normal reading, with no reader-facing broken links, broken section links, ambiguous wikilinks, placeholders, empty references, or missing provenance metadata found by the current audit."
    return (
        "The wiki is now navigable as a reading shelf because every committed top-level topic has a book-style spine. "
        "It is not yet clean as a finished reference set because reader-facing pages still have unresolved links, placeholder lines, or incomplete provenance metadata."
    )


def housekeeping_order(summary: dict[str, object]) -> list[str]:
    order = []
    if int(summary["reader_broken_link_occurrences"]):
        order.append("Fix reader-facing broken links first; they interrupt reading and graph traversal.")
    if int(summary["reader_broken_anchor_occurrences"]):
        order.append("Fix reader-facing broken section links; they make source and study citations land in the wrong place.")
    if int(summary["reader_ambiguous_wikilink_occurrences"]):
        order.append("Qualify ambiguous reader-facing wikilinks whose basename exists in multiple topics.")
    if int(summary["reader_placeholder_hits"]):
        order.append("Remove visible placeholder lines from reader-facing pages.")
    if int(summary["missing_references"]) or int(summary["empty_references"]) or int(summary["missing_confidence"]):
        order.append("Add populated references sections and confidence frontmatter to high-traffic book-spine targets.")
    if int(summary.get("missing_freshness", 0)):
        order.append("Add freshness frontmatter so stable, historical, and current-sensitive pages are not mixed together.")
    if int(summary.get("current_sensitive_without_review_date", 0)):
        order.append("Refresh current-sensitive pages with dated source checks, starting from LLM frontier/local-inference and SpaceX live-company pages.")
    if int(summary["missing_up"]):
        order.append("Add missing up frontmatter so every reader-facing page has explicit parent navigation.")
    if int(summary["stubs_under_1500_bytes"]):
        order.append("Expand or intentionally reclassify remaining thin stubs.")
    if int(summary.get("operational_broken_link_occurrences", 0)):
        order.append("Fix operational broken links outside protected raw, chunk, and template layers.")
    if int(summary.get("operational_placeholder_hits", 0)):
        order.append("Remove placeholder text from operational notes outside templates.")
    if order:
        order.append("Only then spend time on chunk/query/template noise.")
    else:
        order.append("Leave protected chunk/template noise alone unless promoting it into reader-facing wiki pages.")
    return order


def report_link(path: str, label: str) -> str:
    return f"[{label}](<{path}>)"


def table_cell(value: object) -> str:
    return str(value).replace("|", "\\|")


def readiness_missing(requirements: list[dict[str, object]]) -> list[str]:
    missing: list[str] = []
    for requirement in requirements:
        rel_path = str(requirement["path"])
        label = str(requirement.get("label", rel_path))
        path = ROOT / rel_path
        if not path.exists():
            missing.append(f"{label} not found")
            continue
        text = read_text(path)
        for snippet in requirement.get("all", []):
            if str(snippet) not in text:
                missing.append(f"{label} lacks expected route marker")
                break
        any_snippets = [str(item) for item in requirement.get("any", [])]
        if any_snippets and not any(snippet in text for snippet in any_snippets):
            missing.append(f"{label} lacks expected route marker")
        for pattern in requirement.get("none_regex", []):
            if re.search(str(pattern), text, flags=re.MULTILINE):
                missing.append(f"{label} contains generated summary noise")
                break
    return missing


def editorial_gate(
    gate: str,
    evidence: str,
    requirements: list[dict[str, object]],
) -> dict[str, object]:
    missing = readiness_missing(requirements)
    if missing:
        return {
            "gate": gate,
            "status": "Review",
            "evidence": "Review: " + "; ".join(missing[:3]),
            "missing": missing,
        }
    return {"gate": gate, "status": "Ready", "evidence": evidence, "missing": []}


def editorial_readiness_checks() -> list[dict[str, object]]:
    topic_root_requirements = [
        {
            "path": "LLM/LLM.md",
            "label": "LLM root router",
            "all": ["## Start Here", "LLM Book Reading Spine", "LLM Study Index", "LLM Sources Index"],
        },
        {
            "path": "CS Algorithms/CS Algorithms.md",
            "label": "Algorithms root router",
            "all": ["## Start Here", "CS Algorithms Book Reading Spine", "Algorithms Study Index", "CS Algorithms Sources Index"],
        },
        {
            "path": "CS Data Structures/CS Data Structures.md",
            "label": "Data Structures root router",
            "all": ["## Start Here", "CS Data Structures Book Reading Spine", "CS Data Structures Study Index", "CS Data Structures Sources Index"],
        },
        {
            "path": "CS Operating Systems/CS Operating Systems.md",
            "label": "Operating Systems root router",
            "all": ["## Start Here", "CS Operating Systems Book Reading Spine", "OS Study Index", "CS Operating Systems Sources Index"],
        },
        {
            "path": "Japanese/Japanese.md",
            "label": "Japanese root router",
            "all": ["## Reader Router", "Japanese Book Reading Spine", "Japanese Study Index", "Japanese Sources Index"],
        },
        {
            "path": "NES Emulation/NES Emulation.md",
            "label": "NES root router",
            "all": ["## Start Here", "NES Emulation Book Reading Spine", "NES Emulation Study Index", "NES Emulation Sources Index"],
        },
        {
            "path": "Programming Languages/Programming Languages.md",
            "label": "Programming Languages root router",
            "all": ["## Start Here", "Programming Languages Book Reading Spine", "Programming Languages Study Index", "Programming Languages Sources Index"],
        },
        {
            "path": "Project Hail Mary/Project Hail Mary.md",
            "label": "Project Hail Mary root router",
            "all": ["## Start Here", "Project Hail Mary Book Reading Spine", "Science Accuracy Scorecard", "Project Hail Mary Sources Index"],
        },
        {
            "path": "Recipes/Recipes.md",
            "label": "Recipes root router",
            "all": ["## Start Here", "Recipes Book Reading Spine", "Recipe Sources Index"],
        },
        {
            "path": "SpaceX/SpaceX.md",
            "label": "SpaceX root router",
            "all": ["## Start Here", "SpaceX Book Reading Spine", "SpaceX Study Index", "SpaceX Sources Index"],
        },
    ]
    learning_path_requirements = [
        {"path": "LLM/LLM — Learning Path.md", "label": "LLM learning path", "all": ["## Where This Fits"]},
        {"path": "CS Algorithms/CS Algorithms — Learning Path.md", "label": "Algorithms learning path", "all": ["## Where This Fits"]},
        {"path": "CS Data Structures/CS Data Structures — Learning Path.md", "label": "Data Structures learning path", "all": ["## Where This Fits"]},
        {"path": "CS Operating Systems/CS Operating Systems — Learning Path.md", "label": "Operating Systems learning path", "all": ["## Where This Fits"]},
        {"path": "NES Emulation/NES Emulation — Learning Path.md", "label": "NES learning path", "all": ["## Where This Fits"]},
        {"path": "Programming Languages/Programming Languages — Learning Path.md", "label": "Programming Languages learning path", "all": ["## Where This Fits"]},
        {"path": "Project Hail Mary/Project Hail Mary — Learning Path.md", "label": "Project Hail Mary learning path", "all": ["## Where This Fits"]},
        {"path": "SpaceX/SpaceX — Learning Path.md", "label": "SpaceX learning path", "all": ["## Where This Fits"]},
        {"path": "LLM/Study/LLM Study Index.md", "label": "LLM study router", "all": ["## Start Here By Goal", "## Local Inference Minimum Path"]},
        {"path": "CS Algorithms/Study/Algorithms Study Index.md", "label": "Algorithms study router", "all": ["## Start Here By Goal"]},
        {"path": "CS Data Structures/Study/CS Data Structures Study Index.md", "label": "Data Structures study router", "all": ["## Start Here By Goal"]},
        {"path": "CS Operating Systems/Study/OS Study Index.md", "label": "Operating Systems study router", "all": ["## Start Here By Goal"]},
        {"path": "NES Emulation/Study/NES Emulation Study Index.md", "label": "NES study router", "all": ["## Start Here By Goal"]},
        {"path": "Programming Languages/Study/Programming Languages Study Index.md", "label": "Programming Languages study router", "all": ["## Start Here By Goal"]},
        {"path": "SpaceX/Study/SpaceX Study Index.md", "label": "SpaceX study router", "all": ["## Start Here By Goal"]},
    ]
    source_requirements = [
        {"path": "LLM/Sources/Sources Index.md", "label": "LLM sources", "all": ["## How To Use Sources"]},
        {"path": "CS Algorithms/Sources/Sources Index.md", "label": "Algorithms sources", "all": ["## How To Use Sources"]},
        {"path": "CS Data Structures/Sources/Sources Index.md", "label": "Data Structures sources", "all": ["## How To Use Sources"]},
        {"path": "CS Operating Systems/Sources/Sources Index.md", "label": "Operating Systems sources", "all": ["## How To Use Sources"]},
        {"path": "Japanese/Sources/Sources Index.md", "label": "Japanese sources", "all": ["## How To Use Sources"]},
        {"path": "NES Emulation/Sources/Sources Index.md", "label": "NES sources", "all": ["## How To Use Sources"]},
        {"path": "Programming Languages/Sources/Sources Index.md", "label": "Programming Languages sources", "all": ["## How To Use Sources"]},
        {"path": "Project Hail Mary/Sources/Sources Index.md", "label": "Project Hail Mary sources", "all": ["## How To Use Sources"]},
        {"path": "Recipes/Sources/Recipe Sources Index.md", "label": "Recipe sources", "all": ["## How To Use Sources"]},
        {"path": "SpaceX/Sources/Sources Index.md", "label": "SpaceX sources", "all": ["## How To Use Sources"]},
    ]
    generated_summary_requirements = [
        {"path": "index.md", "label": "Generated index summaries", "none_regex": [GENERATED_SUMMARY_NOISE_PATTERN]},
        {"path": "LLM/LLM Book Reading Spine.md", "label": "LLM book-spine summaries", "none_regex": [GENERATED_SUMMARY_NOISE_PATTERN]},
        {"path": "CS Algorithms/CS Algorithms Book Reading Spine.md", "label": "Algorithms book-spine summaries", "none_regex": [GENERATED_SUMMARY_NOISE_PATTERN]},
        {"path": "CS Data Structures/CS Data Structures Book Reading Spine.md", "label": "Data Structures book-spine summaries", "none_regex": [GENERATED_SUMMARY_NOISE_PATTERN]},
        {"path": "CS Operating Systems/CS Operating Systems Book Reading Spine.md", "label": "Operating Systems book-spine summaries", "none_regex": [GENERATED_SUMMARY_NOISE_PATTERN]},
        {"path": "Japanese/Japanese Book Reading Spine.md", "label": "Japanese book-spine summaries", "none_regex": [GENERATED_SUMMARY_NOISE_PATTERN]},
        {"path": "NES Emulation/NES Emulation Book Reading Spine.md", "label": "NES book-spine summaries", "none_regex": [GENERATED_SUMMARY_NOISE_PATTERN]},
        {"path": "Programming Languages/Programming Languages Book Reading Spine.md", "label": "Programming Languages book-spine summaries", "none_regex": [GENERATED_SUMMARY_NOISE_PATTERN]},
        {"path": "Project Hail Mary/Project Hail Mary Book Reading Spine.md", "label": "Project Hail Mary book-spine summaries", "none_regex": [GENERATED_SUMMARY_NOISE_PATTERN]},
        {"path": "Recipes/Recipes Book Reading Spine.md", "label": "Recipe book-spine summaries", "none_regex": [GENERATED_SUMMARY_NOISE_PATTERN]},
        {"path": "SpaceX/SpaceX Book Reading Spine.md", "label": "SpaceX book-spine summaries", "none_regex": [GENERATED_SUMMARY_NOISE_PATTERN]},
    ]
    return [
        editorial_gate(
            "Human front door",
            "[[Welcome]] routes readers to book, study, quality, catalog, and source paths",
            [
                {
                    "path": "Welcome.md",
                    "label": "Welcome reader router",
                    "all": [
                        "## If You Are Here To Read",
                        "[[PersonalKB Book Reading Guide]]",
                        "[[LLM/Study/LLM Study Index|LLM Study Index]]",
                        "[[PersonalKB Wiki Quality Dashboard]]",
                        "[[index|PersonalKB Index]]",
                        "Sources/Sources Index",
                    ],
                }
            ],
        ),
        editorial_gate(
            "Book-mode reading",
            "[[PersonalKB Book Reading Guide]] provides shelf order, cross-topic routes, operating modes, and proof targets",
            [
                {
                    "path": "PersonalKB Book Reading Guide.md",
                    "label": "Book reading guide",
                    "all": ["## One Reading Session", "## Reading Shelf", "## Choose A Reading Route", "## Operating Modes", "Proof target:"],
                }
            ],
        ),
        editorial_gate(
            "Topic root routers",
            "Major topic roots expose book mode, study or practice, provenance, and catalog browsing before domain lists",
            topic_root_requirements,
        ),
        editorial_gate(
            "Study and proof routing",
            "Learning paths and study indexes explain when to use book spines, pass-based curricula, drills, labs, and proof artifacts",
            learning_path_requirements,
        ),
        editorial_gate(
            "Provenance routing",
            "Source indexes explain how to verify claims, classify source type, and handle freshness-sensitive facts",
            source_requirements,
        ),
        editorial_gate(
            "Generated summary prose",
            "Generated index and book-spine summaries use reader prose instead of Mermaid directives, summary labels, generic template claims, or example-only snippets",
            generated_summary_requirements,
        ),
        editorial_gate(
            "Exhaustive catalog boundary",
            "[[index]] labels itself as the generated catalog for search and agent queries, not the first reading path",
            [
                {
                    "path": "_ops/personal_kb.py",
                    "label": "Index generator boundary",
                    "all": ["exhaustive catalog for search and agent queries", "PersonalKB Book Reading Guide", "## Start Here"],
                }
            ],
        ),
    ]


def write_wiki_quality_dashboard(
    *,
    summary: dict[str, object],
    missing_up: list[Note],
    missing_confidence: list[Note],
    missing_freshness: list[Note],
    missing_references: list[Note],
    empty_references: list[Note],
    reader_placeholder_hits: list[dict[str, object]],
    reader_broken_links: list[dict[str, object]],
    reader_broken_anchor_links: list[dict[str, object]],
    reader_ambiguous_wikilinks: list[dict[str, object]],
    current_sensitive_without_review_date: list[dict[str, object]],
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
        wiki_quality_explanation(summary),
        "",
        "## Reader-Facing Wiki Health",
        "",
        "| Check | Count | Meaning |",
        "| --- | ---: | --- |",
        f"| Candidate reader-facing articles | {summary['candidate_articles']} | Wiki pages outside raw, chunk, query, template, audio, task, and ops layers |",
        f"| Broken links in reader-facing articles | {summary['reader_broken_link_occurrences']} | Navigation defects that affect normal reading |",
        f"| Broken section links in reader-facing articles | {summary['reader_broken_anchor_occurrences']} | Wikilinks whose target note exists but requested heading does not |",
        f"| Ambiguous wikilinks in reader-facing articles | {summary['reader_ambiguous_wikilink_occurrences']} | Unqualified links whose note name exists in multiple reader-facing topics |",
        f"| Placeholder lines in reader-facing articles | {summary['reader_placeholder_hits']} | Draft markers visible to readers |",
        f"| Missing references sections | {summary['missing_references']} | Pages that still need a source/provenance footer |",
        f"| Empty references sections | {summary['empty_references']} | Pages with a references heading but no provenance links or notes |",
        f"| Missing confidence frontmatter | {summary['missing_confidence']} | Pages without confidence classification |",
        f"| Missing freshness frontmatter | {summary['missing_freshness']} | Pages without stable/current-sensitive currency classification |",
        f"| Missing up frontmatter | {summary['missing_up']} | Pages without explicit parent navigation |",
        f"| Stubs under 1500 bytes | {summary['stubs_under_1500_bytes']} | Thin pages that may not carry their topic yet |",
        f"| Empty notes | {summary['empty_notes']} | Notes with no body text |",
        f"| Orphan articles | {summary['orphan_articles']} | Reader-facing pages with no inbound wikilinks |",
        "",
        "## Freshness And Currency",
        "",
        "Freshness classification is metadata, not a claim that every current fact has just been rechecked. Current-sensitive pages should gain a `last-verified`, `as-of`, or `source-date` marker when a human or agent refreshes their live claims against sources.",
        "",
        "| Check | Count | Meaning |",
        "| --- | ---: | --- |",
        f"| Current-sensitive reader-facing articles | {summary['current_sensitive_articles']} | Pages about live models, local-inference tooling, SpaceX operations, or other facts likely to age |",
        f"| Current-sensitive pages missing dated review marker | {summary['current_sensitive_without_review_date']} | Refresh queue for pages that need explicit source-date evidence before relying on live claims |",
        "",
        "## Editorial Readiness",
        "",
        "These checks are reader-facing structure checks rather than raw lint counts. They record whether the wiki has the surfaces needed to read, study, verify, and maintain the vault without falling back to a flat inventory.",
        "",
        "| Gate | Status | Evidence |",
        "| --- | --- | --- |",
    ]
    for row in summary.get("editorial_readiness", []):
        lines.append(
            f"| {table_cell(row['gate'])} | {table_cell(row['status'])} | {table_cell(row['evidence'])} |"
        )
    lines.extend(
        [
        "",
        "## Maintenance-Layer Noise",
        "",
        "These counts are still useful, but they include chunks, templates, queries, schema examples, and operational notes. Do not use them alone to judge reading quality. Protected-layer counts come from `_raw`, `_chunks`, and `_templates`, which are evidence or scaffolding layers rather than normal reading pages.",
        "",
        "| Check | Count |",
        "| --- | ---: |",
        f"| Operational broken wikilinks outside protected layers | {summary['operational_broken_link_occurrences']} |",
        f"| Operational placeholder hits outside templates | {summary['operational_placeholder_hits']} |",
        f"| Protected raw/chunk/template broken wikilinks | {summary['protected_broken_link_occurrences']} |",
        f"| Template placeholder hits | {summary['template_placeholder_hits']} |",
        f"| All broken wikilink occurrences | {summary['broken_link_occurrences']} |",
        f"| All placeholder hits | {summary['placeholder_hits']} |",
        f"| Heavy audio embed pages | {summary['heavy_audio_embed_pages']} |",
        "",
        "## Next Housekeeping Order",
        "",
    ]
    )
    lines.extend(f"{index}. {item}" for index, item in enumerate(housekeeping_order(summary), start=1))
    lines.extend(["", "## Top Reader-Facing Broken Links", ""])
    if reader_broken_links:
        for row in reader_broken_links[:25]:
            lines.append(f"- `{row['file']}` -> `{row['target']}`")
    else:
        lines.append("- None.")

    lines.extend(["", "## Top Reader-Facing Broken Section Links", ""])
    if reader_broken_anchor_links:
        for row in reader_broken_anchor_links[:25]:
            lines.append(f"- `{row['file']}:{row['line']}` -> `{row['target']}`")
    else:
        lines.append("- None.")

    lines.extend(["", "## Top Reader-Facing Ambiguous Wikilinks", ""])
    if reader_ambiguous_wikilinks:
        for row in reader_ambiguous_wikilinks[:25]:
            lines.append(f"- `{row['file']}:{row['line']}` -> `{row['target']}` ({row['candidate_count']} candidates)")
    else:
        lines.append("- None.")

    lines.extend(["", "## Top Reader-Facing Placeholder Hits", ""])
    if reader_placeholder_hits:
        for row in reader_placeholder_hits[:25]:
            lines.append(f"- `{row['file']}:{row['line']}` -> {row['text']}")
    else:
        lines.append("- None.")

    lines.extend(["", "## Top Current-Sensitive Pages Missing Dated Review", ""])
    if current_sensitive_without_review_date:
        for row in current_sensitive_without_review_date[:25]:
            lines.append(f"- `{row['file']}` -> {row['reason']}")
    else:
        lines.append("- None.")

    lines.extend(
        [
            "",
            "## Report Files",
            "",
            f"- {report_link('_ops/reports/wiki-quality-summary.json', 'Reader-facing quality summary JSON')}",
            f"- {report_link('_ops/reports/wiki-broken-links.md', 'Reader-facing broken links')}",
            f"- {report_link('_ops/reports/wiki-broken-anchor-links.md', 'Reader-facing broken section links')}",
            f"- {report_link('_ops/reports/wiki-ambiguous-wikilinks.md', 'Reader-facing ambiguous wikilinks')}",
            f"- {report_link('_ops/reports/wiki-placeholder-hits.md', 'Reader-facing placeholder hits')}",
            f"- {report_link('_ops/reports/wiki-current-sensitive-review.md', 'Current-sensitive dated-review queue')}",
            f"- {report_link('_ops/reports/audit-summary.json', 'Full audit summary JSON')}",
            f"- {report_link('_ops/reports/audit-missing-freshness.md', 'Missing freshness frontmatter')}",
            f"- {report_link('_ops/reports/audit-empty-references.md', 'Empty references sections')}",
            f"- {report_link('_ops/reports/audit-operational-broken-links.md', 'Operational broken links')}",
            f"- {report_link('_ops/reports/audit-operational-placeholder-hits.md', 'Operational placeholder hits')}",
            f"- {report_link('_ops/reports/audit-protected-broken-links.md', 'Protected-layer broken links')}",
            f"- {report_link('_ops/reports/audit-template-placeholder-hits.md', 'Template placeholder hits')}",
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
        "This file is generated by `_ops/personal_kb.py index`. It is the exhaustive catalog for search and agent queries, not the best first reading path.",
        "",
        "## Start Here",
        "",
        "| Need | Open |",
        "|---|---|",
        "| Read the vault like a shelf of books | [[PersonalKB Book Reading Guide]] |",
        "| Check reader-facing quality | [[PersonalKB Wiki Quality Dashboard]] |",
        "| Understand vault conventions | [[Welcome|PersonalKB Vault Playbook]] |",
        "| Browse every reader-facing article | Continue below |",
        "",
    ]
    for group in sorted(grouped):
        notes = sorted(grouped[group], key=lambda item: item.rel.lower())
        lines.extend([f"## {group}", ""])
        for note in notes:
            summary = one_line_summary(note.text, note.title)
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
