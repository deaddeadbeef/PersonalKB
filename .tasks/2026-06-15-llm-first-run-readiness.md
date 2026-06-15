# 2026-06-15 LLM first-run readiness

Scope: add a machine-specific readiness snapshot before the first local LLM endpoint run.

Deliverables:
- Add `LLM/Study/Local LLM First Run Readiness Snapshot.md`.
- Record current runtime, GPU, and listener evidence.
- Route it from the LLM MOC, study index, mastery dashboard, and capstone workbook.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Verification:
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- JSON validation for `_ops\reports\audit-summary.json`
- Route search for the snapshot and readiness evidence.
