# 2026-06-15 LLM WSL CUDA vLLM SGLang setup lab

Scope: add a Windows-to-WSL GPU setup lab for production-style local LLM serving with vLLM and SGLang.

Deliverables:
- Add `LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab.md`.
- Route it from the LLM MOC, study index, serving runbook, environment preflight, compatibility matrix, runtime comparison, Windows quickstart, troubleshooting, observability, roadmap, capstone, exam, and deployment notes.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Verification:
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- Route search for the WSL CUDA/vLLM/SGLang setup lab.
