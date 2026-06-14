# 2026-06-15 - LLM observability and operations runbook

## Goal

Add a dedicated local LLM observability runbook for proving model state, endpoint state, request timings, logs, server metrics, resource pressure, and next controlled actions.

## Scope

- Add `LLM/Study/Local LLM Observability and Operations Runbook.md`.
- Route the runbook through the LLM MOC, study index, hosting lab, serving runbook, benchmark log, troubleshooting tree, deployment matrix, mastery roadmap, capstone workbook, self-assessment exam, and serving academic notes.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

## Verification

- External docs checked: Ollama API/generate/ps, LM Studio server status/loaded models/log stream/server start, llama.cpp server slots/metrics, vLLM metrics, SGLang production metrics and benchmarking, and NVIDIA SMI documentation.
- `python _ops\personal_kb.py index`: regenerated `index.md`.
- `python _ops\personal_kb.py audit`: `4852` files, `2981` Markdown files, `845` candidate articles, `20` stubs, `250` missing references, `79` placeholder hits, `938` broken-link occurrences.
