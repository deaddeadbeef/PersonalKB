---
status: done
topic: llm
created: 2026-06-25
---

# LLM Complete Corpus Index Slice

## Goal

Make the LLM wiki corpus consumable by adding a complete index page that links every Markdown note under `LLM/`, grouped by reading/navigation layer rather than relying on scattered era and study pages.

## Acceptance

- Add a reusable generator for the complete LLM corpus index.
- Generate `LLM/LLM Corpus Index.md` with all LLM Markdown notes linked.
- Include fast routes for the main reading path, study path, local hosting path, and source/evidence path.
- Avoid touching dirty live-vault navigation files such as `LLM/LLM.md` and `LLM/Study/LLM Study Index.md`.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

## Completion Evidence

- Added `_ops/generate_llm_corpus_index.py`.
- Generated [[LLM/LLM Corpus Index]] with 581 linked LLM Markdown notes.
- Verified expected `LLM/**/*.md` link targets against wikilinks in the generated page: expected 581, seen 581, missing 0, extra 0.
- Regenerated `index.md` and `_ops/reports/audit-summary.json`.
- Targeted audit searches found no hits for the new corpus index or generator in missing references, placeholder hits, broken links, missing up, missing confidence, stubs, or orphan reports.
