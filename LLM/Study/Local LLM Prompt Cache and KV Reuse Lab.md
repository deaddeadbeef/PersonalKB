---
tags: [study, llm, inference, local-llm, kv-cache, prompt-cache, prefix-caching, benchmarking, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Prompt Cache and KV Reuse Lab

> **One-line summary** Repeated-prefix local inference is only faster when the runtime can reuse prefill work; prove it with cold/warm separation, stable prompt prefixes, TTFT or prompt-eval timing, cache evidence, and a benchmark decision.

Use this after [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] and [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]]. Those notes explain prefill, decode, prompt tokens, and context pressure. This lab tests whether repeated system prompts, few-shot examples, RAG documents, or conversation history are actually being reused across requests.

Use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] when many requests share prefixes at the same time. Use [[LLM/Study/Local LLM Observability and Operations Runbook|Local LLM Observability and Operations Runbook]] when cache counters, slots, metrics, or logs are needed. Use [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook|Local LLM Service Lifecycle and Upgrade Runbook]] when the cache path, runtime version, startup mode, or model residency changed.

## What This Lab Decides

It answers six practical questions:

1. Is the observed speedup just a warm loaded model, or true repeated-prefix reuse?
2. Does the workload have a stable prefix long enough to make caching matter?
3. Does caching reduce prefill or time to first token without changing output quality?
4. Which runtime exposes enough cache evidence to trust the result?
5. Does cache reuse survive the intended restart, slot, model, or deployment boundary?
6. Should the deployment keep prompt caching enabled, change prompt layout, or ignore caching?

Do not claim "prompt caching works" from a second faster run unless load time, prompt length, output length, and cache evidence have been separated.

## Vocabulary

| Term | Meaning | Common confusion |
| --- | --- | --- |
| Model residency | Model weights stay loaded in RAM/VRAM between requests. | This reduces load time, not necessarily prefill time. |
| Prefill | The model processes prompt tokens and builds the first KV cache for the request. | This is the phase prefix caching can skip or reduce. |
| Decode | The model generates output tokens one by one using the request's KV cache. | Prefix caching does not usually speed long answer generation. |
| KV cache | Per-layer key/value states for already processed tokens. | It exists inside one request even without cross-request reuse. |
| Prompt cache / prefix cache | Reuse of KV states from a previous request with the same token prefix. | Requires identical rendered tokens at the beginning. |
| Slot cache | Runtime-managed saved state for a conversation or server slot. | More stateful than automatic prefix matching. |
| Cache hit | The runtime found reusable prefix state. | May be visible as counters, slot state, logs, or lower prefill timing. |
| Eviction | Cached state is removed because memory is needed. | Long contexts and concurrency can evict useful prefixes. |

## Cache-Reuse Workloads

| Workload | Stable prefix | Varying suffix | Expected gain |
| --- | --- | --- | --- |
| Long document Q&A | Document or manual | User question | Lower prefill and TTFT after first question. |
| RAG with fixed corpus excerpt | Retrieved context block | User question or answer format | Only helps when the retrieved context prefix is identical. |
| Few-shot prompting | Instructions and examples | New task instance | Lower prefill when examples stay first and unchanged. |
| Agent loop | System prompt, tool protocol, project context | Latest tool result and next action | Lower repeated context processing. |
| Multi-turn chat | Previous transcript prefix | New user message | Helps if the rendered history prefix is identical and retained. |
| Batch extraction | Schema and instructions | Document item | Helps only if the long part is in the shared prefix, not the unique suffix. |

If each request begins with a different long document, prefix caching cannot help much. Prompt layout matters: put shared tokens first and changing tokens later when the runtime matches prefixes.

## Runtime Cache Map

| Runtime | Cache mechanism to test | Evidence to capture | Caution |
| --- | --- | --- | --- |
| Ollama | Model keep-alive and any response-level prompt timing. | `keep_alive`, `load_duration`, `prompt_eval_count`, `prompt_eval_duration`, wall-clock timing. | Treat faster second runs as warm-model evidence unless prefill timing also improves. |
| LM Studio | Loaded-model residency, TTL, runtime logs, and OpenAI-compatible timing if exposed. | Loaded model, TTL/eviction setting, client TTFT, response usage, logs. | Prefix-cache internals may not be visible; mark as indirect if only wall time changed. |
| llama.cpp CLI | File prompt cache with `--prompt-cache`, `--prompt-cache-all`, and `--prompt-cache-ro`. | First and repeated CLI timings, cache filename, prompt tokens, output cap. | Restored cache is not a guarantee of identical future tokens under the same seed. |
| llama.cpp server | Slots, metrics, slot save/restore, cache-reuse flags when used. | Startup flags, `/slots`, `/metrics`, prompt token/process counters, slot save/restore result. | Server slot behavior and file prompt cache are different controls. |
| vLLM | Automatic Prefix Caching. | Launch flag/config, prompt length, TTFT, prefill metrics or prefix-cache counters if exposed. | Gain is mainly prefill; long outputs can hide it. |
| SGLang | RadixAttention prefix cache; optional hierarchical cache for larger reuse. | Launch flags, metrics/cache hit rate if enabled, TTFT, throughput, memory pressure. | Cache size and eviction policy affect hit rate under mixed workloads. |

## Lab 0: Freeze The Cache Experiment

Fill this before any request.

| Field | Value |
| --- | --- |
| Run id |  |
| Runtime and version |  |
| Model id/path |  |
| Quantization/format |  |
| Endpoint or CLI command |  |
| Cache feature enabled? | yes / no / unknown |
| Model keep-alive or TTL |  |
| Prompt cache path, if file-based |  |
| Slot/cache controls |  |
| Shared prefix source | system / examples / document / history / RAG / tool protocol |
| Shared prefix token count |  |
| Varying suffix token count |  |
| Output cap |  |
| Sampler settings |  |
| Metric source | response fields / streaming TTFT / metrics / logs / wall clock |
| Cache privacy boundary | local only / shared service / multi-tenant / unknown |

Pass signal: another run can recreate the same prefix, suffixes, cache setting, and measurement method.

## Lab 1: Separate Cold Load From Warm Model

Run three requests with the same tiny prompt and fixed output cap.

| Run | Expected state | Load time | Prompt eval / TTFT | Total latency | Interpretation |
| --- | --- | ---: | ---: | ---: | --- |
| Cold | Model not loaded |  |  |  | Measures load plus request. |
| Warm same prompt | Model loaded |  |  |  | Removes most load cost. |
| Warm changed prompt | Model loaded |  |  |  | Shows warm-model baseline without prefix reuse. |

Ollama response fields make this distinction visible:

```powershell
$body = @{
  model = "<model>"
  prompt = "Explain KV cache in two sentences."
  stream = $false
  keep_alive = "10m"
  options = @{ temperature = 0; num_predict = 80 }
} | ConvertTo-Json -Depth 6

Invoke-RestMethod http://localhost:11434/api/generate `
  -Method Post `
  -Body $body `
  -ContentType "application/json" |
  Select-Object total_duration,load_duration,prompt_eval_count,prompt_eval_duration,eval_count,eval_duration
```

If only `load_duration` drops, the win is model residency. If prompt evaluation or TTFT drops on a long repeated prefix, cache reuse may be present.

## Lab 2: Repeated Prefix A/B

Build two prompt sets with the same total output cap.

Set A: stable long prefix, different short suffixes.

```text
<shared system prompt>
<shared long document or examples>
Question: <unique question A/B/C>
```

Set B: changed prefix, same general length.

```text
<different document or shuffled examples>
Question: <unique question A/B/C>
```

Record:

| Request | Prefix id | Prefix tokens | Suffix tokens | Output cap | Cache state | TTFT or prompt eval | Total latency | Output tokens | Cache evidence |
| --- | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | --- |
| A1 | shared-doc-v1 |  |  |  | cold prefix |  |  |  |  |
| A2 | shared-doc-v1 |  |  |  | expected hit |  |  |  |  |
| A3 | shared-doc-v1 |  |  |  | expected hit |  |  |  |  |
| B1 | changed-doc-v1 |  |  |  | expected miss |  |  |  |  |

Interpretation:

| Pattern | Meaning | Next action |
| --- | --- | --- |
| A2/A3 TTFT lower, B1 not lower | Prefix reuse likely. | Keep shared prefix stable and record cache evidence. |
| All warm runs lower equally | Mostly model residency or warm runtime. | Do not claim prompt-cache benefit. |
| No run improves | Cache disabled, prefix too short, prefix not identical, or cache evicted. | Inspect rendered tokens, launch flags, metrics, and memory pressure. |
| TTFT improves but total latency does not | Output generation dominates. | Cache helps interactivity but not long-answer throughput. |
| Quality changes after cache hit | Prompt/template or runtime bug; caching should not be the intended quality control. | Re-run with deterministic settings and compare rendered prompts. |

## Lab 3: Runtime-Specific Proof

### vLLM

Automatic Prefix Caching reuses KV cache when a new request shares the same prefix as an earlier request. For a vLLM experiment, record:

| Field | Evidence |
| --- | --- |
| APC enabled | Engine setting or server flag/config. |
| Prefix token count | Tokenizer count or response usage. |
| Same-prefix requests | A1, A2, A3 request bodies. |
| Changed-prefix control | B1 request body. |
| Prefill/TTFT evidence | Metrics, logs, benchmark output, or streaming first-token timing. |
| Limit note | Whether output length dominated total latency. |

Use `--no-enable-prefix-caching` or equivalent only when doing a controlled on/off comparison. Keep the served model, prompt, sampler, output cap, request rate, and hardware fixed.

### SGLang

SGLang's RadixAttention detects and reuses common token prefixes. For a SGLang experiment, record:

| Field | Evidence |
| --- | --- |
| Radix cache enabled | No `--disable-radix-cache` flag, or explicit launch config. |
| Metrics enabled | `--enable-metrics` or benchmark output. |
| Prefix hit evidence | Cache-hit metric/log if exposed; otherwise TTFT/prefill delta plus changed-prefix control. |
| Cache pressure | Memory, active requests, eviction or HiCache settings if used. |

If using hierarchical cache, also record host-cache size, page size, storage backend, and prefetch policy. Local single-GPU work usually starts with default RadixAttention before adding hierarchical cache complexity.

### llama.cpp

For CLI runs, `--prompt-cache FNAME` creates or reuses a prompt-state file after the initial prompt.

```powershell
llama-cli -m C:\Models\model.gguf `
  --prompt-cache C:\LLM-Runs\shared-prefix.cache `
  --prompt "Long shared prefix ...`nQuestion: A" `
  --temp 0 `
  -n 80
```

For server runs, inspect slots and metrics:

```powershell
Invoke-RestMethod http://127.0.0.1:8080/slots |
  ConvertTo-Json -Depth 8

Invoke-WebRequest http://127.0.0.1:8080/metrics |
  Select-Object -ExpandProperty Content
```

When saving or restoring slot state, record the slot id, filename, saved/restored token count, timings, and whether the next request still includes the matching prefix.

### Ollama and LM Studio

For desktop-first runtimes, treat prompt-cache claims conservatively unless the runtime exposes direct cache evidence. Still run this lab to separate:

- cold load
- warm loaded model
- long prompt prefill
- repeated-prefix timing
- output-generation time

For Ollama, response fields such as `load_duration`, `prompt_eval_count`, `prompt_eval_duration`, `eval_count`, and `eval_duration` are useful. For LM Studio, use loaded-model state, logs, OpenAI-compatible usage fields when present, and client timing.

## Lab 4: Prompt Layout Test

Prefix caching depends on identical starting tokens. Compare two layouts:

| Layout | Shape | Expected cache behavior |
| --- | --- | --- |
| Shared-first | Shared instruction/document/examples, then unique question. | Best chance of reuse. |
| Unique-first | Unique question, then shared instruction/document/examples. | Prefix differs early; lower reuse. |

Record:

| Layout | Prefix tokens shared | TTFT/prompt eval | Cache evidence | Decision |
| --- | ---: | ---: | --- | --- |
| Shared-first |  |  |  |  |
| Unique-first |  |  |  |  |

If shared-first is faster and quality is equal, write that layout into the client harness or RAG prompt builder.

## Lab 5: Cache Pressure And Eviction

Run the same repeated-prefix test at the chosen concurrency or context size.

| Stressor | What changes | Evidence |
| --- | --- | --- |
| Longer prefix | Shared prefix grows from small to realistic. | TTFT, cache memory, hit evidence. |
| More concurrent requests | Active requests increase. | p50/p95 TTFT, queue, memory, hit rate. |
| Mixed prefixes | Several documents/conversations alternate. | Eviction or lower hit rate. |
| Restart | Server or app restarts. | Whether file/slot/hierarchical cache persists. |

Do not optimize for a benchmark-only prefix that the real workload will not reuse.

## Decision Card

Copy this into [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] or [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]].

| Field | Value |
| --- | --- |
| Workload |  |
| Runtime/model |  |
| Cache mechanism | keep-alive / CLI prompt cache / slot cache / APC / RadixAttention / unknown |
| Shared prefix | system / examples / document / history / RAG / tool protocol |
| Prefix tokens |  |
| Suffix tokens |  |
| Output cap |  |
| Cold load separated? | yes / no |
| Changed-prefix control? | yes / no |
| Direct cache evidence | metric / slot / log / file / none |
| TTFT or prefill improvement |  |
| Total latency improvement |  |
| Memory or eviction risk |  |
| Quality unchanged? | yes / no |
| Keep caching? | yes / no / unknown |
| Prompt layout decision |  |
| Retest trigger | new runtime, model, context, prompt layout, cache path, concurrency, restart mode |

## Failure Triage

| Symptom | Likely layer | First controlled change |
| --- | --- | --- |
| Second request faster only because load time disappears | Model residency, not prefix caching. | Record warm baseline and keep-alive separately. |
| Repeated-prefix request does not improve | Prefix mismatch, cache disabled, prefix too short, or eviction. | Compare rendered tokens; inspect cache flags and metrics. |
| Cache hit disappears under concurrency | Cache pressure or eviction. | Lower context/concurrency or increase cache capacity if supported. |
| Long outputs hide cache benefit | Decode dominates total latency. | Compare TTFT/prefill separately from total latency. |
| RAG cache never hits | Retrieved chunks differ or are ordered differently each request. | Stabilize retrieval order or cache only fixed source documents. |
| Prompt cache file grows unexpectedly | Cache is saving conversation/output state too. | Use read-only cache or separate per-workload cache files. |
| Cache reuse crosses privacy boundary | Shared service or multi-tenant risk. | Use cache isolation/salt if supported, or disable shared cache. |
| Quality changes after cache reuse | Runtime/template/sampler issue, not expected cache behavior. | Freeze sampler, verify rendered prompt, and run quality harness. |

## Completion Gate

This lab is complete when all are true:

- [ ] Cold load, warm model, and repeated-prefix runs are separated.
- [ ] Shared prefix and varying suffix token counts are recorded.
- [ ] A changed-prefix control run exists.
- [ ] TTFT, prompt-eval time, or prefill metric is recorded separately from total latency.
- [ ] Output cap and sampler settings are fixed.
- [ ] Runtime cache mechanism and evidence strength are named.
- [ ] Quality is checked after the cache-enabled path.
- [ ] Memory/eviction risk is recorded for the intended workload.
- [ ] Prompt layout decision is written into the client, RAG, or benchmark path.
- [ ] Benchmark log receives the decision card.
- [ ] Troubleshooting row exists if the cache result is a miss, regression, or privacy concern.

## References

Internal:

- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
- [[LLM/Study/Local LLM Service Lifecycle and Upgrade Runbook]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2026 — Reasoning and Agents/Prompt Caching and Inference Infrastructure]]
- [[chunk-llm-117 PagedAttention Eliminates KV Fragmentation]]
- [[chunk-llm-119 PagedAttention Copy-on-Write Sharing]]
- [[chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]]
- [[chunk-llm-260 Prompt caching reduces input token costs 50-90 percent by reusing KV cache for repeated prefixes]]

Current external docs checked 2026-06-15:

- [vLLM Automatic Prefix Caching](https://docs.vllm.ai/en/stable/features/automatic_prefix_caching/)
- [vLLM prefix caching design](https://docs.vllm.ai/en/stable/design/prefix_caching/)
- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [llama.cpp completion README](https://github.com/ggml-org/llama.cpp/blob/master/tools/completion/README.md)
- [SGLang documentation](https://docs.sglang.io/)
- [SGLang server arguments](https://docs.sglang.io/docs/advanced_features/server_arguments)
- [SGLang HiCache design](https://docs.sglang.io/docs/advanced_features/hicache_design)
- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
