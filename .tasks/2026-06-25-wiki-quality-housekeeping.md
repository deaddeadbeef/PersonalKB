---
status: done
created: 2026-06-25
scope: wiki-quality-housekeeping
---
# Add reader-facing wiki quality dashboard

## Goal

Answer whether the wiki corpus is good enough by separating reader-facing wiki health from raw, chunk, query, template, and operations-layer audit noise.

## Scope

- Add reader-facing quality metrics to `_ops/personal_kb.py audit`.
- Generate `PersonalKB Wiki Quality Dashboard.md`.
- Write focused reader-facing reports under `_ops/reports/`.
- Link the dashboard from `PersonalKB Book Reading Guide.md`.
- Avoid touching dirty live Obsidian article edits.

## Verification Plan

- `python _ops\generate_topic_reading_spines.py`
- `python _ops\personal_kb.py audit`
- `python _ops\personal_kb.py index`
- compile checks for changed Python scripts
- validate generated dashboard links and report files
- `git diff --check`

## Completion Evidence

- Added `PersonalKB Wiki Quality Dashboard.md`.
- Added reader-facing audit fields: `reader_placeholder_hits` and `reader_broken_link_occurrences`.
- Added `_ops/reports/wiki-quality-summary.json`, `_ops/reports/wiki-broken-links.md`, and `_ops/reports/wiki-placeholder-hits.md`.
- Linked the quality dashboard from `PersonalKB Book Reading Guide.md`.
- Fixed 13 `[[LLM Sources Index]]` links by routing them to `[[LLM/Sources/Sources Index|LLM Sources Index]]`.
- Latest dashboard verdict: readable with the book spines, not yet polished enough as a clean wiki.
- Latest reader-facing counts: 963 candidate articles, 374 broken links, 58 placeholder hits, 249 missing references, 247 missing confidence, 28 missing up, 20 stubs, 1 empty note, 0 orphans.
