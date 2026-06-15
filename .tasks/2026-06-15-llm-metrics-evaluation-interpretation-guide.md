# 2026-06-15 LLM metrics and evaluation interpretation guide

Scope: add an academic-to-applied guide for interpreting LLM loss, perplexity, benchmark scores, preference scores, calibration, quality rubrics, and local serving metrics.

Deliverables:
- Add `LLM/Study/LLM Metrics and Evaluation Interpretation Guide.md`.
- Route it from the LLM MOC, study index, math primer, training pipeline, paper protocol, mechanism bridge, quality harness, roadmap, capstone, and exam.
- Avoid editing live-dirty `LLM/Study/Local LLM Inference Benchmark Log.md` in this slice.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

Verification:
- `python _ops\personal_kb.py index`
- `python _ops\personal_kb.py audit`
- `git diff --check`
- Route search for the metrics/evaluation guide.
