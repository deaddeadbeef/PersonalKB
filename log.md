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

## [2026-06-06] curate | Japanese Phase 2 weekly review

Scope: add the weekly evidence layer needed before Phase 2 becomes active, with explicit authentic-audio, local-clip, shadowing, and pronunciation-QA fields.

Changed content files:
- `Japanese/Study/Phase 2 Weekly Review.md`
- `Japanese/Japanese.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Learning Path/Phase 2 — Building Blocks.md`
- `Japanese/Listening/Phase 2 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 2 Audio Coverage Map.md`
- `Japanese/Listening/Phase 1 Audio Coverage Map.md`

Maintenance changes:
- Added a Phase 2 weekly review page that records exact authentic audio, local clips, shadowing, and pronunciation checks.
- Routed Start Here, dashboard, study index, Phase 2 plan, and Phase 2 audio pages to the new review.
- Updated the Phase 2 coverage backlog now that the weekly review page exists.

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- Changed-page MP3 embed check.
- `git diff --check`

## [2026-06-06] curate | Japanese pronunciation correction log

Scope: add a dedicated QA log for suspect and resolved local pronunciation clips so corrected audio can be tracked before it returns to daily practice.

Changed content files:
- `Japanese/Speaking/Pronunciation Correction Log.md`
- `Japanese/Speaking/Pronunciation and Audio Accuracy.md`
- `Japanese/Speaking/Speaking Overview.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Phase 2 Weekly Review.md`
- `Japanese/Listening/Phase 1 Audio Coverage Map.md`
- `Japanese/Listening/Phase 2 Audio Coverage Map.md`

Maintenance changes:
- Added an open/resolved correction log seeded with prior OCR and reading-hint repairs.
- Routed pronunciation QA, speaking/listening hubs, dashboard, study index, coverage maps, and Phase 2 weekly review to the log.
- Replaced "add a correction log" backlog language with instructions to use the log when a suspect clip is found.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Changed-page MP3 embed check.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 3 audio coverage

Scope: extend the Japanese audio-support system into Phase 3 so N4 grammar, pitch accent, intermediate listening, media, and keigo-recognition study remain paired with authentic audio and pronunciation QA.

Changed content files:
- `Japanese/Listening/Phase 3 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 3 Audio Coverage Map.md`
- `Japanese/Japanese.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Learning Path/Phase 3 — Expansion.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Study/Phase 2 Weekly Review.md`
- `Japanese/Listening/Phase 2 Audio Coverage Map.md`

Maintenance changes:
- Added a Phase 3 authentic audio spine for N4, pitch, intermediate listening, media, and keigo-recognition practice.
- Added a Phase 3 coverage map with local MP3 counts for required Phase 3 pages.
- Routed Start Here, dashboard, study index, resource policy, listening overview, Phase 3 plan, and Phase 2 exit pages to the new audio support pages.
- Left Phase 1 as the active dashboard phase while making Phase 3 audio-ready.

Verification:
- `python _ops/personal_kb.py audit`
- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- Phase 3 coverage count check across required pages: 494 embedded MP3 clips.
- Local MP3 embed check across changed pages.
- `git diff --check`

## [2026-06-06] fix | Japanese audio index embed overload

Scope: prevent the raw Japanese audio catalog from forcing Obsidian to render the entire MP3 library as inline audio controls.

Changed content files:
- `Japanese/_audio/Audio Index.md`

Maintenance changes:
- Converted the all-clips audio catalog from embedded MP3 players to ordinary clip links.
- Added an audit report for pages that exceed the safe inline MP3 embed threshold.

Verification:
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Full Japanese MP3 validation with `ffprobe`: 1810 checked, 0 bad.
- Audio embed resolution check across Japanese notes.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 4 audio support

Scope: extend the Japanese audio-support system into Phase 4 so N3 grammar, N3 kanji, keigo, business register, culture, and native-speed listening stay paired with local drills, authentic audio, and pronunciation/register QA.

Changed content files:
- `Japanese/Listening/Phase 4 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 4 Audio Coverage Map.md`
- `Japanese/Japanese.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Learning Path/Phase 4 — Intermediate Mastery.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Listening/Phase 3 Audio Coverage Map.md`

Maintenance changes:
- Added a Phase 4 authentic audio spine for native-speed, N3, keigo, business, register, culture, and conversation-fluency practice.
- Added a Phase 4 coverage map with local MP3 counts for required Phase 4 pages.
- Routed Start Here, dashboard, study index, resource policy, listening overview, Phase 4 plan, and Phase 3 next targets to the new audio support pages.
- Left Phase 1 as the active dashboard phase while making Phase 4 audio-ready.

Verification:
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Phase 4 coverage count check across required pages: 312 embedded MP3 clips.
- Local MP3 embed check across changed pages.
- `git diff --check`

## [2026-06-06] fix | Japanese browser-compatible audio clips

Scope: repair Japanese local audio playback in Obsidian after Chromium/Electron rejected the existing Azure 16 kHz / 32 kbps MP3 files as a media format error.

Changed content files:
- `Japanese/_audio/*.mp3`
- `Japanese/_audio/generate_tts.py`
- `_ops/personal_kb.py`
- `index.md`

Maintenance changes:
- Re-encoded all 1810 tracked Japanese MP3 clips to 48 kHz mono / approximately 96 kbps MP3 while preserving filenames and existing Obsidian embeds.
- Updated the TTS generator so future Azure clips use the same browser-compatible MP3 format.
- Updated generated-index cleaning so embedded audio cannot leak into index link aliases or summaries.

Verification:
- Full Japanese MP3 re-encode: 1810 converted, 0 failed.
- Full Japanese MP3 validation with `ffprobe`.
- Chromium audio load spot-check over localhost for repaired clips.
- MP3 embed/link resolution check across the vault.
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 5 audio support

Scope: extend the Japanese audio-support system into Phase 5 so native media, professional output, full keigo, idioms, pitch refinement, JLPT N2/N1 direction, and advanced nuance stay tied to native-source evidence, local drills, and pronunciation/register QA.

Changed content files:
- `Japanese/Listening/Phase 5 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 5 Audio Coverage Map.md`
- `Japanese/Japanese.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Learning Path/Phase 5 — Advanced.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Listening/Phase 4 Audio Coverage Map.md`

Maintenance changes:
- Added a Phase 5 authentic audio spine for native-source listening, output feedback, register, pitch, and advanced nuance.
- Added a Phase 5 coverage map with local MP3 counts for required Phase 5 pages.
- Routed Start Here, dashboard, study index, resource policy, listening overview, Phase 5 plan, and Phase 4 next targets to the new audio support pages.
- Left Phase 1 as the active dashboard phase while making Phase 5 audio-ready.

Verification:
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Phase 5 coverage count check across required pages: 152 embedded MP3 clips.
- Local MP3 embed check across changed pages.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 5 review and output proof

Scope: add Phase 5 review and output-feedback surfaces so advanced listening is backed by native-source evidence, recordings, tutor/native feedback, and register corrections.

Changed content files:
- `Japanese/Study/Phase 5 Weekly Review.md`
- `Japanese/Speaking/Advanced Output and Register Feedback Log.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 5 — Advanced.md`
- `Japanese/Listening/Phase 5 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 5 Audio Coverage Map.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Speaking/Pronunciation Correction Log.md`

Maintenance changes:
- Added a Phase 5 weekly review page that requires exact native-source segments, local clip targets, output proof, and pronunciation/register QA.
- Added an advanced output/register feedback log for recordings, tutor/native feedback, keigo direction, business phrasing, pitch, rhythm, and nuance fixes.
- Routed Phase 5 audio spine, coverage map, dashboard, study index, resources, and pronunciation correction guidance to the new proof pages.

Verification:
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Phase 5 proof-page coverage check.
- Local MP3 embed check across changed pages.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 3-4 weekly audio QA loop

Scope: fill the Phase 3 and Phase 4 review gap so intermediate Japanese study has weekly evidence for authentic audio, local drills, pitch/register checks, and active shadowing or output before Phase 5.

Changed content files:
- `Japanese/Study/Phase 3 Weekly Review.md`
- `Japanese/Study/Phase 4 Weekly Review.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 3 — Expansion.md`
- `Japanese/Learning Path/Phase 4 — Intermediate Mastery.md`
- `Japanese/Listening/Phase 3 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 3 Audio Coverage Map.md`
- `Japanese/Listening/Phase 4 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 4 Audio Coverage Map.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Study/Phase 2 Weekly Review.md`
- `Japanese/Speaking/Pronunciation and Audio Accuracy.md`
- `Japanese/Speaking/Pronunciation Correction Log.md`

Maintenance changes:
- Added Phase 3 and Phase 4 weekly review pages with exact audio-target, local-clip, pitch/register, and active-proof tables.
- Routed Start Here, dashboard, study index, resource policy, daily routine, phase pages, audio spines, and coverage maps to the new review pages.
- Updated pronunciation QA guidance so normal learner corrections route to the current phase review while suspect clip-quality issues stay in the correction log.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Phase 3-4 review link coverage check.
- Local MP3 embed check across changed pages.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 1 weekly audio proof

Scope: strengthen the active Phase 1 review loop so beginner study records exact native-source audio, local clip sets, pronunciation QA, and speaking proof before moving to Phase 2.

Changed content files:
- `Japanese/Study/Phase 1 Weekly Review.md`
- `Japanese/Learning Path/Phase 1 — Foundation.md`
- `Japanese/Listening/Phase 1 Audio Coverage Map.md`
- `Japanese/Study/Japanese Learning Dashboard.md`

Maintenance changes:
- Added a Phase 1 weekly audio evidence table for native or official audio, local clips, shadowing, pronunciation checks, and speaking proof.
- Added Phase 1 exit checks that keep suspect local clips out of daily practice until checked or logged.
- Routed the Phase 1 plan, coverage map, and dashboard checkpoint to the stronger weekly audio evidence requirement.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Phase 1 audio proof link coverage check.
- Local MP3 embed check across changed pages.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 3 pitch accent practice path

Scope: add a focused Phase 3 pitch-accent practice route so local pitch clips are used only as drills after OJAD, NHK, Forvo, course audio, tutor, or native-source checks.

Changed content files:
- `Japanese/Speaking/Pitch Accent/Phase 3 Pitch Accent Practice Path.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 3 — Expansion.md`
- `Japanese/Listening/Phase 3 Audio Coverage Map.md`
- `Japanese/Speaking/Pitch Accent/Pitch Accent — Introduction.md`
- `Japanese/Speaking/Pitch Accent/Pitch Accent — Common Patterns.md`
- `Japanese/Speaking/Pronunciation and Audio Accuracy.md`
- `Japanese/Speaking/Speaking Overview.md`
- `Japanese/Study/Phase 3 Weekly Review.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`

Maintenance changes:
- Added a Phase 3 pitch-accent practice path with source priority, daily loop, four-week path, card rule, and stop conditions.
- Routed Phase 3 Start Here, the Phase 3 coverage map, pitch pages, pronunciation QA, speaking hub, dashboard, study index, and Phase 3 weekly review to the new practice path.
- Replaced the Phase 3 coverage-map pitch backlog item with a concrete practice-page link.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Phase 3 pitch path link coverage check.
- Local MP3 embed check across changed pages.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 4 keigo register checklist

Scope: add a focused Phase 4 keigo/register production checklist so business and formal output is checked against human/native/course models before local clips are used as drills.

Changed content files:
- `Japanese/Speaking/Phase 4 Keigo and Register Production Checklist.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 4 — Intermediate Mastery.md`
- `Japanese/Listening/Phase 4 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 4 Audio Coverage Map.md`
- `Japanese/Speaking/Pronunciation and Audio Accuracy.md`
- `Japanese/Speaking/Speaking Overview.md`
- `Japanese/Study/Phase 4 Weekly Review.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`

Maintenance changes:
- Added a Phase 4 production checklist for role, social direction, form choice, human model, local drill, output, and feedback.
- Routed Phase 4 Start Here, the phase page, audio spine, coverage map, weekly review, dashboard, study index, speaking hub, and pronunciation QA to the checklist.
- Replaced the Phase 4 coverage-map register checklist backlog item with a concrete practice-page link.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Phase 4 register checklist link coverage check.
- Local MP3 embed check across changed pages.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 2 local audio practice

Scope: add a focused Phase 2 local audio ladder so N5 mechanics have a daily clip route instead of requiring page-level clip hunting.

Changed content files:
- `Japanese/Listening/Phase 2 Local Audio Practice.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 2 — Building Blocks.md`
- `Japanese/Listening/Phase 2 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 2 Audio Coverage Map.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Study/Phase 2 Weekly Review.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Study/Daily Study Routine Templates.md`

Maintenance changes:
- Added `Phase 2 Local Audio Practice` with an eight-week local drill ladder for particles, verb/adjective forms, time and counters, daily-life vocabulary, kanji-as-spoken-words, and beginner interactions.
- Kept the authentic source as the pronunciation model through `Phase 2 Authentic Audio Spine`; local clips are controlled drills, not the authority.
- Routed Start Here, Phase 2, the audio map, listening overview, dashboard, study index, resources, daily routines, and weekly review to the new ladder.
- Replaced the Phase 2 coverage-map backlog item about a future ladder with the concrete practice page.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- Phase 2 local audio link coverage check: 0 missing required links; old Phase 2 ladder backlog phrase removed.
- Local MP3 embed check across changed pages: 90 embedded MP3 targets, 0 missing.
- `index.md` MP3 leak check: 0 hits.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 3 local audio practice

Scope: add a focused Phase 3 local audio ladder so N4 expansion, longer sentence output, practical domains, and pitch/register recognition have a daily clip route paired with authentic audio.

Changed content files:
- `Japanese/Listening/Phase 3 Local Audio Practice.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 3 — Expansion.md`
- `Japanese/Listening/Phase 3 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 3 Audio Coverage Map.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Study/Phase 3 Weekly Review.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Grammar/N4 Grammar/N4 Grammar — Potential and Volitional.md`

Maintenance changes:
- Added `Phase 3 Local Audio Practice` with 104 selected local MP3 drills across N4 grammar direction, longer sentences and 1000-word output, practical domains and N4 kanji, plus pitch, fillers, media, and register recognition.
- Kept `Phase 3 Authentic Audio Spine` as the pronunciation/rhythm authority; local clips are controlled drills, and pitch prompts route to the Phase 3 pitch-accent practice path and native/course/tutor checks.
- Routed Start Here, Phase 3, the audio spine, coverage map, listening overview, dashboard, study index, resources, daily routines, and weekly review to the new ladder.
- Corrected a malformed chopsticks-kanji source typo to `お箸が使えますか。`, regenerated `n4pot-006-otsukaemasuka.mp3`, and updated pronunciation manifests and audit reports.

Changed audio/ops files:
- `Japanese/_audio/build_pronunciation_manifest.py`
- `Japanese/_audio/gramn4n3_manifest.json`
- `Japanese/_audio/pronunciation_manifest.json`
- `Japanese/_audio/n4pot-006-otsukaemasuka.mp3`
- `Japanese/_audio/audit-mismatch-report.txt`
- `_ops/reports/audit-summary.json`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.

## [2026-06-07] curate | Japanese pronunciation QA status note

Scope: make the current local-audio QA evidence visible from the learner-facing pronunciation guidance.

Changed content files:
- `Japanese/Speaking/Pronunciation and Audio Accuracy.md`

Maintenance changes:
- Added the current local audio QA status: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 local MP3 files, 1810 pronunciation-manifest entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 1810 ffprobe-checked MP3 files, and 0 format issues.
- Added the current pronunciation audit status: 26 expected reading overrides, 0 source repair overrides, and 0 invalid TTS inputs.
- Added `python Japanese\_audio\audit_audio_integrity.py --no-report` to the correction workflow for missing clips, Obsidian playback errors, and MP3 format issues.
- Kept the learner-facing rule that native/official audio, tutor/native feedback, and accent references remain authoritative for pitch, rhythm, register, and natural delivery.

Verification:
- `python Japanese\_audio\audit_audio_integrity.py --no-report`: 0 missing embedded MP3 files, 0 manifest/file mismatches, 1810 ffprobe-checked MP3 files, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `git diff --check`

## [2026-06-07] curate | Japanese audio QA status hub

Scope: make local audio integrity evidence easy to find from the Japanese Start Here and study navigation.

Changed content files:
- `Japanese/Study/Japanese Audio QA Status.md`
- `Japanese/Japanese.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Speaking/Pronunciation and Audio Accuracy.md`

Maintenance changes:
- Added `Japanese Audio QA Status` with the current local-audio QA evidence, what the checks prove, what still needs native/official audio authority, and the three audit commands.
- Added the QA status page to the Orientation and Setup section of [[Japanese]], the dashboard reading order, the study index audio QA path, and the pronunciation QA references.
- Preserved the rule that local TTS is a drill layer and native/official/tutor/accent-reference audio remains authoritative for pitch, rhythm, register, and natural delivery.

Verification:
- `python Japanese\_audio\audit_audio_integrity.py --no-report`: 2210 Markdown MP3 embeds, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 1810 ffprobe-checked MP3 files, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4751 files, 2880 markdown, 1810 MP3, 0 heavy audio embed pages.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4751 files, 2880 markdown, 1810 MP3, 0 heavy audio embed pages.
- Japanese Audio QA Status link coverage check: 4 hub files plus status-page references present.
- `index.md` MP3 leak check: 0 hits.
- `git diff --check`
- Malformed chopsticks-kanji typo search: 0 hits.
- `ffprobe` check for regenerated `n4pot-006-otsukaemasuka.mp3`: MP3, 48000 Hz, mono, 96000 bps.
- `python _ops\personal_kb.py audit`: 4746 files, 2877 markdown, 1810 MP3, 0 heavy audio embed pages.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4746 files, 2877 markdown, 1810 MP3, 0 heavy audio embed pages.
- Phase 3 local audio link coverage check: 12 required references present.
- Phase 3 stale ladder backlog phrase check: removed old future-ladder wording.
- Local MP3 embed check across changed pages: 133 embedded MP3 targets, 0 missing.
- `index.md` MP3 leak check: 0 hits.
- `git diff --check`

## [2026-06-06] curate | Japanese audio source OCR normalization

Scope: normalize previously repaired OCR source rows so future audio regeneration reads correct Japanese directly from source manifests instead of relying on special-case overrides.

Changed audio/ops files:
- `Japanese/_audio/gap_manifest.json`
- `Japanese/_audio/build_pronunciation_manifest.py`
- `Japanese/_audio/pronunciation_manifest.json`
- `_ops/reports/audit-summary.json`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`

Maintenance changes:
- Corrected `gap_manifest.json` source text for `gap-194-phrase.mp3`, `gap-208-phrase.mp3`, `gap-212-phrase.mp3`, `gap-213-phrase.mp3`, `gap-214-phrase.mp3`, `gap-229-phrase.mp3`, and `gap-257-phrase.mp3`.
- Removed redundant OCR overrides for source rows that now already carry correct Japanese, including the earlier chopsticks, adjective, and swimming-form repairs.
- Rebuilt `pronunciation_manifest.json`; the affected rows now show the intended Japanese as both source text and display text.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- Stale OCR source text search: 0 hits for the corrected malformed strings.
- Affected pronunciation manifest row check: 11 rows match expected source/display text.
- `python _ops\personal_kb.py audit`: 4746 files, 2877 markdown, 1810 MP3, 0 heavy audio embed pages.
- `git diff --check`

## [2026-06-06] curate | Japanese giving contrast audio source normalization

Scope: normalize two N4 giving/receiving contrast rows so the source manifest reads the intended contrast directly instead of relying on harvested-text overrides.

Changed audio/ops files:
- `Japanese/_audio/gramn4n3_manifest.json`
- `Japanese/_audio/build_pronunciation_manifest.py`
- `Japanese/_audio/pronunciation_manifest.json`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`

Maintenance changes:
- Corrected `n4give-018-ageru-kureru.mp3` source text to `あげる、くれる`.
- Corrected `n4give-019-ageru-sashiageru.mp3` source text to `あげる、さしあげる`.
- Removed the two now-redundant harvested-contrast overrides.
- Rebuilt `pronunciation_manifest.json`; both affected rows now show the intended Japanese as unchanged source/display text.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- Stale harvested-contrast source text search: 0 hits.
- Affected pronunciation manifest row check: 2 rows match expected source/display text.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 4 local audio practice

Scope: add a focused Phase 4 local audio ladder so N3 grammar, N3 kanji, adult vocabulary, keigo, business register, cultural expressions, and discourse timing have a daily clip route paired with native-speed authentic audio.

Changed content files:
- `Japanese/Listening/Phase 4 Local Audio Practice.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 4 — Intermediate Mastery.md`
- `Japanese/Listening/Phase 4 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 4 Audio Coverage Map.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Speaking/Phase 4 Keigo and Register Production Checklist.md`
- `Japanese/Study/Phase 4 Weekly Review.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Study/Daily Study Routine Templates.md`

Maintenance changes:
- Added `Phase 4 Local Audio Practice` with 115 selected local MP3 drills across N3 grammar, N3 kanji, work/weather vocabulary, keigo, business phrases, seasonal/cultural expressions, idioms, number culture, source labels, and discourse markers.
- Kept `Phase 4 Authentic Audio Spine` as the pronunciation, rhythm, and register authority; local clips are controlled drills, and register-sensitive prompts route to `Phase 4 Keigo and Register Production Checklist`.
- Routed Start Here, Phase 4, the audio spine, coverage map, listening overview, dashboard, study index, resources, daily routines, weekly review, and keigo/register checklist to the new ladder.
- Checked visible labels on the new ladder against `pronunciation_manifest.json` so local practice text matches the canonical audio text.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4747 files, 2878 markdown, 1810 MP3, 0 heavy audio embed pages.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4747 files, 2878 markdown, 1810 MP3, 0 heavy audio embed pages.
- Phase 4 local audio link coverage check: 13 required references present.
- Phase 4 stale ladder backlog phrase check: removed old future-ladder wording.
- Local MP3 embed check across changed pages: 118 embedded MP3 targets, 0 missing.
- Phase 4 local label/audio text check: 0 mismatches against `pronunciation_manifest.json`.
- `index.md` MP3 leak check: 0 hits.
- `git diff --check`

## [2026-06-06] curate | Japanese Phase 5 local audio practice

Scope: add a focused Phase 5 local audio ladder so advanced media labels, full keigo, professional register, idioms, fillers, pitch prompts, and benchmark tasks have a repeatable precision-drill route paired with native-source audio.

Changed content files:
- `Japanese/Listening/Phase 5 Local Audio Practice.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 5 — Advanced.md`
- `Japanese/Listening/Phase 5 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 5 Audio Coverage Map.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Speaking/Advanced Output and Register Feedback Log.md`
- `Japanese/Study/Phase 5 Weekly Review.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Listening/Anime and Drama — Immersion Listening.md`

Changed audio/ops files:
- `Japanese/_audio/speaking_full_manifest.json`
- `Japanese/_audio/build_pronunciation_manifest.py`
- `Japanese/_audio/pronunciation_manifest.json`
- `Japanese/_audio/listen-010-koe-no-katachi.mp3`
- `Japanese/_audio/Audio Index.md`
- `Japanese/_audio/audit-mismatch-report.txt`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`
- `_ops/reports/audit-summary.json`

Maintenance changes:
- Added `Phase 5 Local Audio Practice` with 100 selected local MP3 drills from the Phase 5 library.
- Kept `Phase 5 Authentic Audio Spine` as the pronunciation, rhythm, register, and comprehension authority; Phase 5 local clips are precision prompts only.
- Routed Start Here, Phase 5, the audio spine, coverage map, listening overview, dashboard, study index, resources, daily routines, weekly review, and output feedback log to the new ladder.
- Checked visible labels on the new ladder against `pronunciation_manifest.json` so local practice text matches the canonical audio text.
- Corrected the A Silent Voice anime/drama source row to learner-facing `聲の形`, renamed the obsolete `listen-010` title clip to `listen-010-koe-no-katachi.mp3`, and regenerated that clip with TTS text `こえの形`.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4748 files, 2879 markdown, 1810 MP3, 0 heavy audio embed pages.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4748 files, 2879 markdown, 1810 MP3, 0 heavy audio embed pages.
- Phase 5 local audio link coverage check: 11 hub files plus local page backlinks present.
- Phase 5 stale ladder and old-title check: 0 hits for old ladder wording or obsolete `listen-010` title text.
- Local MP3 embed check across changed and new Markdown pages: 103 embedded MP3 targets, 0 missing.
- Phase 5 local label/audio text check: 100 labels, 0 mismatches against `pronunciation_manifest.json`.
- Corrected title row check: `listen-010-koe-no-katachi.mp3` has display text `聲の形` and TTS text `こえの形`.
- `ffprobe` on `listen-010-koe-no-katachi.mp3`: MP3, 48 kHz, mono, 96 kbps.
- `index.md` MP3 leak check: 0 hits.
- `git diff --check`

## [2026-06-07] ops | Japanese audio mismatch audit worktree safety

Scope: make the audio-text mismatch audit safe to run from isolated worktrees without writing into the active Obsidian vault.

Changed ops files:
- `Japanese/_audio/audit_mismatches.py`

Maintenance changes:
- Replaced the hardcoded `D:\Vaults\PersonalKB\Japanese` audit root with a default derived from the script's own `_audio` directory.
- Added `--root`, `--report`, and `--no-report` options so future audio checks can run against a chosen vault or in read-only summary mode.
- Reconfigured stdout/stderr for UTF-8 so Japanese filenames and page paths do not crash the summary print on Windows PowerShell.

Verification:
- `python Japanese\_audio\audit_mismatches.py --no-report`: scanned the worktree Japanese root, found 105 markdown files and 2210 audio embeds, exited 0, printed Japanese paths safely, and wrote no report file.
- Worktree report status check: `Japanese/_audio/audit-mismatch-report.txt` unchanged.
- Active vault report status check: `Japanese/_audio/audit-mismatch-report.txt` unchanged.

## [2026-06-07] curate | Japanese gap manifest romaji/gloss normalization

Scope: normalize high-confidence `gap_manifest.json` source rows whose audio text was already correct but whose source text still included romaji hints or English glosses.

Changed audio/ops files:
- `Japanese/_audio/gap_manifest.json`
- `Japanese/_audio/pronunciation_manifest.json`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`

Maintenance changes:
- Removed romaji hints from 22 source rows covering counter/time words, basic location/activity words, transitive verbs, and time adverbs.
- Removed English glosses from transitive verb source rows such as close, put in, put out, turn off, raise, lower, break, and make dirty.
- Reduced pronunciation-audit changed TTS inputs from 87 to 65; the remaining 65 are now exactly the explicit override set.
- Did not regenerate MP3 files because the normalized rows already matched the TTS text used for existing audio.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- Affected-row manifest check: 22 rows now have matching source, display, and TTS text with `unchanged` pronunciation notes.
- Removed-row audit search: the 22 normalized filenames no longer appear in changed TTS inputs.
- Changed MP3 file check: 0 MP3 files changed.
- `git diff --check`

## [2026-06-07] curate | Japanese practice source-row normalization

Scope: normalize source rows whose pronunciation overrides had already replaced English rules, placeholders, slash-separated items, and generic practice prompts with the actual Japanese text used by the audio.

Changed audio/ops files:
- `Japanese/_audio/gap_manifest.json`
- `Japanese/_audio/nontbl_manifest.json`
- `Japanese/_audio/gramn5_full_manifest.json`
- `Japanese/_audio/speaking_full_manifest.json`
- `Japanese/_audio/build_pronunciation_manifest.py`
- `Japanese/_audio/pronunciation_manifest.json`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`

Maintenance changes:
- Normalized 39 source rows to the real Japanese phrase or sentence already used for TTS.
- Removed the now-redundant overrides for table-rule examples, self-introduction placeholders, placeholder sentence patterns, and the English adjective practice prompt.
- Reduced pronunciation-audit changed TTS inputs from 65 to 26; the remaining 26 are true reading-disambiguation cases for particles, counter suffixes, `開ける`, and `聲の形`.
- Did not regenerate MP3 files because the normalized rows already matched the TTS text used for existing audio.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python -m py_compile Japanese\_audio\build_pronunciation_manifest.py`
- Affected-row manifest check: 39 rows now have matching source, display, and TTS text with `unchanged` pronunciation notes.
- Removed-row audit search: the 39 normalized filenames no longer appear in changed TTS inputs.
- Changed MP3 file check: 0 MP3 files changed.
- `git diff --check`

## [2026-06-07] ops | Japanese expected reading override classification

Scope: make the pronunciation audit report distinguish expected reading overrides from source-repair overrides.

Changed audio/ops files:
- `Japanese/_audio/build_pronunciation_manifest.py`
- `_ops/reports/japanese-audio-pronunciation-audit.txt`

Maintenance changes:
- Added expected-reading classification for particle readings, counter suffix readings, `開ける`, and the `聲の形` title reading.
- Added summary counts for expected reading overrides and source repair overrides.
- Regenerated the pronunciation audit report; current state is 26 expected reading overrides and 0 source repair overrides.
- Did not change `pronunciation_manifest.json` or any MP3 files.

Verification:
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python -m py_compile Japanese\_audio\build_pronunciation_manifest.py`
- Pronunciation audit summary check: 26 expected reading overrides and 0 source repair overrides.
- `git diff --check`

## [2026-06-07] ops | Japanese audio integrity audit

Scope: add a repeatable audit for Obsidian audio embed resolution, manifest/file inventory, and MP3 media-format compatibility.

Changed audio/ops files:
- `Japanese/_audio/audit_audio_integrity.py`
- `_ops/reports/japanese-audio-integrity-audit.txt`

Maintenance changes:
- Added a worktree-safe audio integrity audit with `--root`, `--audio-dir`, `--manifest`, `--report`, `--no-report`, and `--skip-ffprobe` options.
- Checks every Japanese Markdown MP3 embed against `Japanese/_audio`.
- Checks `pronunciation_manifest.json` against actual MP3 files.
- Uses `ffprobe` to verify every local MP3 is browser-compatible: MP3 codec, 48 kHz sample rate, mono, 96 kbps.
- Writes a vault-relative report so the evidence is not tied to a specific worktree path.

Verification:
- `python Japanese\_audio\audit_audio_integrity.py`: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest rows missing MP3, 0 MP3 files not in manifest, 0 embedded files not in manifest, 1810 ffprobe-checked MP3 files, 0 ffprobe failures, 0 format issues.
- `python -m py_compile Japanese\_audio\audit_audio_integrity.py`
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.

## [2026-06-07] curate | Japanese authentic audio source setup

Scope: make the official/native audio source setup concrete for the Japanese learning path without changing local MP3 files.

Changed wiki/source files:
- `Japanese/Study/Authentic Audio Source Setup.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`
- `Japanese/Study/Japanese Audio QA Status.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Speaking/Pronunciation and Audio Accuracy.md`
- `Japanese/Japanese.md`
- `Japanese/Sources/Sources Index.md`

Maintenance changes:
- Added a setup note that turns authentic audio into a repeatable weekly choice: one primary official/native source, one exact replayable segment, one pronunciation-reference route, and one weekly proof entry.
- Linked the setup note from Start Here, the study dashboard/index, the resource index, audio QA, and pronunciation guidance.
- Refreshed the Japanese source index with currently checked official routes for GENKI/OTO Navi, Irodori, NHK Easy Japanese, and OJAD.
- Did not modify local MP3 files or pronunciation manifests.

Verification:
- External link checks: GENKI, Irodori, NHK Easy Japanese, and OJAD returned HTTP 200.
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4752 files, 2881 Markdown files, 1810 MP3 files, 0 heavy audio embed pages.
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`: same counts after indexing.
- `git diff --check`

## [2026-06-07] curate | Japanese authentic audio evidence loop

Scope: make authentic audio proof persist across weekly reviews without changing local MP3 files.

Changed wiki/source files:
- `Japanese/Study/Authentic Audio Evidence Log.md`
- `Japanese/Study/Authentic Audio Source Setup.md`
- `Japanese/Study/Japanese Audio QA Status.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Phase 1 Weekly Review.md`
- `Japanese/Study/Phase 2 Weekly Review.md`
- `Japanese/Study/Phase 3 Weekly Review.md`
- `Japanese/Study/Phase 4 Weekly Review.md`
- `Japanese/Study/Phase 5 Weekly Review.md`
- `Japanese/Speaking/Pronunciation Correction Log.md`
- `Japanese/Japanese.md`

Maintenance changes:
- Added a central audio evidence log for one weekly proof row per review cycle.
- Linked the log from the authentic audio setup page, dashboard, study index, Start Here, audio QA status, pronunciation correction log, and all phase weekly review templates.
- Clarified the split between learner evidence, output feedback, and suspect local-clip correction.
- Did not modify local MP3 files or pronunciation manifests.

Verification:
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4753 files, 2882 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`: same counts after indexing.
- Link coverage check for `Authentic Audio Evidence Log`: linked from Start Here, dashboard, study index, source setup, audio QA, pronunciation correction log, all five phase weekly reviews, and `index.md`.
- `index.md` MP3 leak check: 0 results.
- `git diff --check`

## [2026-06-07] curate | Japanese daily audio loop

Scope: make the daily study routine execute the authentic-audio system instead of only pointing at broad phase pages.

Changed wiki/source files:
- `Japanese/Study/Daily Audio Loop.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Authentic Audio Evidence Log.md`
- `Japanese/Japanese.md`

Maintenance changes:
- Added a daily audio loop note with local drill, authentic model, one-feature comparison, evidence logging, and suspect-clip routing.
- Updated the 30-minute, 60-minute, intensive, and minimum viable routines to use the loop.
- Linked the loop from Start Here, the dashboard reading order, the study index, and the evidence log.
- Did not modify local MP3 files or pronunciation manifests.

Verification:
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4754 files, 2883 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`: same counts after indexing.
- Link coverage check for `Daily Audio Loop`: linked from Start Here, dashboard, daily routine, study index, evidence log, and `index.md`.
- `index.md` MP3 leak check: 0 results.
- `git diff --check`

## [2026-06-07] curate | Japanese Phase 1 audio starter assignment

Scope: make the first week of Japanese audio practice concrete without changing local MP3 files.

Changed wiki/source files:
- `Japanese/Study/Phase 1 Audio Starter Assignment.md`
- `Japanese/Study/Daily Audio Loop.md`
- `Japanese/Study/Authentic Audio Evidence Log.md`
- `Japanese/Listening/Phase 1 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 1 Audio Coverage Map.md`
- `Japanese/Study/Phase 1 Weekly Review.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Japanese.md`

Maintenance changes:
- Added a first-week assignment page that chooses one Genki, Irodori, or NHK source path and pairs it with Phase 1 local Week 1 drills.
- Added a copy-ready current-assignment table for [[Authentic Audio Evidence Log]].
- Added a seven-day starter loop and success criteria for Week 1 proof.
- Linked the starter assignment from the dashboard, Start Here, daily audio loop, evidence log, Phase 1 spine, coverage map, and weekly review.
- Did not modify local MP3 files or pronunciation manifests.

Verification:
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4755 files, 2884 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`: same counts after indexing.
- Link coverage check for `Phase 1 Audio Starter Assignment`: linked from Start Here, dashboard, study index, daily audio loop, evidence log, Phase 1 authentic spine, Phase 1 coverage map, Phase 1 weekly review, and `index.md`.
- `index.md` MP3 leak check: 0 results.
- `git diff --check`

## [2026-06-07] curate | Japanese Phase 1 audio assignment ladder

Scope: extend the first-week starter assignment into a complete four-week Phase 1 audio assignment path without changing local MP3 files.

Changed wiki/source files:
- `Japanese/Study/Phase 1 Audio Assignment Ladder.md`
- `Japanese/Study/Phase 1 Audio Starter Assignment.md`
- `Japanese/Study/Daily Audio Loop.md`
- `Japanese/Study/Authentic Audio Evidence Log.md`
- `Japanese/Listening/Phase 1 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 1 Audio Coverage Map.md`
- `Japanese/Study/Phase 1 Weekly Review.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Japanese.md`

Maintenance changes:
- Added a four-week Phase 1 assignment ladder with local clip set, authentic model, comparison target, and output proof for each week.
- Added copy-ready current-assignment templates for Weeks 1-4.
- Linked the ladder from Start Here, dashboard, study index, daily audio loop, starter assignment, evidence log, Phase 1 authentic spine, Phase 1 coverage map, and weekly review.
- Did not modify local MP3 files or pronunciation manifests.

Verification:
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4756 files, 2885 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`: same counts after indexing.
- Link coverage check for `Phase 1 Audio Assignment Ladder`: linked from Start Here, dashboard, study index, daily audio loop, starter assignment, evidence log, Phase 1 authentic spine, Phase 1 coverage map, Phase 1 weekly review, and `index.md`.
- `index.md` MP3 leak check: 0 results.
- `git diff --check`

## [2026-06-07] curate | Japanese Phase 2 audio assignment ladder

Scope: extend the authenticated audio workflow from Phase 1 into the full eight-week Phase 2 N5 building-block path without changing local MP3 files.

Changed wiki/source files:
- `Japanese/Study/Phase 2 Audio Assignment Ladder.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 2 — Building Blocks.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Listening/Phase 2 Audio Coverage Map.md`
- `Japanese/Listening/Phase 2 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 2 Local Audio Practice.md`
- `Japanese/Study/Authentic Audio Evidence Log.md`
- `Japanese/Study/Daily Audio Loop.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Phase 2 Weekly Review.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`

Maintenance changes:
- Added an eight-week Phase 2 assignment ladder for Weeks 5-12 with main pages, local drills, authentic model, comparison target, and output proof.
- Added copy-ready current-assignment templates for Weeks 5-12.
- Linked the ladder from Start Here, dashboard, study index, daily loop, evidence log, Phase 2 path, listening overview, local practice, authentic spine, coverage map, weekly review, and resource routing.
- Regenerated `index.md` and `_ops/reports/audit-summary.json`.
- Did not modify local MP3 files or pronunciation manifests.

Verification:
- `git diff --check`: clean.
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4757 files, 2886 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`: same counts after indexing.
- Link coverage check for `Phase 2 Audio Assignment Ladder`: linked from Start Here, Phase 2 path, listening overview, dashboard, study index, daily audio loop, evidence log, Phase 2 local practice, authentic spine, coverage map, weekly review, resources index, and `index.md`.
- `index.md` MP3 leak check: 0 results.

## [2026-06-07] curate | Japanese Phase 3 audio assignment ladder

Scope: extend the authenticated audio workflow into Phase 3 N4, pitch-accent, media, and register-recognition practice without changing local MP3 files.

Changed wiki/source files:
- `Japanese/Study/Phase 3 Audio Assignment Ladder.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 3 — Expansion.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Listening/Phase 3 Audio Coverage Map.md`
- `Japanese/Listening/Phase 3 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 3 Local Audio Practice.md`
- `Japanese/Speaking/Pitch Accent/Phase 3 Pitch Accent Practice Path.md`
- `Japanese/Study/Authentic Audio Evidence Log.md`
- `Japanese/Study/Authentic Audio Source Setup.md`
- `Japanese/Study/Daily Audio Loop.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Phase 2 Weekly Review.md`
- `Japanese/Study/Phase 3 Weekly Review.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`

Maintenance changes:
- Added a four-block Phase 3 assignment ladder for N4 grammar direction, longer sentences and Core 1000 output, practical domains and N4 kanji, and pitch/media/register recognition.
- Added copy-ready current-assignment templates for Blocks 1-4.
- Added a Block 4 safety rule so pitch, media rhythm, and register checks use source-backed references instead of trusting local TTS.
- Linked the ladder from Start Here, Phase 3 path, listening overview, dashboard, study index, daily audio loop, evidence log, authentic source setup, Phase 2 handoff, Phase 3 local practice, authentic spine, coverage map, pitch path, weekly review, and resources index.
- Regenerated `index.md` and `_ops/reports/audit-summary.json`.
- Did not modify local MP3 files or pronunciation manifests.

Verification:
- `git diff --check`: clean.
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4758 files, 2887 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`: same counts after indexing.
- Link coverage check for `Phase 3 Audio Assignment Ladder`: linked from Start Here, Phase 3 path, listening overview, dashboard, study index, daily audio loop, evidence log, authentic source setup, Phase 2 handoff, Phase 3 local practice, authentic spine, coverage map, pitch path, weekly review, resources index, and `index.md`.
- `index.md` MP3 leak check: 0 results.

## [2026-06-07] curate | Japanese Phase 4 audio assignment ladder

Scope: extend the authenticated audio workflow into Phase 4 N3, native-speed listening, keigo, business register, cultural expressions, and longer output without changing local MP3 files.

Changed wiki/source files:
- `Japanese/Study/Phase 4 Audio Assignment Ladder.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 4 — Intermediate Mastery.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Listening/Phase 3 Audio Coverage Map.md`
- `Japanese/Listening/Phase 4 Audio Coverage Map.md`
- `Japanese/Listening/Phase 4 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 4 Local Audio Practice.md`
- `Japanese/Speaking/Phase 4 Keigo and Register Production Checklist.md`
- `Japanese/Speaking/Speaking Overview.md`
- `Japanese/Study/Authentic Audio Evidence Log.md`
- `Japanese/Study/Authentic Audio Source Setup.md`
- `Japanese/Study/Daily Audio Loop.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Phase 3 Weekly Review.md`
- `Japanese/Study/Phase 4 Weekly Review.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`

Maintenance changes:
- Added a four-block Phase 4 assignment ladder for N3 grammar in longer sentences, N3 kanji and adult-life vocabulary, keigo/business/cultural register, and native-speed support.
- Added copy-ready current-assignment templates for Blocks 1-4.
- Added a register safety rule so keigo, business phrases, idioms, seasonal expressions, pitch, and readings use source-backed references before production.
- Linked the ladder from Start Here, Phase 4 path, listening overview, speaking overview, dashboard, study index, daily audio loop, evidence log, authentic source setup, Phase 3 handoff, Phase 4 local practice, authentic spine, coverage map, keigo/register checklist, weekly review, and resources index.
- Regenerated `index.md` and `_ops/reports/audit-summary.json`.
- Did not modify local MP3 files or pronunciation manifests.

Verification:
- `git diff --check`: clean.
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4759 files, 2888 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`: same counts after indexing.
- Link coverage check for `Phase 4 Audio Assignment Ladder`: linked from Start Here, Phase 4 path, listening overview, speaking overview, dashboard, study index, daily audio loop, evidence log, authentic source setup, Phase 3 handoff, Phase 4 local practice, authentic spine, coverage map, keigo/register checklist, weekly review, resources index, and `index.md`.
- `index.md` MP3 leak check: 0 results.

## [2026-06-07] curate | Japanese Phase 5 audio assignment ladder

Scope: extend the authenticated audio workflow into Phase 5 native-source listening, professional output, pitch, nuance, and N2/N1 refinement without changing local MP3 files.

Changed wiki/source files:
- `Japanese/Study/Phase 5 Audio Assignment Ladder.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 5 — Advanced.md`
- `Japanese/Listening/Listening Overview.md`
- `Japanese/Listening/Phase 4 Audio Coverage Map.md`
- `Japanese/Listening/Phase 5 Audio Coverage Map.md`
- `Japanese/Listening/Phase 5 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 5 Local Audio Practice.md`
- `Japanese/Speaking/Advanced Output and Register Feedback Log.md`
- `Japanese/Speaking/Speaking Overview.md`
- `Japanese/Study/Authentic Audio Evidence Log.md`
- `Japanese/Study/Authentic Audio Source Setup.md`
- `Japanese/Study/Daily Audio Loop.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Japanese Audio QA Status.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Phase 4 Weekly Review.md`
- `Japanese/Study/Phase 5 Weekly Review.md`
- `Japanese/Study/Resources Index — Textbooks, Apps, and Tools.md`

Maintenance changes:
- Added a four-block Phase 5 assignment ladder for native media, full keigo and professional register, nuance/pitch/conversation stance, and N2/N1 benchmark refinement.
- Added copy-ready current-assignment templates for Blocks 1-4.
- Added a native-source safety rule so humor, implication, pitch, keigo, business phrasing, and JLPT-to-real-listening transfer use source-backed references before production.
- Linked the ladder from Start Here, Phase 5 path, listening overview, speaking overview, dashboard, study index, daily audio loop, evidence log, authentic source setup, Phase 4 handoff, Phase 5 local practice, authentic spine, coverage map, output feedback log, weekly review, resources index, and audio QA status.
- Regenerated `index.md` and `_ops/reports/audit-summary.json`.
- Did not modify local MP3 files or pronunciation manifests.

Verification:
- `git diff --check`: clean.
- `python Japanese\_audio\audit_audio_integrity.py --no-report`: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 ffprobe failures, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4760 files, 2889 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`
- Link coverage check for `Phase 5 Audio Assignment Ladder`: linked from Start Here, Phase 5 path, listening overview, speaking overview, dashboard, study index, daily audio loop, evidence log, authentic source setup, Phase 4 handoff, Phase 5 local practice, authentic spine, coverage map, output feedback log, weekly review, resources index, audio QA status, and `index.md`.
- `index.md` MP3 leak check: 0 results.

## [2026-06-07] ops | Japanese source-aware STT audio triage

Scope: replace stale filename-derived STT expectations with a source-aware audit path that uses `pronunciation_manifest.json` while keeping native/course/tutor/reference audio as the pronunciation authority.

Changed wiki/source files:
- `Japanese/_audio/stt_spot_check.py`
- `Japanese/_audio/stt_run.py`
- `Japanese/_audio/stt_full_audit.py`
- `Japanese/_audio/stt_wav_check.py`
- `Japanese/_audio/stt-spot-check-report.txt`
- `Japanese/Study/Japanese Audio QA Status.md`
- `Japanese/Speaking/Pronunciation and Audio Accuracy.md`
- `Japanese/Speaking/Pronunciation Correction Log.md`

Maintenance changes:
- Replaced the legacy `stt_spot_check.py` expectation model so selected clips are compared against `pronunciation_manifest.json` `text` and `display_text`, not filename fragments.
- Preserved old STT entrypoints as wrappers around the source-aware script.
- Regenerated `Japanese/_audio/stt-spot-check-report.txt` as a dry-run source plan: 61 selected clips, 1810 manifest entries, 0 validation problems, live STT not run because `AZURE_SPEECH_KEY` is unavailable in this environment.
- Updated QA notes to state that STT is optional triage only and does not replace native, official-course, tutor, OJAD/NHK/Forvo, or other source-backed pronunciation checks.
- Did not modify local MP3 files.

Verification:
- `python -m py_compile Japanese\_audio\stt_spot_check.py Japanese\_audio\stt_run.py Japanese\_audio\stt_full_audit.py Japanese\_audio\stt_wav_check.py`
- `python Japanese\_audio\stt_spot_check.py`: wrote source-aware dry-run report with 61 selected clips and 0 validation problems.
- `python Japanese\_audio\stt_spot_check.py --live --report <temp>`: returned the expected missing-key path and wrote a source-aware report without live STT.
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4760 files, 2889 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-07] curate | Japanese first-week audio study plan

Scope: make the active Phase 1 starting path immediately executable for a learner by turning setup, kana, local clips, authentic audio, and proof into a seven-day plan.

Changed wiki/source files:
- `Japanese/Study/First Week Japanese Study Plan.md`
- `Japanese/Japanese.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Phase 1 Audio Starter Assignment.md`
- `Japanese/Study/Phase 1 Weekly Review.md`

Maintenance changes:
- Added a day-by-day first-week plan that starts from [[Phase 1 Audio Starter Assignment]], uses [[Daily Audio Loop]], keeps one named authentic segment beside Week 1 local clips, and finishes with [[Phase 1 Weekly Review]] plus [[Authentic Audio Evidence Log]].
- Linked the plan from Start Here, the dashboard reading order, study index, daily routine template, starter assignment, and weekly review.
- Regenerated `index.md` and `_ops/reports/audit-summary.json`.
- Did not modify local MP3 files or pronunciation manifests.

Verification:
- `git diff --check`: clean.
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4761 files, 2890 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.
- Link coverage check for `First Week Japanese Study Plan`: linked from Start Here, dashboard, study index, daily routine template, Phase 1 starter assignment, Phase 1 weekly review, and `index.md`.
- `index.md` MP3 leak check: 0 results.

## [2026-06-07] curate | Japanese first-month audio study plan

Scope: make Phase 1 month one executable after the first week by giving Weeks 2-4 a simple study path tied to authentic audio, local drills, weekly review, and evidence logging.

Changed wiki/source files:
- `Japanese/Study/First Month Japanese Study Plan.md`
- `Japanese/Japanese.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/First Week Japanese Study Plan.md`
- `Japanese/Study/Phase 1 Audio Starter Assignment.md`
- `Japanese/Study/Phase 1 Audio Assignment Ladder.md`
- `Japanese/Study/Phase 1 Weekly Review.md`

Maintenance changes:
- Added a month-one execution guide that keeps Week 1 on the first-week plan, then gives Weeks 2-4 daily shapes for katakana, survival phrases, sentence patterns, greetings, and the first self-introduction.
- Made the pronunciation policy explicit: local clips are drills, authentic/official/native audio is the model, and suspect local clips go to [[Pronunciation Correction Log]].
- Linked the new guide from Start Here, the dashboard, study index, daily routine template, first-week page, Phase 1 starter, Phase 1 ladder, and Phase 1 weekly review.
- Did not modify local MP3 files.

Verification:
- `git diff --check`: clean.
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4762 files, 2891 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.

## [2026-06-07] curate | Japanese second-month audio study plan

Scope: make Weeks 5-8 executable by giving Phase 2 a month-two plan that keeps N5 particles, forms, counters, and daily-life vocabulary tied to authentic audio, local drills, weekly review, and evidence logging.

Changed wiki/source files:
- `Japanese/Study/Second Month Japanese Study Plan.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 2 — Building Blocks.md`
- `Japanese/Listening/Phase 2 Audio Coverage Map.md`
- `Japanese/Listening/Phase 2 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 2 Local Audio Practice.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/First Month Japanese Study Plan.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Phase 2 Audio Assignment Ladder.md`
- `Japanese/Study/Phase 2 Weekly Review.md`

Maintenance changes:
- Added a Week 5-8 execution guide that covers particles, verb/adjective forms, time/counting/counters, and daily-life vocabulary.
- Made the Phase 2 pronunciation policy explicit: grammar counts only when heard and used, local clips are drills, authentic/official/native audio is the model, and suspect local clips go to [[Pronunciation Correction Log]].
- Linked the guide from Start Here, the dashboard, study index, daily routine template, first-month handoff, Phase 2 path, Phase 2 spine, local practice, coverage map, ladder, and weekly review.
- Did not modify local MP3 files.

Verification:
- `git diff --check`: clean.
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4763 files, 2892 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.

## [2026-06-07] curate | Japanese third-month audio study plan

Scope: make Weeks 9-12 executable by giving the second half of Phase 2 a month-three plan that keeps kanji, pronunciation, interactions, shopping, restaurants, and polite service tied to authentic audio, local drills, weekly review, and evidence logging.

Changed wiki/source files:
- `Japanese/Study/Third Month Japanese Study Plan.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 2 — Building Blocks.md`
- `Japanese/Listening/Phase 2 Audio Coverage Map.md`
- `Japanese/Listening/Phase 2 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 2 Local Audio Practice.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Second Month Japanese Study Plan.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Phase 2 Audio Assignment Ladder.md`
- `Japanese/Study/Phase 2 Weekly Review.md`

Maintenance changes:
- Added a Week 9-12 execution guide covering kanji as spoken words, first N5 kanji vocabulary, difficult sounds, daily interactions, shopping/restaurants, and です/ます service rhythm.
- Made the Phase 2 completion policy explicit: kanji starts from spoken words, local clips are drills, authentic/official/native audio is the model, and suspect local clips go to [[Pronunciation Correction Log]].
- Linked the guide from Start Here, the dashboard, study index, daily routine template, second-month handoff, Phase 2 path, Phase 2 spine, local practice, coverage map, ladder, and weekly review.
- Did not modify local MP3 files.

Verification:
- `git diff --check`: clean.
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4764 files, 2893 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.

## [2026-06-07] curate | Japanese fourth-month audio study plan

Scope: make the first month of Phase 3 executable by giving Block 1 a month-four plan that keeps N4 conditionals, passive/causative, and giving/receiving tied to authentic audio, local drills, weekly review, and evidence logging.

Changed wiki/source files:
- `Japanese/Study/Fourth Month Japanese Study Plan.md`
- `Japanese/Japanese.md`
- `Japanese/Learning Path/Phase 3 — Expansion.md`
- `Japanese/Listening/Phase 3 Audio Coverage Map.md`
- `Japanese/Listening/Phase 3 Authentic Audio Spine.md`
- `Japanese/Listening/Phase 3 Local Audio Practice.md`
- `Japanese/Study/Daily Study Routine Templates.md`
- `Japanese/Study/Third Month Japanese Study Plan.md`
- `Japanese/Study/Japanese Learning Dashboard.md`
- `Japanese/Study/Japanese Study Index.md`
- `Japanese/Study/Phase 3 Audio Assignment Ladder.md`
- `Japanese/Study/Phase 3 Weekly Review.md`

Maintenance changes:
- Added a Week 13-16 execution guide for Phase 3 Block 1: te-form review, conditionals, passive/causative, giving/receiving, and consolidation.
- Made the Phase 3 entry policy explicit: hear full sentences before memorizing pattern labels, local clips are drills, authentic/course/tutor/native audio is the model, and suspect local clips go to [[Pronunciation Correction Log]].
- Linked the guide from Start Here, the dashboard, study index, daily routine template, third-month handoff, Phase 3 path, Phase 3 spine, local practice, coverage map, ladder, and weekly review.
- Did not modify local MP3 files.

Verification:
- `git diff --check`: clean.
- `python Japanese\_audio\audit_audio_integrity.py --no-report --skip-ffprobe`: 2210 Markdown MP3 embeds, 1759 unique embedded MP3 files, 1810 MP3 files, 1810 pronunciation entries, 0 missing embedded MP3 files, 0 manifest/file mismatches, 0 format issues.
- `python Japanese\_audio\build_pronunciation_manifest.py --check`: wrote 1810 entries and refreshed the pronunciation audit.
- `python Japanese\_audio\audit_reading_hints.py --fail-on-findings`: 0 findings.
- `python _ops\personal_kb.py audit`: 4765 files, 2894 Markdown files, 1810 MP3 files, 0 heavy audio embed pages, 938 broken-link occurrences.

## [2026-06-14] curate | LLM local hosting and inference lab

Scope: make the LLM topic more actionable by adding a source-backed hands-on local inference path that connects open-weight theory, quantization, KV cache, serving runtimes, and practical API testing.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-local-inference-curation.md`
- `LLM/LLM.md`
- `LLM/LLM — Learning Path.md`
- `LLM/Study/Inference and Efficiency - Review Drill.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `log.md`

Maintenance changes:
- Added a local inference lab covering runtime selection, Ollama, LM Studio, llama.cpp, vLLM, benchmarking, troubleshooting, and the academic reading spine behind deployment choices.
- Linked the lab from the LLM MOC, study index, learning path, and inference review drill.
- Used existing chunks for stable inference/quantization claims and official current docs for live tool behavior.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4777 files, 2906 Markdown files, 808 candidate articles, 21 stubs, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4779 files, 2908 Markdown files, 809 candidate articles, 20 stubs, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-14] curate | LLM inference provenance pass

Scope: strengthen the applied local-inference route by replacing placeholder evidence sections in core inference notes with existing chunks, raw-source links, and cross-links to the local hosting lab.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-inference-provenance-pass.md`
- `LLM/2022 — Alignment and Chat/Quantization.md`
- `LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching.md`
- `LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse.md`
- `LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs.md`
- `log.md`

Maintenance changes:
- Replaced placeholder supporting-chunk and reference sections in the inference cluster.
- Linked KV cache, batching, serving, and quantization notes to existing source-backed chunks.
- Fixed stale Quantization See Also links to the current vault paths.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4779 files, 2908 Markdown files, 809 candidate articles, 20 stubs, 252 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4780 files, 2909 Markdown files, 809 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.
