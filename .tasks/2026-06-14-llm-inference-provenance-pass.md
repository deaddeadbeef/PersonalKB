# LLM Inference Provenance Pass

## Goal

Strengthen the applied local-inference path by replacing placeholder evidence sections in core inference notes with existing source-backed chunks and raw/source references.

## Scope

- Work in the isolated `llm-inference-provenance-pass` worktree.
- Touch only the LLM wiki/study layer plus generated audit/index reports, task state, and `log.md`.
- Target the inference cluster used by the local LLM lab:
  - `KV Cache and Context Reuse`
  - `Batching and Continuous Batching`
  - `Serving Architectures and Throughput-Latency Trade-offs`
  - `Quantization`

## Verification Evidence

- Baseline: `python _ops/personal_kb.py audit`
- Baseline counts: 4779 files, 2908 Markdown files, 809 candidate articles, 20 stubs, 252 missing references, 79 placeholder hits, 938 broken-link occurrences.
- Final: `python _ops/personal_kb.py index`
- Final: `python _ops/personal_kb.py audit`
- Final counts: 4780 files, 2909 Markdown files, 809 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- Final: `git diff --check`
