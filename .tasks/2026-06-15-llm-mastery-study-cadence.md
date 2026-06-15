# LLM mastery study cadence curation slice

Scope: add a learner-facing study cadence that turns the dense LLM roadmap into weekly academic and applied proof work.

Deliverables:

- Add `LLM/Study/LLM Mastery Study Cadence.md`.
- Route it from the LLM hub, study index, mastery roadmap, capstone workbook, and self-assessment exam.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Constraints:

- Avoid editing live-dirty LLM files: `LLM/LLM — Learning Path.md`, `LLM/Study/Local LLM Inference Benchmark Log.md`, `LLM/Study/Local LLM Troubleshooting Decision Tree.md`, `LLM/Study/Local LLM Security and Privacy Runbook.md`, and `LLM/Study/Local Embedding and Reranker Hosting Lab.md`.
- Keep the cadence evidence-first: each week must produce recall, mechanism bridge, applied artifact, and capstone link.

Verification:

- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- `python -m json.tool _ops\reports\audit-summary.json`
