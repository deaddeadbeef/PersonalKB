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
SINGLE_LINK_BULLET_RE = re.compile(r"^(\s*-\s+\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\])(?:\s+—\s+.*)?$")
AUDIO_EMBED_RE = re.compile(r"!\[\[[^\]]+\.mp3(?:[#|][^\]]*)?\]\]", re.IGNORECASE)
EMBED_RE = re.compile(r"!\[\[[^\]]+\]\]")
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
    freshness: str = "stable"
    last_verified: str | None = None


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
        folder="Stock Trading",
        title="Stock Trading",
        slug="stock-trading",
        spine_name="Stock Trading Book Reading Spine.md",
        up="[[Stock Trading/Stock Trading|Stock Trading]]",
        promise="Read stock trading as a controlled learning system: ownership, market plumbing, filings, risk limits, and paper practice before real capital.",
        sections=(
            Section("Prologue: No Live Capital Yet", (), "Start with the map, learning path, study index, and source index before touching strategy.", root=True),
            Section("Book I: What A Stock Is", ("Foundations",), "Build the object model: equity ownership, returns, risk, time horizon, and diversification."),
            Section("Book II: Market Plumbing And Account Rules", ("Market Mechanics",), "Learn how orders, brokers, settlement, cash accounts, and margin rules shape every trade."),
            Section("Book III: Evidence Before Thesis", ("Analysis",), "Use filings, fundamentals, price action, momentum, and volatility as evidence layers rather than signals to chase."),
            Section("Book IV: Risk And Paper Practice", ("Risk Management", "Study"), "Turn every idea into a bounded paper experiment with a journal, review rule, and proof artifact."),
            Section("Appendix: Sources", ("Sources",), "Refresh official sources before relying on settlement, margin, tax, broker, or regulatory claims."),
        ),
        freshness="current-sensitive",
        last_verified="2026-07-01",
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
        freshness="current-sensitive",
    ),
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def strip_frontmatter(text: str) -> str:
    match = re.match(r"\A---\s*\r?\n.*?\r?\n---\s*\r?\n", text, flags=re.DOTALL)
    return text[match.end() :] if match else text


def strip_code_fences(text: str) -> str:
    return re.sub(r"^```.*?^```\s*", "", text, flags=re.MULTILINE | re.DOTALL)


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
    value = SUMMARY_LABEL_RE.sub("", value)
    value = re.sub(r"\s+", " ", value).strip(" -")
    value = value.strip(" -—")
    return value.replace("|", "/")


def title_for(path: Path) -> str:
    text = read_text(path)
    for line in strip_frontmatter(text).splitlines():
        if line.startswith("# "):
            return clean_text(line[2:])
    return path.stem.replace("|", "/")


def fallback_summary_for_title(title: str) -> str:
    title = clean_text(title)
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
            or GENERIC_SUMMARY_RE.search(clean_text(cleaned))
        ):
            flush()
            continue
        block.append(cleaned)
    flush()
    return candidates


def summary_for(path: Path, limit: int = 220) -> str:
    text = strip_code_fences(strip_frontmatter(read_text(path)))
    for cleaned in one_line_summary_blocks(text):
        return truncate(clean_text(cleaned), limit)
    title = title_for(path)
    fallback = fallback_summary_for_title(title)
    if fallback and prefer_title_summary(title):
        return truncate(fallback, limit)
    for candidate in paragraph_summary_candidates(text):
        cleaned_text = clean_text(candidate)
        if (
            not cleaned_text
            or ROUTE_SUMMARY_SKIP_RE.match(cleaned_text)
            or GENERIC_SUMMARY_RE.search(cleaned_text)
        ):
            continue
        if cleaned_text:
            return truncate(cleaned_text, limit)
    return truncate(fallback, limit)


def finish_summary(value: str) -> str:
    value = value.strip().rstrip(" ,;:—-")
    if not value:
        return value
    if re.search(r'[.!?][)"\']?$', value):
        return value
    return f"{value}."


def truncate(value: str, limit: int) -> str:
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
        f"freshness: {topic.freshness}",
    ]
    if topic.last_verified:
        lines.append(f"last-verified: {topic.last_verified}")
    lines.extend(
        [
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
    )

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


def resolve_wikilink_target(target: str) -> Path:
    path = ROOT / target
    if path.suffix.lower() != ".md":
        path = path.with_suffix(".md")
    return path


def enrich_llm_book_spine() -> tuple[Path, int, int]:
    output = ROOT / "LLM" / "LLM Book Reading Spine.md"
    lines = read_text(output).splitlines()
    enriched = 0
    changed = 0
    skip_rest = False
    next_lines: list[str] = []
    for line in lines:
        if line.startswith("## Appendices") or line.startswith("## References"):
            skip_rest = True
        if not skip_rest:
            match = SINGLE_LINK_BULLET_RE.match(line)
            if match:
                target_path = resolve_wikilink_target(match.group(2))
                if target_path.exists():
                    summary = summary_for(target_path)
                    if summary:
                        enriched += 1
                        next_line = f"{match.group(1)} — {summary}"
                        if next_line != line:
                            changed += 1
                        line = next_line
        next_lines.append(line)
    output.write_text("\n".join(next_lines).rstrip() + "\n", encoding="utf-8")
    return output, enriched, changed


def render_root_guide(results: list[tuple[Topic, Path, int]]) -> Path:
    llm_count = sum(1 for path in (ROOT / "LLM").rglob("*.md") if is_reader_article(path))
    lines = [
        "---",
        "type: generated-reading-guide",
        "tags: [vault-index, book, reading-path, navigation]",
        'up: "[[index]]"',
        "confidence: verified",
        "freshness: stable",
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
        "## One Reading Session",
        "",
        "Use this loop when you sit down to read. It keeps the vault from becoming passive browsing.",
        "",
        "| Step | Do | Leave behind |",
        "| --- | --- | --- |",
        "| 1. Choose | Pick one route, one topic spine, and one Book section | A single page or section target |",
        "| 2. Read | Read the overview first, then at most three linked articles | Three claims, mechanisms, or decisions worth remembering |",
        "| 3. Explain | Close the page and explain the mechanism, story, or tradeoff in your own words | A short note, spoken explanation, or margin summary |",
        "| 4. Prove | Use a drill, lab, source index, recipe execution, or decision table only if the claim matters | One proof artifact, source check, run result, or next action |",
        "| 5. Stop | Stop when the proof target is satisfied or the missing evidence is named | The next session starts from that evidence gap |",
        "",
        "A good session is small enough to finish. If you open more than one shelf, write down why the second shelf changes the first one.",
        "",
        "## Reading Shelf",
        "",
        "| Topic | Book spine | Linked reader-facing articles |",
        "| --- | --- | ---: |",
        f"| LLM | [[LLM/LLM Book Reading Spine|LLM Book Reading Spine]] | {llm_count} |",
    ]
    for topic, output, count in results:
        lines.append(f"| {topic.title} | {internal_link(output, output.stem, ROOT)} | {count} |")
    lines.extend(
        [
            "",
            "## Choose A Reading Route",
            "",
            "Use these routes when you do not know which shelf to open next. Each route is intentionally cross-topic: a second brain is strongest when it turns isolated notes into reusable judgment.",
            "",
            "### Route A: Local LLM Builder",
            "",
            "Goal: understand LLMs academically and operate local inference with enough systems intuition to debug real failures.",
            "",
            "1. [[LLM/LLM Book Reading Spine|LLM Book Reading Spine]] — read through architecture, training, inference, evaluation, and the local-hosting practicum.",
            "2. [[CS Data Structures/CS Data Structures Book Reading Spine|CS Data Structures Book Reading Spine]] — focus on memory layout, tries, indexes, caches, and persistent structures.",
            "3. [[CS Algorithms/CS Algorithms Book Reading Spine|CS Algorithms Book Reading Spine]] — focus on asymptotics, search, graphs, strings, compression, and approximation limits.",
            "4. [[CS Operating Systems/CS Operating Systems Book Reading Spine|CS Operating Systems Book Reading Spine]] — focus on processes, memory, file systems, I/O, virtualization, and security.",
            "5. [[Programming Languages/Programming Languages Book Reading Spine|Programming Languages Book Reading Spine]] — focus on runtimes, memory management, concurrency, modules, and error handling.",
            "",
            "Proof target: after this route, you should be able to explain a local inference request from prompt text to tokens, tensors, KV cache, scheduler, sampling, output parsing, evaluation, and deployment decision.",
            "",
            "### Route B: Computer Science Backbone",
            "",
            "Goal: build the stable CS substrate that supports systems work, emulator work, language design, and LLM infrastructure.",
            "",
            "1. [[CS Algorithms/CS Algorithms Book Reading Spine|CS Algorithms]] — procedures, proof, cost, graphs, strings, compression, and limits.",
            "2. [[CS Data Structures/CS Data Structures Book Reading Spine|CS Data Structures]] — storage shapes, operation costs, memory locality, trees, hashes, graphs, and advanced indexes.",
            "3. [[CS Operating Systems/CS Operating Systems Book Reading Spine|CS Operating Systems]] — resource abstraction, concurrency, memory, files, I/O, virtualization, and protection.",
            "4. [[Programming Languages/Programming Languages Book Reading Spine|Programming Languages]] — type systems, modules, runtimes, memory models, concurrency models, and metaprogramming.",
            "",
            "Proof target: choose a data structure, algorithm, runtime model, and OS constraint for a concrete program without relying on vibes or memorized names.",
            "",
            "### Route C: Builder And Emulator",
            "",
            "Goal: turn low-level CS knowledge into an implementation-grade mental model.",
            "",
            "1. [[NES Emulation/NES Emulation Book Reading Spine|NES Emulation]] — rebuild the machine from CPU, PPU, APU, bus, mapper, input, and architecture notes.",
            "2. [[CS Operating Systems/CS Operating Systems Book Reading Spine|CS Operating Systems]] — use scheduling, memory, I/O, and synchronization to reason about emulator correctness and performance.",
            "3. [[Programming Languages/Programming Languages Book Reading Spine|Programming Languages]] — use runtime, memory, error, and concurrency tradeoffs to judge implementation choices.",
            "4. [[CS Algorithms/CS Algorithms Book Reading Spine|CS Algorithms]] and [[CS Data Structures/CS Data Structures Book Reading Spine|CS Data Structures]] — use only the parts needed for testing, indexing, state snapshots, and performance.",
            "",
            "Proof target: explain one emulator bug as a mismatch between hardware state, timing, memory mapping, and frontend behavior.",
            "",
            "### Route D: Language Learner",
            "",
            "Goal: keep Japanese study operational instead of letting the vault become an attractive distraction.",
            "",
            "1. [[Japanese/Japanese Book Reading Spine|Japanese Book Reading Spine]] — follow the phase path before browsing grammar or culture pages.",
            "2. Use [[Japanese/Study/Japanese Learning Dashboard|Japanese Learning Dashboard]] as the daily control panel.",
            "3. Use grammar, vocabulary, listening, and speaking pages only when they support the current phase.",
            "4. Use source pages when choosing resources or checking audio/provenance.",
            "",
            "Proof target: every reading session should end in a concrete review item, listening loop, speaking script, or phase checkpoint.",
            "",
            "### Route E: Science, Space, And Story",
            "",
            "Goal: read ambitious technical narratives without losing the boundary between evidence, extrapolation, fiction, and current events.",
            "",
            "1. [[SpaceX/SpaceX Book Reading Spine|SpaceX]] — read the industrial story from Falcon through Starship, Starlink, business logic, and Mars architecture.",
            "2. [[Project Hail Mary/Project Hail Mary Book Reading Spine|Project Hail Mary]] — read the novel and science ledger side by side.",
            "3. Use source indexes aggressively: these topics mix stable engineering, live company facts, speculative architecture, and fictional claims.",
            "",
            "Proof target: classify a claim as verified, plausible, uncertain, policy, or fictional before reusing it.",
            "",
            "### Route F: Market Literacy And Trading Discipline",
            "",
            "Goal: relearn stocks from ownership and market plumbing through evidence, risk, and paper-trading discipline without turning early knowledge into live-capital action.",
            "",
            "1. [[Stock Trading/Stock Trading Book Reading Spine|Stock Trading]] — read ownership, return, market mechanics, account rules, filings, price action, and risk in order.",
            "2. [[Stock Trading/Analysis/Company Filing Worksheet|Company Filing Worksheet]] — turn one filing into a bounded thesis before looking for trade setups.",
            "3. [[Stock Trading/Study/Paper Trading Lab|Paper Trading Lab]] — run a ten-trade paper batch with planned risk and post-trade review.",
            "",
            "Proof target: produce one completed filing worksheet and ten paper-trade journal rows with no live capital, no margin, and no unplanned order types.",
            "",
            "## Operating Modes",
            "",
            "- **Story mode:** read only book spines and overview pages. Stop before drills, chunks, raw notes, and operational runners.",
            "- **Mechanism mode:** open the detailed articles in spine order and explain the causal machinery in your own words.",
            "- **Proof mode:** use study pages, labs, drills, benchmarks, recipes, or source indexes to produce evidence that you can apply the idea.",
            "- **Maintenance mode:** use [[PersonalKB Wiki Quality Dashboard]] and [[log|PersonalKB Maintenance Log]] only when improving the vault itself.",
            "",
            "## What To Read Next",
            "",
            "If a topic feels overwhelming, read its spine prologue and first Book section only. If a page feels too easy, jump to its practice or source appendix. If a claim matters for a decision, leave the article path and go to the source index before trusting it.",
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
    llm_output, llm_enriched, llm_changed = enrich_llm_book_spine()
    print(
        f"wrote {llm_output.relative_to(ROOT).as_posix()} "
        f"({llm_enriched} enriched chapter links, {llm_changed} changed)"
    )
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
