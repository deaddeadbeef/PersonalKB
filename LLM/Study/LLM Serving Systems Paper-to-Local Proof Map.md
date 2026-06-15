---
tags: [study, llm, papers, serving, systems, inference, local-llm, scheduler, kv-cache, batching, proof]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, deep-dive, practice]
last-verified: 2026-06-16
---

# LLM Serving Systems Paper-to-Local Proof Map

> **One-line summary** Serving-systems papers become useful when each academic claim predicts a local symptom, a runtime metric, and a proof artifact you can capture before changing model, runtime, concurrency, or cache settings.

Use this after [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]], [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map|LLM 20-Paper Fast Path Synthesis Map]], and [[LLM/Study/LLM Paper Claim Ledger|LLM Paper Claim Ledger]] when the paper cluster is about inference speed, memory, batching, KV cache, scheduler policy, prefix reuse, or tail latency. Then route the result through [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]], [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner|LLM Academic-to-Local Defense Matrix Runner]], [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]], and [[LLM/Study/Local LLM Queueing and Tail Latency Field Guide|Local LLM Queueing and Tail Latency Field Guide]].

The goal is not to memorize runtime trivia. The goal is to defend why a local observation, such as slow first token, high p95 latency, OOM at concurrency, preemption, or cache-hit improvement, follows from a named systems mechanism.

## Read In This Order

1. **FlashAttention:** attention speed can be limited by memory movement, not only arithmetic count.
2. **Orca:** autoregressive generation is a multi-iteration service workload, so static request batching wastes opportunity.
3. **PagedAttention and vLLM:** KV cache is dynamic memory, and better block management can raise throughput at the same latency target.
4. **Sarathi-Serve:** prefill and decode stress different paths; chunked prefill can reduce interference between long prompts and decode work.
5. **SGLang and RadixAttention:** structured LLM programs repeat prefixes; prefix/KV reuse can lower first-token latency when the prefix actually matches.
6. **Current runtime docs and metrics:** vLLM and SGLang expose metrics that can support or falsify the paper-derived claim on a real local endpoint.

## Systems Claim Matrix

| Paper or source | Core systems claim | Mechanism to explain | Local symptom to predict | Proof artifact | Do not conclude |
|---|---|---|---|---|---|
| FlashAttention | Exact attention can be faster when the algorithm reduces high-bandwidth-memory traffic. | SRAM/HBM tiling, online softmax, sequence-length memory pressure. | Long prompts or larger context show different TTFT/throughput under runtimes with different attention kernels. | [[LLM/Study/Local LLM Runtime Comparison Runner|Runtime comparison runner]] plus prompt-token sweep and benchmark audit. | A faster kernel does not make the model smarter or prove quality. |
| Orca | LLM serving needs iteration-level scheduling and selective batching because each request generates token by token. | New and finished requests should enter or leave the batch at generation-step boundaries. | Mixed output lengths waste less capacity when the runtime admits requests continuously. | [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner|Concurrency runner]] plus scheduler-state row. | Peak tokens/sec alone does not prove good chat latency. |
| PagedAttention and vLLM | KV cache fragmentation and duplication can waste memory, so paged/block KV management improves concurrency. | KV cache as virtual-memory-like blocks; sharing and reduced fragmentation. | OOM, preemption, or sharp p95 degradation appears as context or active sequences grow. | [[LLM/Study/Local LLM KV Cache Sizing Runner|KV-cache sizing runner]], [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|serving scheduler lab]], and vLLM `/metrics` evidence. | Weight quantization alone does not prove concurrency fit. |
| Sarathi-Serve | Prefill and decode have different latency/utilization trade-offs, and chunked prefills can reduce stalls. | Split long prefill into chunks and interleave with decode work. | A small number of long prompts can raise short-request TTFT unless scheduler policy protects decode. | Long/short mixed-load row in [[LLM/Study/Local LLM Queueing and Tail Latency Field Guide|Queueing and Tail Latency Field Guide]]. | Better throughput can still be a worse interactive service. |
| SGLang and RadixAttention | Repeated prefixes in structured LLM programs can reuse KV cache through prefix-aware caching. | Radix-tree prefix cache, prompt-prefix identity, cache-hit behavior. | Repeated system prompt, examples, tools, or RAG prefix lowers TTFT only when prefix identity is preserved. | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner|Prompt cache and KV reuse runner]] with changed-prefix control and SGLang metrics. | A warm model is not the same as verified prefix reuse. |
| vLLM and SGLang production metrics | Runtime metrics can turn scheduler claims into inspectable evidence. | Request counts, token counters, cache hit rate, preemptions, TTFT histograms, queue/running state where exposed. | A paper claim has support only if runtime state changes in the predicted direction under a controlled workload. | [[LLM/Study/Local LLM Observability and Operations Runner|Observability runner]] plus metrics snapshots. | Missing metrics are not proof that the mechanism is absent. |

## Local Proof Routing

| If the paper claim is about | First route | Minimum local proof |
|---|---|---|
| Memory hierarchy or attention kernels | [[LLM/Study/Local LLM Runtime Comparison Runner|Runtime comparison runner]] | Same model, prompt suite, sampler, output cap, context target, and hardware path; compare timing and memory. |
| Continuous batching or scheduling | [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Serving internals and scheduler lab]] | Cold/warm, short/long, repeated-prefix, scheduler-state, queue, p95, and one-variable tuning rows. |
| KV cache capacity or fragmentation | [[LLM/Study/Local LLM KV Cache Sizing Runner|KV-cache sizing runner]] | Architecture-aware cache estimate, context, active sequences, cache dtype, observed memory, and preemption/OOM evidence. |
| Tail latency under mixed load | [[LLM/Study/Local LLM Queueing and Tail Latency Field Guide|Queueing and Tail Latency Field Guide]] | Arrival rate, service time, p95 total latency, p95 TTFT, utilization warning, error rate, and admission policy. |
| Prefix reuse | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner|Prompt cache and KV reuse runner]] | Repeated-prefix row, changed-prefix control, TTFT/prefill delta, cache metric if exposed, and privacy/cache decision. |
| Metrics and operations | [[LLM/Study/Local LLM Observability and Operations Runner|Observability and Operations Runner]] | `/v1/models`, loaded model, metrics, slots or queue state, redacted logs, resource snapshot, and next controlled action. |
| Deployment choice | [[LLM/Study/LLM Deployment Decision Matrix|Deployment Decision Matrix]] | Paper claim, local prediction, measured artifact, rejected alternative, privacy/cost/ops consequence, and retest trigger. |

## Oral Defense Prompts

Answer these without notes before claiming the serving-systems cluster is understood:

- Why can FlashAttention be exact and still faster?
- Why does static batching waste work in autoregressive decoding?
- Why can KV cache, not model weights, be the concurrency limiter?
- Why can chunked prefill lower tail latency for mixed short and long prompts?
- Why does prefix caching need a changed-prefix control?
- Which runtime metric would prove or falsify a PagedAttention, preemption, or prefix-reuse claim?
- What local evidence would make you reject a higher-throughput setting because p95 TTFT got worse?

## Proof Card Template

Copy this into a paper row, scheduler-lab result, or capstone workbook note.

| Field | Answer |
|---|---|
| Paper/source |  |
| Claim type | attention kernel / batching / KV cache / prefill-decode / prefix reuse / metrics |
| Mechanism |  |
| Local prediction |  |
| Controlled workload |  |
| Runtime and launch settings |  |
| Metrics or logs required |  |
| Primary proof artifact |  |
| Confounders controlled | model / quantization / prompt / sampler / output cap / context / hardware / route |
| Result | supports / contradicts / inconclusive |
| Next route |  |

Pass signal: the row states a paper-derived prediction before the local run, then accepts or rejects the runtime change from measured evidence instead of intuition.

## References

Internal routes:

- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Paper Claim Ledger]]
- [[LLM/Study/LLM Paper-to-Local Proof Router]]
- [[LLM/Study/LLM Academic-to-Local Defense Matrix Runner]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Queueing and Tail Latency Field Guide]]
- [[LLM/Study/Local LLM KV Cache Sizing Runner]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Runner]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Runner]]
- [[LLM/Study/Local LLM Observability and Operations Runner]]
- [[LLM/Study/Local LLM Runtime Comparison Runner]]
- [[LLM/Study/LLM Deployment Decision Matrix]]

External sources checked 2026-06-16:

- [FlashAttention](https://arxiv.org/abs/2205.14135)
- [Orca: A Distributed Serving System for Transformer-Based Generative Models](https://www.usenix.org/conference/osdi22/presentation/yu)
- [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve](https://arxiv.org/abs/2403.02310)
- [vLLM Optimization and Tuning](https://docs.vllm.ai/en/stable/configuration/optimization/)
- [vLLM Production Metrics](https://docs.vllm.ai/en/v0.14.0/usage/metrics/)
- [SGLang paper](https://arxiv.org/pdf/2312.07104)
- [SGLang documentation](https://docs.sglang.io/)
- [SGLang production metrics](https://docs.sglang.io/docs/references/production_metrics)
