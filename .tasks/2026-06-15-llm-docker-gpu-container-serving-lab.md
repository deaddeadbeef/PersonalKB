# 2026-06-15 LLM Docker GPU container serving lab

Scope: add a local LLM Docker/GPU container serving lab that bridges WSL CUDA proof into reproducible vLLM/SGLang container serving and Open WebUI provider wiring.

Deliverables:
- Add `LLM/Study/Local LLM Docker GPU Container Serving Lab.md`.
- Route it from the LLM MOC, study index, environment preflight, WSL CUDA setup lab, hosting lab, first inference evidence pack, serving runbook, observability, lifecycle, compatibility, comparison, deployment, roadmap, capstone, and exam notes.
- Leave live-dirty LLM security, troubleshooting, benchmark, and embedding/reranker notes untouched in this slice.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Verification:
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- Route search for the Docker GPU container serving lab.
