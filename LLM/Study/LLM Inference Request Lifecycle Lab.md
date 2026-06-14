---
tags: [study, llm, inference, local-llm, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [core, practice]
---

# LLM Inference Request Lifecycle Lab

> **One-line summary** A local LLM request is not just "send prompt, get text"; it is a pipeline from messages to tokens, prefill, logits, sampling, stopping, detokenization, streaming, and measurement.

Use this after [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]] proves the endpoint exists. The hosting lab answers "can I run it?" This lab answers "do I understand what happens during one request?" Use [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] when the sampling step needs deeper tuning, reproducibility, or runtime-parameter comparison. Use [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] when prompt length, reserved output, history, RAG context, or tool schemas may change the result. Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] when the frozen request should become a reusable script.

## Outcome

After this lab you should be able to:

- trace a prompt from text through tokenization, prefill, decode, sampling, stopping, and returned text
- explain why time to first token and decode tokens/sec measure different phases
- change one sampling knob at a time without confusing quality, randomness, and latency
- diagnose common request-level failures such as bad stop sequences, missing max-token caps, malformed JSON, and unstable high-temperature output
- record request settings so a benchmark or quality evaluation is reproducible
- turn one frozen request into a client harness row with timing, parsing, error, and benchmark fields

## Request Lifecycle

| Stage | What happens | Evidence to capture |
|---|---|---|
| 1. Client request | The caller sends model id, messages or prompt, sampling parameters, output cap, and stream flag. | Full request body, client code, or [[LLM/Study/Local LLM Client Harness Lab|client harness]] config. |
| 2. Prompt assembly | Chat messages become the runtime's prompt format or chat template. RAG systems may add retrieved context here. Use [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] if the formatting is uncertain. | System prompt, user prompt, retrieved context, and template if visible. |
| 3. Tokenization | Raw text becomes token IDs. Token count determines context use, output headroom, and prefill cost. | Prompt token count, rendered-template token count, or [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|context budget]] when available. |
| 4. Prefill | The model processes the whole input prefix and builds the initial [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV cache]]. | Time to first token, prompt token count, cache/context length. |
| 5. Decode loop | Each step produces logits for the next token, applies constraints and sampling settings, appends one token, and extends the cache. | Decode tokens/sec, output token count, sampling settings. |
| 6. Stop condition | Generation stops at an EOS token, stop sequence, tool/schema boundary, or max-token cap. | Stop reason, stop sequence, max output tokens. |
| 7. Detokenization | Token IDs are converted back into text or structured output. | Returned text plus any parse/validation result. |
| 8. Application handling | The caller displays, streams, parses, stores, evaluates, or retries the response. | Parsed object, citation check, client harness row, benchmark row, or quality decision. |

The key academic bridge is [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals|Language Model Fundamentals]]: autoregressive generation samples a next-token distribution, appends the token, and repeats. Use [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]] when you want to see the same logits and sampling loop inside a toy model you trained yourself. The key deployment bridge is [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]]: prefill and decode have different performance bottlenecks.

## Sampling Knobs

| Knob | What it controls | Use when | Failure mode |
|---|---|---|---|
| `temperature` | Scales logits before softmax. Lower is more deterministic; higher is more varied. | Lower for extraction, citation-heavy RAG, tests, and structured output. | Too high causes unstable facts and format drift; too low can be repetitive. |
| `top_p` | Sorts likely tokens and keeps the smallest set whose cumulative probability reaches `p`. | General creative variation without opening the whole vocabulary. | Too low can make output bland or truncate plausible alternatives. |
| `top_k` | Keeps only the `k` most likely tokens. | Runtimes where fixed shortlist control is useful. | Too small can force awkward phrasing or wrong tokens. |
| `max_tokens` | Caps generated output length. | Every benchmark and endpoint smoke test. | Missing caps cause runaway cost, latency, or rambling. |
| `stop` | Ends generation when a token sequence appears. | Delimited outputs, tool protocols, or transcript boundaries. | Bad stops cut valid output or fail to stop at all. |
| Seed, if supported | Controls random-number initialization. | Reproducible comparisons. | Unsupported or hidden seeds make repeated sampling hard to compare. |
| Grammar/schema constraints | Masks invalid next tokens or validates structure. | JSON, tool calls, SQL-like output, extraction. | Wrong schema can force lossy or invalid answers. |

For deterministic tests, start with low temperature, a clear `max_tokens` cap, and the same prompt every time. For brainstorming or alternate phrasings, raise temperature only after the baseline answer is correct. For a full temperature/top-p/top-k/min-p/penalty sweep, use [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]].

## Lab 1: Freeze One Request

Choose one served model and one local endpoint from [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]. Save the exact request:

| Field | Value |
|---|---|
| Runtime |  |
| Model id |  |
| Endpoint |  |
| System prompt |  |
| User prompt |  |
| Context/RAG input |  |
| Temperature |  |
| Top-p |  |
| Top-k |  |
| Max output tokens |  |
| Stop sequences |  |
| Stream mode |  |

Pass signal: another run can reproduce the same request settings without guessing.

## Lab 2: Separate Prefill From Decode

Run the same prompt twice: once with a short input, once with a longer input. Keep model, runtime, sampling, and max output tokens fixed. For RAG, tool, or multi-turn prompts, fill a budget row in [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] first.

Record:

| Run | Prompt tokens | Output tokens | Time to first token | Total latency | Decode tokens/sec | Notes |
|---|---:|---:|---:|---:|---:|---|
| Short prompt |  |  |  |  |  |  |
| Long prompt |  |  |  |  |  |  |

Interpretation:

- If time to first token grows sharply with prompt length, the bottleneck is likely prefill, context assembly, or queueing.
- If tokens/sec is weak after the first token, the bottleneck is likely decode speed, model size, memory bandwidth, quantization, or hardware.
- If memory spikes only on the long prompt, inspect KV-cache growth before blaming the model weights.

## Lab 3: Sampling A/B Test

Use one factual prompt and one open-ended prompt. Keep the prompt and model fixed. Change one knob at a time.

| Run | Prompt class | Temperature | Top-p | Top-k | Max tokens | Output summary | Decision |
|---|---|---:|---:|---:|---:|---|---|
| Baseline | Factual | 0 |  |  |  |  |  |
| Higher temperature | Factual |  |  |  |  |  |  |
| Baseline | Open-ended | 0 |  |  |  |  |  |
| Higher temperature | Open-ended |  |  |  |  |  |  |

Pass signal: you can explain whether the change affected correctness, diversity, format, latency, or only wording.

## Lab 4: Stop And Structure

Run two controlled outputs:

1. A delimited answer with a stop sequence.
2. A JSON answer with a simple schema expectation.

Record:

| Test | Expected boundary | Actual stop reason | Parse/validation result | Fix needed |
|---|---|---|---|---|
| Stop sequence |  |  |  |  |
| JSON object |  |  |  |  |

Use [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation|Structured Output and Constrained Generation]] when prompt-only formatting is not enough. A response that looks correct in chat but fails parsing has not passed the application boundary.

## Lab 5: Streaming Versus Non-Streaming

Run the same request once with streaming off and once with streaming on if the runtime supports it.

| Mode | User-visible first output | Total latency | Output tokens | Notes |
|---|---:|---:|---:|---|
| Non-streaming |  |  |  |  |
| Streaming |  |  |  |  |

Pass signal: you can explain why streaming can improve perceived responsiveness even when total generation time is similar.

## Request-Level Failure Triage

| Symptom | Likely layer | First check |
|---|---|---|
| Output starts in the wrong role or style | Prompt assembly/chat template | Verify system/user messages and runtime template. |
| Good short answers, bad long-context answers | Context assembly or prefill pressure | Count prompt tokens with [[LLM/Study/Local LLM Context Window and Token Budgeting Lab|Local LLM Context Window and Token Budgeting Lab]] and inspect retrieved context order. |
| Correct idea but invalid JSON | Structured output boundary | Add schema validation or constrained decoding. |
| Output cuts off mid-answer | `max_tokens` or stop sequence | Raise cap or inspect stop strings. |
| Output rambles | Missing cap or weak stop | Add `max_tokens`, stop sequence, or stricter prompt. |
| Same benchmark changes every run | Sampling randomness | Lower temperature, fix seed if supported, and keep parameters stable. |
| First token slow, later tokens okay | Prefill, context, or queueing | Compare prompt tokens and server queue/concurrency. |
| Later tokens slow | Decode bottleneck | Inspect model size, quantization, GPU offload, and KV cache. |
| Instruct model behaves like raw text completion | Chat-template or tokenizer mismatch | Run [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]]. |

## Benchmark Row Add-On

Append these request-level fields to the run row in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]:

| Field | Why |
|---|---|
| Prompt tokens | Explains prefill cost and context pressure. |
| Output tokens | Normalizes total latency and tokens/sec. |
| Temperature/top-p/top-k | Makes quality and reproducibility interpretable. |
| Max output tokens | Prevents accidental unbounded comparisons. |
| Stop reason | Separates successful completion from truncation. |
| Stream mode | Distinguishes perceived latency from total latency. |
| Parse/validation result | Required for structured output and tool boundaries. |

## Completion Gate

This lab is complete when you have:

- [ ] one frozen local request with model, endpoint, prompt, and sampling settings
- [ ] one short-vs-long prompt comparison separating prefill from decode
- [ ] one sampling A/B test with a written decision
- [ ] one stop-sequence or structured-output boundary test
- [ ] one streaming comparison if the runtime supports streaming
- [ ] one client harness log row with status, timing, and error fields
- [ ] one benchmark row updated with request-level fields
- [ ] one explanation linking the observed bottleneck to tokenization, KV cache, sampling, or serving

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals]]
- [[LLM/Pre-2017 — Before Transformers/Tokenization]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding]]
- [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[chunk-llm-119 PagedAttention Copy-on-Write Sharing]]
- [[chunk-llm-214 KV Cache Memory Bandwidth Bottleneck]]
- [[chunk-llm-222 Speculative Sampling Distribution Guarantee]]
