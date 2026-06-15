# LLM workload-to-model selection curation slice

Scope: add a durable local LLM model-selection playbook that bridges workload definition, academic evaluation, candidate choice, and local hosting evidence.

Deliverables:

- Add `LLM/Study/Local LLM Workload to Model Selection Playbook.md`.
- Route it from the LLM hub, study index, roadmap, capstone, exam, practicum sequence, sizing guide, and quality harness.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Constraints:

- Avoid editing live-dirty LLM files: `LLM/LLM — Learning Path.md`, `LLM/Study/Local LLM Inference Benchmark Log.md`, `LLM/Study/Local LLM Troubleshooting Decision Tree.md`, `LLM/Study/Local LLM Security and Privacy Runbook.md`, and `LLM/Study/Local Embedding and Reranker Hosting Lab.md`.
- Do not hard-code a current model-name shortlist; model availability and licenses drift. Use model-card verification fields instead.

Verification:

- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- `python -m json.tool _ops\reports\audit-summary.json`
