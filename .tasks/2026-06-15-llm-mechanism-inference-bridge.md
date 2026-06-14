# 2026-06-15 LLM mechanism-to-inference bridge

Scope: add a study bridge that connects academic LLM mechanisms to local inference and hosting decisions.

Deliverables:
- Add `LLM/Study/LLM Mechanism-to-Inference Bridge Map.md`.
- Route it from the LLM MOC, study index, mastery roadmap, capstone workbook, and self-assessment exam.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Verification:
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- Route search for the bridge note and key section terms.
