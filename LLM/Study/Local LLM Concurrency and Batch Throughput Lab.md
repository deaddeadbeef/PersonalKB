---
tags: [study, llm, inference, local-llm, concurrency, batching, throughput, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Concurrency and Batch Throughput Lab

> **One-line summary** A local LLM server is not ready for shared use or batch work until concurrency, queueing, TTFT, TPOT, throughput, memory headroom, and failure behavior are measured under controlled load.

Use this after [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]], [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]], [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], and [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]]. Those notes prove a single request and its evidence schema. This lab proves what happens when more than one request is active.

Read it with [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching|Batching and Continuous Batching]], [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Architectures and Throughput-Latency Trade-offs]], [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]], [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]], and [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]]. The academic point is direct: active sequences multiply KV-cache pressure, batching changes hardware utilization, repeated prefixes may reuse prefill work, draft verification can reduce decode latency, and queueing can make a fast model feel slow.

## What This Lab Decides

This lab answers five practical questions:

1. How many simultaneous local requests can the setup handle before latency or failures become unacceptable?
2. Does more concurrency improve useful throughput, or does it only add queue time?
3. Is the bottleneck prefill, decode, scheduler/queue, memory, network/client, or model quality?
4. Should the workload stay single-user, use a small local queue, move to a throughput runtime, run offline batch jobs, or use a hosted/self-hosted service?
5. What concurrency setting should be written into the deployment decision?

Do not infer concurrency from a single smoke test. A server can pass one request and still fail the first real batch.

## Load Control Vocabulary

| Concept | Meaning | Evidence |
|---|---|---|
| Single-request baseline | One request at a time with fixed prompt, sampler, context, and output cap. | TTFT, total latency, tokens/sec, quality row. |
| Concurrency | Number of outstanding active requests allowed at once. | Client setting, runtime setting, observed in-flight count. |
| Request rate | How quickly new requests are submitted. | Requests/sec, inter-arrival pattern, burstiness note. |
| Queue time | Time a request waits before prefill begins. | Client send time vs first server work or first token. |
| TTFT | Time to first user-visible token. | Streaming client or runtime timing. |
| TPOT / ITL | Time per output token or inter-token latency during decode. | Streaming timing or benchmark tool output. |
| Throughput | Requests/sec, output tokens/sec, or total tokens/sec. | Benchmark summary. |
| Saturation point | First concurrency where throughput stops improving or latency/failures exceed the target. | Concurrency ladder row. |
| Backpressure | Limit or rejection that prevents unlimited in-flight work. | Max queue, max concurrency, 429/503, client semaphore. |

Interactive chat cares about TTFT and tail latency. Batch extraction cares more about documents/hour and retryable failures. Record which one is the actual objective before running the ladder.

## Runtime Concurrency Map

| Runtime | Concurrency control to inspect | First evidence |
|---|---|---|
| Ollama | `OLLAMA_NUM_PARALLEL`, `OLLAMA_MAX_QUEUE`, `OLLAMA_MAX_LOADED_MODELS`, `keep_alive`, context length, and memory headroom. | FAQ/settings, native API timings, overload or queue behavior. |
| LM Studio | Max Concurrent Predictions when loading a model, model TTL, context length, GPU offload, and loaded model id. | Model loader settings, `/v1/models`, parallel request result. |
| llama.cpp server | `--parallel`, continuous batching flag, `/slots`, prompt-cache/slot controls, and metrics endpoint if enabled. | Startup command, `/slots`, prompt/generation metrics, deferred request count, cache save/restore when used. |
| vLLM | Benchmark `--request-rate`, `--max-concurrency`, burst/load pattern controls, and prefix-caching setting against a running OpenAI-compatible server. | Benchmark output with throughput, TTFT, TPOT, failure count, and cache/prefix evidence when exposed. |
| SGLang | `bench_serving` concurrency/rate settings, RadixAttention/default cache state, and server launch config. | Benchmark JSONL/console output with TTFT, TPOT, ITL, throughput, success count, and cache-hit evidence when exposed. |
| Open WebUI or another UI | Provider concurrency and UI request behavior. | Provider benchmark first, then UI-specific queue/history behavior. |

If speculative decoding is enabled, record the draft method, accepted-token evidence, and memory overhead before interpreting concurrency results. A draft path can improve single-user TPOT while reducing memory headroom or batch efficiency under load.

If a UI is slow, benchmark the provider endpoint directly before debugging the UI. If the provider is already saturated, the UI is not the root cause.

## Lab 0: Safety And Boundary

Keep first load tests on loopback. Concurrency tests can produce long outputs, high memory use, hot hardware, and large logs.

| Boundary | Required decision |
|---|---|
| Host binding | Loopback for first tests; no LAN/public exposure without [[LLM/Study/Local LLM Security and Privacy Runbook|Security and Privacy Runbook]]. |
| Prompt data | Synthetic prompts unless private logging is reviewed. |
| Output cap | Fixed `max_tokens` or runtime equivalent for every run. |
| Stop condition | Fixed stop strings or explicit no-stop decision. |
| Abort policy | Know how to stop the client and server without corrupting run evidence. |
| Thermal/power | Watch GPU/CPU temperature and memory on laptops. |

## Lab 1: Freeze The Single-Request Baseline

Run one boring prompt through [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] before any concurrency test.

| Field | Value |
|---|---|
| Runtime and version |  |
| Model id |  |
| Base URL and route |  |
| Prompt id |  |
| Prompt tokens |  |
| Output cap |  |
| Sampler settings |  |
| Context budget row |  |
| TTFT |  |
| Total latency |  |
| Output tokens/sec or TPOT |  |
| Quality decision | pass / hold / fail |

Pass signal: the single-request row is good enough that a concurrency test would answer a serving question rather than hide a prompt, quality, or compatibility failure.

## Lab 2: Concurrency Ladder

Use the same prompt suite, sampler, context target, output cap, model, and route. Change only the concurrency limit.

| Run | Max concurrency | Request rate | Prompts | Success | Errors | p50 TTFT | p95 TTFT | p50 total latency | Output tok/s | Peak RAM/VRAM | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| C1 | 1 |  |  |  |  |  |  |  |  |  | baseline |
| C2 | 2 |  |  |  |  |  |  |  |  |  |  |
| C4 | 4 |  |  |  |  |  |  |  |  |  |  |
| C8 | 8 |  |  |  |  |  |  |  |  |  |  |

Stop the ladder when any hard limit appears:

- quality fails because outputs truncate, drift, or ignore instructions
- p95 TTFT exceeds the interactive target
- total latency exceeds the batch SLA
- memory headroom disappears
- the server returns overload, timeout, OOM, or stream errors
- throughput stops improving across two higher concurrency levels

The best concurrency is not always the highest one. Pick the lowest setting that meets throughput with acceptable tail latency and headroom.

## Lab 3: Short Versus Long Prompt Mix

Continuous batching helps most when request lengths vary. Test a mixed workload instead of only identical prompts.

| Mix | Short prompts | Long prompts | Output cap | Expected stress |
|---|---:|---:|---:|---|
| Uniform short | 100% | 0% | fixed | decode throughput and client overhead |
| Uniform long | 0% | 100% | fixed | prefill and KV-cache pressure |
| Mixed | 80% | 20% | fixed | queue fairness, chunked prefill, straggler behavior |

Interpretation:

- If short prompts slow sharply when long prompts enter, prefill scheduling or queueing is the bottleneck.
- If total throughput improves but p95 TTFT becomes unacceptable, the setup is better for batch than chat.
- If OOM appears only in the mixed or long run, the issue is context/concurrency KV-cache pressure.

## Lab 4: Backpressure And Queue Policy

Do not let every caller submit unlimited requests.

| Policy | Use when | Evidence |
|---|---|---|
| Client semaphore | A local script controls maximum in-flight requests. | Config value and run log. |
| Runtime max parallel | Runtime supports per-model parallelism or server slots. | Startup/env setting and observed behavior. |
| Runtime queue limit | Runtime rejects overload after a bounded queue. | 429/503/error row and retry policy. |
| Batch/offline queue | Latency is not user-facing. | Checkpointed input list, retry count, output manifest. |
| Hosted/self-hosted service | Local hardware cannot meet the target. | Rejected local decision plus deployment memo. |

The failure mode to avoid is silent unbounded queueing: requests appear accepted but wait so long that users or batch jobs time out elsewhere.

## Lab 5: Decision Card

Copy this into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]], or the capstone workbook.

| Field | Value |
|---|---|
| Workload |  |
| Interactivity target | interactive / async / offline batch |
| Model/runtime |  |
| Route |  |
| Prompt mix | short / long / mixed / RAG / tool |
| Repeated-prefix/cache result |  |
| Best concurrency |  |
| Saturation point |  |
| Backpressure policy |  |
| Queue or overload behavior |  |
| p95 TTFT |  |
| Throughput | requests/sec / output tok/s / documents/hour |
| Peak RAM/VRAM |  |
| Quality result under load | pass / hold / fail |
| Failure layer | client / queue / prefill / decode / KV cache / runtime / quality |
| Deployment decision | single-user local / local queue / self-hosted server / hosted API / batch offline / change runtime |
| Retest trigger | new model, new context, new hardware, new traffic, new runtime |

## Failure Triage

| Symptom | Likely layer | First check |
|---|---|---|
| C1 passes but C2 fails | KV-cache headroom, runtime parallelism, or client bug. | Memory, server settings, two-request raw logs. |
| TTFT rises faster than total throughput | Queueing, prefill contention, or long prompt mix. | Prompt tokens, queue time, p95 TTFT. |
| Same long prefix is still slow under load | Prefix cache miss, eviction, or prompt layout mismatch. | Run [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] with changed-prefix control. |
| Single request is faster with speculation but C2/C4 regresses | Draft model/cache/buffers compete with batching or KV-cache headroom. | Run [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] with the selected concurrency setting. |
| Tokens/sec improves but users wait too long | Throughput/latency trade-off pushed too far. | Lower max concurrency or split batch vs chat workload. |
| Server returns overload | Queue limit reached. | Runtime max queue, client retry policy, backpressure setting. |
| OOM under concurrency | KV cache, context, active sequences, or loaded model count. | Context budget, active sequence count, model memory. |
| Streaming parser errors only under load | Client stream handling or server disconnects. | Raw chunk excerpts and partial output length. |
| Quality drops under load | Truncation, timeout, changed output caps, or thermal throttling. | Compare request body and output length to C1. |
| GPU utilization low but latency high | Client bottleneck, queue policy, CPU pre/post-processing, or network. | Client timestamps, server logs, utilization timeline. |

## Completion Gate

This lab is complete when:

- [ ] single-request baseline exists
- [ ] context and output caps are fixed
- [ ] concurrency ladder has at least C1, C2, and one higher setting or a named blocker
- [ ] p50/p95 TTFT or equivalent latency evidence is recorded
- [ ] throughput and success/error counts are recorded
- [ ] peak memory or headroom is recorded
- [ ] quality is checked under the selected concurrency setting
- [ ] backpressure or queue behavior is explicit
- [ ] deployment decision states single-user, local queue, batch, self-hosted, hosted, or change runtime

## References

Internal routes:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]

Current external docs checked 2026-06-15:

- [Ollama FAQ](https://docs.ollama.com/faq)
- [LM Studio parallel requests](https://lmstudio.ai/docs/app/advanced/parallel-requests)
- [LM Studio lms load](https://lmstudio.ai/docs/cli/local-models/load)
- [vLLM benchmark CLI](https://docs.vllm.ai/en/latest/benchmarking/cli/)
- [SGLang benchmarking and profiling](https://sgl-project.github.io/developer_guide/benchmark_and_profiling.html)
- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
