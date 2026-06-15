# 2026-06-15 LLM command cookbook

Scope: add a compact copyable command reference for local LLM serving and inference.

Deliverables:
- Add `LLM/Study/Local LLM Command Cookbook.md`.
- Cover Windows preflight, listener checks, Ollama native, OpenAI-compatible smoke tests, LM Studio, llama-cpp-python, WSL vLLM/SGLang, Docker host proof, Python clients, streaming, benchmark rows, teardown, diagnostics, and evidence destinations.
- Route it from the LLM MOC, study index, mastery roadmap, cadence, hands-on practicum, Windows quickstart, and serving runbook.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Verification:
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- JSON validation for `_ops/reports/audit-summary.json`
- Route search for command cookbook, Ollama, OpenAI-compatible, llama.cpp, vLLM, and SGLang phrases.
