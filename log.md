---
type: maintenance-log
tags: [vault-log, generated]
---
# PersonalKB Maintenance Log

Append-only record of ingest, query, lint, and refinement operations.

## [2026-04-27] setup | LLM wiki operating loop

Scope: initialized agent schema, audit tooling, generated index, and maintenance log.

Changed files:
- `AGENTS.md`
- `_ops/`
- `index.md`
- `log.md`

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`

## [2026-04-27] refine | CS Data Structures pilot

Scope: pilot refinement of 10 CS Data Structures wiki notes with missing references and pending chunk placeholders.

Changed content files:
- `CS Data Structures/Advanced Structures/Disjoint Sets and Union-Find.md`
- `CS Data Structures/Advanced Structures/Fenwick Trees.md`
- `CS Data Structures/Advanced Structures/Segment Trees.md`
- `CS Data Structures/Advanced Structures/Skip Lists.md`
- `CS Data Structures/Graphs/Adjacency List and Adjacency Matrix.md`
- `CS Data Structures/Graphs/Graph Properties and Terminology.md`
- `CS Data Structures/Hash-Based Structures/Bloom Filters and Probabilistic Structures.md`
- `CS Data Structures/Hash-Based Structures/Hash Tables and Hash Functions.md`
- `CS Data Structures/Heaps and Priority Queues/Binary Heaps.md`
- `CS Data Structures/Heaps and Priority Queues/Priority Queue ADT.md`

Maintenance changes:
- Regenerated `_ops/reports/` and `index.md`.
- Fixed `_ops/personal_kb.py` wiki-link resolution for note names containing decimal points.

Audit deltas:
- Missing references: 286 -> 280
- Placeholder hits: 124 -> 114
- Broken link occurrences: 973 -> 953

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`

## [2026-04-27] refine | CS Data Structures batch 2

Scope: bounded refinement of 10 CS Data Structures wiki notes in foundational concepts, graph representations, and collision resolution.

Changed content files:
- `CS Data Structures/Foundational Concepts/Abstract Data Types.md`
- `CS Data Structures/Foundational Concepts/Amortized Analysis.md`
- `CS Data Structures/Foundational Concepts/Asymptotic Analysis and Big-O Notation.md`
- `CS Data Structures/Foundational Concepts/Data Structure Comparison and Selection.md`
- `CS Data Structures/Foundational Concepts/Memory Layout and Cache Performance.md`
- `CS Data Structures/Foundational Concepts/Pointer-Based vs Array-Based Structures.md`
- `CS Data Structures/Graphs/Graph Representations Overview.md`
- `CS Data Structures/Graphs/Implicit and Compressed Graph Representations.md`
- `CS Data Structures/Graphs/Weighted and Directed Graphs.md`
- `CS Data Structures/Hash-Based Structures/Collision Resolution Strategies.md`

Maintenance changes:
- Regenerated `_ops/reports/` and `index.md`.
- Normalized references to `[[CS Data Structures/Sources/Sources Index|Sources Index]]`.
- Replaced pending chunk placeholders with existing chunk links and explicit source-gap notes where extracted chunk coverage is incomplete.

Audit deltas:
- Missing references: 280 -> 278
- Placeholder hits: 114 -> 104
- Broken link occurrences: 953 -> 953

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`

## [2026-04-27] refine | CS Data Structures batch 3

Scope: bounded refinement of 10 CS Data Structures wiki notes in advanced structures, hash-based structures, heaps, and linear structures.

Changed content files:
- `CS Data Structures/Advanced Structures/Interval Trees and Range Trees.md`
- `CS Data Structures/Advanced Structures/k-d Trees and Spatial Data Structures.md`
- `CS Data Structures/Hash-Based Structures/Consistent Hashing.md`
- `CS Data Structures/Hash-Based Structures/Cuckoo Hashing.md`
- `CS Data Structures/Hash-Based Structures/Universal and Perfect Hashing.md`
- `CS Data Structures/Heaps and Priority Queues/Binomial Heaps.md`
- `CS Data Structures/Heaps and Priority Queues/Fibonacci Heaps.md`
- `CS Data Structures/Heaps and Priority Queues/Heap Applications and d-ary Heaps.md`
- `CS Data Structures/Linear Structures/Arrays and Dynamic Arrays.md`
- `CS Data Structures/Linear Structures/Circular Buffers.md`

Maintenance changes:
- Regenerated `_ops/reports/` and `index.md`.
- Normalized references to `[[CS Data Structures/Sources/Sources Index|Sources Index]]`.
- Replaced selected-note pending chunk placeholders with existing chunk links and explicit source-gap notes where extracted chunk coverage is incomplete.

Audit deltas:
- Missing references: 278 -> 276
- Placeholder hits: 104 -> 94
- Broken link occurrences: 953 -> 953

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 1 audio coverage map

Scope: add a coverage map that shows how each required Phase 1 page is supported by local clips, authentic audio, and pronunciation QA.

Changed content files:
- `Japanese/Listening/Phase 1 Audio Coverage Map.md`
- `Japanese/Japanese.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Learning Path/Phase 1 — Foundation.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Phase 1 Weekly Review.md`
- `Japanese/Listening/Phase 1 Local Audio Practice.md`
- `Japanese/Listening/Phase 1 Authentic Audio Spine.md`

Maintenance changes:
- Added a Phase 1 coverage table with embedded local clip counts for required pages.
- Routed Start Here, the dashboard, study index, Phase 1 plan, weekly review, and audio pages to the coverage map.

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- Phase 1 coverage count check across required pages.
- Local MP3 embed check across changed audio pages: 44 embeds, 0 missing.
- `git diff --check`

## [2026-06-06] curate | Japanese pronunciation and audio accuracy

Scope: add a policy/practice page for deciding when local TTS clips are safe, when native/official audio is required, and how to log/fix suspect pronunciation.

Changed content files:
- `Japanese/Speaking/Pronunciation and Audio Accuracy.md`
- `Japanese/Speaking/Speaking Overview.md`
- `Japanese/Speaking/Pronunciation — Difficult Sounds for English Speakers.md`
- `Japanese/Speaking/Pitch Accent/Pitch Accent — Introduction.md`
- `Japanese/Speaking/Pitch Accent/Pitch Accent — Common Patterns.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Listening/Phase 1 Local Audio Practice.md`
- `Japanese/Listening/Phase 1 Authentic Audio Spine.md`
- `Japanese/Sources/Sources Index.md`
- `Japanese/Japanese.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Japanese Learning Dashboard.md`

Maintenance changes:
- Added checked pronunciation-source provenance for OJAD, NHK accent dictionary, and Forvo.
- Routed Start Here, speaking/listening hubs, pitch pages, and Phase 1 audio pages to the new accuracy guide.

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- Local MP3 embed check across changed audio/pronunciation pages: 110 embeds, 0 missing.
- New pronunciation-source links verified by web open; local HTTP probes returned 200 for NHK links, while OJAD/Forvo required browser/web verification.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 1 authentic audio spine

Scope: add a human-recorded/official-course audio route for Phase 1 so local pronunciation drills are paired with authentic audio from the start.

Changed content files:
- `Japanese/Listening/Phase 1 Authentic Audio Spine.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Listening/Beginner Listening Resources.md`
- `Japanese/Listening/Phase 1 Local Audio Practice.md`
- `Japanese/Learning Path/Phase 1 — Foundation.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Phase 1 Weekly Review.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Japanese.md`
- `Japanese/Sources/Sources Index.md`

Maintenance changes:
- Added verified audio-source provenance for GENKI, Irodori, and NHK Easy Japanese.
- Routed Phase 1 listening decisions through an authentic audio spine plus the existing local clip ladder.

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- Local MP3 embed check: 41 embeds, 0 missing.
- External source URL status check for the new audio-source links.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 1 local audio ladder

Scope: add a learner-facing daily audio path for Phase 1 so Japanese listening starts from ordered, local clips instead of the raw audio catalog.

Changed content files:
- `Japanese/Listening/Phase 1 Local Audio Practice.md`
- `Japanese/Listening/Beginner Listening Resources.md`
- `Japanese/Learning Path/Phase 1 — Foundation.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Japanese.md`

Maintenance changes:
- Routed Start Here, the dashboard, study index, daily routine, and resource policy to the new Phase 1 audio ladder.
- Kept native course audio as the authenticity anchor and local manifest-guarded clips as the repeatable pronunciation practice layer.

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- Local MP3 embed check: 41 embeds, 0 missing.
- `git diff --check`

## [2026-06-06] refine | Japanese audio reading-hint audit

Scope: added a repeatable pronunciation-manifest audit for entries with explicit romaji hints, then repaired the remaining high-confidence reading risks it found.

Changed content files:
- `Japanese/_audio/audit_reading_hints.py`
- `Japanese/_audio/build_pronunciation_manifest.py`
- `Japanese/_audio/pronunciation_manifest.json`
- `Japanese/_audio/gap-058-(ikkagetsu).mp3`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`
- `_ops/reports/japanese-audio-reading-hints-audit.txt`

Maintenance changes:
- Added a reading-hint audit that compares parenthesized romaji hints against pronunciation-manifest TTS text readings.
- Forced `一か月 (ikkagetsu)` to synthesize from `いっかげつ`.
- Forced `開ける (akeru)` to synthesize from `あける`; regenerated output matched the existing clip bytes, but the manifest now locks the intended reading.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`
- manifest/audio inventory check: `1810` entries, `1810` MP3 files, `0` missing, `0` extra, `0` zero-size
- `ffprobe` duration check for `gap-058-(ikkagetsu).mp3` and `gap-184-(akeru)-open.mp3`
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`

## [2026-06-06] refine | Japanese audio OCR cleanup

Scope: targeted repair pass for remaining OCR-corrupted Japanese text that fed local pronunciation clips.

Changed content files:
- `Japanese/Grammar/N5 Grammar/N5 Grammar — Adjectives.md`
- `Japanese/Grammar/N5 Grammar/N5 Grammar — Verb Forms.md`
- `Japanese/_audio/Audio Index.md`
- `Japanese/_audio/build_pronunciation_manifest.py`
- `Japanese/_audio/gramn5_full_manifest.json`
- `Japanese/_audio/pronunciation_manifest.json`
- `Japanese/_audio/adj-007-atsui.mp3`
- `Japanese/_audio/verb-018-oyogu.mp3`
- `Japanese/_audio/verb-019-oyoide.mp3`
- `_ops/personal_kb.py`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`

Maintenance changes:
- Repaired `暮い` to `暑い` for the N5 adjective hot example and regenerated `adj-007-atsui.mp3`.
- Repaired the ぐ -> いで verb example from `泣ぐ -> 泣いで` to `泳ぐ -> 泳いで`.
- Renamed the misleading `verb-018-kyuu-gu.mp3` clip to `verb-018-oyogu.mp3` and regenerated the affected verb audio.
- Added pronunciation-manifest overrides so these OCR repairs remain stable if the audio manifest is rebuilt.
- Excluded AgentOS `.tasks/` notes from wiki-content audit metrics so task state does not count as Japanese article debt.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py`
- targeted audio inventory check for `adj-007-atsui.mp3`, `verb-018-oyogu.mp3`, and `verb-019-oyoide.mp3`
- `ffprobe` duration check for the three regenerated MP3 files
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`

## [2026-05-17] refine | Japanese audio pronunciation regeneration

Scope: rebuilt the Japanese audio generation path and regenerated the full audio inventory from pronunciation-safe TTS inputs.

Changed content files:
- `Japanese/Vocabulary/Core Words/Core 500 — Daily Life Vocabulary.md`
- `Japanese/_audio/*.mp3`
- `Japanese/_audio/build_pronunciation_manifest.py`
- `Japanese/_audio/generate_tts.py`
- `Japanese/_audio/pronunciation_manifest.json`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`

Maintenance changes:
- Added a canonical pronunciation manifest covering all 1,810 Japanese MP3 files.
- Replaced bad TTS inputs harvested from rule text, placeholders, romanization notes, particle spellings, and OCR-corrupted terms with pronounceable Japanese.
- Regenerated all 1,810 audio clips with Azure Japanese neural TTS; unchanged TTS inputs remained byte-identical where Azure output matched the previous clip.
- Corrected visible OCR errors in the Core 500 daily-life vocabulary table so the page text and fixed audio agree.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`
- manifest/audio inventory check: `1810` entries, `1810` MP3 files, `0` missing, `0` extra, `0` zero-size
- `ffprobe` duration check across all `1810` MP3 files: `0` failures
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`

## [2026-05-06] remove | Body Recomp section

Scope: removed the Body Recomp topic from the active vault and maintenance rotation.

Removed files:
- `Body Recomp/`

Maintenance changes:
- Removed the Body Recomp row from `Welcome.md`.
- Removed Body Recomp from `_ops/engineer-daemon-mission.md` scope rotation and risk notes.
- Regenerated `_ops/reports/` and `index.md`.

Audit counts:
- Files total: 4711
- Markdown files: 2842
- Candidate articles: 755
- Stubs under 1500 bytes: 21
- Missing confidence: 251
- Missing references: 252
- Broken link occurrences: 941

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`

## [2026-05-05] refine | supervised CS Data Structures review and graphs pass

Scope: supervised integration of Engineer curation cycles 2 and 3 into the main vault.

Changed content files:
- `CS Data Structures/Study/DS Review — Advanced Structures.md`
- `CS Data Structures/Graphs/Graphs Overview.md`

Maintenance changes:
- Applied only note-content changes from the successful Engineer worktree commits.
- Regenerated `_ops/reports/` and `index.md` from the combined vault state.
- Preserved the two unrelated dirty user files without staging or modifying them.

Audit counts:
- Stubs under 1500 bytes: 22
- Missing confidence: 253
- Missing references: 252
- Broken link occurrences: 941

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`

## [2026-05-05] refine | Engineer recurring CS Data Structures integration

Scope: supervised integration of the successful Engineer recurring wiki-curation cycles into the main vault.

Changed content files:
- `CS Data Structures/Hash-Based Structures/Hash-Based Structures Overview.md`
- `CS Data Structures/Study/CS Data Structures Study Index.md`
- `CS Data Structures/Study/DS Cheatsheet — Operation Complexities.md`
- `CS Data Structures/Study/DS Review — Hash Tables.md`
- `CS Data Structures/Study/DS Review — Heaps and Priority Queues.md`
- `CS Data Structures/Study/DS Review — Linear Structures.md`
- `CS Data Structures/Study/DS Review — Trees and Balancing.md`
- `CS Data Structures/Tries and String Structures/Tries and String Structures Overview.md`
- `Priority Queues and Heaps.md`

Maintenance changes:
- Applied only note-content changes from the successful Engineer worktree commits.
- Regenerated `_ops/reports/` and `index.md` from the combined vault state.
- Reconciled independently-authored overlapping edits in the hash-table, heap, and hash-based overview notes.

Audit counts:
- Missing references: 257
- Placeholder hits: 79
- Broken link occurrences: 945

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`

## [2026-05-04] ops/refine | engineer daemon mission and CS Data Structures pilot cycle 1

Scope: saved the long-running engineer-daemon curation mission, created the CS Data Structures pilot report, and completed the first bounded pilot pass on 3 safe hub notes.

Changed content files:
- `CS Data Structures/CS Data Structures.md`
- `CS Data Structures/Advanced Structures/Advanced Structures Overview.md`
- `CS Data Structures/Foundational Concepts/Foundational Concepts Overview.md`

Maintenance changes:
- Added `_ops/engineer-daemon-mission.md`.
- Added `_ops/reports/cs-data-structures-pilot.md`.
- Regenerated `_ops/reports/` and `index.md`.
- Added missing `up`, `confidence`, and `## References` metadata for the selected notes.
- Left pre-existing dirty files out of scope.

Audit deltas:
- Missing `up`: 31 -> 30
- Missing `confidence`: 268 -> 265
- Missing references: 270 -> 267
- Placeholder hits: 79 -> 79
- Broken link occurrences: 950 -> 950

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`

## [2026-04-28] refine | CS Data Structures batch 5 rerun

Scope: bounded refinement of 10 CS Data Structures wiki notes in tries, string structures, and advanced structures.

Changed content files:
- `CS Data Structures/Advanced Structures/Concurrent Data Structures.md`
- `CS Data Structures/Advanced Structures/External Memory Structures.md`
- `CS Data Structures/Advanced Structures/LRU and LFU Caches.md`
- `CS Data Structures/Advanced Structures/Persistent and Immutable Structures.md`
- `CS Data Structures/Tries and String Structures/Compressed Tries and Radix Trees.md`
- `CS Data Structures/Tries and String Structures/Rope Data Structure.md`
- `CS Data Structures/Tries and String Structures/Suffix Arrays.md`
- `CS Data Structures/Tries and String Structures/Suffix Trees.md`
- `CS Data Structures/Tries and String Structures/Ternary Search Trees.md`
- `CS Data Structures/Tries and String Structures/Tries and Prefix Trees.md`

Maintenance changes:
- Regenerated `_ops/reports/` and `index.md`.
- Normalized references to `[[CS Data Structures/Sources/Sources Index|Sources Index]]`.
- Replaced selected-note pending chunk placeholders with existing chunk links and explicit source-gap notes where extracted chunk coverage is incomplete.

Audit counts:
- Missing references: 271
- Placeholder hits: 81
- Broken link occurrences: 951

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `git diff --check`

## [2026-04-27] refine | CS Data Structures batch 4

Scope: bounded refinement of 10 CS Data Structures wiki notes in linear structures and trees.

Changed content files:
- `CS Data Structures/Linear Structures/Doubly Linked Lists and Circular Lists.md`
- `CS Data Structures/Linear Structures/Queues and Deques.md`
- `CS Data Structures/Linear Structures/Singly Linked Lists.md`
- `CS Data Structures/Linear Structures/Stacks.md`
- `CS Data Structures/Trees/AVL Trees.md`
- `CS Data Structures/Trees/B-Trees and B-Plus Trees.md`
- `CS Data Structures/Trees/Binary Search Trees.md`
- `CS Data Structures/Trees/Binary Trees and Traversals.md`
- `CS Data Structures/Trees/Red-Black Trees.md`
- `CS Data Structures/Trees/Splay Trees and Treaps.md`

Maintenance changes:
- Regenerated `_ops/reports/` and `index.md`.
- Normalized references to `[[CS Data Structures/Sources/Sources Index|Sources Index]]`.
- Replaced selected-note pending chunk placeholders with existing chunk links and explicit source-gap notes where extracted chunk coverage is incomplete.

Audit deltas:
- Missing references: 276 -> 270
- Placeholder hits: 94 -> 84
- Broken link occurrences: 953 -> 953

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`

## [2026-05-05] refine | heaps hub redirect note

Scope: replaced the empty root heap note with a compact redirect/index note and added verification metadata plus references to the heaps overview.

Changed content files:
- `Priority Queues and Heaps.md`
- `CS Data Structures/Heaps and Priority Queues/Heaps and Priority Queues Overview.md`

Maintenance changes:
- Updated `log.md` and repaired a path-qualified ambiguous related-hub link.
- Planned/generated audit and index outputs via the standard `_ops/personal_kb.py` maintenance workflow.

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`

## [2026-05-05] refine | CS Data Structures trie leaf references

Scope: bounded curation of 3 CS Data Structures trie/string leaf notes outside the 0886df0 integration set.

Changed content files:
- `CS Data Structures/Tries and String Structures/Compressed Tries and Radix Trees.md`
- `CS Data Structures/Tries and String Structures/Suffix Trees.md`
- `CS Data Structures/Tries and String Structures/Tries and Prefix Trees.md`

Maintenance changes:
- Regenerated `_ops/reports/` and `index.md`.
- Split combined supporting/reference headings into audit-recognized `## Supporting Chunks` and `## References` sections.
- Repaired obvious broken cross-links to existing CS Data Structures overview notes.

Audit deltas:
- Missing references: 257 -> 254
- Broken link occurrences: 945 -> 941

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`

## [2026-05-17] refine | Japanese learning cockpit

Scope: first human-facing curation pass for the Japanese vault, focused on making the topic consumable for systematic self-study.

Changed content files:
- `Japanese/Japanese.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Sources/Sources Index.md`
- `Japanese/Study/Study Roadmap — Beginner to Intermediate.md`
- `Japanese/Speaking/Speaking Overview.md`
- `Japanese/Culture/Culture Overview.md`

Maintenance changes:
- Added a day-to-day study dashboard with current phase, twelve-week runway, daily loop, checkpoints, reading order, and curation backlog.
- Replaced generic generated prose in the Japanese hub and study index with navigation aimed at a human learner.
- Added checked external source links for JLPT, Irodori, Genki, Tae Kim, Anki, and WaniKani.
- Repaired existing Japanese navigation links that pointed to the non-existent `Keigo — Politeness Levels Overview` page.

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`

## [2026-05-17] refine | Japanese Phase 1 wiki curation

Scope: first content-level curation batch for the Japanese wiki, focused on the pages a human learner consumes during Phase 1.

Changed content files:
- `Japanese/Learning Path/Phase 1 — Foundation.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Phase 1 Weekly Review.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Writing Systems/Writing Systems Overview.md`
- `Japanese/Writing Systems/Hiragana/Hiragana Complete Guide.md`
- `Japanese/Writing Systems/Katakana/Katakana Complete Guide.md`
- `Japanese/Grammar/N5 Grammar/N5 Grammar — Sentence Patterns.md`
- `Japanese/Vocabulary/Core Words/Core 100 — Survival Japanese.md`

Maintenance changes:
- Replaced generated filler in key Phase 1 pages with concrete study instructions, checkpoints, and practice ladders.
- Added a weekly review note for Phase 1 so the learner can track actual study evidence.
- Preserved existing audio references, kana charts, and supporting chunk links.

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`

## [2026-05-17] refine | Japanese Start Here sequence

Scope: expanded the Japanese hub into the canonical ordered consumption path for the whole Japanese wiki.

Changed content files:
- `Japanese/Japanese.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`

Maintenance changes:
- Replaced the shallow Start Here link table with a staged order covering orientation, Phase 1, Phase 2, Phase 3, Phase 4, Phase 5, and reference-only pages.
- Linked the dashboard and study index back to `[[Japanese#Start Here]]` so daily execution and full navigation agree.

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 2 audio coverage

Scope: extend the Japanese audio-support system into Phase 2 so N5 grammar, vocabulary, kanji, conversation, and register study remain paired with authentic pronunciation models and local clips.

Changed content files:
- `Japanese/Listening/Phase 2 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 2 Audio Coverage Map.md`
- `Japanese/Japanese.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Learning Path/Phase 2 — Building Blocks.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Listening/Phase 1 Audio Coverage Map.md`

Maintenance changes:
- Added a Phase 2 authentic audio spine for Genki, Irodori, NHK, tutor, or native-speaker audio.
- Added a Phase 2 coverage map with local MP3 counts for required Phase 2 pages.
- Routed Start Here, the dashboard, study index, resource policy, listening overview, and Phase 2 plan to the new audio support pages.
- Left Phase 1 as the active dashboard phase while making Phase 2 audio-ready.

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- Phase 2 coverage count check across required pages: 663 embedded MP3 clips.
- Local MP3 embed check across changed pages.
- `git diff --check`
