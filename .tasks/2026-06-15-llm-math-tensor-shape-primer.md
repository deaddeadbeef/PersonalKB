# 2026-06-15 LLM math and tensor-shape primer

Scope: add a compact academic primer for the math and tensor shapes behind LLM training, attention, and inference.

Deliverables:
- Add `LLM/Study/LLM Math and Tensor Shape Primer.md`.
- Route it from the LLM MOC, study index, architecture cheatsheet, attention lab, tiny decoder lab, mastery roadmap, capstone workbook, and self-assessment exam.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Verification:
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- Route search for the primer note and key math/tensor terms.
