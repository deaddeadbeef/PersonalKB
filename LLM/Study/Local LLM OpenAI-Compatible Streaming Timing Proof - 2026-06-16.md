---
tags: [study, llm, local-llm, inference, streaming, latency, openai-compatible, ollama, evidence, proof]
up: "[[LLM/Study/LLM Mastery Dashboard]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [practice]
last-verified: 2026-06-16
last-machine-check: 2026-06-16T07:35:35+08:00
---

# Local LLM OpenAI-Compatible Streaming Timing Proof - 2026-06-16

> **One-line summary** The local Ollama OpenAI-compatible route now has saved client and streaming timing evidence: the non-streaming reusable client call passed, and the streaming call measured first event, first visible content, reasoning chunks, final text, usage, and completion.

Use this after [[LLM/Study/Local LLM Request Lifecycle Proof - 2026-06-16|Local LLM Request Lifecycle Proof - 2026-06-16]]. The lifecycle proof showed that the OpenAI-compatible response had token/output evidence but no native prefill timing. This note fills the client-observable timing gap. It does not replace native server-side prefill/decode timing from the Ollama native route.

Update: [[LLM/Study/Local LLM First Benchmark Row Proof - 2026-06-16|Local LLM First Benchmark Row Proof - 2026-06-16]] now converts this client/streaming evidence into a first-smoke benchmark row and a passing benchmark evidence audit for interpretation-only use.

## Verdict

| Gate | Status | Evidence |
|---|---|---|
| Non-streaming client harness | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-client-harness\client-runs.jsonl` |
| Streaming timing harness | `pass` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-streaming-timing\streaming-runs.jsonl` |
| Streaming events | `pass`, `224` events, `4` content chunks, `218` reasoning chunks | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-streaming-timing\events\20260616-072026-b4fd682f-SMOKE-01.jsonl` |
| Streamed output | `pass`, exact visible text `local llm ok` | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-streaming-timing\outputs\20260616-072026-b4fd682f-SMOKE-01.txt` |

## Fixed Conditions

| Field | Value |
|---|---|
| Runtime | Ollama OpenAI-compatible route |
| Base URL | `http://127.0.0.1:11434/v1` |
| Route | `/chat/completions` |
| Model | `qwen3.5:2b-q4_K_M` |
| Prompt id | `SMOKE-01` |
| Prompt | `Reply with exactly: local llm ok` |
| Temperature | `0` |
| Max tokens | `512` |
| Usage request | `stream_options.include_usage=true` for the streaming row |
| Boundary | loopback |

## Client Harness Row

| Field | Value |
|---|---|
| Run id | `20260616-071926-ab620b98` |
| Status | `pass` |
| Stream | `false` |
| Latency | `6.520s` |
| Finish reason | `stop` |
| Prompt tokens | `28` |
| Output tokens | `265` |
| Total tokens | `293` |
| Output | `local llm ok` |
| Request | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-client-harness\requests\20260616-071926-ab620b98-SMOKE-01.json` |
| Response | `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-client-harness\responses\20260616-071926-ab620b98-SMOKE-01.json` |

## Streaming Timing Row

| Field | Value |
|---|---|
| Run id | `20260616-072026-b4fd682f` |
| Status | `pass` |
| HTTP status | `200` |
| First SSE event | `0.367s` |
| First visible content / client TTFT | `1.721s` |
| Total latency | `1.737s` |
| Event count | `224` |
| Content chunk count | `4` |
| Reasoning chunk count | `218` |
| Tool-call chunk count | `0` |
| Done marker | `true` |
| Finish reason | `stop` |
| Prompt tokens | `28` |
| Output tokens | `265` |
| Total tokens | `293` |
| Output | `local llm ok` |

The event stream started with OpenAI-compatible chunks whose `delta.reasoning` field carried hidden-reasoning text, then ended with content chunks reconstructing `local llm ok`, a `finish_reason=stop` chunk, and a final usage-only chunk.

## What This Proves

- A reusable standard-library client can call the local OpenAI-compatible route and save request, response, output, latency, usage, and JSONL evidence.
- The OpenAI-compatible streaming route emits parseable server-sent events, a done marker, usage fields, and final visible content.
- Client-observable first event and first visible content timing now exist for the first-smoke OpenAI-compatible route.
- The streaming parser now counts both `delta.thinking` and `delta.reasoning` chunks as reasoning/thinking stream chunks, matching the observed Ollama event shape.

## What This Does Not Prove

- It does not provide native server-side prefill and decode durations for the OpenAI-compatible route. Use [[LLM/Study/Local LLM Request Lifecycle Proof - 2026-06-16|Local LLM Request Lifecycle Proof - 2026-06-16]] for native server phase timing.
- It does not prove stable benchmark performance; the non-streaming and streaming rows were not a controlled repeated benchmark.
- It does not prove workload quality; the prompt was a route-smoke prompt.
- It does not prove concurrency, long context, cache reuse, UI behavior, or operations readiness.

## Next Actions

1. Treat OpenAI-compatible client and streaming timing as evidenced for the first-smoke route.
2. Keep native timing and OpenAI-compatible timing separate in benchmark and evidence-pack audits: native has server prefill/decode fields, while OpenAI-compatible has client latency and stream timing.
3. Use [[LLM/Study/Local LLM First Benchmark Row Proof - 2026-06-16|Local LLM First Benchmark Row Proof - 2026-06-16]] as the current interpreted first-smoke benchmark row before any evidence-pack audit.
4. Continue toward operations with [[LLM/Study/Local LLM Observability and Operations Runner|Local LLM Observability and Operations Runner]] and lifecycle/rollback proof.

## References

Internal routes:

- [[LLM/Study/LLM Mastery Dashboard]]
- [[LLM/Study/LLM Mastery Status Snapshot - 2026-06-16]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/Local LLM First Inference Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Request Lifecycle Proof - 2026-06-16]]
- [[LLM/Study/Local LLM First Client Harness Runner]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Proof - 2026-06-16]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Benchmark Evidence Audit Runner]]

Evidence files:

- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-client-harness\client-runs.jsonl`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-streaming-timing\streaming-runs.jsonl`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-streaming-timing\events\20260616-072026-b4fd682f-SMOKE-01.jsonl`
- `C:\Users\fpan1\Documents\local-llm-runs\2026-06-16-first-local-inference\openai-compatible-client-streaming\first-streaming-timing\outputs\20260616-072026-b4fd682f-SMOKE-01.txt`
