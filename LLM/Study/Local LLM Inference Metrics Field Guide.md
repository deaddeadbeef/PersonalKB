---
tags: [study, llm, inference, local-llm, metrics, benchmark, latency, throughput]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [intuition, core, practice]
last-verified: 2026-06-15
---

# Local LLM Inference Metrics Field Guide

> **One-line summary** Local inference metrics are useful only when each number is tied to a phase, claim, confounder, and next controlled action.

Use this after [[LLM/Study/Local LLM End-to-End Mental Model|Local LLM End-to-End Mental Model]] and before [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]], or [[LLM/Study/Local LLM Serving Internals and Scheduler Lab|Local LLM Serving Internals and Scheduler Lab]]. Use [[LLM/Study/Local LLM First Response Debrief Card|Local LLM First Response Debrief Card]] when the immediate job is to interpret one first Ollama response JSON, and [[LLM/Study/Local LLM First Streaming Timing Runner|Local LLM First Streaming Timing Runner]] when the immediate job is to separate first stream event, first visible content delta, chunk count, and total latency. [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide|LLM Metrics and Evaluation Interpretation Guide]] explains metrics across training, papers, evaluation, and deployment. This note is the local inference field guide: what each measurement means during a real served request.

## Measurement Rule

Do not write a number without its owner.

```text
metric -> request phase -> claim -> confounder -> next controlled action
```

Example:

```text
TTFT high -> prefill or queue phase -> prompt/context is expensive
-> confounders: cold load, streaming client, prefix cache miss, queue
-> next action: compare cold/warm short/long prompts before changing model
```

## Request Timeline Metrics

| Metric | Phase | What it can prove | What it cannot prove |
|---|---|---|---|
| Load time | Before request or first request | Model residency, disk/load overhead, startup penalty. | Steady-state decode speed or quality. |
| Queue wait | Before prefill | Server saturation, admission policy, or too much concurrency. | Model weakness. |
| First stream event | Stream transport | The server began returning streamed events. | The user saw meaningful text. |
| Time to first token (TTFT) | Queue plus prefill plus first decode step | Cold start, prompt length, context assembly, scheduler, or cache effects. | Later-token speed by itself. |
| First content delta | Stream parser and first visible token/text | The user-visible answer began. | The final answer is correct or complete. |
| Prefill tokens/sec | Prompt processing | How efficiently input context is processed when exposed by the runtime. | Answer quality or decode speed. |
| Time per output token (TPOT) / inter-token latency (ITL) | Decode | Later-token speed, memory bandwidth, kernel/offload path, active sequence pressure. | Prompt/context cost. |
| Output tokens/sec | Decode as seen by user/client | User-visible generation rate under the measured condition. | Throughput under load or correctness. |
| Total latency | Whole request | User wait time for this prompt and output length. | Which phase caused the wait. |
| Prompt tokens | Prompt assembly and prefill | Context cost, KV-cache floor, and fair comparison denominator. | Semantic difficulty. |
| Output tokens | Decode | Normalizes total latency and cost of long answers. | Whether the answer is useful. |
| Peak RAM/VRAM | Load, KV cache, runtime overhead | Fit, headroom, and OOM risk. | Correctness, safety, or route compatibility. |
| Active requests / queue depth | Scheduler | Saturation, batching, backpressure, and p95 risk. | Single-request quality. |
| Error rate / timeout rate | Whole stack | Stability boundary for workload and traffic. | Root cause without logs and layer evidence. |
| Quality pass/hold/fail | Evaluation | Whether speed is usable for the workload. | Hardware efficiency or serving bottleneck. |

## Claims By Metric

| Claim | Strongest first evidence | Route |
|---|---|---|
| The endpoint responds. | Smoke response, served model id, route, status code. | [[LLM/Study/Local LLM Serving Runbook]] |
| The prompt is too long. | Rendered prompt tokens, output reserve, context margin. | [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]] |
| First token is slow because of input work. | Short-vs-long TTFT with warm model and fixed output cap. | [[LLM/Study/LLM Inference Request Lifecycle Lab]] |
| Later tokens are slow. | TPOT/ITL or output tokens/sec across fixed prompts. | [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]] |
| Model fits but workload does not. | Weight memory plus KV/cache/concurrency headroom. | [[LLM/Study/Local LLM Model and Hardware Sizing Guide]] |
| A quantization choice is acceptable. | Memory/speed gain plus unchanged quality row. | [[LLM/Study/Local LLM Quantization and GPU Offload Lab]] |
| Runtime A beats runtime B. | Same prompt suite, sampler, context, model family, route, benchmark, and quality rows. | [[LLM/Study/Local LLM Runtime Comparison Lab]] |
| A local setup handles shared use. | Concurrency ladder with p50/p95 TTFT, throughput, memory, errors, and backpressure. | [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]] |
| Repeated prefixes help. | Repeated-prefix run plus changed-prefix control and cache evidence. | [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]] |
| Speculative decoding helps. | No-spec baseline, spec run, accepted-token or latency evidence, memory, and quality. | [[LLM/Study/Local LLM Speculative Decoding Lab]] |
| The answer is good enough. | Workload-specific quality row with rubric and failure owner. | [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| The service is maintainable. | Logs, metrics, state, restart/rollback, and retest trigger. | [[LLM/Study/Local LLM Observability and Operations Runbook]] |

## Confounder Checklist

Control these before comparing numbers:

| Confounder | Why it matters |
|---|---|
| Cold versus warm model | First request can include loading and initialization. |
| Prompt token count | More input mainly changes prefill, context, and KV-cache pressure. |
| Output token count or cap | Longer answers make total latency look worse even with identical TPOT. |
| Sampler settings | Temperature, filters, stops, and schema constraints can change length and stability. |
| Chat template and tokenizer | Same visible text can become different token sequences. |
| Streaming client overhead | UI or client buffering can distort perceived first-token timing. |
| Route shape | Native and OpenAI-compatible endpoints may expose different timing fields. |
| Quantization and offload | Memory, decode speed, and quality can all change together. |
| Hardware boundary | Windows, WSL, Docker, CPU, GPU, and shared memory paths are not equivalent. |
| Concurrency | Single-user speed does not predict p95 latency under load. |
| Prefix cache | Warm model is not the same as repeated-prefix KV reuse. |
| Model revision or artifact | A tag, GGUF file, adapter, or converted model can silently differ. |

If two rows differ on more than one confounder, treat the result as exploratory.

## Minimum Benchmark Row

Use [[LLM/Study/Local LLM First Benchmark Row Builder|Local LLM First Benchmark Row Builder]] to generate this row from the first client and streaming logs when those files already exist. Use this row for the first credible local inference benchmark:

| Field | Value |
|---|---|
| Run id |  |
| Date |  |
| Workload and prompt id |  |
| Runtime and route |  |
| Model id and artifact |  |
| Quantization and offload |  |
| Hardware boundary | CPU / GPU / WSL / Docker / other |
| Cold or warm |  |
| Prompt tokens |  |
| Output cap and output tokens |  |
| Sampler settings |  |
| TTFT |  |
| TPOT / ITL |  |
| Output tokens/sec |  |
| Total latency |  |
| Peak RAM/VRAM |  |
| Queue or active requests |  |
| Quality pass/hold/fail |  |
| Failed or missing layer |  |
| Next controlled action |  |

Pass signal: another person can tell whether the next action is about prompt length, model size, runtime, quantization, scheduler, client, or quality.

## Triage Recipes

| Observation | First interpretation | Next controlled action |
|---|---|---|
| First request slow, later requests normal | Load/model residency. | Separate load time from request timing; record warm baseline. |
| Short prompt TTFT fine, long prompt TTFT high | Prefill/context pressure. | Count rendered tokens and reduce or cache the prefix. |
| TTFT high for short warm prompts | Queue, scheduler, route, or client overhead. | Inspect active requests, logs, route timing, and streaming client. |
| TPOT poor across all prompts | Decode bottleneck. | Check model size, quantization, offload, backend, and hardware utilization. |
| Total latency high but TPOT acceptable | Output too long or cap too high. | Fix output cap and compare task-complete answer length. |
| OOM only on long prompts | KV cache/context headroom. | Reduce context, retrieved chunks, output cap, or active sequences. |
| OOM only under concurrency | KV cache plus scheduler capacity. | Run concurrency ladder before changing model quality assumptions. |
| Fast response fails rubric | Quality is the blocker. | Keep speed evidence, then run quality harness or change model/prompt/RAG. |
| Runtime A faster but less accurate | Quantization, template, sampler, or artifact drift. | Freeze compatibility and quality rows before accepting speed. |
| UI feels slow but provider endpoint is fast | Client/UI layer. | Compare provider harness timing with UI timing. |

## Metric Anti-Patterns

- Reporting total latency without prompt tokens and output tokens.
- Comparing runtimes with different prompts, samplers, templates, or model artifacts.
- Treating warm-model speed as proof of prompt-cache reuse.
- Treating output tokens/sec as quality.
- Treating a single smoke response as deployment readiness.
- Raising concurrency until throughput improves while p95 TTFT becomes unusable.
- Keeping a quantization setting because it loads, without a quality row.
- Comparing a native endpoint timing object to an OpenAI-compatible client without naming the route difference.

## Completion Gate

You understand local inference metrics when you can answer these without notes:

- [ ] Which phase owns TTFT, and what confounders can inflate it?
- [ ] Why do TPOT and output tokens/sec measure decode, not prompt handling?
- [ ] Why must total latency be normalized by prompt and output tokens?
- [ ] Why can a model fit at load time but OOM under long context or concurrency?
- [ ] Why is warm model residency not the same as prefix-cache reuse?
- [ ] Which metric would make you reduce context instead of changing model?
- [ ] Which metric would make you change quantization or offload?
- [ ] Which metric would make you reject a fast model on quality grounds?
- [ ] What single next controlled action follows from the latest benchmark row?

## References

- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/Local LLM End-to-End Mental Model]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Local LLM First Response Debrief Card]]
- [[LLM/Study/Local LLM First Streaming Timing Runner]]
- [[LLM/Study/Local LLM First Benchmark Row Builder]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Observability and Operations Runbook]]
