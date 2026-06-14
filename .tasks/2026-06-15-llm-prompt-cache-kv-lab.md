# 2026-06-15 - LLM prompt cache and KV reuse lab

## Goal

Add a dedicated local LLM prompt-cache and KV-reuse lab so warm-model behavior, prefill timing, repeated-prefix reuse, prompt layout, cache evidence, and cache privacy are measured before claiming a local service is optimized.

## Scope

- Add `LLM/Study/Local LLM Prompt Cache and KV Reuse Lab.md`.
- Route the lab through the LLM MOC, study index, request lifecycle, context budgeting, runtime compatibility/comparison, concurrency, observability, lifecycle, benchmark log, troubleshooting tree, mastery roadmap, capstone workbook, self-assessment exam, deployment matrix, and related KV-cache/prompt-caching academic notes.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

## Verification

- External docs checked: vLLM Automatic Prefix Caching, vLLM prefix-caching design, llama.cpp server README, llama.cpp completion README, SGLang docs/server arguments/HiCache design, and Ollama generate endpoint.
- Regenerated `index.md` with `python _ops\personal_kb.py index`.
- Regenerated `_ops/reports/audit-summary.json` with `python _ops\personal_kb.py audit`.
- Audit result: 4,858 files, 2,987 markdown files, 848 candidate articles, 938 broken-link occurrences.
