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

## [2026-06-14] curate | LLM mastery roadmap

Scope: make the LLM study area easier to consume as a complete mastery path by adding competency gates that connect academic reading, active recall, implementation practice, evaluation, and local inference.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-mastery-roadmap.md`
- `LLM/LLM.md`
- `LLM/LLM — Learning Path.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `log.md`

Maintenance changes:
- Added a mastery roadmap with six levels, proof gates, capstone sequence, and completion checklist.
- Linked the roadmap from the LLM MOC, learning path, study index, and local inference lab.
- Kept the note policy-oriented and source-backed by existing LLM wiki notes and the sources index.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4780 files, 2909 Markdown files, 809 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4782 files, 2911 Markdown files, 810 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-14] curate | LLM local inference benchmark log

Scope: make local LLM hosting practice more reproducible by adding a benchmark/run-log note that records the evidence behind model, runtime, quantization, hardware, latency, memory, and quality decisions.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-local-inference-benchmark-log.md`
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `log.md`

Maintenance changes:
- Added a local inference benchmark log with run metadata, measurement definitions, a prompt suite, pass/hold/fail rubric, and troubleshooting links.
- Linked the log from the LLM MOC, study index, local inference lab, and mastery roadmap proof gates.
- Kept the note as practice guidance backed by existing LLM wiki notes and the local inference lab rather than introducing new current claims.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4782 files, 2911 Markdown files, 810 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4784 files, 2913 Markdown files, 811 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-14] curate | LLM local serving runbook

Scope: make local LLM hosting more operational by adding a source-checked runbook for starting local model servers, proving native/OpenAI-compatible endpoints, recording evidence, and diagnosing inference failures.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-local-serving-runbook.md`
- `LLM/LLM.md`
- `LLM/LLM — Learning Path.md`
- `LLM/Study/Inference and Efficiency - Review Drill.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `log.md`

Maintenance changes:
- Added a local serving runbook with runtime decision path, endpoint map, Ollama native smoke test, OpenAI-compatible smoke test, runtime-specific start points, measurement guidance, comparison gates, and failure triage.
- Linked the runbook from the LLM MOC, learning path, study index, inference drill, local hosting lab, benchmark log, and mastery roadmap.
- Checked current runtime docs for Ollama, LM Studio, llama-cpp-python, vLLM, SGLang, and Open WebUI before writing endpoint guidance.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4784 files, 2913 Markdown files, 811 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4786 files, 2915 Markdown files, 812 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-14] curate | LLM model and hardware sizing guide

Scope: make local LLM hosting decisions more rigorous by adding a model/hardware sizing guide that connects parameter count, quantization, KV-cache memory, context length, concurrency, runtime fit, and benchmark proof.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-model-hardware-sizing.md`
- `LLM/LLM.md`
- `LLM/2022 — Alignment and Chat/Quantization.md`
- `LLM/Study/Inference and Efficiency - Review Drill.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `LLM/Study/Local LLM Model and Hardware Sizing Guide.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `log.md`

Maintenance changes:
- Added a local model and hardware sizing guide with weight-memory estimates, KV-cache planning, hardware bands, quantization choices, context/concurrency checks, runtime fit, and a decision-record template.
- Linked the guide from the LLM MOC, study index, local inference lab, serving runbook, benchmark log, mastery roadmap, inference drill, and quantization note.
- Kept the guide as policy/practice guidance backed by existing source-linked inference notes and chunks.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4786 files, 2915 Markdown files, 812 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4788 files, 2917 Markdown files, 813 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-14] curate | LLM quality evaluation harness

Scope: make local LLM hosting decisions quality-aware by adding a workload-specific harness for prompt suites, rubric scoring, pairwise comparisons, RAG/citation checks, judge-bias controls, and pass/hold/fail gates.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-quality-evaluation-harness.md`
- `LLM/LLM.md`
- `LLM/Study/Inference and Efficiency - Review Drill.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `LLM/Study/Local LLM Quality Evaluation Harness.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `log.md`

Maintenance changes:
- Added a local quality evaluation harness that defines the evaluation ladder, prompt set, 0/1/2 rubric dimensions, pass/hold/fail gate, pairwise comparison protocol, RAG/citation checks, contamination controls, and a run log template.
- Linked the harness from the LLM MOC, study index, inference drill, local benchmark log, serving runbook, and mastery roadmap.
- Kept the note as policy/practice guidance backed by existing source-linked evaluation notes and chunks rather than introducing new current claims.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4788 files, 2917 Markdown files, 813 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4790 files, 2919 Markdown files, 814 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-14] curate | LLM local RAG assistant lab

Scope: make the RAG portion of LLM mastery more applied by adding a local assistant lab that connects corpus ingestion, chunking, embeddings, retrieval, reranking, context assembly, local generation, citations, and failure diagnosis.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-local-rag-assistant-lab.md`
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `LLM/Study/Local LLM Quality Evaluation Harness.md`
- `LLM/Study/Local RAG Assistant Lab.md`
- `LLM/Study/RAG and Prompting - Review Drill.md`
- `log.md`

Maintenance changes:
- Added a local RAG assistant lab with workload scoping, corpus metadata, chunking policy, embedding/index flow, retrieval/reranking/context assembly, local endpoint generation, answer verification, failure triage, benchmark logging, and completion gates.
- Linked the lab from the LLM MOC, study index, mastery roadmap, local inference lab, benchmark log, quality harness, and RAG drill.
- Kept the lab as practice guidance backed by existing source-linked retrieval, chunking, embedding, RAG evaluation, and DPR notes rather than introducing new current tooling claims.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4790 files, 2919 Markdown files, 814 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4792 files, 2921 Markdown files, 815 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-14] curate | LLM paper reading protocol

Scope: strengthen the academic side of LLM mastery by adding a reusable paper-reading protocol for extracting claims, mechanisms, evidence, limitations, and deployment implications from research papers.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-paper-reading-protocol.md`
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Paper Reading Protocol.md`
- `LLM/Study/LLM Study Index.md`
- `log.md`

Maintenance changes:
- Added a paper reading protocol with reading passes, a paper-card template, claim taxonomy, evidence checklist, 20-paper fast-path lens, deployment implication matrix, red flags, vault-capture workflow, and completion gate.
- Linked the protocol from the LLM MOC, study index, and mastery roadmap.
- Kept the note as policy/practice guidance backed by the existing source catalog and timeline notes rather than adding new current claims.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4792 files, 2921 Markdown files, 815 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4794 files, 2923 Markdown files, 816 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-14] curate | LLM attention implementation lab

Scope: strengthen the architecture capstone by adding a hands-on attention implementation lab for scaled dot-product attention, causal masking, multi-head tensor reshaping, tests, and inference-memory implications.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-attention-implementation-lab.md`
- `LLM/2017 — The Transformer/Attention Mechanism.md`
- `LLM/LLM.md`
- `LLM/Study/Attention Implementation Lab.md`
- `LLM/Study/Foundations and Architecture - Review Drill.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `log.md`

Maintenance changes:
- Added an attention implementation lab with tensor-shape tables, minimal scaled dot-product attention code, causal mask code, multi-head self-attention skeleton, tests, debugging checklist, MQA/GQA extension, and completion gate.
- Linked the lab from the LLM MOC, study index, mastery roadmap, foundations drill, and attention mechanism note.
- Kept the lab as policy/practice guidance backed by existing source-linked attention and MQA chunks rather than introducing new current claims.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4794 files, 2923 Markdown files, 816 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4796 files, 2925 Markdown files, 817 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-14] curate | LLM mastery capstone workbook

Scope: add a single workbook for collecting proof of LLM mastery across paper reading, attention implementation, local inference, benchmarking, local quality evaluation, RAG, and deployment decision-making.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-mastery-capstone-workbook.md`
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `log.md`

Maintenance changes:
- Added an LLM mastery capstone workbook with an evidence ledger, paper-map template, attention implementation proof template, local inference proof template, RAG proof template, evaluation proof template, deployment decision memo, and completion audit.
- Linked the workbook from the LLM MOC, study index, and mastery roadmap so it is reachable from the main study path.
- Kept the workbook as practice/evidence guidance backed by existing study notes rather than introducing new current model or runtime claims.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4796 files, 2925 Markdown files, 817 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4798 files, 2927 Markdown files, 818 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-14] curate | LLM inference request lifecycle lab

Scope: add a request-level inference lab that connects local endpoint calls to the academic mechanics of tokenization, prefill, logits, sampling, stopping, detokenization, streaming, and benchmark measurement.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-inference-request-lifecycle.md`
- `LLM/LLM.md`
- `LLM/Study/Inference and Efficiency - Review Drill.md`
- `LLM/Study/LLM Inference Request Lifecycle Lab.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `log.md`

Maintenance changes:
- Added an inference request lifecycle lab with the request pipeline, sampling knobs, frozen-request worksheet, prefill-vs-decode comparison, sampling A/B test, stop/structured-output test, streaming comparison, failure triage, and benchmark row add-on.
- Linked the lab from the LLM MOC, study index, mastery roadmap, local hosting lab, and inference review drill.
- Kept runtime-specific current endpoint claims in the already verified local serving runbook; this pass uses existing source-linked foundation, tokenization, KV-cache, serving, speculative decoding, and structured-output notes.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4798 files, 2927 Markdown files, 818 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4800 files, 2929 Markdown files, 819 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-14] curate | LLM chat template and tokenizer compatibility lab

Scope: add a local-inference compatibility lab for diagnosing tokenizer, special-token, chat-template, role-boundary, and stop-condition mismatches before blaming model quality.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-chat-template-tokenizer-lab.md`
- `LLM/LLM.md`
- `LLM/Study/Chat Template and Tokenizer Compatibility Lab.md`
- `LLM/Study/Inference and Efficiency - Review Drill.md`
- `LLM/Study/LLM Inference Request Lifecycle Lab.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `log.md`

Maintenance changes:
- Added a chat template and tokenizer compatibility lab with a compatibility chain, model package card, rendered prompt check, base-vs-chat behavior test, tokenizer sanity set, stop/role boundary test, failure triage, benchmark add-on, and completion gate.
- Linked the lab from the LLM MOC, study index, mastery roadmap, request lifecycle lab, local serving runbook, and inference review drill.
- Kept the pass as durable compatibility guidance backed by existing tokenization, instruction tuning, system prompt, structured-output, function-calling, and serving notes rather than adding new current runtime claims.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4800 files, 2929 Markdown files, 819 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4802 files, 2931 Markdown files, 820 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-14] curate | LLM local security and privacy runbook

Scope: add a local-hosting security and privacy runbook for endpoint exposure, logs, RAG corpus boundaries, prompt injection, tool permissions, and go/no-go checks before sharing a local model server.

Changed wiki/source files:
- `.tasks/2026-06-14-llm-local-security-privacy-runbook.md`
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Security and Privacy Runbook.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `LLM/Study/Local RAG Assistant Lab.md`
- `log.md`

Maintenance changes:
- Added a local LLM security and privacy runbook with a security model, exposure levels, pre-run checklist, endpoint boundary checks, prompt/log/storage map, RAG privacy checks, tool/agent boundary, incident triage, and go/no-go gate.
- Linked the runbook from the LLM MOC, study index, mastery roadmap, local serving runbook, and local RAG assistant lab.
- Kept the pass as durable local-hosting security guidance backed by existing system prompt, function-calling, RAG, local serving, and serving architecture notes rather than adding new current runtime claims.
- Did not modify protected raw, chunk, template, media, or Obsidian config paths.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4802 files, 2931 Markdown files, 820 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4804 files, 2933 Markdown files, 821 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | LLM context window and token budgeting lab

Scope: add a practical context-window and token-budgeting lab for local inference requests that need measured prompt, history, RAG, tool, output, and margin accounting.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-context-token-budgeting.md`
- `LLM/Study/Local LLM Context Window and Token Budgeting Lab.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Chat Template and Tokenizer Compatibility Lab.md`
- `LLM/Study/LLM Inference Request Lifecycle Lab.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `LLM/Study/Local RAG Assistant Lab.md`
- `LLM/Study/Local LLM Model and Hardware Sizing Guide.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `LLM/Study/Local LLM Troubleshooting Decision Tree.md`
- `LLM/Study/Inference and Efficiency - Review Drill.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `index.md`
- `log.md`

Maintenance changes:
- Added a context-budget formula, runtime context map, tokenizer sanity count, rendered prompt budget table, RAG packing budget, overflow/truncation test, prompt-length performance test, failure triage, benchmark add-on, and completion gate.
- Linked the lab from tokenizer/template, lifecycle, benchmark, RAG, sizing, serving, troubleshooting, review, roadmap, capstone, and exam notes.
- Checked current Hugging Face, Ollama, vLLM, and llama.cpp docs for tokenization, chat templates, context length, and runtime context controls.
- Did not modify unrelated active-vault Japanese, CS, recipe, or learning-path edits.

Verification:
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4830 files, 2959 Markdown files, 834 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-15] curate | LLM local tool calling and structured output lab

Scope: add a practical local tool-calling and structured-output lab for schema validation, policy checks, tool execution, result injection, bounded agent loops, and tool failure evaluation.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-local-tool-calling-lab.md`
- `LLM/LLM.md`
- `LLM/Study/Local LLM Tool Calling and Structured Output Lab.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Agents and Evaluation - Review Drill.md`
- `LLM/Study/Local LLM OpenAI-Compatible API Contract Lab.md`
- `LLM/Study/Decoding and Sampling Controls Lab.md`
- `LLM/Study/Local LLM Client Harness Lab.md`
- `LLM/Study/Local LLM Security and Privacy Runbook.md`
- `LLM/Study/Local LLM Quality Evaluation Harness.md`
- `LLM/Study/Local LLM Troubleshooting Decision Tree.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `LLM/Study/LLM Deployment Decision Matrix.md`
- `index.md`
- `log.md`

Maintenance changes:
- Added a local tool-calling lab with structured-output distinction, runtime support map, tool contract card, structured-output baseline, single-tool proof, failure tests, bounded multi-turn loop, quality row, failure triage, benchmark add-on, and completion gate.
- Linked the lab from the LLM MOC, study index, agents drill, API contract, decoding controls, client harness, security runbook, quality harness, troubleshooting tree, benchmark log, serving runbook, deployment matrix, roadmap, capstone, and exam.
- Checked current OpenAI, Ollama, vLLM, llama.cpp, and llama-cpp-python docs for function calling, structured outputs, local tool calling, and schema-constrained output behavior.
- Did not modify unrelated active-vault Japanese, CS, recipe, or learning-path edits.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4830 files, 2959 Markdown files, 834 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4832 files, 2961 Markdown files, 835 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-15] curate | LLM local RAG minimal Python harness

Scope: add a practical local RAG implementation harness that turns the conceptual RAG lab into reproducible corpus, chunking, embedding, retrieval, cited-answer, refusal, failure, benchmark, and quality artifacts.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-local-rag-harness.md`
- `LLM/LLM.md`
- `LLM/Study/Local RAG Minimal Python Harness.md`
- `LLM/Study/Local RAG Assistant Lab.md`
- `LLM/Study/RAG and Prompting - Review Drill.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `LLM/Study/Local LLM Context Window and Token Budgeting Lab.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `LLM/Study/Local LLM Quality Evaluation Harness.md`
- `LLM/Study/Local LLM Security and Privacy Runbook.md`
- `LLM/Study/Local LLM Troubleshooting Decision Tree.md`
- `LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide.md`
- `LLM/Study/LLM Deployment Decision Matrix.md`
- `index.md`
- `log.md`

Maintenance changes:
- Added a minimal local RAG harness with artifact contract, stack choices, runtime smoke checks, corpus manifest, chunk records, Chroma/Ollama embedding/index pattern, retrieval evidence, context assembly, local OpenAI-compatible generation, unsupported-question refusal, failure rows, benchmark rows, quality rows, and completion gate.
- Linked the harness from the LLM MOC, study index, RAG lab, RAG drill, roadmap, capstone workbook, self-assessment, hosting lab, context budget lab, benchmark log, quality harness, security runbook, troubleshooting tree, adaptation guide, and deployment matrix.
- Checked current Ollama, Chroma, and Sentence Transformers docs for local embeddings, OpenAI-compatible local generation, vector-store collections/querying/persistence, and semantic-search assumptions.
- Did not modify unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4832 files, 2961 Markdown files, 835 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4834 files, 2963 Markdown files, 836 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-15] curate | LLM 20-paper fast path synthesis map

Scope: add an academic synthesis map that turns the 20-paper fast path into one causal story from Transformer architecture through pretraining, scaling, systems, open models, alignment, adaptation, reasoning, RAG, agents, evaluation, and local deployment implications.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-20-paper-synthesis-map.md`
- `LLM/LLM.md`
- `LLM/Study/LLM 20-Paper Fast Path Synthesis Map.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/LLM Paper Reading Protocol.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `index.md`
- `log.md`

Maintenance changes:
- Added a synthesis map with a one-page causal story, cluster matrix, per-paper mastery questions, local-hosting bridge, oral recall gate, and completion gate.
- Linked the map from the LLM MOC, study index, paper reading protocol, mastery roadmap, capstone workbook, and self-assessment exam.
- Updated the capstone paper-map row with the new proof link while keeping the status honest: study map drafted; oral proof not yet passed.
- Used existing vault raw source notes and `LLM/Sources/Sources Index.md`; no new external-source claims were added.
- Did not modify unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4834 files, 2963 Markdown files, 836 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4836 files, 2965 Markdown files, 837 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-15] curate | LLM first local inference evidence pack

Scope: add a first-run evidence pack that tells the learner exactly what to save from a local LLM run: machine preflight, model provenance, runtime compatibility, endpoint proof, OpenAI-compatible smoke test, client harness row, benchmark row, quality decision, security boundary, and next action.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-first-inference-evidence-pack.md`
- `LLM/LLM.md`
- `LLM/Study/Local LLM First Inference Evidence Pack.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `index.md`
- `log.md`

Maintenance changes:
- Added a first local inference evidence pack with run-card fields, preflight evidence, model/runtime fit checks, runtime start points, native and OpenAI-compatible smoke tests, client-harness requirements, benchmark row, quality decision, completion gate, and current official docs.
- Linked the evidence pack from the LLM MOC, study index, hosting lab, serving runbook, mastery roadmap, capstone workbook, and self-assessment exam.
- Checked current Ollama, LM Studio, llama.cpp, llama-cpp-python, and vLLM docs for local endpoints, OpenAI-compatible serving, model-list proof, and usage metrics.
- Did not modify unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4836 files, 2965 Markdown files, 837 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4838 files, 2967 Markdown files, 838 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-15] curate | LLM mechanism-to-inference bridge map

Scope: add an academic-to-applied bridge map that forces local LLM symptoms, runtime settings, and hosting decisions to name the underlying mechanism, the local control surface, the evidence artifact, and the next controlled decision.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-mechanism-inference-bridge.md`
- `LLM/LLM.md`
- `LLM/Study/LLM Mechanism-to-Inference Bridge Map.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `index.md`
- `log.md`

Maintenance changes:
- Added a mechanism-to-inference bridge table connecting tokenization, chat templates, autoregression, attention, positional encoding, KV cache, MQA/GQA, quantization, sampling, batching, prompt caching, RAG, tool calling, post-training, evaluation, and deployment to local evidence artifacts.
- Added failure triage and oral-drill tables that translate local symptoms into mechanisms, controls, and next decisions.
- Linked the bridge from the LLM MOC, study index, mastery roadmap, capstone workbook, and self-assessment exam.
- Checked primary papers and current official docs for attention, Chinchilla, RoPE, FlashAttention, GQA, PagedAttention/vLLM, GPTQ, AWQ, chat templates, Ollama metrics, llama.cpp server, and LM Studio OpenAI compatibility.
- Did not modify unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4838 files, 2967 Markdown files, 838 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4840 files, 2969 Markdown files, 839 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-15] curate | LLM Windows local first-run quickstart

Scope: add a Windows-first local LLM quickstart that turns the broader hosting and evidence runbooks into exact PowerShell steps for preflight capture, Ollama or LM Studio loopback API proof, listener checks, quality mini-suite, and first decision row.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-windows-local-quickstart.md`
- `LLM/LLM.md`
- `LLM/Study/Local LLM Windows First-Run Quickstart.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `LLM/Study/Local LLM First Inference Evidence Pack.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `index.md`
- `log.md`

Maintenance changes:
- Added a Windows-first quickstart with run-folder setup, PowerShell preflight capture, Ollama native and OpenAI-compatible smoke tests, LM Studio server/API path, listener boundary check, quality mini-suite, decision row, and troubleshooting order.
- Linked the quickstart from the LLM MOC, study index, hosting lab, serving runbook, first inference evidence pack, mastery roadmap, capstone workbook, and self-assessment exam.
- Checked current Ollama, LM Studio, llama.cpp, llama-cpp-python, and vLLM docs for Windows installation, local server startup, OpenAI-compatible routes, usage metrics, and Windows/WSL serving boundaries.
- Did not modify unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4840 files, 2969 Markdown files, 839 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4842 files, 2971 Markdown files, 840 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-15] curate | LLM math and tensor shape primer

Scope: add a compact academic primer that connects LLM math and tensor shapes to implementation, training, and local inference diagnostics.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-math-tensor-shape-primer.md`
- `LLM/LLM.md`
- `LLM/Study/LLM Math and Tensor Shape Primer.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/LLM Architecture Cheatsheet.md`
- `LLM/Study/Attention Implementation Lab.md`
- `LLM/Study/Tiny Decoder-Only Transformer Training Lab.md`
- `LLM/Study/LLM Inference Request Lifecycle Lab.md`
- `LLM/Study/Local LLM Model and Hardware Sizing Guide.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `index.md`
- `log.md`

Maintenance changes:
- Added a math and tensor-shape primer covering token IDs, embeddings, hidden states, logits, softmax, cross-entropy, perplexity, shifted targets, attention shapes, transformer block shape contracts, parameter memory, KV-cache arithmetic, prefill versus decode, and common math-to-implementation bugs.
- Routed the primer from the LLM MOC, study index, architecture cheatsheet, attention lab, tiny decoder lab, request lifecycle lab, model/hardware sizing guide, mastery roadmap, capstone workbook, and self-assessment exam.
- Kept the pass grounded in existing internal source/chunk notes; no new current model or runtime claims were added.
- Did not modify unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4842 files, 2971 Markdown files, 840 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4844 files, 2973 Markdown files, 841 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-15] curate | LLM local runtime comparison lab

Scope: add a dedicated lab for comparing local LLM runtimes with controlled endpoint, benchmark, quality, compatibility, and deployment evidence.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-runtime-comparison-lab.md`
- `LLM/LLM.md`
- `LLM/Study/Local LLM Runtime Comparison Lab.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `LLM/Study/Local LLM Runtime and Model Compatibility Matrix.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `LLM/Study/Local LLM Quality Evaluation Harness.md`
- `LLM/Study/LLM Deployment Decision Matrix.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `index.md`
- `log.md`

Maintenance changes:
- Added a runtime comparison lab covering Ollama, LM Studio, llama.cpp, vLLM, SGLang, and UI-over-provider comparisons with frozen prompts, sampler settings, context target, output cap, benchmark rows, quality rows, and a decision card.
- Routed the lab from the LLM MOC, study index, serving runbook, runtime compatibility matrix, benchmark log, quality harness, deployment matrix, mastery roadmap, capstone workbook, and self-assessment exam.
- Checked current official runtime/API docs for Ollama native and OpenAI-compatible routes, LM Studio OpenAI-compatible endpoints, llama.cpp server routes/timings, vLLM serving/CLI, and SGLang OpenAI-compatible chat completions.
- Did not modify unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4844 files, 2973 Markdown files, 841 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4846 files, 2975 Markdown files, 842 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-15] curate | LLM reasoning budget lab

Scope: add a dedicated lab for local reasoning models, thinking mode, reasoning parsers, test-time compute, trace policy, and measured quality/latency trade-offs.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-reasoning-budget-lab.md`
- `LLM/LLM.md`
- `LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/LLM Inference Request Lifecycle Lab.md`
- `LLM/Study/Decoding and Sampling Controls Lab.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `LLM/Study/Local LLM Quality Evaluation Harness.md`
- `LLM/Study/Local LLM OpenAI-Compatible API Contract Lab.md`
- `LLM/Study/Local LLM Runtime and Model Compatibility Matrix.md`
- `LLM/Study/Local LLM Runtime Comparison Lab.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `LLM/2026 — Reasoning and Agents/Reasoning Models and Test-Time Compute.md`
- `LLM/2026 — Reasoning and Agents/DeepSeek R1 and Open Reasoning.md`
- `index.md`
- `log.md`

Maintenance changes:
- Added a reasoning-budget lab covering capability/parser smoke tests, effort sweeps, trace visibility policy, reasoning-versus-sampling controls, RAG/tool reasoning checks, benchmark add-on fields, failure triage, and a decision card.
- Routed the lab from the LLM MOC, study index, inference lifecycle, decoding controls, benchmark log, quality harness, API contract, runtime compatibility matrix, runtime comparison lab, serving runbook, mastery roadmap, capstone workbook, self-assessment exam, and 2026 reasoning notes.
- Checked current Ollama thinking/API, LM Studio Responses/API changelog, vLLM reasoning outputs, SGLang reasoning parser, and Open WebUI reasoning/thinking settings.
- Did not modify unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4846 files, 2975 Markdown files, 842 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4848 files, 2977 Markdown files, 843 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-15] curate | LLM concurrency and batch throughput lab

Scope: add a dedicated lab for local LLM concurrency, queueing, batch throughput, saturation, and backpressure decisions.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-concurrency-batch-throughput-lab.md`
- `LLM/LLM.md`
- `LLM/Study/Local LLM Concurrency and Batch Throughput Lab.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `LLM/Study/Local LLM Runtime Comparison Lab.md`
- `LLM/Study/Local LLM Model and Hardware Sizing Guide.md`
- `LLM/Study/Local LLM Troubleshooting Decision Tree.md`
- `LLM/Study/LLM Deployment Decision Matrix.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching.md`
- `LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs.md`
- `index.md`
- `log.md`

Maintenance changes:
- Added a concurrency and batch throughput lab covering single-request baselines, concurrency ladders, short/long prompt mixes, queue policy, backpressure, p50/p95 TTFT, throughput, saturation point, and deployment decisions.
- Routed the lab from the LLM MOC, study index, hosting lab, serving runbook, benchmark log, runtime comparison lab, sizing guide, troubleshooting tree, deployment matrix, mastery roadmap, capstone workbook, self-assessment exam, and the academic batching/serving notes.
- Checked current Ollama concurrency/queue settings, LM Studio parallel requests, vLLM benchmark load controls, SGLang benchmark/profiling tools, and llama.cpp server slots/continuous batching/metrics.
- Did not modify unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

Verification:
- Baseline `python _ops\personal_kb.py audit`: 4848 files, 2977 Markdown files, 843 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- Final `python _ops\personal_kb.py audit`: 4850 files, 2979 Markdown files, 844 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- `git diff --check`: clean.

## [2026-06-15] curate | LLM observability and operations runbook

Scope: add a dedicated local LLM operations runbook for proving loaded-model state, endpoint route, request timings, logs, server metrics, resource pressure, error evidence, and the next controlled change.

Changed wiki/source files:
- `.tasks/2026-06-15-llm-observability-ops-runbook.md`
- `LLM/LLM.md`
- `LLM/Study/Local LLM Observability and Operations Runbook.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `LLM/Study/Local LLM Inference Benchmark Log.md`
- `LLM/Study/Local LLM Troubleshooting Decision Tree.md`
- `LLM/Study/LLM Deployment Decision Matrix.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Self-Assessment Exam.md`
- `LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs.md`
- `LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching.md`
- `LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added an observability and operations runbook with metric vocabulary, runtime-specific state/metrics map, PowerShell evidence commands, operations rows, symptom-to-evidence map, privacy note, and completion gate.
- Routed the runbook from the LLM MOC, study index, hosting lab, serving runbook, benchmark log, troubleshooting tree, deployment matrix, mastery roadmap, capstone workbook, self-assessment exam, and serving/KV/batching academic notes.
- Checked current Ollama API/generate/ps, LM Studio server/loaded-model/log CLI, llama.cpp server metrics, vLLM metrics, SGLang production metrics/benchmarking, and NVIDIA SMI docs.
- Did not modify unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

Verification:
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4852 files, 2981 Markdown files, 845 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | LLM failure triage runner

Scope: add a repeatable local LLM failure triage artifact so failed endpoint, route, client, quality, RAG, tool, security, or operations runs can be turned into proof-quality diagnostic evidence before reruns support downstream decisions.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/Local LLM Failure Triage Runner.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/Local LLM Capstone Project Blueprint.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `LLM/Study/Local LLM First Smoke Request Runner.md`
- `LLM/Study/Local LLM First Endpoint Run Sheet.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added a standard-library failure triage runner that validates symptom, canonical failed layer, proof link, mechanism or request-phase owner, ruled-out layers, and one controlled next action.
- Routed failed local runs from the LLM MOC, study index, dashboard, roadmap, capstone workbook, capstone blueprint, hands-on practicum, serving runbook, first smoke runner, and first endpoint run sheet.
- Added a `local-failure-triage` default gate to the mastery evidence audit runner.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_llm_failure_triage_runner.py` from the note.
- Failure triage fixtures: pass -> exit 0 `failure_triage_ready`; hold -> exit 1 `failure_triage_incomplete`; fail -> exit 2 `failure_triage_failed`.
- Extracted and compiled `llm_mastery_evidence_audit_runner.py`; default manifest -> exit 1 `mastery_evidence_incomplete`, 29 gates, 29 holds.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4944 files, 3073 Markdown files, 908 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | LLM paper claim audit runner

Scope: add a repeatable academic evidence audit for the LLM fast-path paper set so paper claims can be checked for coverage, claim anatomy, source proof, local implication, and follow-up proof routes before they support capstone or mastery claims.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Paper Claim Audit Runner.md`
- `LLM/Study/LLM Paper Claim Ledger.md`
- `LLM/Study/LLM Paper-to-Local Proof Router.md`
- `LLM/Study/LLM 20-Paper Fast Path Synthesis Map.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/Local LLM Capstone Project Blueprint.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added a standard-library paper claim audit runner that validates expected fast-path coverage, claim type, main claim, evidence type, limitation, mechanism, source proof, local implication, and follow-up route.
- Routed the runner from the LLM MOC, study index, paper claim ledger, paper-to-local proof router, 20-paper synthesis map, dashboard, roadmap, capstone workbook, capstone blueprint, and mastery evidence audit.
- Added an `academic-paper-claim-audit` default gate to the mastery evidence audit runner.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `llm_paper_claim_audit_runner.py` from the note.
- Paper claim audit fixtures: pass -> exit 0 `paper_claim_audit_ready`; hold -> exit 1 `paper_claim_audit_incomplete`; fail -> exit 2 `paper_claim_audit_failed`.
- Extracted and compiled `llm_mastery_evidence_audit_runner.py`; default manifest -> exit 1 `mastery_evidence_incomplete`, 30 gates, 30 holds.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4945 files, 3074 Markdown files, 909 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | LLM academic-to-local defense matrix runner

Scope: add a repeatable defense matrix for the LLM mastery path so academic paper claims, mechanisms, local predictions, artifacts, metrics, failure owners, and decisions can be checked together before a capstone or oral/practical defense counts.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Academic-to-Local Defense Matrix Runner.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/LLM Paper-to-Local Proof Router.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added a standard-library academic-to-local defense matrix runner that validates expected clusters, paper proof, mechanism, local prediction, local artifact, metric kind, controlled variable, confounder, failure owner, decision, defense answer, and next route.
- Routed the runner from the LLM MOC, study index, dashboard, roadmap, capstone workbook, paper-to-local proof router, and mastery evidence audit.
- Added an `academic-to-local-defense-matrix` default gate to the mastery evidence audit runner.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `llm_academic_to_local_defense_matrix_runner.py` from the note.
- Defense matrix fixtures: pass -> exit 0 `defense_matrix_ready`; hold -> exit 1 `defense_matrix_incomplete`; fail -> exit 2 `defense_matrix_failed`.
- Extracted and compiled `llm_mastery_evidence_audit_runner.py`; default manifest -> exit 1 `mastery_evidence_incomplete`, 31 gates, 31 holds.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4946 files, 3075 Markdown files, 910 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | LLM first endpoint evidence audit runner

Scope: add a repeatable audit for first local endpoint run folders so hosting a local LLM and running inference requires machine, model, runtime, route, response, debrief, and decision proof before the run counts.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/Local LLM First Endpoint Evidence Audit Runner.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/Local LLM First Endpoint Run Sheet.md`
- `LLM/Study/Local LLM First Inference Evidence Pack.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/Local LLM Capstone Project Blueprint.md`
- `LLM/Study/Local LLM Windows First-Run Quickstart.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added a standard-library first endpoint evidence audit runner that checks run card, preflight, runtime install state, model pull or custody, runtime health, smoke summary, native response, OpenAI-compatible response when required, first-response debrief, decision, and optional quality boundary evidence.
- Routed the runner from the LLM MOC, study index, dashboard, roadmap, capstone workbook, capstone blueprint, hands-on practicum, first endpoint run sheet, first inference evidence pack, and Windows first-run quickstart.
- Added a `local-first-endpoint-evidence-audit` default gate to the mastery evidence audit runner.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `first_endpoint_audit.py` from the note.
- First endpoint audit fixtures: pass -> exit 0 `first_endpoint_evidence_ready`; hold -> exit 1 `first_endpoint_evidence_incomplete`; fail -> exit 2 `first_endpoint_evidence_failed`.
- Extracted and compiled `llm_mastery_evidence_audit_runner.py`; default manifest -> exit 1 `mastery_evidence_incomplete`, 32 gates, 32 holds.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4947 files, 3076 Markdown files, 911 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | LLM application integration evidence runner

Scope: add a repeatable audit for the boundary where a proven local endpoint and reusable client are wired into a real app, CLI, UI, job, RAG assistant, or tool loop before result synthesis or deployment readiness can count it.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/Local LLM Application Integration Evidence Runner.md`
- `LLM/Study/LLM Deployment Readiness Audit Runner.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Capstone Project Blueprint.md`
- `LLM/Study/Local LLM Client Harness Lab.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added a standard-library application integration evidence runner that checks app contract, endpoint contract, client flow, user flow, response handling, failure behavior, privacy/logging, evaluation handoff, operations handoff, promotion decision, and optional RAG/tool or concurrency boundaries.
- Routed the runner from the LLM MOC, study index, dashboard, roadmap, capstone workbook, capstone blueprint, client harness lab, hands-on practicum, deployment readiness audit, and mastery evidence audit.
- Added `application_integration` to the deployment readiness audit runner and `local-application-integration` to the mastery evidence audit runner.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_llm_application_integration_evidence_runner.py` from the note.
- Application integration fixtures: pass -> exit 0 `application_integration_ready`; hold -> exit 1 `application_integration_incomplete`; fail -> exit 2 `application_integration_failed`.
- Extracted and compiled `llm_deployment_readiness_audit_runner.py`; pass manifest with `application_integration` row -> exit 0 `deployment_readiness_ready`, 14 rows, 14 passes.
- Extracted and compiled `llm_mastery_evidence_audit_runner.py`; default manifest -> exit 1 `mastery_evidence_incomplete`, 33 gates, 33 holds.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4948 files, 3077 Markdown files, 912 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | LLM recall and remediation audit runner

Scope: add a repeatable audit for scored recall and exam rows so academic and applied LLM knowledge has coverage, routes for misses, remediation artifacts, applied proof, and next review before it supports mastery claims.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Recall and Remediation Audit Runner.md`
- `LLM/Study/LLM Active Recall Question Bank.md`
- `LLM/Study/LLM Daily Mastery Session Run Sheet.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/LLM Mastery Exam Run Sheet.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added a standard-library recall/remediation audit runner that checks recall domain coverage, numeric scores, answer artifacts, miss reasons, remediation artifacts, next-review dates, applied proof links, overall threshold, and hard-fail applied-domain zeroes.
- Routed the runner from the LLM MOC, study index, dashboard, active recall bank, daily session sheet, exam run sheet, capstone workbook, roadmap, and mastery evidence audit.
- Added `exam-recall-remediation-audit` to the mastery evidence audit runner default gate set.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `llm_recall_remediation_audit_runner.py` from the note.
- Recall/remediation fixtures: pass -> exit 0 `recall_remediation_ready`; hold -> exit 1 `recall_remediation_incomplete`; fail -> exit 2 `recall_remediation_failed`.
- Extracted and compiled `llm_mastery_evidence_audit_runner.py`; default manifest -> exit 1 `mastery_evidence_incomplete`, 34 gates, 34 holds.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4949 files, 3078 Markdown files, 913 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | Local LLM artifact custody audit runner

Scope: add a repeatable audit for model artifact custody so local inference evidence can prove the source identity, local bytes, file inventory, verification method, unsafe-file decision, conversion/import trail, runtime handoff, and cleanup plan before compatibility, serving, benchmark, or deployment claims depend on a model.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/Local LLM Artifact Custody Audit Runner.md`
- `LLM/Study/Local LLM Artifact Download Cache and Conversion Lab.md`
- `LLM/Study/Local LLM Model Acquisition and Provenance Checklist.md`
- `LLM/Study/Local LLM Runtime and Model Compatibility Matrix.md`
- `LLM/Study/LLM Deployment Readiness Audit Runner.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added a standard-library artifact custody audit runner that checks source identity, pinned revision/tag/file/digest, local path or runtime id, inventory proof, verification proof, unsafe-file decisions, conversion/import proof, runtime handoff, cleanup plan, and rejected/blocked artifact failures.
- Routed the runner from the LLM MOC, study index, mastery dashboard, artifact lab, acquisition checklist, runtime compatibility matrix, capstone workbook, mastery roadmap, mastery evidence audit, and deployment readiness audit.
- Added `local-artifact-custody-audit` to the mastery evidence audit default gate set.
- Added `artifact_custody` to the deployment readiness audit default evidence kinds.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_llm_artifact_custody_audit_runner.py` from the note.
- Artifact custody fixtures: pass -> exit 0 `artifact_custody_ready`; hold -> exit 1 `artifact_custody_incomplete`; fail -> exit 2 `artifact_custody_failed`.
- Extracted and compiled `llm_mastery_evidence_audit_runner.py`; default manifest -> exit 1 `mastery_evidence_incomplete`, 35 gates, 35 holds.
- Extracted and compiled `llm_deployment_readiness_audit_runner.py`; default empty rows -> exit 1 `deployment_readiness_incomplete`, 15 rows, 15 holds; pass manifest with `artifact_custody` row -> exit 0 `deployment_readiness_ready`, 15 rows, 15 passes.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4950 files, 3079 Markdown files, 914 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | Local LLM reasoning budget audit runner

Scope: add a repeatable audit for reasoning-mode and test-time-compute evidence so local quality, runtime, result-synthesis, or deployment decisions can prove the trigger, parser, effort sweep, latency cost, quality delta, trace policy, selected effort, and retest trigger before treating thinking mode as a win.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner.md`
- `LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab.md`
- `LLM/Study/Decoding and Sampling Controls Lab.md`
- `LLM/Study/LLM Inference Request Lifecycle Lab.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `LLM/Study/Local LLM Quality Evaluation Harness.md`
- `LLM/Study/Local LLM Result Synthesis Runner.md`
- `LLM/Study/LLM Deployment Readiness Audit Runner.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added a standard-library reasoning budget runner that checks fixed model/runtime/route/prompt controls, distinct effort settings, parser or reasoning-output shape, raw response and final-answer evidence, trace policy, timing, quality, selected effort, token impact, and retest trigger.
- Routed the runner from the LLM MOC, study index, dashboard, roadmap, capstone workbook, practicum sequence, request lifecycle lab, decoding lab, reasoning lab, quality harness, result synthesis, deployment readiness audit, and mastery evidence audit.
- Added `local-reasoning-budget` to the mastery evidence audit default gate set.
- Added conditional checks in result synthesis and deployment readiness so reasoning-backed quality rows hold when they lack reasoning-budget audit output.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_llm_reasoning_budget_runner.py` from the note.
- Reasoning budget fixtures: pass -> exit 0 `reasoning_budget_ready`; hold -> exit 1 `reasoning_budget_incomplete`; fail -> exit 2 `reasoning_budget_failed`.
- Extracted and compiled `llm_mastery_evidence_audit_runner.py`; default manifest -> exit 1 `mastery_evidence_incomplete`, 36 gates, 36 holds, including `local-reasoning-budget`.
- Extracted and compiled `llm_deployment_readiness_audit_runner.py`; default empty rows -> exit 1 `deployment_readiness_incomplete`, 15 rows, 15 holds; reasoning-backed quality row without reasoning-budget audit -> exit 1 `deployment_readiness_incomplete`.
- Extracted and compiled `local_llm_result_synthesis_runner.py`; reasoning-backed quality row without reasoning-budget audit -> exit 1 `hold_for_missing_or_incomplete_evidence`.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4951 files, 3080 Markdown files, 915 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | Local LLM first runtime health runner

Scope: add a repeatable no-generation runtime health runner so the first local LLM endpoint path can prove listener reachability, native API state, installed/running/OpenAI-compatible model ids, expected-model visibility, loopback boundary, missing layer, and next route before the first prompt.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/Local LLM First Runtime Health Runner.md`
- `LLM/Study/Local LLM First Runtime Health Snapshot.md`
- `LLM/Study/Local LLM First Model Pull Runner.md`
- `LLM/Study/Local LLM First Smoke Request Runner.md`
- `LLM/Study/Local LLM First Endpoint Run Sheet.md`
- `LLM/Study/Local LLM First Endpoint Evidence Audit Runner.md`
- `LLM/Study/Local LLM First Inference Evidence Pack.md`
- `LLM/Study/Local LLM Serving Runbook.md`
- `LLM/Study/Local LLM Command Cookbook.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added a standard-library runtime health runner that performs no generation request and emits JSON, Markdown, CSV, and JSONL evidence for listener, native route, `/api/tags`, `/api/ps`, `/v1/models`, expected model, and boundary checks.
- Routed the first model pull pass path into the runtime health runner before smoke requests.
- Added `local-runtime-health` to the mastery evidence audit default gate set.
- Updated the endpoint evidence audit runtime-health gate to discover runner output saved under a run-id folder.
- Routed the runner from the LLM MOC, study index, dashboard, capstone workbook, roadmap, evidence pack, endpoint sheet, serving runbook, command cookbook, and hands-on practicum sequence.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_llm_first_runtime_health_runner.py` from the note.
- Runtime health fixtures: pass -> `runtime_health_ready`; hold -> `runtime_health_incomplete`; fail -> `runtime_health_failed`.
- Extracted and compiled `llm_mastery_evidence_audit_runner.py`; default manifest -> 40 gates, 40 holds, including `local-runtime-health`.
- Extracted and compiled `local_llm_first_endpoint_evidence_audit_runner.py`; runtime-health gate globs include `*/*runtime-health*.json`.
- Extracted and compiled `local_llm_first_model_pull_runner.py`; pass fixture routes to `LLM/Study/Local LLM First Runtime Health Runner` when `next_route` is supplied.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4958 files, 3087 Markdown files, 922 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | Bind first smoke request to runtime health proof

Scope: tighten the first local inference request so smoke output is bound to saved runtime-health evidence, and make the first smoke request plus first-response debrief explicit mastery gates before endpoint or quality claims.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/Local LLM First Smoke Request Runner.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Updated the standard-library first smoke request runner to read `LOCAL_LLM_RUNTIME_HEALTH_JSON`, require runtime-health proof by default, record runtime-health path/status/decision/model visibility, and skip both prompt routes when health proof is missing or mismatched.
- Added `local-first-smoke-request` and `local-first-response-debrief` to the mastery evidence audit default gate set.
- Updated the dashboard, capstone workbook, roadmap, LLM MOC, and study index so the first controlled prompt is explicitly tied to runtime-health JSON and first-response debrief evidence.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_llm_first_smoke_request_runner.py` from the note.
- Smoke runner fixtures: fake local server plus valid health proof -> `pass`; missing health proof -> `hold` with both routes skipped; mismatched health proof -> `hold` with both routes skipped.
- Extracted and compiled `llm_mastery_evidence_audit_runner.py`; default manifest -> 42 gates, 42 holds, including `local-first-smoke-request` and `local-first-response-debrief`.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4958 files, 3087 Markdown files, 922 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | Bind response debrief to health-bound smoke proof

Scope: tighten the first local response debrief so it only passes when the saved smoke summary carries runtime-health-ready provenance from before the first prompt.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/Local LLM First Response Debrief Runner.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Study Index.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added `LOCAL_LLM_REQUIRE_HEALTH_BOUND_SMOKE` to the first-response debrief runner.
- Carried runtime-health path, status, decision, expected model, model visibility, and block reason into debrief JSON and Markdown output.
- Routed missing or mismatched runtime-health provenance to the runtime health runner and smoke request runner instead of allowing a debrief pass.
- Updated the mastery audit gate, dashboard, capstone workbook, LLM MOC, and study index to name health-bound smoke provenance as part of the response-debrief evidence.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `first_response_debrief.py` and `llm_mastery_evidence_audit.py` from their notes.
- First-response debrief fixtures: health-bound smoke summary -> `pass`; missing runtime-health proof -> `hold` with `runtime health proof`; mismatched runtime-health proof -> `hold`; explicit `LOCAL_LLM_REQUIRE_HEALTH_BOUND_SMOKE=false` control -> `pass`.
- Mastery evidence audit default manifest -> `hold`, 42 gates, 42 holds, with `local-first-response-debrief` requiring health-bound smoke provenance.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4958 files, 3087 Markdown files, 922 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | Bind template compatibility to first-response debrief

Scope: tighten the chat-template/tokenizer compatibility runner so template, route, stop, benchmark, and quality claims are attached to a health-bound first-response debrief.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/Chat Template and Tokenizer Compatibility Runner.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Study Index.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added required `upstream_first_response_debrief` evidence to the chat-template/tokenizer compatibility runner.
- Made the runner parse linked first-response debrief JSON and hold if the debrief is not `pass`, runtime health is not `runtime_health_ready`, the model id disagrees with the compatibility manifest, or the native response path is missing.
- Updated the runner output routing so failed/held evidence rows point to the owning note instead of JSON artifacts.
- Updated the mastery audit gate, dashboard, capstone workbook, LLM MOC, and study index to name health-bound first-response debrief evidence before template/tokenizer compatibility can support quality or deployment decisions.
- Checked current Ollama API, chat, OpenAI-compatible, and Modelfile references on 2026-06-15.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `chat_template_tokenizer_compatibility_runner.py` from the note.
- Compatibility fixtures: full manifest with health-bound debrief -> `pass` with 9 rows; missing upstream debrief -> `hold`; held debrief -> `hold`; non-ready runtime health -> `hold`; debrief/manifest model mismatch -> `hold`.
- Mastery evidence audit default manifest -> `hold`, 42 gates, 42 holds, with `local-template-tokenizer-compatibility` requiring health-bound first-response debrief evidence.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4958 files, 3087 Markdown files, 922 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | Require template compatibility in endpoint audit

Scope: tighten the first endpoint evidence audit so a local endpoint cannot count unless the health-bound response debrief and template/tokenizer compatibility packet both pass.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/Local LLM First Endpoint Evidence Audit Runner.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Study Index.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Changed the first endpoint evidence audit runner so `first-response-debrief` must report `pass`; a held debrief no longer satisfies endpoint proof.
- Added required `template-tokenizer-compatibility` evidence to the endpoint audit default gate set.
- Routed the new gate to [[LLM/Study/Chat Template and Tokenizer Compatibility Runner]] and required compatibility JSON to report `pass`.
- Updated the mastery audit gate, dashboard, capstone workbook, LLM MOC, and study index to name pass-state debrief plus template/tokenizer compatibility as endpoint evidence.
- Checked current Ollama API, generate, chat, and OpenAI-compatible references on 2026-06-15.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `first_endpoint_evidence_audit.py` from the note.
- Endpoint audit fixtures: complete run -> `pass` with 12 gates, 11 pass, 1 optional skip; missing template compatibility -> `hold`; held debrief -> `hold`; failed template compatibility -> `fail`.
- Mastery evidence audit default manifest -> `hold`, 42 gates, 42 holds, with `local-first-endpoint-evidence-audit` requiring template/tokenizer compatibility evidence.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4958 files, 3087 Markdown files, 922 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-15] curate | Gate first quality probes on endpoint evidence

Scope: tighten the first quality probe runner so it cannot send quality-probe requests unless the first endpoint evidence audit has already passed.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/Local LLM First Quality Probe Runner.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Study Index.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added `LOCAL_LLM_ENDPOINT_AUDIT_JSON` and `LOCAL_LLM_REQUIRE_ENDPOINT_AUDIT` to the first quality probe runner.
- Made the runner find or read the first endpoint evidence audit JSON and require `status == pass` before sending probe requests.
- Added hold-output behavior for missing or held endpoint evidence so the runner writes results JSON/CSV/Markdown and JSONL without sending endpoint requests.
- Updated the dashboard, capstone workbook, LLM MOC, and study index so first quality probes are explicitly endpoint-audit-bound.
- Checked current Ollama chat/structured-output docs and OpenAI evaluation docs on 2026-06-15.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `first_quality_probe_runner.py` from the note.
- Fixture server checks: missing endpoint audit -> `hold` with zero requests; held endpoint audit -> `hold` with zero requests; passing endpoint audit -> five probe requests, five responses, five outputs, and `pass`; explicit endpoint-audit opt-out -> `pass` with `endpoint_audit.status == skipped`.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4958 files, 3087 Markdown files, 922 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-16] curate | Add first inference evidence pack audit

Scope: make the first local inference packet auditable as a whole before it can count as mastery or capstone evidence.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Evidence Audit Runner.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM First Inference Evidence Pack.md`
- `LLM/Study/Local LLM First Inference Evidence Pack Audit Runner.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner]] as the full first-run packet gate after endpoint evidence, API contract, client harness, benchmark row, quality probe, security/privacy row, and final decision artifacts exist.
- Made [[LLM/Study/Local LLM First Inference Evidence Pack]] distinguish endpoint audit from full packet audit.
- Updated the LLM MOC, study index, mastery dashboard, practicum sequence, capstone workbook, and mastery evidence audit runner so the first local run cannot be promoted on endpoint response alone.
- Added `local-first-inference-pack-audit` to the mastery evidence audit default gates.
- Checked current Ollama chat, usage metrics, OpenAI-compatible docs, and OpenAI streaming docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `first_inference_evidence_pack_audit.py` from the note.
- Fixture checks: complete packet -> `pass` / `first_inference_pack_ready`; missing quality probe -> `hold`; streaming required but absent -> `hold`; failed security artifact -> `fail`; explicitly native-scoped packet -> `pass` with incompatible gates skipped.
- Extracted and compiled `llm_mastery_evidence_audit_runner.py`; default fixture manifest -> `hold`, 43 gates, 43 holds, including `local-first-inference-pack-audit`.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4959 files, 3088 Markdown files, 923 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-16] curate | Add first-run command plan runner

Scope: add a pre-execution planner that generates and audits the first local LLM PowerShell command sequence before install, model pull, runtime health, smoke, and evidence-packet audit commands are run.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Command Cookbook.md`
- `LLM/Study/Local LLM First Endpoint Run Sheet.md`
- `LLM/Study/Local LLM First Run Command Plan Runner.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `LLM/Study/Local LLM Windows First-Run Quickstart.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM First Run Command Plan Runner]] with a standard-library Python runner that writes command-plan JSON, Markdown, PowerShell, CSV, and JSONL outputs without installing, pulling, or sending inference requests.
- The runner validates run root, runtime, model id, runtime boundary, storage decision, install scope, pull scope, and loopback-only API bases before marking the plan ready.
- Routed the dashboard, study index, LLM MOC, command cookbook, first-run quickstart, endpoint run sheet, practicum sequence, and capstone workbook through the command-plan step before first execution.
- Checked current Ollama Windows, download, quickstart, CLI, tags, chat, generate, and OpenAI-compatible docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `first_run_command_plan.py` from the note.
- Fixture checks: complete manifest -> `pass` / `first_run_command_plan_ready` with 15 planned steps; missing model id -> `hold`; wildcard native URL -> `fail`; native-only scope -> `pass` with OpenAI-compatible smoke step omitted.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4960 files, 3089 Markdown files, 924 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-16] curate | Add first model source recheck runner

Scope: make the first local model choice source-verifiable before the command plan, model pull gate, or endpoint run sheet can depend on a mutable registry tag.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM First Model Candidate Ladder.md`
- `LLM/Study/Local LLM First Model Pull Gate.md`
- `LLM/Study/Local LLM First Model Pull Runner.md`
- `LLM/Study/Local LLM First Model Source Recheck Runner.md`
- `LLM/Study/Local LLM First Run Command Plan Runner.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM First Model Source Recheck Runner]] with a standard-library Python runner that fetches model pages and checks expected tag, digest, size, context, modality, parameter, license, and quantization snippets before any pull.
- Updated [[LLM/Study/Local LLM First Model Candidate Ladder]] and [[LLM/Study/Local LLM First Model Pull Gate]] with 2026-06-16 source facts for `qwen3.5:4b`, `qwen3.5:2b-q4_K_M`, `qwen3:4b-instruct`, `qwen3.5:9b`, and `qwen3:8b`.
- Updated [[LLM/Study/Local LLM First Run Command Plan Runner]] so generated plans now include a source-recheck manifest before the model pull step and hold when the source page or source check date is missing.
- Routed the LLM MOC, study index, mastery dashboard, and capstone workbook through the source-recheck step before first model pull.
- Checked current Ollama qwen3.5/qwen3 model pages and tags plus Ollama show/tags API docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `first_model_source_recheck.py` and `first_run_command_plan.py` from their notes.
- Source-recheck fixture checks: complete source page -> `pass`; missing expected snippet -> `fail`; missing source check date -> `hold`; optional contradicted stretch candidate -> overall `pass` because required candidates passed.
- Command-plan fixture checks: complete manifest -> `pass` with 16 planned steps including `06-plan-model-source-recheck`; missing source page -> `hold`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4961 files, 3090 Markdown files, 925 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.

## [2026-06-16] curate | Add Windows runtime install runner

Scope: turn the manual Windows Ollama install gate into a repeatable no-generation runner before source recheck, model pull, runtime health, and endpoint smoke evidence.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM First Endpoint Run Sheet.md`
- `LLM/Study/Local LLM First Run Command Plan Runner.md`
- `LLM/Study/Local LLM Windows First-Run Quickstart.md`
- `LLM/Study/Local LLM Windows Runtime Install Gate.md`
- `LLM/Study/Local LLM Windows Runtime Install Runner.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Windows Runtime Install Runner]] with a standard-library Python runner that writes install-readiness JSON, Markdown, CSV, and JSONL outputs without installing, pulling, or sending inference.
- The runner audits official installer source, install method, `ollama` command path, `ollama --version`, `ollama ls`, `OLLAMA_MODELS` process/user inheritance, loopback listener state, `/api/version`, and `/api/tags`.
- Updated [[LLM/Study/Local LLM First Run Command Plan Runner]] so generated first-run plans now include `windows-runtime-install-manifest.json` and a `07-plan-runtime-install-runner` step.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, Windows quickstart, endpoint run sheet, and manual install gate through the install runner before first model pull.
- Checked current Ollama Windows, download, CLI, API introduction, authentication, `/api/version`, and `/api/tags` docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `windows_runtime_install_runner.py` from the note.
- Runtime-install fixture checks: complete installed runtime -> `pass` / `windows_runtime_install_ready`; missing command/listener -> `hold`; non-official source and wildcard listener -> `fail`.
- Extracted and compiled `first_run_command_plan.py`; complete manifest -> `pass` with 17 planned steps including `07-plan-runtime-install-runner`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4962 files, 3091 Markdown files, 926 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Harden first model pull upstream proof

Scope: make the first model pull runner reject unaudited pulls by requiring upstream source-recheck and runtime-install runner outputs before runtime health or endpoint smoke.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM First Model Pull Gate.md`
- `LLM/Study/Local LLM First Model Pull Runner.md`
- `LLM/Study/Local LLM First Run Command Plan Runner.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Updated [[LLM/Study/Local LLM First Model Pull Runner]] so `source_recheck_output` and `runtime_install_runner_output` are required JSON inputs and must report pass before a model pull can be accepted.
- The pull runner now writes upstream-proof rows alongside pull-artifact rows and distinguishes missing upstream proof, held upstream proof, and failed upstream proof.
- Updated [[LLM/Study/Local LLM First Run Command Plan Runner]] so generated plans write pull-gate filenames, capture `/api/show`, and generate `first-model-pull-manifest.json` before runtime health.
- Updated [[LLM/Study/Local LLM First Model Pull Gate]], the LLM MOC, and the study index to reflect the stricter upstream-proof contract.
- Checked current Ollama CLI, `/api/tags`, `/api/show`, and `/api/ps` docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_llm_first_model_pull_runner.py` from the note.
- Model-pull runner fixture checks: complete upstream proof -> `pass` / `first_model_pull_ready`; missing install-runner output -> `hold`; failed install-runner output -> `fail`.
- Extracted and compiled `first_run_command_plan.py`; complete manifest -> `pass` with 19 planned steps including `10b-capture-model-show` and `10c-plan-first-model-pull-runner`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4962 files, 3091 Markdown files, 926 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Add head-aware KV-cache sizing runner

Scope: connect academic attention-cache geometry to local hosting decisions by adding a reusable runner for MHA/MQA/GQA cache memory before hardware sizing, model selection, long-context, or concurrency evidence depends on cache fit.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/2024-2025 - Frontier and Efficiency/KV Cache and Context Reuse.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Math and Tensor Shape Primer.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `LLM/Study/Local LLM Hardware Sizing Runner.md`
- `LLM/Study/Local LLM KV Cache Sizing Runner.md`
- `LLM/Study/Local LLM Model Selection Runner.md`
- `LLM/Study/Local LLM Model and Hardware Sizing Guide.md`
- `LLM/Study/Local LLM Workload to Model Selection Playbook.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM KV Cache Sizing Runner]] with a standard-library Python runner that writes JSON, Markdown, CSV, and JSONL cache-fit evidence.
- The runner estimates cache memory from layers, hidden size, `num_attention_heads`, `num_key_value_heads`, context tokens, active sequences, and cache dtype, or accepts measured `kv_cache_gb`.
- The runner distinguishes MHA, MQA, GQA, measured, and invalid geometry, and holds when `num_key_value_heads`, source proof, cache budget, or quantized-cache proof is missing.
- Updated the sizing guide, math primer, KV-cache concept page, workload playbook, model-selection runner, hardware-sizing runner, study index, mastery dashboard, capstone workbook, practicum sequence, and LLM MOC so cache-fit proof is routed before long-context, concurrency, model-selection, or hardware-fit claims.
- Checked current Hugging Face Transformers cache docs, Hugging Face Llama config docs, and vLLM PagedAttention/prefix-cache docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_llm_kv_cache_sizing_runner.py` from the note.
- KV-cache runner fixture checks: GQA fit -> `pass` / `kv_cache_sizing_ready` with 0.5 GiB estimate; missing `num_key_value_heads` -> `hold`; over-budget cache -> `fail`; quantized cache without proof -> `hold`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4963 files, 3092 Markdown files, 927 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Add local model metadata card runner

Scope: make saved model metadata a first-class evidence gate before custody, compatibility, tokenizer, context, or KV-cache runners consume architecture and tokenizer facts.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Artifact Custody Audit Runner.md`
- `LLM/Study/Local LLM Artifact Download Cache and Conversion Lab.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `LLM/Study/Local LLM KV Cache Sizing Runner.md`
- `LLM/Study/Local LLM Model Acquisition and Provenance Checklist.md`
- `LLM/Study/Local LLM Model Metadata Card Runner.md`
- `LLM/Study/Local LLM Model and Hardware Sizing Guide.md`
- `LLM/Study/Local LLM Runtime Compatibility Runner.md`
- `LLM/Study/Local LLM Runtime and Model Compatibility Matrix.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Model Metadata Card Runner]] with a standard-library Python runner that audits saved `config.json`, tokenizer config, special tokens, generation config, Ollama `/api/show`, and file-inventory artifacts without downloading, querying, or running inference.
- The runner writes JSON, Markdown, CSV, and JSONL metadata-card outputs with normalized architecture, tokenizer/template, Ollama package, inventory, and downstream handoff fields.
- The runner holds on missing downstream metadata, such as absent `num_key_value_heads` before KV-cache sizing, and fails on contradictory attention geometry or blocked unsafe-file decisions.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, practicum sequence, acquisition checklist, artifact lab, custody audit, runtime compatibility, compatibility matrix, sizing guide, and KV-cache runner through the metadata-card gate.
- Checked current Hugging Face Hub download, Hugging Face Transformers configuration, Ollama `/api/show`, Ollama Modelfile, and Ollama context-length docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_llm_model_metadata_card_runner.py` from the note.
- Metadata-card fixture checks: complete Hugging Face-style metadata -> `pass` / `model_metadata_ready`; missing `num_key_value_heads` -> `hold` / `metadata_incomplete`; `num_key_value_heads` greater than `num_attention_heads` -> `fail` / `metadata_conflict`; Ollama show-only metadata -> `hold` / `metadata_incomplete`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4964 files, 3093 Markdown files, 928 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Add llama.cpp GGUF server evidence runner

Scope: give the local-hosting path a dedicated proof gate for GGUF models served through `llama-server` or `llama-cpp-python` before OpenAI-compatible client, benchmark, runtime-comparison, or deployment evidence depends on that endpoint.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Command Cookbook.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `LLM/Study/Local LLM Hosting and Inference Lab.md`
- `LLM/Study/Local LLM Runtime Comparison Lab.md`
- `LLM/Study/Local llama.cpp GGUF Server Runner.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local llama.cpp GGUF Server Runner]] with a standard-library Python runner that audits saved llama.cpp endpoint evidence without building, starting a server, downloading, or sending live inference.
- The runner validates launch command, GGUF path, alias, loopback boundary, listener proof, `/health`, `/v1/models`, `/v1/chat/completions`, optional `/props`, optional `/metrics`, GPU/offload proof, and upstream metadata/compatibility/KV-cache cards.
- Updated the LLM MOC, study index, command cookbook, hosting lab, practicum sequence, mastery dashboard, capstone workbook, and runtime comparison lab so llama.cpp GGUF server proof sits before generic API contract, client, benchmark, or runtime-comparison claims.
- Checked current llama.cpp server README, llama.cpp README server section, llama.cpp build docs, and llama-cpp-python OpenAI-compatible server docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_llama_cpp_gguf_server_runner.py` from the note.
- llama.cpp runner fixture checks: complete loopback GGUF proof -> `pass` / `llama_cpp_server_ready`; non-loopback without approval -> `fail` / `llama_cpp_server_blocked`; `/health` loading -> `hold` / `llama_cpp_server_incomplete`; model id mismatch -> `fail` / `llama_cpp_server_blocked`; missing chat response -> `hold` / `llama_cpp_server_incomplete`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4965 files, 3094 Markdown files, 929 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Add Open WebUI provider integration runner

Scope: close the UI/provider evidence gap so Open WebUI transcripts only support local-LLM app, lifecycle, security, or capstone claims after the UI identity, provider route, expected model, storage, secrets, and boundary are proven.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Application Integration Evidence Runner.md`
- `LLM/Study/Local LLM Capstone Project Blueprint.md`
- `LLM/Study/Local LLM Docker GPU Container Serving Lab.md`
- `LLM/Study/Local LLM Security and Privacy Runner.md`
- `LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook.md`
- `LLM/Study/Local Open WebUI Provider Integration Runner.md`
- `_ops/reports/audit-broken-links.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local Open WebUI Provider Integration Runner]] with a standard-library Python runner that audits saved Open WebUI evidence without starting a UI, clicking a browser, or sending live inference.
- The runner checks UI install identity, loopback exposure, provider base URL classification, endpoint/security proof handoffs, model visibility, harmless transcript text, persistent data path, `WEBUI_SECRET_KEY` proof, redacted config/log artifacts, export boundary, and optional app/lifecycle proof.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, Docker GPU serving lab, app integration runner, security/privacy runner, lifecycle runbook, and capstone blueprint through the Open WebUI provider gate.
- Checked current Open WebUI docs, quick start, OpenAI-compatible provider setup, environment configuration, hardening, FAQ, and upstream README on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_open_webui_provider_integration_runner.py` from the note.
- Open WebUI runner fixture checks: complete loopback UI/provider proof -> `pass` / `open_webui_provider_ready`; non-loopback UI bind without approval -> `fail` / `open_webui_provider_blocked`; missing `WEBUI_SECRET_KEY` proof -> `hold` / `open_webui_provider_incomplete`; expected model absent from model visibility -> `fail`; transcript missing expected harmless text -> `hold`; raw secret-like value in config/log artifact -> `fail`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4966 files, 3095 Markdown files, 930 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Add RAG prompt-injection source-boundary runner

Scope: make RAG prompt-injection and source-trust proof repeatable before retrieved untrusted content supports app, tool, export, security, result-synthesis, or capstone claims.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Capstone Project Blueprint.md`
- `LLM/Study/Local LLM Security and Privacy Runner.md`
- `LLM/Study/Local RAG Assistant Lab.md`
- `LLM/Study/Local RAG Evidence Runner.md`
- `LLM/Study/Local RAG Minimal Python Harness.md`
- `LLM/Study/Local RAG Prompt Injection and Source Boundary Runner.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local RAG Prompt Injection and Source Boundary Runner]] with a standard-library Python runner that audits saved adversarial RAG artifacts without calling a model, embedding text, or crawling files.
- The runner checks attack cases, selected/retrieved poisoned chunks, context delimiters, untrusted-context tags, answer/refusal behavior, forbidden strings, poisoned citations, tool-call escalation, export boundary, guardrail/logging evidence, and linked RAG/security proof.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, RAG assistant lab, minimal RAG harness, RAG evidence runner, security/privacy runner, and capstone blueprint through the new source-boundary gate.
- Checked current OWASP LLM01 prompt injection, OWASP LLM08 vector/embedding weaknesses, OWASP prompt-injection cheat sheet, NCSC prompt-injection guidance, Greshake et al. indirect prompt injection, PoisonedRAG, and NIST AI RMF Generative AI Profile sources on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, dirty older LLM edits, or the dirty live security runbook.

Verification:
- Extracted and compiled `local_rag_prompt_injection_source_boundary_runner.py` from the note.
- RAG injection runner fixture checks: clean poisoned-context case -> `pass` / `rag_injection_boundary_ready`; missing delimiter -> `fail` / `rag_injection_boundary_blocked`; forbidden injected phrase in answer -> `fail`; required refusal not marked -> `fail`; poisoned chunk not retrieved/selected -> `hold` / `rag_injection_boundary_incomplete`; missing high-risk guardrail -> `hold`; disallowed tool call -> `fail`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4967 files, 3096 Markdown files, 931 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Add model acquisition license gate runner

Scope: make model source, license, gated access, artifact pinning, and unsafe-file posture auditable before any local download, serving, benchmark, or deployment evidence depends on a candidate model.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Artifact Custody Audit Runner.md`
- `LLM/Study/Local LLM Artifact Download Cache and Conversion Lab.md`
- `LLM/Study/Local LLM Model Acquisition and License Gate Runner.md`
- `LLM/Study/Local LLM Model Acquisition and Provenance Checklist.md`
- `LLM/Study/Local LLM Model Metadata Card Runner.md`
- `LLM/Study/Local LLM Runtime Compatibility Runner.md`
- `LLM/Study/Local LLM Workload to Model Selection Playbook.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Model Acquisition and License Gate Runner]] with a standard-library Python runner that audits a saved candidate manifest without scraping registries, downloading model files, or giving legal advice.
- The runner checks model-card review, intended-use fit, license scope flags, gated-access status, exact revision/tag/file, safe or unsafe artifact format, `trust_remote_code`, malware/pickle scan status, source proof artifacts, and open-source AI claim basis.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, acquisition checklist, artifact download lab, custody audit, metadata-card runner, workload playbook, and runtime compatibility runner through the new acquisition/license gate.
- Checked current Hugging Face model-card, gated-model, malware-scan, pickle-scan, Safetensors, SPDX license-list, and Open Source AI Definition sources on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty older LLM edits.

Verification:
- Extracted and compiled `local_llm_model_acquisition_license_gate_runner.py` from the note.
- Model-acquisition fixture checks: clean proof -> `pass` / `acquisition_ready`; commercial use blocked by license -> `fail` / `acquisition_blocked`; gated pending -> `hold` / `acquisition_incomplete`; gated denied -> `fail`; floating `HEAD` revision -> `fail`; unsafe `.bin` file without review -> `fail`; infected scan -> `fail`; open-source AI claim with only open-weights evidence -> `hold`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4968 files, 3097 Markdown files, 932 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Add adaptation readiness runner

Scope: make the prompt/RAG/SFT/LoRA/QLoRA/DPO/distillation/continued-pretraining/no-train decision auditable before training, adapter serving, result synthesis, deployment, or capstone evidence depends on it.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide.md`
- `LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner.md`
- `LLM/Study/LLM Deployment Readiness Audit Runner.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Result Synthesis Runner.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/LLM Adaptation and Fine-Tuning Readiness Runner]] with a standard-library Python runner that audits a saved adaptation manifest without training a model, inspecting private data, or calling a provider.
- The runner checks baseline failure, selected method, rejected alternatives, dataset format, train/validation/held-out split, preference-pair shape for DPO, leakage and duplicate checks, privacy egress, chat-template proof, LoRA/QLoRA/DPO/distillation config, held-out eval, deployment target, retention, and rollback.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, mastery roadmap, adaptation guide, result-synthesis runner, and deployment-readiness runner through the new adaptation readiness gate.
- Checked current Hugging Face TRL SFTTrainer, DPOTrainer, TRL dataset-format, PEFT LoRA, Transformers chat-template docs, plus LoRA, QLoRA, and DPO papers on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, dirty older LLM edits, or dirty live local-inference notes.

Verification:
- Extracted and compiled `llm_adaptation_fine_tuning_readiness_runner.py` from the note.
- Adaptation runner fixture checks: complete LoRA plan -> `pass` / `adaptation_ready`; training when baseline already passes -> `fail` / `adaptation_blocked`; DPO with prompt-completion data instead of preference pairs -> `fail`; train/held-out overlap -> `fail`; missing held-out eval -> `hold` / `adaptation_incomplete`; private data egress without approval -> `fail`; QLoRA without quantized-base or memory plan -> `hold`; no-train decision without reason -> `hold`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4969 files, 3098 Markdown files, 933 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Add quantization offload evidence runner

Scope: make GGUF/AWQ/GPTQ/FP8/INT8, GPU-offload, CPU fallback, KV-cache precision, benchmark, quality, and rejected-alternative decisions auditable before result synthesis or deployment evidence depends on a local quantized baseline.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Deployment Readiness Audit Runner.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner.md`
- `LLM/Study/Local LLM Quantization and GPU Offload Lab.md`
- `LLM/Study/Local LLM Result Synthesis Runner.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Quantization and GPU Offload Evidence Runner]] with a standard-library Python runner that audits a saved manifest without downloading models, benchmarking endpoints, scraping model pages, or deciding current runtime support from memory.
- The runner checks baseline scope, artifact/runtime support, memory estimate, load state, offload sweep, KV-cache/context row, benchmark, quality regression, decision card, rejected candidate, selected-candidate fields, peak-memory budget, and proof links.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, mastery roadmap, quantization/offload lab, result-synthesis runner, and deployment-readiness runner through the new keep/reject gate.
- Checked current vLLM quantization, SGLang quantization, llama.cpp server, Ollama context-length/FAQ, LM Studio load/per-model, Hugging Face Hub GGUF, and Transformers GGUF docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, dirty older LLM edits, or dirty live local-inference notes.

Verification:
- Extracted and compiled `local_llm_quantization_offload_evidence_runner.py` from the note.
- Quantization/offload fixture checks: complete Q4 with Q8 baseline -> `pass` / `quantization_offload_ready`; one candidate without baseline blocker -> `hold` / `quantization_offload_incomplete`; selected candidate quality fail while kept -> `fail` / `quantization_offload_blocked`; peak VRAM over budget -> `fail`; missing offload sweep -> `hold`; critical unsupported quantization -> `fail`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4970 files, 3099 Markdown files, 934 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Add benchmark evidence audit runner

Scope: make local LLM benchmark rows auditable before timing, throughput, memory, runtime, quantization, context, prompt-cache, speculative-decoding, result-synthesis, or deployment decisions depend on them.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Deployment Readiness Audit Runner.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Benchmark Evidence Audit Runner.md`
- `LLM/Study/Local LLM First Benchmark Row Builder.md`
- `LLM/Study/Local LLM Inference Metrics Field Guide.md`
- `LLM/Study/Local LLM Result Synthesis Runner.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Benchmark Evidence Audit Runner]] with a standard-library Python runner that audits saved benchmark rows and proof links without benchmarking a live endpoint.
- The runner checks workload contract, run identity, source artifacts, prompt/token accounting, timing metrics, memory/context metrics, fixed settings, quality boundary, and interpretation/next-action evidence.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, mastery roadmap, first benchmark-row builder, metrics guide, result-synthesis runner, and deployment-readiness runner through the new audit gate.
- Checked current Ollama usage metrics, vLLM benchmark CLI, SGLang benchmark/profiling, NVIDIA NIM LLM benchmarking metrics, and NVIDIA GenAI-Perf docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, dirty older LLM edits, or dirty live local-inference notes.

Verification:
- Extracted and compiled `local_llm_benchmark_evidence_audit_runner.py` from the note.
- Benchmark evidence fixture checks: complete warm single-run -> `pass` / `benchmark_evidence_ready`; missing token accounting -> `hold` / `benchmark_evidence_incomplete`; quality fail while decision keeps -> `fail` / `benchmark_evidence_blocked`; TTFT greater than total latency -> `fail`; comparison with two changed variables -> `hold`; missing proof path -> `hold`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4971 files, 3100 Markdown files, 935 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Add runtime comparison runner

Scope: make Ollama, LM Studio, llama.cpp, vLLM, SGLang, Docker/WSL, or UI-over-provider runtime choices auditable before result synthesis or deployment evidence depends on a winner.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Deployment Decision Matrix.md`
- `LLM/Study/LLM Deployment Readiness Audit Runner.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Benchmark Evidence Audit Runner.md`
- `LLM/Study/Local LLM Result Synthesis Runner.md`
- `LLM/Study/Local LLM Runtime Comparison Lab.md`
- `LLM/Study/Local LLM Runtime Comparison Runner.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Runtime Comparison Runner]] with a standard-library Python runner that audits saved runtime-comparison manifests without starting servers or benchmarking live endpoints.
- The runner checks workload contract, candidate identity, endpoint proof, frozen controls, benchmark audit, quality boundary, security boundary, selected runtime, rejected alternative, and decision-card review trigger.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, mastery roadmap, runtime-comparison lab, benchmark-evidence audit, result-synthesis runner, deployment decision matrix, and deployment-readiness runner through the new runtime-comparison audit gate.
- Checked current Ollama OpenAI compatibility, LM Studio OpenAI-compatible endpoints, llama.cpp server, vLLM OpenAI-compatible server, and SGLang OpenAI-compatible completions docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, dirty older LLM edits, or dirty live local-inference notes.

Verification:
- Extracted and compiled `local_llm_runtime_comparison_runner.py` from the note.
- Runtime comparison fixture checks: complete exact two-runtime comparison -> `pass` / `runtime_comparison_ready`; one runtime only -> `hold` / `runtime_comparison_incomplete`; closest-equivalent comparison without approximation reason -> `hold`; selected runtime quality fail -> `fail` / `runtime_comparison_blocked`; exposed `0.0.0.0` endpoint without approval -> `fail`; candidate prompt suites differ -> `fail`; missing benchmark audit proof -> `hold`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4972 files, 3101 Markdown files, 936 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.

## [2026-06-16] curate | Add capacity SLO planning runner

Scope: make local LLM service-level claims auditable before measured benchmark, concurrency, observability, security, and runtime-comparison evidence feeds result synthesis or deployment readiness.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Deployment Decision Matrix.md`
- `LLM/Study/LLM Deployment Readiness Audit Runner.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Capacity and SLO Planning Runner.md`
- `LLM/Study/Local LLM Concurrency and Batch Throughput Runner.md`
- `LLM/Study/Local LLM Observability and Operations Runner.md`
- `LLM/Study/Local LLM Result Synthesis Runner.md`
- `LLM/Study/Local LLM Runtime Comparison Runner.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Capacity and SLO Planning Runner]] with a standard-library Python runner that audits a saved capacity/SLO manifest without starting a server, loading a model, scraping metrics, or generating traffic.
- The runner checks workload SLO, selected serving path, demand model, measured capacity, resource headroom, admission/backpressure, quality boundary, security boundary, operations evidence, cost/owner, and retest trigger.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, mastery roadmap, concurrency runner, observability runner, runtime-comparison runner, result-synthesis runner, deployment decision matrix, and deployment-readiness runner through the new capacity/SLO gate.
- Checked current vLLM production/design metrics, SGLang production metrics, llama.cpp server metrics/slots, NVIDIA NIM LLM benchmarking metrics, NVIDIA GenAI-Perf, Ollama usage metrics, and LM Studio local server docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, dirty older LLM edits, or dirty live local-inference notes.

Verification:
- Extracted and compiled `local_llm_capacity_slo_planning_runner.py` from the note.
- Capacity/SLO fixture checks: complete exact SLO -> `pass` / `capacity_slo_ready`; missing latency target -> `hold` / `capacity_slo_incomplete`; selected p95 latency over target -> `fail` / `capacity_slo_blocked`; error rate above budget -> `fail`; exposed service without security proof -> `fail`; missing capacity proof -> `hold`; shared SLO missing backpressure -> `hold`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4973 files, 3102 Markdown files, 937 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.
- `rg` over `_ops/reports/audit-broken-links.md` found no false broken-link hits for the new runner or embedded code strings.

## [2026-06-16] curate | Add queueing and tail latency field guide

Scope: add the theory bridge between raw local LLM benchmark numbers and service behavior under load, so arrival rate, service time, p95/p99 latency, queue wait, prefill/decode, KV-cache pressure, batching, and admission control are explainable before SLO or deployment claims.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Deployment Decision Matrix.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Capacity and SLO Planning Runner.md`
- `LLM/Study/Local LLM Concurrency and Batch Throughput Runner.md`
- `LLM/Study/Local LLM Queueing and Tail Latency Field Guide.md`
- `LLM/Study/Local LLM Serving Internals and Scheduler Lab.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Queueing and Tail Latency Field Guide]] with a standard-library worksheet that audits saved demand, tail-latency, admission-policy, and proof-link rows without calling a model.
- The guide teaches the queueing mental model for local LLM hosting: arrival rate, service time, effective parallelism, utilization warning, queue wait, p95/p99 latency, prefill, decode, KV-cache pressure, batching, and overload behavior.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, mastery roadmap, serving-internals lab, concurrency runner, capacity/SLO runner, and deployment decision matrix through the new theory-to-operations bridge.
- Checked current Orca, PagedAttention, Sarathi-Serve, vLLM optimization/metrics, SGLang metrics, and llama.cpp server docs on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, dirty older LLM edits, or dirty live local-inference notes.

Verification:
- Extracted and compiled `local_llm_queueing_tail_latency_worksheet.py` from the note.
- Queueing/tail-latency fixture checks: complete worksheet -> `pass` / `tail_latency_ready`; missing arrival rate -> `hold` / `tail_latency_incomplete`; utilization over 0.8 -> `hold`; utilization at or above 1.0 -> `fail` / `tail_latency_blocked`; p95 over target -> `fail`; error rate over budget -> `fail`; missing queue limit -> `hold`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4974 files, 3103 Markdown files, 938 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.
- `rg` over `_ops/reports/audit-broken-links.md` found no false broken-link hits for the new guide or embedded worksheet strings.

## [2026-06-16] curate | Add serving systems paper-to-local proof map

Scope: add the academic-to-applied bridge for serving-systems papers so FlashAttention, Orca, PagedAttention/vLLM, Sarathi-Serve, SGLang/RadixAttention, and runtime metrics claims can be defended with local scheduler, KV-cache, queueing, prefix-cache, observability, and deployment proof.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM 20-Paper Fast Path Synthesis Map.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mechanism-to-Inference Bridge Map.md`
- `LLM/Study/LLM Paper Claim Ledger.md`
- `LLM/Study/LLM Serving Systems Paper-to-Local Proof Map.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Queueing and Tail Latency Field Guide.md`
- `LLM/Study/Local LLM Serving Internals and Scheduler Lab.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/LLM Serving Systems Paper-to-Local Proof Map]] with a read order, systems-claim matrix, local proof routing table, oral-defense prompts, and proof-card template.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, mastery roadmap, 20-paper map, paper claim ledger, mechanism bridge, queueing guide, and serving-internals lab through the new paper-to-local systems bridge.
- Added a serving-systems addendum to [[LLM/Study/LLM Paper Claim Ledger]] for Orca, PagedAttention/vLLM, Sarathi-Serve, and SGLang/RadixAttention.
- Checked current FlashAttention, Orca, PagedAttention/vLLM, Sarathi-Serve, vLLM optimization/metrics, SGLang paper/docs/metrics sources on 2026-06-16.
- Did not modify unrelated active-vault Japanese, CS, recipe, dirty older LLM edits, or dirty live local-inference notes.

Verification:
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4975 files, 3104 Markdown files, 939 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.
- `rg` over `_ops/reports/audit-broken-links.md` found no false broken-link hits for the new note, serving-systems title, FlashAttention, Orca, PagedAttention, Sarathi, SGLang, or RadixAttention terms.

## [2026-06-16] curate | Add local LLM first-run readiness runner

Scope: add a no-install runner that refreshes local machine evidence before the first local LLM installer, model pull, or smoke request.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM First Run Readiness Runner.md`
- `LLM/Study/Local LLM First Run Readiness Snapshot.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `LLM/Study/Local LLM Model Store Readiness Snapshot.md`
- `LLM/Study/Local LLM Windows First-Run Quickstart.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM First Run Readiness Runner]] with a standard-library Python runner that checks command availability, environment variables, model-store paths, disk space, common local LLM listener ports, and NVIDIA GPU visibility before any install or model pull.
- The runner writes JSON, CSV, Markdown, and JSONL evidence files, then classifies the machine as `pass` / `ready_for_first_runtime_step`, `hold` / `readiness_incomplete`, or `fail` / `readiness_blocked`.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, mastery roadmap, first-run snapshot, model-store snapshot, Windows quickstart, and hands-on practicum through the new readiness refresh step.
- No new current external-source claims were added in this pass; the note is an internal machine-state evidence procedure.
- Did not modify unrelated active-vault Japanese, CS, recipe, dirty older LLM edits, or dirty live local-inference notes.

Verification:
- Extracted `local_llm_first_run_readiness_runner.py` from the note and ran `python -m py_compile`: clean.
- Runner self-test: 4 cases passed.
- Live no-install scan from a temporary manifest returned `exit_code=2`, `hold` / `readiness_incomplete`, with expected holds for missing `D:\Models` directories and unset custom cache variables; GPU proof saw `NVIDIA GeForce RTX 3080 Ti`, 12288 MiB VRAM, driver 610.47, with no common local LLM listener active.
- `git diff --check`: clean before final index/audit rerun.

## [2026-06-16] curate | Add local LLM model-store bootstrap runner

Scope: add the controlled bridge between first-run readiness holds and the Windows runtime install gate: dry-run or apply the run folder, model-store directories, and user cache variables before any model pull.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM First Run Command Plan Runner.md`
- `LLM/Study/Local LLM First Run Readiness Runner.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `LLM/Study/Local LLM Model Store Bootstrap Runner.md`
- `LLM/Study/Local LLM Model Store Readiness Snapshot.md`
- `LLM/Study/Local LLM Windows First-Run Quickstart.md`
- `LLM/Study/Local LLM Windows Model Store and Cache Plan.md`
- `LLM/Study/Local LLM Windows Runtime Install Gate.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Model Store Bootstrap Runner]] with a standard-library Python runner that writes JSON, CSV, Markdown, and JSONL evidence for model-store directory creation plans and user cache-variable actions.
- The runner defaults to dry-run mode and requires both `--apply` and `confirm_apply=create-model-store-and-user-env` before changing directories or user-level environment variables.
- Routed the LLM MOC, study index, mastery dashboard, capstone workbook, mastery roadmap, first-run readiness runner, command-plan runner, model-store snapshot/plan, runtime install gate, Windows quickstart, and hands-on practicum through the new bootstrap step.
- Updated [[LLM/Study/Local LLM First Run Command Plan Runner]] so custom storage manifests generate a model-store bootstrap manifest instead of only a commented manual `setx` review step.
- No new current external-source claims were added in this pass; the note is an internal machine-state evidence procedure.
- Did not modify unrelated active-vault Japanese, CS, recipe, dirty older LLM edits, or dirty live local-inference notes.

Verification:
- Extracted and compiled `local_llm_model_store_bootstrap_runner.py` and `first_run_command_plan_runner.py` from their notes.
- Bootstrap runner self-test: 4 cases passed.
- Real-target dry run against `D:\Models` returned `exit_code=2`, `hold` / `bootstrap_pending`, with 9 planned actions and `D:\Models` still absent afterward.
- Temporary-path `--apply` run with `set_user_env=false` returned `pass` / `bootstrap_ready_for_new_shell_check` and created only temp run/model directories.
- Command-plan fixture returned `pass` / `first_run_command_plan_ready`, planned 20 steps, and the generated Markdown/PowerShell included `05b-plan-model-store-bootstrap`.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4977 files, 3106 Markdown files, 941 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.
- `rg` over `_ops/reports/audit-broken-links.md` found no false broken-link hits for the new note or embedded bootstrap runner decision strings.

## [2026-06-16] curate | Add LLM mastery status snapshot

Scope: add a current, human-facing proof-state card that says exactly what is known, what is still unproven, and what to run next before claiming LLM mastery or local-inference readiness.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/LLM Mastery Status Snapshot - 2026-06-16.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/LLM Mastery Status Snapshot - 2026-06-16]] with a verified hold/not-started/pass map for academic proof, mechanism understanding, model-store setup, runtime install, model pull, smoke request, benchmark, quality, and operations evidence.
- Captured fresh local machine evidence from PowerShell: `ollama`, `lms`, and `hf` are not on PATH; no listeners are active on common local LLM ports; `D:\Models` and `C:\Users\fpan1\Documents\local-llm-runs` are absent; NVIDIA tooling sees `NVIDIA GeForce RTX 3080 Ti`, 12288 MiB VRAM, driver 610.47; `C:` has 347.1 GB free and `D:` has 582.2 GB free.
- Routed the snapshot through the LLM MOC, study index, mastery dashboard, capstone workbook, and mastery roadmap so Obsidian has a single current status card.
- No new current external-source claims were added in this pass; all machine claims come from the fresh local shell evidence.
- Did not modify unrelated active-vault Japanese, CS, recipe, dirty older LLM edits, or dirty live local-inference notes.

Verification:
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: 4978 files, 3107 Markdown files, 942 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 939 broken-link occurrences.
- Targeted `rg` over `_ops/reports/audit-broken-links.md` found no broken-link hits for the new snapshot title or local-inference status terms.

## [2026-06-16] curate | Prove first local Ollama inference

Scope: turn the local LLM track from setup-only notes into a proved first inference on this Windows machine, while keeping the mastery status honest about remaining academic, quality, security, and capstone work.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Roadmap.md`
- `LLM/Study/LLM Mastery Status Snapshot - 2026-06-16.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM First Inference Proof - 2026-06-16.md`
- `LLM/Study/Local LLM First Model Candidate Ladder.md`
- `LLM/Study/Local LLM First Model Pull Gate.md`
- `LLM/Study/Local LLM First Model Source Recheck Runner.md`
- `LLM/Study/Local LLM Hands-On Practicum Sequence.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Applied the model-store bootstrap path for `D:\Models`, `D:\Models\ollama`, `D:\Models\hf`, `D:\Models\hf\hub`, and `D:\Models\gguf`, with user environment variables for `OLLAMA_MODELS`, `HF_HOME`, and `HF_HUB_CACHE`.
- Installed and proved Ollama on Windows, including installer hash/signature evidence, CLI path evidence, listener evidence, `/api/version`, and `/api/tags`.
- Source-checked, pulled, and audited `qwen3.5:2b-q4_K_M` after the older 4B candidate snippets drifted.
- Proved both native `/api/generate` and OpenAI-compatible `/v1/chat/completions` loopback inference with the response text `local llm ok`.
- Added [[LLM/Study/Local LLM First Inference Proof - 2026-06-16]] and routed it through the LLM MOC, study index, mastery dashboard, roadmap, hands-on practicum, model ladder, pull gate, source recheck runner, status snapshot, and capstone workbook.
- Updated the status/dashboard/capstone notes to mark the first local endpoint, runtime install, model pull, runtime health, smoke request, and response debrief as passed, while keeping quality, security/privacy, endpoint audit, evidence-pack audit, academic no-notes defense, and capstone gates held.
- Adjusted the first-model candidate/source notes so the selected fallback model is the current proved path and stale optional 4B snippets do not block the selected source check.
- Did not modify unrelated active-vault Japanese, CS, recipe, or non-LLM dirty files.

Verification:
- Bootstrap dry-run returned `hold` / `bootstrap_pending`; bootstrap apply returned `pass` / `bootstrap_ready_for_new_shell_check`.
- Post-bootstrap readiness returned `pass` / `ready_for_first_runtime_step`.
- Ollama installer script hash was recorded, Authenticode signer was `Ollama Inc.`, and runtime install returned `pass` / `windows_runtime_install_ready` with Ollama `0.30.8`.
- Selected model source recheck returned `pass` / `first_model_source_rechecked` for `qwen3.5:2b-q4_K_M`.
- First model pull runner returned `pass` / `first_model_pull_ready`; runtime metadata showed digest `124a03c347777e8e4e5955c33610ae01d9d90d8c2a718bfba069c498d5c7f3c9`, size 1.9 GB, parameter size 2.3B, quantization `Q4_K_M`, context length 262144, and capabilities `vision`, `completion`, `tools`, `thinking`.
- Runtime health returned `pass` / `runtime_health_ready`, with the model visible through native and OpenAI-compatible model-list APIs.
- Native smoke with `think=false` returned `local llm ok`; OpenAI-compatible smoke with a larger completion cap returned `local llm ok`.
- First response debrief returned `pass`, with model match `true`, text match `true`, cold-load owner, total time 0.691 seconds, load time 0.405 seconds, prompt throughput 161.09 tokens/s, and decode throughput 31.51 tokens/s.
- Current official Ollama Windows, download, CLI, generate, thinking, and OpenAI-compatibility docs were checked before making current runtime claims.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: regenerated `_ops/reports/audit-summary.json`.
- Targeted `rg` over `_ops/reports/audit-broken-links.md` found no broken-link hits for the new first-inference proof note, selected model id, or evidence folder names.

## [2026-06-16] curate | Audit first local endpoint and run first quality probe

Scope: promote the first Ollama endpoint from route proof to audited endpoint proof, then run the first private quality probe without mistaking a smoke response for model quality.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Status Snapshot - 2026-06-16.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16.md`
- `LLM/Study/Local LLM First Inference Proof - 2026-06-16.md`
- `LLM/Study/Local LLM First Quality Probe Runner.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16]] with evidence paths for chat/template/tokenizer compatibility, endpoint evidence audit, the initial held quality run, and the `think=false` quality rerun.
- Extracted and compiled the compatibility, endpoint-audit, and quality-probe runners from the vault notes into `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference`.
- Added run-folder support artifacts `run-card.md`, `decision.md`, `first-smoke-summary-pass.json`, `ollama-native-response.json`, and `openai-compatible-chat.json` so the default endpoint audit globs can find the already-saved first smoke evidence.
- Ran chat/template/tokenizer controls against `/api/chat`, including route sentinel output, JSON boundary output, role-marker leak check, and five tokenizer sanity prompt-eval counts.
- Updated [[LLM/Study/Local LLM First Quality Probe Runner]] so it records `LOCAL_LLM_THINK`, sends `think` in `/api/chat` requests, and includes the `think` column in JSON/CSV outputs.
- Routed the result through the LLM MOC, study index, mastery dashboard, status snapshot, capstone workbook, and first-inference proof note.
- Did not modify unrelated active-vault Japanese, CS, recipe, or non-LLM dirty files.

Verification:
- `python -m py_compile chat_template_tokenizer_compatibility_runner.py first-endpoint-evidence-audit.py first-quality-probe-runner.py`: clean before runner execution.
- Ollama health check returned version `0.30.8` and visible model `qwen3.5:2b-q4_K_M`.
- Chat/template/tokenizer compatibility runner returned `pass` / `chat_template_compatibility_ready`, 9 rows, 9 pass, 0 hold, 0 fail.
- First endpoint evidence audit initially held on default glob mismatches, then passed after root-level evidence aliases: `pass` / `first_endpoint_evidence_ready`, 12 gates, 11 pass, 0 hold, 0 fail, 0 critical gaps.
- First quality probe without thinking control held 0/5 because responses spent the output cap in `message.thinking` and emitted empty final content.
- First quality probe with `LOCAL_LLM_THINK=false` returned `hold`, 5 cases, 3 pass, 2 hold, 0 error; JSON, extraction, and grounded refusal passed; arithmetic and strict constraint following held.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: regenerated `_ops/reports/audit-summary.json`.
- Targeted `rg` over `_ops/reports/audit-broken-links.md` found no broken-link hits for the new endpoint-audit/quality note, selected evidence paths, or quality-run id.

## [2026-06-16] curate | Prove loopback security boundary for first local endpoint

Scope: prove the current Ollama endpoint's local security/privacy boundary without sending another generation request, then route the result through the LLM wiki.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Status Snapshot - 2026-06-16.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16.md`
- `LLM/Study/Local LLM First Inference Proof - 2026-06-16.md`
- `LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16]] with result, manifest, boundary-policy, listener, environment, and rerun explanation evidence paths.
- Extracted and compiled the security/privacy runner into `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference`.
- Wrote a security/privacy manifest for the current Ollama loopback endpoint, expected model `qwen3.5:2b-q4_K_M`, local-only export boundary, and empty RAG/tool/UI roots.
- Ran the first security pass, diagnosed the self-scan hold caused by the runner source containing secret-detection regex examples, replaced that log input with a runner script proof file, and reran to pass.
- Routed the pass through the LLM MOC, study index, mastery dashboard, status snapshot, capstone workbook, first endpoint audit note, and first inference proof note.
- Did not modify unrelated active-vault Japanese, CS, recipe, or non-LLM dirty files.

Verification:
- `python -m py_compile security-privacy-runner.py`: clean.
- Ollama health check returned version `0.30.8` and visible model `qwen3.5:2b-q4_K_M`.
- Security/privacy runner returned `pass` / `loopback_private_ready`; `/v1/models`, `/api/tags`, and `/api/ps` returned HTTP 200; expected model was visible; endpoint hosts were classified as loopback; scoped config/log secret scan had no findings.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: regenerated `_ops/reports/audit-summary.json`.
- Targeted `rg` over `_ops/reports/audit-broken-links.md` found no broken-link hits for the new security proof note, result id, manifest, or model id.

## [2026-06-16] curate | Diagnose held local LLM quality probes

Scope: run a focused remediation pass for the two held first-quality probes before promoting the first local endpoint toward capstone evidence.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Status Snapshot - 2026-06-16.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM First Endpoint Audit and Quality Probe - 2026-06-16.md`
- `LLM/Study/Local LLM First Inference Proof - 2026-06-16.md`
- `LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16.md`
- `LLM/Study/Local LLM Security and Privacy Proof - 2026-06-16.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16]] with the focused remediation result, interpretation, and next tool/model/structured-output routes.
- Created and compiled `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\quality-remediation-runner.py`.
- Ran eight focused variants over `K-01` and `C-01` while keeping runtime, model, route, boundary, temperature, and thinking mode fixed.
- Routed the held remediation result through the LLM MOC, study index, mastery dashboard, status snapshot, capstone workbook, first endpoint audit note, first inference proof note, and security proof note.
- Did not modify unrelated active-vault Japanese, CS, recipe, or non-LLM dirty files.

Verification:
- `python -m py_compile quality-remediation-runner.py`: clean.
- Ollama health check returned version `0.30.8` and visible model `qwen3.5:2b-q4_K_M`.
- Quality remediation runner returned `hold`, 1 pass, 7 hold, 0 error; output-cap changes did not clear `K-01` or `C-01`, prompt hardening did not clear `K-01`, and `C-01` passed only when the exact target template was supplied.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: regenerated `_ops/reports/audit-summary.json`.
- Targeted `rg` over `_ops/reports/audit-broken-links.md` found no broken-link hits for the new quality remediation note, result id, result path, or held probe ids.

## [2026-06-16] curate | Prove calculator tool remediation for held arithmetic probe

Scope: remediate the held `K-01` arithmetic probe with a deterministic local calculator tool loop before making any broader local-model quality claim.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Status Snapshot - 2026-06-16.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16.md`
- `LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16]] with native calculator tool-loop evidence for the previously held `K-01` arithmetic prompt.
- Created and compiled `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\calculator-tool-remediation-runner.py`.
- Ran the calculator tool remediation runner against `http://127.0.0.1:11434/api/chat` with `qwen3.5:2b-q4_K_M`, loopback boundary, `think=false`, and temperature `0`.
- Routed the proof through the LLM MOC, study index, mastery dashboard, status snapshot, capstone workbook, and the prior quality remediation note.
- Kept the remaining quality boundary explicit: `K-01` has a native calculator tool route, but `C-01`, broader quality, request lifecycle, evidence-pack audit, and academic defense remain incomplete.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty LLM files outside this routed slice.

Verification:
- `python -m py_compile calculator-tool-remediation-runner.py`: clean.
- Calculator remediation runner returned `pass` / `pass/native_tool_loop_remediation_ready`, 4 pass rows, 1 diagnostic hold, native tool-call status `pass`, native tool-result follow-up status `pass`, direct ad hoc finalizer status `hold`, accepted path `native_tool_loop`.
- Native tool-result follow-up returned `answer=410; reason=The calculation of 17 multiplied by 23 plus 19 results in 410.`
- Bad expression denial blocked `__import__('os').system('whoami')` before execution.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: regenerated `_ops/reports/audit-summary.json`.
- Targeted `rg` over `_ops/reports/audit-broken-links.md` found no broken-link hits for the calculator proof note, run id, runner path, or evidence paths.

## [2026-06-16] curate | Prove structured-format remediation for held constraint probe

Scope: remediate the held `C-01` strict-format probe with explicit structured IDs and deterministic application rendering before making any broader local-model quality claim.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Status Snapshot - 2026-06-16.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM Calculator Tool Remediation Proof - 2026-06-16.md`
- `LLM/Study/Local LLM Quality Remediation Probe - 2026-06-16.md`
- `LLM/Study/Local LLM Structured Format Remediation Proof - 2026-06-16.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Structured Format Remediation Proof - 2026-06-16]] with structured-output and deterministic-renderer evidence for the previously held `C-01` strict-format prompt.
- Created and compiled `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\structured-format-remediation-runner.py`.
- Ran the structured-format remediation runner against `http://127.0.0.1:11434/api/chat` with `qwen3.5:2b-q4_K_M`, loopback boundary, `think=false`, and temperature `0`.
- Routed the proof through the LLM MOC, study index, mastery dashboard, status snapshot, capstone workbook, prior quality remediation note, and calculator remediation note.
- Kept the remaining quality boundary explicit: `K-01` is tool-owned, `C-01` is renderer-owned, and a full quality/evidence-pack audit still needs to reconcile model-owned, tool-owned, and renderer-owned rows.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty LLM files outside this routed slice.

Verification:
- `python -m py_compile structured-format-remediation-runner.py`: clean.
- Structured-format remediation runner returned `pass` / `pass/app_rendered_structured_format_ready`, 2 pass rows, 3 diagnostic holds, accepted path `schema_explicit_enum_claim_selection`.
- Original free-text control held with three long bullets.
- Free-form structured fields held with off-topic six-word strings.
- Loose enum selection held because the model invented `RouteClaim_01` and `QualityClaim_02`.
- Explicit enum selection plus deterministic rendering passed with `- Route proof verifies endpoint reachability` and `- Quality proof verifies useful behavior`.
- Bad-shape denial blocked an unexpected `extra` field before rendering.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: regenerated `_ops/reports/audit-summary.json`.
- Targeted `rg` over `_ops/reports/audit-broken-links.md` and `_ops/reports/audit-placeholder-hits.md` found no hits for the structured-format proof note, run id, runner path, or evidence paths.

## [2026-06-16] curate | Prove first local request lifecycle

Scope: map the saved first local Ollama request and response across the full request lifecycle before using it as capstone evidence.

Changed wiki/source files:
- `LLM/LLM.md`
- `LLM/Study/LLM Inference Request Lifecycle Lab.md`
- `LLM/Study/LLM Inference Request Lifecycle Runner.md`
- `LLM/Study/LLM Mastery Capstone Workbook.md`
- `LLM/Study/LLM Mastery Dashboard.md`
- `LLM/Study/LLM Mastery Status Snapshot - 2026-06-16.md`
- `LLM/Study/LLM Study Index.md`
- `LLM/Study/Local LLM End-to-End Mental Model.md`
- `LLM/Study/Local LLM First Inference Proof - 2026-06-16.md`
- `LLM/Study/Local LLM Request Lifecycle Proof - 2026-06-16.md`
- `_ops/reports/audit-summary.json`
- `index.md`
- `log.md`

Maintenance changes:
- Added [[LLM/Study/Local LLM Request Lifecycle Proof - 2026-06-16]] with native first-smoke lifecycle evidence and OpenAI-compatible contrast evidence.
- Updated the lifecycle runner code block so native Ollama nested `options` values are surfaced as sampler evidence.
- Ran the lifecycle runner against the saved native `think=false` first-smoke request/response pair.
- Ran the lifecycle runner against the saved OpenAI-compatible first-smoke request/response pair as a contrast row.
- Routed the proof through the LLM MOC, study index, mastery dashboard, status snapshot, capstone workbook, first-inference proof, lifecycle lab, lifecycle runner, and end-to-end mental model.
- Kept the remaining boundary explicit: native lifecycle proof passed, OpenAI-compatible prefill timing is still missing, and quality/evidence-pack/operations/academic gates are still open.
- Did not modify unrelated active-vault Japanese, CS, recipe, or dirty LLM files outside this routed slice.

Verification:
- Native lifecycle runner returned `pass` / `lifecycle_trace_ready`, 8 phase rows, 0 findings.
- Native phase evidence includes sampler `temperature=0`, `num_predict=32`, `think=false`; `prompt_tokens=20`; `prefill_s=0.1242`; `output_tokens=5`; `decode_s=0.1587`; `decode_tokens_per_s=31.5113`; `finish_reason=stop`; exact output `local llm ok`.
- OpenAI-compatible contrast runner returned `hold` / `lifecycle_trace_partial` because prefill timing was missing while client request, prompt assembly, tokenization, decode token count, stop, and output parsing passed.
- `git diff --check`: clean.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: regenerated `_ops/reports/audit-summary.json`.
- Targeted `rg` over `_ops/reports/audit-broken-links.md` and `_ops/reports/audit-placeholder-hits.md` found no hits for the request lifecycle proof note, run ids, runner path, or evidence paths.
