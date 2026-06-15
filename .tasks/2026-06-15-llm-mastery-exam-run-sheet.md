# LLM mastery exam run sheet

## Intent

Add an Obsidian-visible artifact that turns the existing LLM self-assessment exam into scored evidence and remediation work.

## Scope

- Add `LLM/Study/LLM Mastery Exam Run Sheet.md`.
- Route it from the LLM home page, study index, dashboard, roadmap, self-assessment exam, active recall bank, and capstone workbook.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

## Verification

- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`
- JSON parse for `_ops/reports/audit-summary.json`
- route search for `LLM Mastery Exam Run Sheet`
