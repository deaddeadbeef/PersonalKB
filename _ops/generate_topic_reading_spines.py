#!/usr/bin/env python3
"""Generate book-style reading spines for PersonalKB topic folders."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

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
ROOT_NON_ARTICLES = {
    "AGENTS.md",
    "index.md",
    "log.md",
    "PersonalKB Book Reading Guide.md",
    "Untitled.base",
}
SKIP_NOTE_NAMES = {
    "LLM Book Reading Spine.md",
}
WIKILINK_INLINE_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")
AUDIO_EMBED_RE = re.compile(r"!\[\[[^\]]+\.mp3(?:[#|][^\]]*)?\]\]", re.IGNORECASE)
EMBED_RE = re.compile(r"!\[\[[^\]]+\]\]")
MONTH_WORD_ORDER = {
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4,
    "fifth": 5,
    "sixth": 6,
    "seventh": 7,
    "eighth": 8,
    "ninth": 9,
    "tenth": 10,
    "eleventh": 11,
    "twelfth": 12,
    "thirteenth": 13,
    "fourteenth": 14,
    "fifteenth": 15,
}


@dataclass(frozen=True)
class Section:
    heading: str
    folders: tuple[str, ...]
    note: str
    root: bool = False


@dataclass(frozen=True)
class Topic:
    folder: str
    title: str
    slug: str
    spine_name: str
    up: str
    promise: str
    sections: tuple[Section, ...]


TOPICS = (
    Topic(
        folder="CS Algorithms",
        title="CS Algorithms",
        slug="cs-algorithms",
        spine_name="CS Algorithms Book Reading Spine.md",
        up="[[CS Algorithms/CS Algorithms|CS Algorithms]]",
        promise="Follow the subject from precise procedures, through proof and growth rates, into the classic families of algorithmic ideas.",
        sections=(
            Section("Prologue: What An Algorithm Is", (), "Start with the map, the learning path, and the vocabulary for exact procedures.", root=True),
            Section("Book I: Proof, Cost, And Recurrence", ("Analysis",), "Build the mental tools: asymptotics, invariants, recurrences, and dynamic programming."),
            Section("Book II: Sorting And Searching", ("Sorting", "Searching"), "Watch small ordering problems become the laboratory for lower bounds and tradeoffs."),
            Section("Book III: Divide, Choose, And Backtrack", ("Divide and Conquer", "Greedy", "Backtracking", "Techniques"), "Compare the main problem-solving patterns by the kind of promise each one needs."),
            Section("Book IV: Graphs As Worlds", ("Graphs",), "Move from arrays to relationships: traversal, paths, spanning trees, and flow."),
            Section("Book V: Strings, Compression, And Cryptography", ("Strings", "Compression", "Cryptography"), "Read sequence algorithms, coding, and secrecy as applied versions of the same design discipline."),
            Section("Book VI: Hardness And Limits", ("Complexity",), "End the theory arc with what efficient computation can and cannot plausibly do."),
            Section("Book VII: The Textbook Walkthrough", ("Books",), "Use chapter notes as the guided classroom route through the source material."),
            Section("Appendices: Practice And Sources", ("Study", "Sources"), "Switch from reading to recall, selection, and provenance."),
        ),
    ),
    Topic(
        folder="CS Data Structures",
        title="CS Data Structures",
        slug="cs-data-structures",
        spine_name="CS Data Structures Book Reading Spine.md",
        up="[[CS Data Structures/CS Data Structures|CS Data Structures]]",
        promise="Read data structures as a story about arranging memory so operations become cheap, predictable, and composable.",
        sections=(
            Section("Prologue: Containers, Interfaces, And Cost", (), "Start with the map, learning path, and foundational vocabulary.", root=True),
            Section("Book I: Linear Memory And Direct Access", ("Foundational Concepts", "Linear Structures", "Hash-Based Structures"), "Learn the baseline shapes: arrays, lists, stacks, queues, hashes, and tables."),
            Section("Book II: Trees, Priority, And Prefixes", ("Trees", "Heaps and Priority Queues", "Tries and String Structures"), "Add hierarchy, ordering, priority, and character-by-character structure."),
            Section("Book III: Relationships As Data", ("Graphs",), "Treat networks as first-class structures rather than incidental references."),
            Section("Book IV: Advanced Access Patterns", ("Advanced Structures",), "Read the specialized structures by the query pattern or machine constraint they optimize."),
            Section("Appendices: Practice And Sources", ("Study", "Sources"), "Use drills, cheatsheets, and source indexes after the first reading pass."),
        ),
    ),
    Topic(
        folder="CS Operating Systems",
        title="CS Operating Systems",
        slug="cs-operating-systems",
        spine_name="CS Operating Systems Book Reading Spine.md",
        up="[[CS Operating Systems/CS Operating Systems|CS Operating Systems]]",
        promise="Read operating systems as the machinery that turns hostile hardware, shared resources, and failures into usable abstractions.",
        sections=(
            Section("Prologue: What An OS Promises", (), "Start with the map, learning path, foundations, and design vocabulary.", root=True),
            Section("Book I: Processes And Coordination", ("Processes", "Synchronization", "Deadlocks"), "Begin with execution, scheduling, mutual exclusion, and the ways coordination can fail."),
            Section("Book II: Memory, Files, And I/O", ("Memory", "File Systems", "IO"), "Follow the path from address spaces to persistence and device boundaries."),
            Section("Book III: Many Machines, One Illusion", ("Multiprocessor", "Virtualization"), "Scale the OS story across cores, virtual machines, and distributed systems."),
            Section("Book IV: Protection And Real Systems", ("Security", "Case Studies", "Design"), "Read the defensive model and the concrete systems that embody it."),
            Section("Book V: The Textbook Walkthrough", ("Books",), "Use Modern Operating Systems chapter notes as a classroom route."),
            Section("Appendices: Practice And Sources", ("Study", "Sources"), "Move into review drills, study indexes, and provenance."),
        ),
    ),
    Topic(
        folder="Japanese",
        title="Japanese",
        slug="japanese",
        spine_name="Japanese Book Reading Spine.md",
        up="[[Japanese/Japanese|Japanese]]",
        promise="Read the Japanese vault as a staged acquisition path: scripts, grammar, vocabulary, listening, output, and cultural register.",
        sections=(
            Section("Prologue: The Learning Contract", (), "Start with the main map and the study control pages that keep the language plan from turning into random browsing.", root=True),
            Section("Book I: The Phase Road", ("Learning Path", "Study"), "Use the monthly and weekly plans as the plot line of the language project."),
            Section("Book II: Writing Systems", ("Writing Systems",), "Learn how kana and kanji divide the work of reading."),
            Section("Book III: Grammar", ("Grammar",), "Build sentence machinery from N5 patterns toward N3-level nuance."),
            Section("Book IV: Vocabulary", ("Vocabulary",), "Turn word lists into usable domains of action."),
            Section("Book V: Listening And Pronunciation", ("Listening",), "Make audio evidence, shadowing, and native-source checks part of the reading path."),
            Section("Book VI: Speaking", ("Speaking",), "Convert recognition into scripts, pronunciation, pitch awareness, and output practice."),
            Section("Book VII: Culture And Register", ("Culture",), "Read politeness, work language, idioms, and cultural cues as part of communicative competence."),
            Section("Appendix: Sources", ("Sources",), "Use source indexes only when you need provenance or resource selection."),
        ),
    ),
    Topic(
        folder="NES Emulation",
        title="NES Emulation",
        slug="nes-emulation",
        spine_name="NES Emulation Book Reading Spine.md",
        up="[[NES Emulation/NES Emulation|NES Emulation]]",
        promise="Read NES emulation as a reconstruction project: hardware model first, then CPU, graphics, audio, cartridges, and emulator architecture.",
        sections=(
            Section("Prologue: The Machine To Rebuild", (), "Start with the main map, learning path, and hardware overview.", root=True),
            Section("Book I: CPU, Bus, And Memory", ("CPU — The 6502 Processor", "Memory Map and Bus"), "Understand instruction execution and the address-space contract before touching pixels."),
            Section("Book II: Picture, Sound, And Input", ("PPU — Picture Processing Unit", "APU — Audio Processing Unit", "Input and Controllers"), "Move from computation to the user-visible frame, audio stream, and controller state."),
            Section("Book III: Cartridges And Mappers", ("Cartridges and Mappers",), "Read cartridges as hardware extensions that change the rules of the base machine."),
            Section("Book IV: Emulator Architecture And Polish", ("Emulator Architecture", "CRT Simulation", "Extended Features"), "Turn component knowledge into a working emulator with timing, presentation, and tooling."),
            Section("Appendices: Practice And Sources", ("Study", "Sources"), "Use drills, cheatsheets, and source registries to test the emulator model."),
        ),
    ),
    Topic(
        folder="Programming Languages",
        title="Programming Languages",
        slug="programming-languages",
        spine_name="Programming Languages Book Reading Spine.md",
        up="[[Programming Languages/Programming Languages|Programming Languages]]",
        promise="Read programming languages as design tradeoffs: what a language makes easy, what it makes explicit, and what its runtime must pay for.",
        sections=(
            Section("Prologue: Why Languages Differ", (), "Start with the map, learning path, genealogy, and language-profile shelves.", root=True),
            Section("Book I: Families And Paradigms", ("Language Genealogy", "Language Profiles", "Programming Paradigms"), "Understand language families and the problem-solving styles they promote."),
            Section("Book II: Types, Modules, And Errors", ("Type Systems", "Module Systems", "Error Handling"), "Read the static and organizational tools that make large programs tractable."),
            Section("Book III: Compilation, Runtime, And Memory", ("Compilation and Runtime", "Memory Management"), "Follow source code into execution, allocation, lifetime, and garbage collection."),
            Section("Book IV: Concurrency And Metaprogramming", ("Concurrency Models", "Metaprogramming"), "End with the places where languages expose control over time, parallelism, and code itself."),
            Section("Appendices: Practice And Sources", ("Study", "Sources"), "Use study drills and source indexes after the conceptual pass."),
        ),
    ),
    Topic(
        folder="Project Hail Mary",
        title="Project Hail Mary",
        slug="project-hail-mary",
        spine_name="Project Hail Mary Book Reading Spine.md",
        up="[[Project Hail Mary/Project Hail Mary|Project Hail Mary]]",
        promise="Read this topic as two books at once: the novel's emotional mystery and the science ledger behind each speculative move.",
        sections=(
            Section("Prologue: The Mission Brief", (), "Start with the main map, learning path, and science scorecard.", root=True),
            Section("Book I: The Novel Spine", ("Novel",), "Read the chapter notes, arcs, timeline, and themes as the narrative backbone."),
            Section("Book II: The Astrophage Crisis", ("Astrophage", "Astronomy"), "Understand the organism, the stellar symptom, and the planetary stakes."),
            Section("Book III: Getting There And Surviving It", ("Propulsion",), "Read the ship, drive, relativity, torpor, and engineering constraints."),
            Section("Book IV: Rocky, Erid, And First Contact", ("Xenobiology", "Characters"), "Move from alien biology into language, friendship, ethics, and choice."),
            Section("Book V: Adaptation And Evidence", ("Adaptation", "Sources"), "Use screen-adaptation notes and source indexes as the afterword."),
        ),
    ),
    Topic(
        folder="Recipes",
        title="Recipes",
        slug="recipes",
        spine_name="Recipes Book Reading Spine.md",
        up="[[Recipes/Recipes|Recipes]]",
        promise="Read the recipe shelf as a practical meal-prep book: targets first, then repeatable categories, then weekly execution.",
        sections=(
            Section("Prologue: Targets And The Meal System", (), "Start with the main recipe map and the weekly plan.", root=True),
            Section("Book I: Portable High-Protein Meals", ("Recipe Library",), "Read by category, then choose meals by protein target, prep burden, and flavor profile."),
            Section("Appendices: Weekly Plans And Sources", ("Weekly Plans", "Sources"), "Use plans for execution and sources for provenance."),
        ),
    ),
    Topic(
        folder="SpaceX",
        title="SpaceX",
        slug="spacex",
        spine_name="SpaceX Book Reading Spine.md",
        up="[[SpaceX/SpaceX|SpaceX]]",
        promise="Read SpaceX as an industrial story: founding purpose, vehicle learning loops, reusability, operations, Starlink cash flow, and Mars architecture.",
        sections=(
            Section("Prologue: The Thesis", (), "Start with the map and learning path before diving into vehicles or missions.", root=True),
            Section("Book I: Origins And Falcon", ("Origins and History", "Falcon Program"), "Begin with founding, Falcon 1 survival, Falcon 9 maturation, and fleet operations."),
            Section("Book II: Engines, Reuse, And Human Spaceflight", ("Engines and Propulsion", "Reusability", "Dragon and Human Spaceflight"), "Read the engineering systems that made cadence, crew transport, and cost change possible."),
            Section("Book III: Starship And Starlink", ("Starship Program", "Starlink"), "Pair the Mars-class vehicle with the satellite business intended to fund and use it."),
            Section("Book IV: Facilities, Missions, And Deep Dives", ("Launch Operations and Facilities", "Missions and Payloads", "Technology Deep Dives"), "Study the operations layer and the technical subsystems that make high cadence credible."),
            Section("Book V: Business And Mars", ("Business and Economics", "Mars and Beyond"), "End with market disruption, funding logic, and the long-range settlement architecture."),
            Section("Appendices: Practice And Sources", ("Study", "Sources"), "Use drills, cheatsheets, and source indexes after the narrative pass."),
        ),
    ),
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def strip_frontmatter(text: str) -> str:
    match = re.match(r"\A---\s*\r?\n.*?\r?\n---\s*\r?\n", text, flags=re.DOTALL)
    return text[match.end() :] if match else text


def clean_text(value: str) -> str:
    value = AUDIO_EMBED_RE.sub("", value)
    value = EMBED_RE.sub("", value)
    value = re.sub(r"^\[![^\]]+\]\s*", "", value)

    def replace_link(match: re.Match[str]) -> str:
        display = match.group(2)
        if display:
            return display.strip()
        return match.group(1).replace("\\", "/").rsplit("/", 1)[-1].strip()

    value = WIKILINK_INLINE_RE.sub(replace_link, value)
    value = value.replace("**", "").replace("__", "").replace("*", "")
    value = value.replace("`", "")
    value = re.sub(r"\s+", " ", value).strip(" -")
    value = value.strip(" -—")
    return value.replace("|", "/")


def title_for(path: Path) -> str:
    text = read_text(path)
    for line in strip_frontmatter(text).splitlines():
        if line.startswith("# "):
            return clean_text(line[2:])
    return path.stem.replace("|", "/")


def summary_for(path: Path, limit: int = 150) -> str:
    text = strip_frontmatter(read_text(path))
    for line in text.splitlines():
        cleaned = line.strip()
        if cleaned.startswith(">"):
            cleaned = cleaned.lstrip("> ").strip()
            cleaned = re.sub(r"\*\*One-line summary\*\*:?", "", cleaned).strip()
            if cleaned:
                return truncate(clean_text(cleaned), limit)
    for line in text.splitlines():
        cleaned = line.strip()
        if not cleaned or cleaned.startswith("#") or cleaned.startswith("|") or cleaned.startswith("```"):
            continue
        if cleaned.startswith("- ") or cleaned.startswith("* "):
            continue
        return truncate(clean_text(cleaned), limit)
    return ""


def truncate(value: str, limit: int) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "..."


def natural_key(path: Path) -> tuple[object, ...]:
    rel = path.as_posix().lower()
    return tuple(int(part) if part.isdigit() else part for part in re.split(r"(\d+)", rel))


def note_priority(path: Path, topic: Topic | None = None) -> tuple[object, ...]:
    name = path.stem.lower()
    parent = path.parent.name.lower()
    root_rank = 20
    if topic and path.parent == ROOT / topic.folder:
        if name == topic.folder.lower():
            root_rank = 0
        elif "learning path" in name:
            root_rank = 1
        elif "scorecard" in name:
            root_rank = 2
        else:
            root_rank = 5

    special_rank = 50
    if "learning dashboard" in name:
        special_rank = 0
    elif "overview" in name:
        special_rank = 1
    elif "chapter index" in name or name.endswith("study index") or name.endswith("sources index"):
        special_rank = 2
    elif "learning path" in name:
        special_rank = 3
    elif "timeline" in name:
        special_rank = 4
    elif name.startswith("arc - "):
        special_rank = 5
    elif "cheatsheet" in name or "scorecard" in name:
        special_rank = 6
    elif "review drill" in name or "weekly review" in name:
        special_rank = 80
    elif parent == "sources":
        special_rank = 90

    month_rank = 60
    for word, number in MONTH_WORD_ORDER.items():
        if name.startswith(f"{word} week"):
            month_rank = 0
            break
        if name.startswith(f"{word} month"):
            month_rank = number
            break
    phase_match = re.search(r"phase\s+(\d+)", name)
    phase_rank = int(phase_match.group(1)) if phase_match else 50

    chapter_match = re.search(r"chapter\s+(\d+)", name)
    chapter_rank = int(chapter_match.group(1)) if chapter_match else 999
    if "epilogue" in name:
        chapter_rank = 1000

    return (root_rank, special_rank, month_rank, phase_rank, chapter_rank, natural_key(path))


def is_reader_article(path: Path) -> bool:
    if path.suffix.lower() != ".md":
        return False
    rel_parts = path.relative_to(ROOT).parts
    if path.name in ROOT_NON_ARTICLES or path.name in SKIP_NOTE_NAMES:
        return False
    if path.name.endswith("Book Reading Spine.md"):
        return False
    if path.name.startswith("_"):
        return False
    return set(rel_parts).isdisjoint(NON_WIKI_PARTS)


def topic_paths(topic: Topic) -> list[Path]:
    base = ROOT / topic.folder
    return sorted((path for path in base.rglob("*.md") if is_reader_article(path)), key=lambda path: note_priority(path, topic))


def obsidian_link(path: Path, display: str | None = None) -> str:
    target = path.relative_to(ROOT).with_suffix("").as_posix()
    label = (display or title_for(path)).replace("|", "/")
    return f"[[{target}|{label}]]"


def internal_link(path: Path, display: str | None = None, source_dir: Path | None = None) -> str:
    label = (display or title_for(path)).replace("|", "/")
    if "#" not in path.name:
        return obsidian_link(path, label)
    base = source_dir or ROOT
    target = path.relative_to(base).as_posix().replace("#", "%23")
    return f"[{label}](<{target}>)"


def section_paths(topic: Topic, section: Section, remaining: set[Path]) -> list[Path]:
    base = ROOT / topic.folder
    folder_order = {folder: index for index, folder in enumerate(section.folders)}

    def sort_key(path: Path) -> tuple[object, ...]:
        rel_parts = path.relative_to(base).parts
        if len(rel_parts) == 1:
            return (-1, note_priority(path, topic))
        return (folder_order.get(rel_parts[0], 999), note_priority(path, topic))

    if section.root:
        roots = [path for path in remaining if path.parent == base]
        folder_hits = [
            path
            for path in remaining
            if len(path.relative_to(base).parts) > 1 and path.relative_to(base).parts[0] in section.folders
        ]
        paths = roots + folder_hits
    else:
        paths = [
            path
            for path in remaining
            if len(path.relative_to(base).parts) > 1 and path.relative_to(base).parts[0] in section.folders
        ]
    return sorted(paths, key=sort_key)


def render_note_list(paths: list[Path], source_dir: Path) -> list[str]:
    lines: list[str] = []
    for path in paths:
        summary = summary_for(path)
        suffix = f" — {summary}" if summary else ""
        lines.append(f"- {internal_link(path, source_dir=source_dir)}{suffix}")
    return lines


def render_topic(topic: Topic) -> tuple[Path, int]:
    paths = topic_paths(topic)
    remaining = set(paths)
    output = ROOT / topic.folder / topic.spine_name
    lines = [
        "---",
        "type: generated-reading-spine",
        f"tags: [{topic.slug}, index, book, reading-path, navigation]",
        f'up: "{topic.up}"',
        "confidence: verified",
        "tier-coverage: [intuition, core, deep-dive, practice]",
        "---",
        f"# {topic.title} Book Reading Spine",
        "",
        topic.promise,
        "",
        "This page is the reader-facing spine. Treat it like the table of contents of a good book: read the chapter openers first, then deepen through the linked articles, then use study notes and sources as appendices.",
        "",
        "## How To Read This Topic",
        "",
        "1. **First pass: story.** Read the prologue and each Book heading, opening only overview and learning-path pages first.",
        "2. **Second pass: mechanism.** Return to every linked article in order and follow the concepts inside each chapter.",
        "3. **Third pass: practice.** Use study drills, checklists, labs, plans, or recipes to prove the knowledge operationally.",
        "4. **Fourth pass: evidence.** Use source indexes when a claim matters or when the page is time-sensitive.",
        "",
    ]

    linked_count = 0
    for section in topic.sections:
        paths_for_section = section_paths(topic, section, remaining)
        if not paths_for_section:
            continue
        for path in paths_for_section:
            remaining.discard(path)
        linked_count += len(paths_for_section)
        lines.extend([f"## {section.heading}", "", section.note, ""])
        lines.extend(render_note_list(paths_for_section, output.parent))
        lines.append("")

    if remaining:
        paths_for_section = sorted(remaining, key=lambda path: note_priority(path, topic))
        linked_count += len(paths_for_section)
        lines.extend(
            [
                "## Appendix: Remaining Reader-Facing Notes",
                "",
                "These notes are part of the topic corpus but do not belong cleanly to the main narrative chapters yet.",
                "",
            ]
        )
        lines.extend(render_note_list(paths_for_section, output.parent))
        lines.append("")

    source_index = ROOT / topic.folder / "Sources" / "Sources Index.md"
    lines.extend(
        [
            "## Coverage",
            "",
            f"- Reader-facing articles linked here: {linked_count}",
            "- Protected raw, chunk, template, query, audio, and operations folders are intentionally not expanded here.",
            "- The root vault index remains the exhaustive generated listing across every topic.",
            "",
            "## References",
            "",
            f"- {topic.up}",
        ]
    )
    if source_index.exists():
        lines.append(f"- {internal_link(source_index, source_dir=output.parent)}")
    lines.append("")

    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return output, linked_count


def render_root_guide(results: list[tuple[Topic, Path, int]]) -> Path:
    lines = [
        "---",
        "type: generated-reading-guide",
        "tags: [vault-index, book, reading-path, navigation]",
        'up: "[[index]]"',
        "confidence: verified",
        "tier-coverage: [intuition, core, deep-dive, practice]",
        "---",
        "# PersonalKB Book Reading Guide",
        "",
        "This is the front door for reading the vault as a shelf of books instead of a pile of notes. Each linked spine gives one topic a narrative order, while the generated root index remains the exhaustive catalog.",
        "",
        "## How To Use The Shelf",
        "",
        "1. Pick one topic and read its spine like a book table of contents.",
        "2. Read overview pages first, then the detailed articles in each Book section.",
        "3. Use study pages, drills, checklists, labs, or recipe plans only after the main story makes sense.",
        "4. Use source indexes when you need provenance, citations, or a factual audit trail.",
        "",
        "## Reading Shelf",
        "",
        "| Topic | Book spine | Linked reader-facing articles |",
        "| --- | --- | ---: |",
        f"| LLM | [[LLM/LLM Book Reading Spine|LLM Book Reading Spine]] | existing spine |",
    ]
    for topic, output, count in results:
        lines.append(f"| {topic.title} | {internal_link(output, output.stem, ROOT)} | {count} |")
    lines.extend(
        [
            "",
            "## Back-Of-Book Tools",
            "",
            "- [[index|PersonalKB Index]] — generated exhaustive vault index.",
            "- [[PersonalKB Wiki Quality Dashboard]] — current reader-facing quality verdict and next cleanup order.",
            "- [[log|PersonalKB Maintenance Log]] — maintenance history.",
            "- [[LLM/LLM Corpus Index|LLM Corpus Index]] — complete LLM corpus map.",
            "",
            "## References",
            "",
            "- [[index|PersonalKB Index]]",
            "- [[PersonalKB Wiki Quality Dashboard]]",
            "- [[log|PersonalKB Maintenance Log]]",
            "",
            f"Generated: {datetime.now().isoformat(timespec='seconds')}",
            "",
        ]
    )
    output = ROOT / "PersonalKB Book Reading Guide.md"
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return output


def main() -> int:
    results: list[tuple[Topic, Path, int]] = []
    for topic in TOPICS:
        output, count = render_topic(topic)
        results.append((topic, output, count))
        print(f"wrote {output.relative_to(ROOT).as_posix()} ({count} linked articles)")
    guide = render_root_guide(results)
    print(f"wrote {guide.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
