# LLM runtime stack anatomy curation slice

Scope: add a unifying note that explains the local LLM runtime stack from hardware through client/UI, workload, and operations evidence.

Deliverables:

- Add `LLM/Study/Local LLM Runtime Stack Anatomy.md`.
- Route it from the main LLM study surfaces and adjacent local inference notes.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Constraints:

- Avoid editing live-dirty LLM files such as `LLM/LLM — Learning Path.md`, `Local LLM Inference Benchmark Log.md`, `Local LLM Troubleshooting Decision Tree.md`, `Local LLM Security and Privacy Runbook.md`, and `Local Embedding and Reranker Hosting Lab.md`.
- Keep the slice Obsidian-readable and evidence-oriented.

Verification:

- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- `python -m json.tool _ops\reports\audit-summary.json`
