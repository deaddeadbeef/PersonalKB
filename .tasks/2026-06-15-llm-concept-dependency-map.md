# 2026-06-15 LLM concept dependency map

Scope: add a subject-wide dependency map that ties academic LLM concepts to applied local inference, RAG, tool, evaluation, operations, and deployment proof.

Deliverables:
- Add `LLM/Study/LLM Concept Dependency Map.md`.
- Route it from the LLM MOC, study index, mastery roadmap, capstone workbook, and study cadence.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Verification:
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- JSON validation for `_ops/reports/audit-summary.json`
- Route search for the concept dependency map and key dependency sections.
