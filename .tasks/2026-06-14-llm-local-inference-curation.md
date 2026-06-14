# LLM Local Inference Curation

## Goal

Make the LLM wiki useful for both academic understanding and hands-on local inference practice.

## Current Pass

- Work in the isolated `llm-local-inference-curation` worktree.
- Add a learner-facing local hosting and inference lab.
- Wire the lab into the LLM MOC, study index, learning path, and inference review drill.
- Use existing vault chunks for stable theory and checked official documentation for current tool behavior.
- Regenerate the vault index and audit reports.

## Verification Evidence

- Baseline: `python _ops/personal_kb.py audit`
- Baseline counts: 4777 files, 2906 Markdown files, 808 candidate articles, 21 stubs, 79 placeholder hits, 938 broken-link occurrences.
- Final: `python _ops/personal_kb.py index`
- Final: `python _ops/personal_kb.py audit`
- Final counts: 4779 files, 2908 Markdown files, 809 candidate articles, 20 stubs, 79 placeholder hits, 938 broken-link occurrences.
- Final: `git diff --check`
