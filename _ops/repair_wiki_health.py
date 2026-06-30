#!/usr/bin/env python3
"""Apply safe, mechanical wiki-health repairs for PersonalKB."""

from __future__ import annotations

import re
import unicodedata
from collections import Counter
from pathlib import Path

import personal_kb as kb


LINK_RE = re.compile(r"(!)?\[\[([^\]]+)\]\]")
FRONTMATTER_RE = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|$)", re.DOTALL)
PLACEHOLDER_CHUNK_LINE = "*(To be populated as chunks are created)*"
TBD_RE = re.compile(r"\bTBD\b")

MANUAL_REDIRECTS = {
    "Adjacency List vs Matrix": "Adjacency List and Adjacency Matrix",
    "Adjacency Matrix": "Adjacency List and Adjacency Matrix",
    "Array": "Arrays and Dynamic Arrays",
    "Arrays": "Arrays and Dynamic Arrays",
    "Backtracking": "Backtracking Overview",
    "BERT": "BERT and Encoder Lineage",
    "Binary Tree": "Binary Trees and Traversals",
    "Bloom Filter": "Bloom Filters and Probabilistic Structures",
    "B-Trees": "B-Trees and B-Plus Trees",
    "B-Trees and B+ Trees": "B-Trees and B-Plus Trees",
    "CS Algorithms Index": "CS Algorithms",
    "C Sharp — Language Profile": "C# — Language Profile",
    "Catastrophic Forgetting": "Continual Fine-Tuning and Catastrophic Forgetting",
    "Common Idioms and Proverbs": "Idioms and Proverbs — ことわざ",
    "Competition and Industry Response": "Competition Landscape",
    "Cost Revolution": "Cost Revolution in Spaceflight",
    "Crew Dragon": "Crew Dragon Design",
    "Deques": "Queues and Deques",
    "Dijkstra’s Algorithm": "Dijkstra's Algorithm",
    "Direct-to-Cell": "Direct-to-Cell Technology",
    "Divide and Conquer": "Divide and Conquer Overview",
    "Doubly Linked Lists": "Doubly Linked Lists and Circular Lists",
    "Dynamic Arrays": "Arrays and Dynamic Arrays",
    "Dynamic Programming Overview": "Dynamic Programming",
    "Exceptions": "Exception-Based Error Handling",
    "Falcon 9 Evolution and Versions": "Falcon 9 Evolution",
    "Falcon Heavy": "Falcon Heavy Design and Missions",
    "Falcon Specifications and Performance": "Falcon Performance Specifications",
    "Function Calling Conventions": "Function Calling",
    "Funding and Valuation": "SpaceX Funding and Valuation",
    "Graph Search — BFS and DFS": "BFS and DFS",
    "Gradual Typing": "Gradual and Optional Typing",
    "Hash Sets": "Hash Tables and Hash Functions",
    "Hash Table": "Hash Tables and Hash Functions",
    "Hash Tables": "Hash Tables and Hash Functions",
    "Historical Languages — Overview": "Historical Languages Overview",
    "Human Landing System (HLS)": "Human Landing System",
    "ICL Scaling Laws": "Scaling Laws",
    "In-Situ Resource Utilization (ISRU)": "In-Situ Resource Utilization",
    "Interval Trees": "Interval Trees and Range Trees",
    "Keigo — Kenjougo": "Keigo — Kenjōgo (Humble)",
    "Keigo — Sonkeigo": "Keigo — Sonkeigo (Honorific)",
    "Keigo — Teineigo": "Keigo — Teineigo (Polite)",
    "Macro Systems": "Macro Systems Compared",
    "NES Cheatsheet — Memory Map and Registers": "Cheatsheet — NES Memory Maps and Registers",
    "NES Review — APU Sound Channels": "APU — Audio Processing Unit Overview",
    "NES Review — Emulator Architecture": "Emulator Architecture Overview",
    "Object-Oriented Programming": "Object-Oriented Programming Philosophies",
    "Priority Queue": "Priority Queue ADT",
    "Prototype": "Prototype vs Class-Based OOP",
    "Quantization Techniques": "Quantization",
    "Queue": "Queues and Deques",
    "Queues": "Queues and Deques",
    "Quick Sort": "Quicksort",
    "Reinforcement Learning from Human Feedback (RLHF)": "Reinforcement Learning from Human Feedback",
    "RLHF (Reinforcement Learning from Human Feedback)": "Reinforcement Learning from Human Feedback",
    "Scaling Laws and Chinchilla": "Scaling Laws",
    "Seasonal Greetings and Customs": "Seasonal Greetings and Cultural Expressions",
    "Sorting Algorithms Overview": "Sorting Overview",
    "Splay Trees": "Splay Trees and Treaps",
    "Starlink Constellation Design": "Constellation Design and Orbits",
    "Starlink Ground Infrastructure": "Ground Infrastructure",
    "Starlink Satellite Generations": "Satellite Generations",
    "Starship Flight Test Campaign": "Integrated Flight Tests",
    "Starship Variants": "Starship Variants and Applications",
    "Thematic — Body and Health": "Thematic Vocabulary — Body and Health",
    "Thematic — Food and Dining": "Thematic Vocabulary — Food and Drink",
    "Thematic — Home and Family": "Thematic Vocabulary — Home and Daily Life",
    "Thematic — Nature and Weather": "Thematic Vocabulary — Nature and Weather",
    "Thematic — Numbers, Time, and Dates": "Thematic Vocabulary — Numbers, Time, and Dates",
    "Thematic — Travel and Transportation": "Thematic Vocabulary — Travel and Transportation",
    "Thematic — Work and Business": "Thematic Vocabulary — Work and Office",
    "Thermal Protection System (TPS)": "Thermal Protection System",
    "Topological Sort": "DAG and Topological Sort",
    "Tries": "Tries and Prefix Trees",
    "Union-Find (Disjoint Sets)": "Disjoint Sets and Union-Find",
}


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.replace("’", "'").replace("`", "'")
    value = value.replace("—", " ").replace("–", " ").replace("-", " ")
    value = re.sub(r"[^\w+#]+", " ", value, flags=re.UNICODE)
    return re.sub(r"\s+", " ", value).strip().lower()


def split_target(raw: str) -> tuple[str, str | None]:
    if "|" in raw:
        target, display = raw.split("|", 1)
        return target.strip(), display.strip()
    return raw.strip(), None


def frontmatter_has(fm: str, key: str) -> bool:
    return re.search(rf"(?m)^{re.escape(key)}\s*:", fm) is not None


def set_frontmatter_field(text: str, key: str, value: str) -> str:
    match = FRONTMATTER_RE.match(text)
    line = f'{key}: "{value}"' if key == "up" else f"{key}: {value}"
    if match:
        fm = match.group(1).rstrip()
        if frontmatter_has(fm, key):
            return text
        body = text[match.end() :]
        return f"---\n{fm}\n{line}\n---\n{body}"
    return f"---\n{line}\n---\n{text}"


def first_heading(path: Path, text: str) -> str:
    return kb.first_heading(path, text)


def target_for_path(path: Path, stem_counts: Counter[str]) -> str:
    stem = path.stem
    if stem_counts[stem] == 1 and not any(part.startswith("_") for part in path.relative_to(kb.ROOT).parts):
        return stem
    target = kb.rel(path)
    return target[:-3] if target.endswith(".md") else target


def build_target_indexes() -> tuple[dict[str, Path], dict[str, Path], Counter[str]]:
    markdown = kb.markdown_files()
    stem_counts = Counter(path.stem for path in markdown)
    normalized: dict[str, Path] = {}
    id_prefix: dict[str, Path] = {}
    for path in markdown:
        stem = path.stem
        normalized.setdefault(normalize(stem), path)
        normalized.setdefault(normalize(kb.rel(path)[:-3]), path)
        id_match = re.match(r"((?:raw|chunk)-[a-z]+-\d{3})\b", stem)
        if id_match:
            id_prefix.setdefault(id_match.group(1), path)
    return normalized, id_prefix, stem_counts


def broken_targets() -> set[str]:
    report = kb.REPORT_DIR / "wiki-broken-links.md"
    targets: set[str] = set()
    if not report.exists():
        return targets
    for line in report.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| ") or line.startswith("| file") or line.startswith("| ---"):
            continue
        parts = [part.strip().replace("\\|", "|") for part in line.strip("|").split("|")]
        if len(parts) >= 2:
            targets.add(parts[1])
    return targets


def resolve_target(target: str, normalized: dict[str, Path], id_prefix: dict[str, Path], stem_counts: Counter[str]) -> str | None:
    if "#" in target:
        base, anchor = target.split("#", 1)
    else:
        base, anchor = target, ""
    base = base.strip()

    manual = MANUAL_REDIRECTS.get(base)
    if manual:
        path = normalized.get(normalize(manual))
        if path:
            resolved = target_for_path(path, stem_counts)
            return f"{resolved}#{anchor}" if anchor else resolved

    id_match = re.match(r"((?:raw|chunk)-[a-z]+-\d{3})\b", base)
    if id_match and id_match.group(1) in id_prefix:
        resolved = target_for_path(id_prefix[id_match.group(1)], stem_counts)
        return f"{resolved}#{anchor}" if anchor else resolved

    path = normalized.get(normalize(base))
    if path:
        resolved = target_for_path(path, stem_counts)
        return f"{resolved}#{anchor}" if anchor else resolved

    return None


def repair_links() -> tuple[int, Counter[str]]:
    normalized, id_prefix, stem_counts = build_target_indexes()
    broken = broken_targets()
    unlinked: Counter[str] = Counter()
    changed_files = 0

    def replace(match: re.Match[str]) -> str:
        embedded = match.group(1)
        raw = match.group(2)
        target, display = split_target(raw)
        if embedded or target not in broken:
            return match.group(0)

        resolved = resolve_target(target, normalized, id_prefix, stem_counts)
        if resolved:
            if display:
                return f"[[{resolved}|{display}]]"
            if normalize(target) == normalize(resolved.rsplit("/", 1)[-1]):
                return f"[[{resolved}]]"
            return f"[[{resolved}|{target}]]"

        visible = display or target
        unlinked[target] += 1
        if re.match(r"^(?:raw|chunk)-[a-z]+-\d{3}\b", target):
            return f"`{visible}`"
        return visible

    for path in sorted(path for path in kb.markdown_files() if kb.is_wiki_article(path)):
        text = kb.read_text(path)
        repaired = LINK_RE.sub(replace, text)
        if repaired != text:
            path.write_text(repaired, encoding="utf-8")
            changed_files += 1

    write_unlinked_report(unlinked)
    return changed_files, unlinked


def write_unlinked_report(unlinked: Counter[str]) -> None:
    lines = ["# Wiki Link Repair Unlinked Targets", "", f"Count: {sum(unlinked.values())}", ""]
    if unlinked:
        lines.extend(["| target | occurrences |", "| --- | ---: |"])
        for target, count in sorted(unlinked.items(), key=lambda item: (-item[1], item[0].lower())):
            escaped = target.replace("|", "\\|")
            lines.append(f"| {escaped} | {count} |")
    else:
        lines.append("- None.")
    (kb.REPORT_DIR / "wiki-link-repair-unlinked-targets.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )


def confidence_for(path: Path) -> str:
    parts = path.relative_to(kb.ROOT).parts
    name = path.stem
    if "Project Hail Mary" in parts:
        return "fictional"
    if name in {"Welcome", "PersonalKB Book Reading Guide", "PersonalKB Wiki Quality Dashboard"}:
        return "policy"
    if any(token in name for token in ["Learning Path", "Reading Spine", "Review Drill", "Cheatsheet", "Checklist", "Guide"]):
        return "policy"
    if "Study" in parts:
        return "policy"
    if name == "Sources Index":
        return "verified"
    if parts and parts[0].startswith("CS "):
        return "verified"
    if parts and parts[0] == "Recipes":
        return "policy"
    return "plausible"


def up_for(path: Path) -> str:
    parts = path.relative_to(kb.ROOT).parts
    if len(parts) == 1:
        return "[[index]]"

    domain = parts[0]
    domain_root = kb.ROOT / domain / f"{domain}.md"
    domain_link = f"[[{domain}/{domain}|{domain}]]" if domain_root.exists() else "[[index]]"
    if len(parts) == 2:
        if path == domain_root:
            return "[[index]]"
        return domain_link

    folder = path.parent
    folder_name = folder.name
    overview_candidates = [
        folder / f"{folder_name} Overview.md",
        folder / f"{folder_name} Overview — Domain.md",
        folder / f"{folder_name} — Overview.md",
    ]
    for candidate in overview_candidates:
        if candidate.exists() and candidate != path:
            target = kb.rel(candidate)[:-3]
            return f"[[{target}|{candidate.stem}]]"
    return domain_link


def add_metadata_and_references() -> int:
    changed_files = 0
    for path in sorted(path for path in kb.markdown_files() if kb.is_wiki_article(path)):
        text = kb.read_text(path)
        updated = text
        fm = kb.frontmatter(updated)
        if not frontmatter_has(fm, "up"):
            updated = set_frontmatter_field(updated, "up", up_for(path))
            fm = kb.frontmatter(updated)
        if not frontmatter_has(fm, "confidence"):
            updated = set_frontmatter_field(updated, "confidence", confidence_for(path))
        if not re.search(r"^## References\s*$", updated, flags=re.MULTILINE):
            updated = updated.rstrip() + "\n\n## References\n"
            source_index = kb.ROOT / path.relative_to(kb.ROOT).parts[0] / "Sources" / "Sources Index.md" if len(path.relative_to(kb.ROOT).parts) > 1 else None
            if source_index and source_index.exists():
                domain = path.relative_to(kb.ROOT).parts[0]
                target = kb.rel(source_index)[:-3]
                updated += f"- [[{target}|{domain} Sources Index]]\n"
            else:
                updated += "- [[index|PersonalKB Index]]\n"
        if updated != text:
            path.write_text(updated.rstrip() + "\n", encoding="utf-8")
            changed_files += 1
    return changed_files


def normalize_reference_headings() -> int:
    changed_files = 0
    trailing_references = re.compile(
        r"\n## References\n- \[\[[^\]]+\|[^\]]+ Sources Index\]\]\n?$",
        flags=re.MULTILINE,
    )
    for path in sorted(path for path in kb.markdown_files() if kb.is_wiki_article(path)):
        text = kb.read_text(path)
        updated = text
        updated = updated.replace("## References to Sources Index", "## References")
        if "## Supporting Chunks / References" in updated and "### References" in updated:
            updated = updated.replace("## Supporting Chunks / References", "## Supporting Chunks")
            updated = updated.replace("### References", "## References", 1)
            updated = trailing_references.sub("", updated).rstrip() + "\n"
        if updated.count("\n## References\n") > 1:
            updated = trailing_references.sub("", updated).rstrip() + "\n"
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed_files += 1
    return changed_files


def repair_placeholders() -> int:
    changed_files = 0
    for path in sorted(path for path in kb.markdown_files() if kb.is_wiki_article(path)):
        text = kb.read_text(path)
        updated = text.replace(PLACEHOLDER_CHUNK_LINE, "- No supporting chunk notes are attached yet.")
        updated = TBD_RE.sub("not confirmed in vault sources", updated)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed_files += 1
    return changed_files


def repair_empty_notes() -> int:
    path = kb.ROOT / "LLM" / "Architecture Variants" / "Efficient Attention and Long-Context Variants.md"
    if not path.exists():
        return 0
    text = kb.read_text(path)
    if text.strip() and re.search(r"^# ", text, flags=re.MULTILINE):
        return 0
    path.write_text(
        "\n".join(
            [
                "---",
                "tags: [llm, architecture, attention, long-context]",
                'up: "[[LLM/LLM|LLM]]"',
                "confidence: plausible",
                "tier-coverage: [core]",
                "---",
                "# Efficient Attention and Long-Context Variants",
                "",
                "This Architecture Variants note is a navigation alias for the maintained dated article on efficient attention and long-context variants.",
                "",
                "- Maintained article: [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants|Efficient Attention and Long-Context Variants]]",
                "",
                "## References",
                "- [[LLM/Sources/Sources Index|LLM Sources Index]]",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return 1


def main() -> int:
    kb.REPORT_DIR.mkdir(parents=True, exist_ok=True)
    empty_notes = repair_empty_notes()
    link_files, unlinked = repair_links()
    reference_heading_files = normalize_reference_headings()
    metadata_files = add_metadata_and_references()
    placeholder_files = repair_placeholders()
    print(
        "\n".join(
            [
                "wiki repair complete",
                f"link_changed_files={link_files}",
                f"unlinked_targets={sum(unlinked.values())}",
                f"metadata_reference_changed_files={metadata_files}",
                f"placeholder_changed_files={placeholder_files}",
                f"empty_notes_filled={empty_notes}",
                f"reference_heading_changed_files={reference_heading_files}",
            ]
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
