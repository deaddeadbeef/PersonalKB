---
status: done
topic: llm
created: 2026-06-25
---

# LLM Book Reading Spine Slice

## Goal

Make the LLM wiki readable like a coherent book by adding a curated narrative reading spine that orders the existing wiki articles into chapters, separates first-pass reading from labs/runners/evidence layers, and keeps the complete corpus index as the back-of-book index.

## Acceptance

- Add a book-mode reading page under `LLM/`.
- Link the main era articles and the practical local-hosting path in a deliberate chapter order.
- Explain how to read article notes, lab notes, runner notes, raw sources, chunks, and the complete corpus index.
- Add the book-mode page to the generated corpus index fast routes.
- Avoid editing dirty live-vault files such as `LLM/LLM.md`, `LLM/LLM — Learning Path.md`, and `LLM/Study/LLM Study Index.md`.
- Regenerate `LLM/LLM Corpus Index.md`, `index.md`, and `_ops/reports/audit-summary.json`.

## Completion Evidence

- Added [[LLM/LLM Book Reading Spine]] as a narrative book-mode reading order across the main wiki articles plus local LLM practicum and paper-defense routes.
- Updated `_ops/generate_llm_corpus_index.py` so [[LLM/LLM Corpus Index]] exposes `Book mode` as a fast route.
- Regenerated [[LLM/LLM Corpus Index]] with 582 expected LLM Markdown targets, 582 seen LLM targets, 0 missing, and 0 extra.
- Link check over [[LLM/LLM Book Reading Spine]] found 145 wikilinks and 0 missing targets.
- Targeted audit searches found no hits for the new book spine or generator in missing references, placeholder hits, broken links, missing up, missing confidence, stubs, or orphan reports.
