# LLM local practicum sequence curation slice

Scope: add an ordered learner-facing sequence for local LLM hosting and inference practice.

Deliverables:

- Add `LLM/Study/Local LLM Hands-On Practicum Sequence.md`.
- Route it from core LLM study surfaces and adjacent local-inference notes.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Constraints:

- Avoid editing live-dirty LLM files: `LLM/LLM — Learning Path.md`, `Local LLM Inference Benchmark Log.md`, `Local LLM Troubleshooting Decision Tree.md`, `Local LLM Security and Privacy Runbook.md`, and `Local Embedding and Reranker Hosting Lab.md`.
- Keep the sequence practical, evidence-oriented, and Obsidian-readable.

Verification:

- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- `python -m json.tool _ops\reports\audit-summary.json`
