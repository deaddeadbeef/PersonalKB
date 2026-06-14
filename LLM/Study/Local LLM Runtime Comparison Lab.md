---
tags: [study, llm, inference, local-llm, runtime, benchmark]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [practice]
last-verified: 2026-06-15
---

# Local LLM Runtime Comparison Lab

> **One-line summary** Runtime comparison is a controlled experiment: keep the workload, prompt suite, sampler, context target, model family, and evidence schema fixed, then change one serving layer at a time.

Use this after [[LLM/Study/Local LLM Environment Preflight Lab|Local LLM Environment Preflight Lab]], [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist|Local LLM Model Acquisition and Provenance Checklist]], [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]], and [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]. Those notes prove that a candidate can run. This lab proves whether one runtime is better for a named workload than another.

Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] to run the same request shape against each endpoint. Save speed rows in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], quality rows in [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], and the final choice in [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]].

Use [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab|Local LLM Concurrency and Batch Throughput Lab]] when runtime choice depends on batching, queueing, saturation, or multi-client throughput rather than only a single request. Use [[LLM/Study/Local LLM Quantization and GPU Offload Lab|Local LLM Quantization and GPU Offload Lab]] when runtime choice depends on GGUF versus AWQ/GPTQ/FP8/INT8, GPU offload, CPU fallback, or KV-cache precision. Use [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] when runtime choice depends on repeated system prompts, documents, examples, RAG context, tool protocols, or chat history. Use [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] when runtime choice depends on draft-model, EAGLE, MTP, n-gram, or another speculative decoding path.

## What This Lab Decides

This lab answers a narrow question:

> For this workload, on this machine, is runtime A or runtime B the better serving path?

Do not use it to crown a universal best runtime. A desktop GUI can beat a server stack for a private Windows workflow. A GPU server stack can beat a desktop runtime for concurrent traffic. A low-level GGUF server can beat both when the job is edge control, explicit quantization, or CPU inference.

## Comparison Rule

Make the comparison fair before measuring:

```text
same workload -> same prompts -> same sampler -> same context target -> same output cap -> one changed serving layer
```

If the model artifact cannot be the same, keep the model family, size class, instruction tuning, and quantization as close as possible, then mark the comparison as approximate. If the tokenizer or chat template differs, the comparison is partly a compatibility comparison, not only a runtime comparison.

If a reasoning model is involved, also freeze thinking mode, effort value, reasoning parser, output cap, and trace visibility policy. Otherwise the comparison is partly a reasoning-budget comparison.

## Candidate Pairs

| Pair | Best question | Keep fixed | Main evidence |
|---|---|---|---|
| Ollama vs LM Studio | Which Windows desktop path is easiest and compatible enough? | Same model family/size if possible, same OpenAI-compatible prompt. | Setup friction, served model id, endpoint shape, timing, quality. |
| Ollama vs llama.cpp | Managed local model package or explicit GGUF/server control? | Same GGUF or closest Ollama package, same context and sampler. | Quantization evidence, template behavior, timing fields, memory, route differences. |
| llama.cpp vs vLLM | Laptop/edge control or GPU serving stack? | Same model family/size, same chat prompt and output cap. | TTFT, decode speed, memory, batching/concurrency, API support. |
| vLLM vs SGLang | General GPU serving or structured/prefix-heavy serving? | Same Hugging Face model id/path, same prompt suite. | Batch behavior, structured output, tool/parser support, latency and throughput. |
| Runtime vs UI frontend | Does a UI change behavior after provider endpoint works? | Same provider endpoint and prompt. | Proves whether the issue belongs to the frontend, not the model server. |

Open WebUI and similar tools are frontends over providers. Do not compare them as model loaders until the underlying Ollama, LM Studio, llama.cpp, vLLM, SGLang, or other provider endpoint is already proven.

## Evidence Prerequisites

Before the first comparison run, fill these rows:

| Evidence | Required before comparison |
|---|---|
| Machine preflight | OS, shell, CPU/RAM, GPU/VRAM, disk, runtime boundary, host/port plan. |
| Acquisition card | Model card, license, gated access, exact artifact, revision/tag/digest, local path. |
| Compatibility card | Artifact container, quantization, tokenizer, chat template, runtime support, model id, route. |
| Quantization/offload card | Baseline quant, accepted quant, GPU offload, CPU/GPU split, KV-cache type, memory headroom, quality result. |
| Security boundary | Loopback binding by default, log/data boundary known, no accidental LAN exposure. |
| Prompt suite | At least one smoke prompt, one workload prompt, one structured prompt, and one long-context or RAG prompt if relevant. |
| Sampler preset | Temperature, top-p, top-k/min-p when supported, penalties, seed behavior, stops, max output tokens. |
| Reasoning settings | Thinking mode, reasoning effort, parser setting, output split, trace length policy, and trace visibility policy when a reasoning-capable model is used. |
| Concurrency settings | Max concurrency, request rate, queue limit, batch/offline mode, and backpressure policy if more than one request is active. |
| Prompt-cache settings | Cold/warm separation, repeated-prefix run, changed-prefix control, cache evidence, and prompt layout if repeated prefixes matter. |
| Speculative decoding settings | No-spec baseline, spec method/model, accepted-token evidence, decode-latency delta, memory overhead, and quality result if a draft path matters. |
| Measurement schema | TTFT, total latency, output tokens/sec, prompt tokens, output tokens, peak RAM/VRAM, error class, quality score. |

If any row is missing, the comparison can still be exploratory, but it should not drive a deployment decision.

## Endpoint Map

Use explicit base URLs so the client harness can swap runtimes without changing prompt logic.

| Runtime | First endpoint or base URL | First proof |
|---|---|---|
| Ollama native | `http://localhost:11434/api/generate` | Native response plus usage fields such as prompt and eval durations. |
| Ollama OpenAI-compatible | `http://localhost:11434/v1` | `/v1/chat/completions` works with an OpenAI-compatible client. |
| LM Studio | `http://localhost:1234/v1` | `/v1/models` and `/v1/chat/completions` use the loaded model id. |
| llama.cpp server | `http://localhost:8080/v1` by default | `llama-server` loads the GGUF and `/v1/chat/completions` responds. |
| vLLM | `http://localhost:8000/v1` by default | `vllm serve <model>` starts the OpenAI-compatible server. |
| SGLang | chosen launch port, often `http://localhost:30000/v1` in local examples | `python -m sglang.launch_server ...` starts and answers via OpenAI-compatible chat completions. |

Loopback is the default for local experiments. If a command or UI binds to `0.0.0.0`, stop and run [[LLM/Study/Local LLM Security and Privacy Runbook|Local LLM Security and Privacy Runbook]] before continuing.

## Shared Smoke Request

Use one small request for the endpoint proof:

```powershell
$BaseUrl = "http://localhost:1234/v1"
$Model = "<served-model-id>"
$Body = @{
  model = $Model
  messages = @(
    @{ role = "user"; content = "Reply with exactly: local runtime ok" }
  )
  temperature = 0
  max_tokens = 16
} | ConvertTo-Json -Depth 6

Invoke-RestMethod `
  -Uri "$BaseUrl/chat/completions" `
  -Method Post `
  -ContentType "application/json" `
  -Headers @{ Authorization = "Bearer local" } `
  -Body $Body
```

Change only `$BaseUrl` and `$Model` for an OpenAI-compatible comparison. If the runtime has a useful native endpoint, such as Ollama `/api/generate`, record that separately rather than mixing it into the OpenAI-compatible comparison row.

## Prompt Suite

Run at least these prompts with the same system message, sampler, and output cap.

| Prompt id | Purpose | Expected behavior |
|---|---|---|
| SMOKE-01 | Endpoint shape | Exact phrase or small deterministic response. |
| WORK-01 | Real workload | Solves the actual task class you care about. |
| JSON-01 | Structured output | Valid JSON matching a small schema. |
| LONG-01 | Prefill/context pressure | Uses the relevant span without losing the instruction. |
| RAG-01 | Retrieval/citation, if relevant | Answers only from supplied evidence and refuses missing support. |
| TOOL-01 | Tool/schema, if relevant | Produces a valid call or structured output without executing unsafe work. |

Do not tune the prompt after seeing runtime A and then reuse the tuned prompt against runtime B. Either freeze it first or rerun both sides.

## Measurement Table

Create one row per runtime and prompt.

| Run id | Runtime | Model/artifact | Base URL | Prompt id | Prompt tokens | Output tokens | TTFT | Total latency | Tokens/sec | Peak RAM/VRAM | Quality score | Error/failure layer | Decision |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  | pass/hold/fail |  | keep/tune/reject |

For Ollama native calls, save `total_duration`, `load_duration`, `prompt_eval_count`, `prompt_eval_duration`, `eval_count`, and `eval_duration`. For llama.cpp server responses, save the `timings` and `usage` objects when present. For OpenAI-compatible routes that do not expose all timings, use the client harness to record wall-clock TTFT and total latency.

## Interpret The Result

| Observation | Plausible meaning | Next controlled change |
|---|---|---|
| Runtime A loads and B cannot load | Artifact, quantization, architecture, or hardware support mismatch. | Fill the compatibility card before changing model. |
| Same model, different role-marker behavior | Chat template or tokenizer handling differs. | Run [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]]. |
| A has better TTFT, similar decode speed | Prefill, prompt caching, scheduling, or cold-start path differs. | Compare short vs long prompt, warm vs cold run, and repeated-prefix vs changed-prefix controls. |
| A has similar TTFT, better tokens/sec | Decode loop, speculative decoding, offload, kernel, quantization, or memory bandwidth differs. | Check hardware utilization, draft-token acceptance, quantization, GPU layers, and backend logs. |
| A is faster but quality drops | Runtime path, quantization, template, sampler default, or output cap changed. | Freeze sampler and rerun quality harness before accepting speed. |
| B is slower but more stable under load | Scheduler, batching, KV cache, or memory management is better for concurrency. | Add a small concurrency sweep before deployment. |
| UI behavior differs but provider output matches | Frontend prompt assembly, model id, history, system message, or stop policy differs. | Debug UI settings after provider endpoint is proven. |

The common mistake is treating every difference as runtime quality. Many differences are actually model artifact, tokenizer/template, sampler default, context, or client-route differences.

## Decision Card

Copy this into the benchmark log, capstone workbook, or project note.

| Field | Value |
|---|---|
| Workload |  |
| Candidate runtimes |  |
| Comparison type | exact artifact / closest equivalent / UI-over-same-provider |
| Frozen prompt suite |  |
| Frozen sampler/output cap |  |
| Compatibility cards |  |
| API contract cards |  |
| Benchmark rows |  |
| Quality rows |  |
| Security boundary |  |
| Winner |  |
| Why it won | quality / TTFT / tokens-sec / memory / reliability / setup / API support / security |
| Rejected alternative |  |
| Remaining uncertainty |  |
| Next review trigger | new model, new hardware, new runtime version, new workload, concurrency change |

## Completion Gate

The runtime comparison is complete when:

- [ ] two candidate runtimes have compatibility evidence cards
- [ ] both runtimes answer the same smoke request, or one has a named load/route failure
- [ ] the same prompt suite, sampler, context target, and output cap were used
- [ ] benchmark rows record TTFT, total latency, output tokens/sec or timing substitute, prompt/output tokens, and memory where available
- [ ] quality rows explain pass, hold, or fail for the workload
- [ ] at least one difference is assigned to a concrete layer: artifact, tokenizer, template, runtime, route, sampler, hardware, context, quality, UI, or security
- [ ] the winning runtime and rejected alternative are written as a decision card
- [ ] the deployment matrix uses the decision instead of a preference

## References

Internal routes:

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM Environment Preflight Lab]]
- [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]]
- [[LLM/Study/Local LLM Quantization and GPU Offload Lab]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding]]

Current external docs checked 2026-06-15:

- [Ollama API introduction](https://docs.ollama.com/api/introduction)
- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [Ollama usage metrics](https://docs.ollama.com/api/usage)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [LM Studio OpenAI compatibility endpoints](https://lmstudio.ai/docs/developer/openai-compat)
- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/latest/serving/online_serving/openai_compatible_server/)
- [vLLM CLI guide](https://docs.vllm.ai/en/latest/cli/)
- [SGLang OpenAI-compatible chat completions](https://docs.sglang.io/docs/basic_usage/openai_api_completions)
