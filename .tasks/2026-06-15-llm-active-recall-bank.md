# 2026-06-15 LLM active recall question bank

Scope: add a mixed active-recall bank that tests academic LLM mechanisms and applied local-inference skills together.

Deliverables:
- Add `LLM/Study/LLM Active Recall Question Bank.md`.
- Cover field map, math/attention, training/scaling, papers, evaluation, first endpoint, serving performance, model selection, RAG, tools, operations/security, and deployment prompts.
- Route it from the LLM MOC, study index, mastery roadmap, study cadence, and capstone workbook.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Verification:
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- JSON validation for `_ops/reports/audit-summary.json`
- Route search for the active recall bank and key cluster headings.
