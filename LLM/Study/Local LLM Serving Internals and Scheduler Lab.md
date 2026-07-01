---
tags: [study, llm, inference, local-llm, serving, scheduler, kv-cache, batching]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [core, deep-dive, practice]
last-verified: 2026-06-15
---

# Local LLM Serving Internals and Scheduler Lab

> **One-line summary** A local LLM server is understandable when you can explain each latency or OOM symptom as scheduler, prefill, decode, KV-cache, batching, slot, or admission-control behavior instead of vague runtime magic.

Use this after [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]] proves one endpoint and before [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] or [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner|Local LLM Concurrency and Batch Throughput Runner]] when the next question is why throughput, TTFT, TPOT, queueing, or OOM changes under load. Use [[LLM/Study/LLM Serving Systems Paper-to-Local Proof Map|LLM Serving Systems Paper-to-Local Proof Map]] first when the hypothesis comes from FlashAttention, Orca, PagedAttention, Sarathi-Serve, SGLang, or runtime metrics. Use [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]] first if the timing and memory numbers have not yet been mapped to request phases and confounders. Use [[LLM/Study/Local LLM Queueing and Tail Latency Field Guide|Local LLM Queueing and Tail Latency Field Guide]] first when the missing step is arrival rate, service time, utilization, p95/p99, queue wait, or admission-policy reasoning. Use [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Local LLM Context Window and Token Budgeting Runner]] first when prompt length, RAG context, history, or tool schemas may be the prefill or KV-cache driver. Use [[LLM/Study/Local LLM Observability and Operations Runner|Local LLM Observability and Operations Runner]] when the scheduler claim needs repeatable route, loaded-model, metrics, slots, resource, and log-tail artifacts. Use [[LLM/Study/Local LLM Scheduler Evidence Audit Runner|Local LLM Scheduler Evidence Audit Runner]] after the scheduler rows exist to audit hypothesis, latency phase, scheduler state, long-prompt interference, tuning delta, capacity event, and decision-card evidence before changing concurrency, queue, cache, or deployment policy.

Read it with [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]], [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching|Batching and Continuous Batching]], and [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Architectures and Throughput-Latency Trade-offs]]. Those notes explain the mechanisms. This lab turns them into local evidence rows for vLLM, SGLang, llama.cpp, LM Studio, and similar servers.

If vLLM or SGLang is running inside WSL from Windows, complete [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab|Local LLM WSL CUDA vLLM and SGLang Setup Lab]] first. Scheduler evidence is not meaningful until WSL GPU visibility, Python environment, loopback route, `/v1/models`, and basic metrics/logs are proven.

## What This Lab Decides

It answers six serving-internals questions:

1. Is latency coming from queue wait, prefill, decode, streaming/client overhead, or cold load?
2. Is the server compute-bound, memory-bandwidth-bound, or KV-cache-capacity-bound?
3. Does the runtime admit new requests continuously, queue them, reject them, or preempt/recompute them?
4. Are long prompts starving decode traffic, and would chunked prefill or lower batched-token budget help?
5. Are slots, max sequences, max batched tokens, or max concurrent predictions set for the workload?
6. Does the local benchmark support interactive chat, offline batch, shared service, or a runtime change?

Do not call a serving stack "fast" or "slow" until these layers are separated.

## Mechanism Map

| Mechanism | What happens | Local symptom | Evidence |
| --- | --- | --- | --- |
| Cold load | Weights move into runtime memory before useful inference starts. | First request is much slower than later requests. | Load duration, model residency, keep-alive or loaded-model state. |
| Prefill | Prompt tokens are processed and KV cache is built. | TTFT grows with prompt length, RAG context, or tool schemas. | Prompt tokens, prefill duration, TTFT, long-vs-short prompt row. |
| Decode | One token per active sequence is generated each iteration. | Later tokens/sec or TPOT is poor while TTFT is acceptable. | Output tokens, TPOT/ITL, GPU memory bandwidth/utilization, active sequences. |
| KV-cache allocation | Keys and values are stored for active prompt and generated tokens. | OOM appears with long context or higher concurrency. | Context length, active requests, cache usage, preemption/OOM logs. |
| PagedAttention | KV cache is managed in pages/blocks to reduce fragmentation and allow flexible sharing. | More active sequences fit than with naive contiguous allocation. | Runtime support, cache metrics, concurrency ladder, preemption count. |
| Continuous batching | Requests can enter and exit batches at token-iteration granularity. | Throughput improves under mixed output lengths, but latency may shift. | Running/waiting counts, request-rate benchmark, p50/p95 TTFT and TPOT. |
| Chunked prefill | Long prompt prefill is split and interleaved with decode work. | Long prompts hurt short-request latency less than full prefill would. | Long/short mix, `max_num_batched_tokens`, TTFT/ITL trade-off. |
| Prefix cache | Shared prompt prefixes reuse existing KV work. | Repeated system prompts or agent loops reduce TTFT only when prefix matches. | Cache-hit metrics, changed-prefix control, prompt-cache lab row. |
| Admission control | Runtime or client limits active/queued requests. | Requests reject, queue, time out, or tail latency explodes. | Max concurrency, queue limit, error codes, waiting count, retry policy. |

## Runtime Scheduler Map

| Runtime | Scheduler or memory concepts to inspect | First proof |
| --- | --- | --- |
| Ollama | Loaded model residency, queue/parallel settings, response timing fields, context length. | `/api/ps`, native response durations, environment/config values. |
| LM Studio | Max Concurrent Predictions, llama.cpp engine version, model TTL, per-model settings. | Model loader settings, `/v1/models`, parallel request smoke test. |
| llama.cpp server | Slots, `--parallel`, continuous batching, prompt cache/slot state, metrics endpoint. | Startup command, `/slots`, `/metrics` when enabled, per-slot request state. |
| vLLM | PagedAttention, continuous batching, chunked prefill, preemption/recompute, `max_num_seqs`, `max_num_batched_tokens`, `gpu_memory_utilization`, prefix caching. | `/metrics`, server logs, benchmark output, preemption warning count. |
| SGLang | RadixAttention, continuous batching, paged attention, zero-overhead CPU scheduler, prefill-decode disaggregation, metrics. | Launch command, `/metrics` with metrics enabled, benchmark/profiling output. |
| Open WebUI | UI queue and provider behavior after provider proof. | Provider endpoint benchmark first, then UI-specific timing. |

Treat UI latency as downstream evidence. If the provider endpoint is saturated, the UI is not the root cause.

## Lab 0: Freeze The Scheduler Hypothesis

Before changing any launch flag, write the symptom as a falsifiable hypothesis.

| Field | Value |
| --- | --- |
| Run id |  |
| Runtime and version |  |
| Model and quantization |  |
| Hardware path | CPU / CUDA / ROCm / Metal / WSL / Docker / remote |
| Workload | chat / RAG / tool / batch / mixed |
| Symptom |  |
| Suspected mechanism | cold load / queue / prefill / decode / KV cache / batching / prefix cache / admission |
| Fixed prompt suite |  |
| Fixed sampler and output cap |  |
| Fixed route and client |  |
| One variable to change |  |

Pass signal: the next experiment changes one scheduler or memory variable, not model, prompt, sampler, runtime, and workload together.

## Lab 1: Split Latency Into Phases

Capture a single short request, one long request, and one repeated-prefix request.

| Row | Prompt class | Prompt tokens | Output cap | Cold/warm | TTFT | TPOT/ITL | Total latency | Output tok/s | Decision |
| --- | --- | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |
| S1 | short |  |  | cold |  |  |  |  |  |
| S2 | short |  |  | warm |  |  |  |  |  |
| L1 | long |  |  | warm |  |  |  |  |  |
| P1 | repeated prefix |  |  | warm |  |  |  |  |  |

Interpretation:

- Cold S1 slow and warm S2 normal -> load/model residency.
- Long L1 TTFT high and TPOT normal -> prefill/context pressure.
- Long L1 OOM -> KV cache, context target, or concurrency headroom.
- P1 not faster than L1 -> prefix cache miss, disabled cache, or prompt mismatch.
- TPOT poor across all rows -> decode bottleneck, model size, offload, quantization kernel, or memory bandwidth.

## Lab 2: Observe Scheduler State

Save the runtime state before and after a controlled request.

| Runtime | State evidence |
| --- | --- |
| llama.cpp | `/slots`, startup flags, `--parallel`, continuous batching setting, prompt/generation metrics if enabled. |
| vLLM | `/metrics`, logs, running/waiting request counts, KV-cache usage, preemption warnings, prefix-cache counters if enabled. |
| SGLang | metrics endpoint, request counts, cache-hit rate, token counters, launch flags, benchmark JSONL if used. |
| LM Studio | Max Concurrent Predictions setting, model loader options, server logs, response usage/timing. |
| Ollama | `/api/ps`, response durations, parallel/queue settings, loaded-model state. |

Minimum scheduler row:

| Run id | Runtime | Running | Waiting/queued | Slots/max seqs | Batched-token budget | KV/cache signal | Preemptions/OOM | Backpressure behavior |
| --- | --- | ---: | ---: | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

If the runtime does not expose a field, write "not exposed" instead of guessing.

## Lab 3: Long-Prompt Interference Test

This test explains whether long prefills are harming short interactive requests.

| Mix | Short prompts | Long prompts | Concurrency | Expected stress |
| --- | ---: | ---: | ---: | --- |
| short-only | 100% | 0% |  | decode/client overhead |
| long-only | 0% | 100% |  | prefill and KV cache |
| mixed | 80% | 20% |  | scheduler fairness and chunked prefill |

Record:

| Mix | p50 TTFT | p95 TTFT | p50 TPOT/ITL | Output tok/s | Queue/waiting | Peak RAM/VRAM | Decision |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| short-only |  |  |  |  |  |  |  |
| long-only |  |  |  |  |  |  |  |
| mixed |  |  |  |  |  |  |  |

Interpretation:

- Mixed p95 TTFT spikes while throughput improves: throughput setting is hurting chat responsiveness.
- Long-only OOM but short-only passes: context/KV-cache capacity, not model load.
- Mixed request failures: admission control, queue limit, preemption, or timeout policy.
- Mixed stable with good utilization: continuous batching/chunked prefill is working for this workload.

## Lab 4: Tune One Scheduler Variable

Choose only one variable per run.

| Variable | Runtime examples | Expected effect | Risk |
| --- | --- | --- | --- |
| Max active sequences | vLLM `max_num_seqs`, runtime slots, max concurrent predictions. | More concurrency and throughput. | Higher tail latency and KV-cache pressure. |
| Batched-token budget | vLLM `max_num_batched_tokens`. | Balance TTFT, ITL, and throughput. | Too low starves prefill; too high can hurt decode responsiveness. |
| GPU memory allocation | vLLM `gpu_memory_utilization`, cache size flags. | More KV-cache room. | Less headroom for runtime/driver/other processes. |
| Parallel slots | llama.cpp `--parallel`, LM Studio Max Concurrent Predictions. | More simultaneous requests. | Smaller per-slot context or memory contention. |
| Prefix cache | vLLM APC, SGLang RadixAttention, llama.cpp slot/prompt cache. | Lower repeated-prefix TTFT. | Cache eviction, privacy/logging, false cache-hit assumptions. |
| Output cap | `max_tokens`, `num_predict`, equivalent. | Bound decode time and queue occupancy. | Truncated answers if cap is too small. |

Decision row:

| Run | Changed variable | Previous value | New value | p95 TTFT delta | TPOT delta | Throughput delta | Peak memory delta | Keep? |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- |
|  |  |  |  |  |  |  |  |  |

Keep the setting only if the target workload improves and quality still passes.

## Lab 5: Preemption And OOM Triage

When a runtime reports preemption, recompute, OOM, or cache exhaustion, treat it as a capacity signal.

| Symptom | Likely cause | First controlled change |
| --- | --- | --- |
| vLLM preemption warnings | KV-cache space insufficient for active batched requests. | Lower `max_num_seqs` or `max_num_batched_tokens`, reduce context/output cap, or increase available cache memory. |
| OOM only at higher concurrency | KV cache or runtime buffers, not just model weights. | Lower concurrency, reduce context, choose smaller model, or use tensor/pipeline parallelism when available. |
| OOM after quantization seemed to fit | Weight memory improved but KV/cache/runtime headroom did not. | Re-run sizing and quantization/offload lab with target concurrency. |
| Long prompts delay all users | Full prefill or scheduler policy is blocking decode traffic. | Test chunked prefill/batched-token budget or split chat and batch workloads. |
| Prefix cache helps single user but not mixed load | Cache eviction or prefix mismatch under churn. | Run prompt-cache lab with concurrent changed-prefix controls. |

Do not raise concurrency to hide latency. That can improve total tokens/sec while making p95 TTFT worse.

## Decision Card

| Field | Value |
| --- | --- |
| Workload |  |
| Runtime/model |  |
| Main bottleneck | cold load / queue / prefill / decode / KV cache / scheduler / client |
| Scheduler evidence |  |
| KV/cache evidence |  |
| Best concurrency or slots |  |
| Batched-token or queue policy |  |
| Long-prompt policy | accept / chunk / separate queue / reject / batch offline |
| Prefix-cache decision | off / on / not exposed / not useful |
| Backpressure policy |  |
| Benchmark row |  |
| Quality row |  |
| Deployment decision | single-user / local queue / self-hosted server / hosted API / offline batch / change runtime |
| Retest trigger | new model, context, runtime, driver, traffic mix, or hardware |

## Completion Gate

This lab is complete when all are true:

- [ ] A scheduler hypothesis is written before tuning.
- [ ] Cold/warm, short/long, and repeated-prefix rows are recorded or explicitly skipped with a reason.
- [ ] Runtime scheduler state is captured from metrics, logs, slots, or an explicit "not exposed" note.
- [ ] A long-prompt interference test distinguishes prefill, decode, queue, and KV-cache pressure.
- [ ] One scheduler variable is changed at a time.
- [ ] Preemption, OOM, or queue behavior has a named owner when present.
- [ ] The final decision card states best concurrency/slots, queue policy, long-prompt policy, and retest trigger.
- [ ] [[LLM/Study/Local LLM Scheduler Evidence Audit Runner|Local LLM Scheduler Evidence Audit Runner]] passes or links each scheduler evidence gap to a remediation route.
- [ ] [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] receives the selected concurrency and saturation evidence.
- [ ] [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] receives the operations evidence, with [[LLM/Study/Local LLM Observability and Operations Runner|Local LLM Observability and Operations Runner]] output when service state, metrics, slots, logs, or resource pressure are part of the claim.
- [ ] [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] receives the deployment decision when the run affects a real workload.

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM Serving Systems Paper-to-Local Proof Map]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/Local LLM Queueing and Tail Latency Field Guide]]
- [[LLM/Study/Local LLM WSL CUDA vLLM and SGLang Setup Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Local LLM Scheduler Evidence Audit Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Runner]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/_chunks/chunk-llm-117 PagedAttention Eliminates KV Fragmentation]]
- [[LLM/_chunks/chunk-llm-118 vLLM Continuous Batching Throughput]]
- [[LLM/_chunks/chunk-llm-119 PagedAttention Copy-on-Write Sharing]]
- [[LLM/_chunks/chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]]

Current external docs and papers checked 2026-06-15:

- [vLLM documentation](https://docs.vllm.ai/)
- [vLLM optimization and tuning](https://docs.vllm.ai/en/latest/configuration/optimization/)
- [SGLang documentation](https://sgl-project.github.io/)
- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [LM Studio parallel requests](https://lmstudio.ai/docs/app/advanced/parallel-requests)
- [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [SARATHI: Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills](https://arxiv.org/abs/2308.16369)
