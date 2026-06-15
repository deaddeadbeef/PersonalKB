# LLM daily mastery session run sheet

## Intent

Add an Obsidian-visible artifact that makes one study session produce both academic recall evidence and applied local-inference progress.

## Scope

- Add `LLM/Study/LLM Daily Mastery Session Run Sheet.md`.
- Route it from LLM home, study index, dashboard, cadence, roadmap, and capstone workbook.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

## Verification

- `python _ops/personal_kb.py index`
- `python _ops/personal_kb.py audit`
- `git diff --check`
- JSON parse for `_ops/reports/audit-summary.json`
- route search for `LLM Daily Mastery Session Run Sheet`
