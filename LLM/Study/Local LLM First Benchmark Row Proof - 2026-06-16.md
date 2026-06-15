---
tags: [study, llm, local-llm, inference, benchmark, latency, metrics, evidence, audit, proof]
up: "[[LLM/Study/LLM Mastery Dashboard]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-16
last-machine-check: 2026-06-16T07:35:35+08:00
---

# Local LLM First Benchmark Row Proof - 2026-06-16

> **One-line summary** The first-smoke OpenAI-compatible client/streaming evidence now has a normalized benchmark row and a passing benchmark evidence audit, scoped only to first-run interpretation rather than model comparison, capacity planning, or quality approval.

Use this after [[LLM/Study/Local LLM OpenAI-Compatible Streaming Timing Proof - 2026-06-16|Local LLM OpenAI-Compatible Streaming Timing Proof - 2026-06-16]]. That note proves the client and streaming route. This note proves that the raw timing and token evidence can be summarized into a reviewable row with explicit quality and capacity boundaries.

## Verdict

| Gate | Status | Evidence |
|---|---|---|
| Benchmark row builder | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-benchmark-row\20260616-072026-b4fd682f-benchmark-row.json` |
| Benchmark Markdown row | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-benchmark-row\20260616-072026-b4fd682f-benchmark-row.md` |
| Benchmark evidence audit | `pass/benchmark_evidence_ready` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\20260616-072026-b4fd682f-first-smoke-benchmark-audit-benchmark-evidence-audit.json` |
| Audit issue list | `pass`, 0 issues | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\20260616-072026-b4fd682f-first-smoke-benchmark-audit-benchmark-evidence-audit.md` |

## Benchmark Row

| Field | Value |
|---|---|
| Run id | `20260616-072026-b4fd682f` |
| Runtime and route | `local-openai-compatible` `/chat/completions` |
| Model | `qwen3.5:2b-q4_K_M` |
| Artifact | Ollama tag digest `124a03c347777e8e4e5955c33610ae01d9d90d8c2a718bfba069c498d5c7f3c9` |
| Quantization | `Q4_K_M` |
| Hardware boundary | Windows native / RTX 3080 Ti / loopback |
| Cold or warm | warm after prior local inference proof calls |
| Prompt id | `SMOKE-01` |
| Prompt class | route smoke |
| Prompt tokens | `28` |
| Output tokens | `265` |
| First event | `0.367s` |
| First visible content / client TTFT | `1.721s` |
| Total latency | `1.737s` |
| Client output tokens/sec | `152.562` |
| Native eval tokens/sec, separate native route | `31.511` |
| Quality decision | `hold`: route-smoke only; first quality probe held at 3/5; `K-01` is tool-owned; `C-01` is renderer-owned |
| Next controlled action | Use this as first-run interpretation only; run quality/evidence-pack audit before result synthesis or deployment. |

## Audit Coverage

| Required kind | Status |
|---|---|
| workload contract | `pass` |
| run identity | `pass` |
| source artifacts | `pass` |
| prompt/token accounting | `pass` |
| timing metrics | `pass` |
| memory/context metrics | `pass` with explicit non-exposure note |
| fixed settings | `pass` |
| quality boundary | `pass` |
| interpretation and next action | `pass` |

Peak RAM/VRAM, queue depth, and context margin were not captured during this first-smoke client/streaming row. The audit treats that as an explicit non-exposure note, not as capacity evidence.

## What This Proves

- The first OpenAI-compatible streaming run can be converted into a benchmark JSON row, Markdown copy row, and append-only JSONL row.
- The benchmark row resolves its proof paths for client log, streaming log, native timing contrast, benchmark JSON, and audit output.
- The row has route/model identity, prompt and output token counts, first-event timing, client TTFT, total latency, fixed sampler settings, quality boundary, and next action.
- The benchmark evidence audit found no blocking or hold issues for the scoped first-smoke interpretation row.

## What This Does Not Prove

- It does not prove the model is useful for real work; quality remains held until the model-owned, tool-owned, and renderer-owned rows are reconciled.
- It does not prove capacity, memory headroom, concurrency, p50/p95 latency, throughput under load, cache behavior, or service stability.
- It does not compare Ollama with LM Studio, llama.cpp, vLLM, SGLang, Docker, WSL, or another runtime.
- It does not promote the first inference evidence pack to capstone-ready; API contract, final decision, quality, and operations gates still need separate handling.

## Next Actions

1. Treat this as the current interpreted first-smoke benchmark row.
2. Do not use the row for model/runtime comparison or deployment decisions.
3. Use [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner|Local LLM First Inference Evidence Pack Audit Runner]] only after the remaining packet gates are scoped honestly.
4. Continue the applied track with quality reconciliation, first inference evidence-pack audit, lifecycle/observability, or deployment decision proof.

## References

Internal routes:

- [[LLM/Study/LLM Mastery Dashboard]]
- [[LLM/Study/LLM Mastery Status Snapshot - 2026-06-16]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible Streaming Timing Proof - 2026-06-16]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Benchmark Evidence Audit Runner]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM First Inference Evidence Pack Audit Runner]]

Evidence files:

- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-benchmark-row.py`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\local_llm_benchmark_evidence_audit_runner.py`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-benchmark-evidence-audit-manifest.json`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-benchmark-row\20260616-072026-b4fd682f-benchmark-row.json`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-benchmark-row\20260616-072026-b4fd682f-benchmark-row.md`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\20260616-072026-b4fd682f-first-smoke-benchmark-audit-benchmark-evidence-audit.json`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\20260616-072026-b4fd682f-first-smoke-benchmark-audit-benchmark-evidence-audit.md`
