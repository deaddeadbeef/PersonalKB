# 2026-06-15 LLM Windows local quickstart

Scope: add a Windows-first local LLM quickstart that turns the broader local-hosting runbooks into exact PowerShell steps.

Deliverables:
- Add `LLM/Study/Local LLM Windows First-Run Quickstart.md`.
- Route it from the LLM MOC, study index, hosting lab, serving runbook, first inference evidence pack, roadmap, capstone, and exam.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Verification:
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- Route search for the quickstart note and key Windows/Ollama/LM Studio phrases.
