# 2026-06-15 - LLM service lifecycle and upgrade runbook

## Goal

Add a dedicated local LLM service lifecycle runbook for pinning runtime/model state, proving startup mode, backing up model/UI data, upgrading one layer at a time, rolling back safely, and validating a service after change.

## Scope

- Add `LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook.md`.
- Route the runbook through the LLM MOC, study index, hosting lab, serving runbook, observability runbook, benchmark log, troubleshooting tree, deployment matrix, mastery roadmap, capstone workbook, self-assessment exam, and serving architecture note.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

## Verification

- External docs checked: Ollama FAQ/Windows/API docs, LM Studio headless/llmster/TTL docs, Open WebUI update/backup/quick-start docs, and vLLM Docker deployment docs.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: `4854` files, `2983` Markdown files, `846` candidate articles, `20` stubs, `250` missing references, `79` placeholder hits, `938` broken-link occurrences.
