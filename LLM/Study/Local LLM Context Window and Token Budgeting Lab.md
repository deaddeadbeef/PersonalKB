---
tags: [study, llm, inference, local-llm, tokenization, context-window, benchmarking, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [core, practice]
last-verified: 2026-06-15
---

# Local LLM Context Window and Token Budgeting Lab

> **One-line summary** A local request fits only when system prompt, chat template, user text, history, retrieved context, tool schemas, reserved output, and safety margin all fit inside the runtime context limit.

Use this after [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] and before long-context, RAG, tool, or benchmark runs. The chat-template lab proves the request is serialized correctly. This lab proves the serialized request has a measured budget and will not silently crowd out the answer. Use [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Local LLM Context Window and Token Budgeting Runner]] when the same budget should be saved as JSON, CSV, Markdown, and JSONL evidence.

Pair this with [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] when you need to explain prefill latency, [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab|Local LLM Prompt Cache and KV Reuse Lab]] when repeated prefixes might reduce prefill or TTFT, [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] and [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]] when retrieved chunks consume context, and [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] when prompt tokens must explain TTFT and memory.

## Outcome

After this lab you should be able to:

- count prompt tokens with the same tokenizer or runtime that will serve the request
- reserve output tokens before filling the prompt window
- budget system text, chat-template overhead, user text, history, RAG chunks, tool schemas, and safety margin
- explain tokenizer differences across model families without comparing words or characters
- connect prompt length to prefill latency, KV-cache memory, and long-context failures
- diagnose context overflow, silent truncation, short answers, slow first token, and lost evidence

## Mental Model

Tokens are not words. The model sees token IDs produced by a specific tokenizer plus whatever special tokens and role markers the chat template adds. A context window is a shared sequence budget: prompt tokens and generated tokens compete for the same maximum sequence length.

For local hosting, context is also memory. Longer prompts increase prefill work before the first generated token. Longer active sequences grow the [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV cache]]. RAG chunks, chat history, tool schemas, and verbose system prompts are not free metadata; they are prompt tokens.

## Context Budget Formula

Use this planning equation before a long or document-grounded request:

```text
runtime context limit
  >= system and policy tokens
   + chat-template and special-token overhead
   + current user/task tokens
   + chat history tokens
   + retrieved context tokens
   + tool/schema tokens
   + reserved output tokens
   + safety margin
```

Starter policy:

| Budget item | Starter rule |
|---|---|
| Runtime context limit | Copy from runtime setting or model metadata, not from memory. |
| Reserved output | Decide first; use the smallest cap that can complete the task. |
| Safety margin | Keep 5-10 percent open unless the runtime has proven truncation behavior. |
| History | Keep only turns needed for the task. Summarize or drop stale turns. |
| Retrieved context | Budget by token count, not chunk count. |
| Tool schemas | Count the rendered schema or route-specific tool payload when possible. |

Pass signal: you can say exactly why the request fits, what will be removed first if it does not fit, and how many output tokens remain.

## Runtime Context Map

| Runtime or stack | Context control | Output cap | Token evidence to capture |
|---|---|---|---|
| Ollama | `num_ctx`, app context setting, or `OLLAMA_CONTEXT_LENGTH` when serving | `num_predict` or OpenAI-compatible `max_tokens` | `prompt_eval_count`, `eval_count`, `ollama ps` context column, Modelfile settings. |
| llama.cpp server | Server context-size setting and loaded model metadata | OpenAI-compatible `max_tokens` or native `n_predict` | Token-count endpoint or server metrics/log fields when enabled. |
| vLLM | `--max-model-len`, model config, GPU memory fit | OpenAI-compatible request cap | Usage fields, engine args, truncation settings, server logs. |
| Hugging Face Transformers | `tokenizer.model_max_length` or model config, plus generation limits | `max_new_tokens` | `apply_chat_template(..., tokenize=True)` output length and generated token count. |
| OpenAI-compatible clients | Provider/running server decides the real context | `max_tokens` or compatible output field | Request body, response usage, and provider-specific unsupported-field notes. |

Do not assume the model card limit, runtime launch setting, and client output cap are the same thing. A server may lower context because of memory, ignore an unsupported field, or apply a template you did not count.

## Lab 1: Tokenizer Sanity Count

Use the serving tokenizer, not a convenient different tokenizer. Count this small set before counting a production prompt.

| Text class | Example | Token count | Observation |
|---|---|---:|---|
| Plain English | `The model answered correctly.` |  | Baseline compression. |
| Mixed script | English + Japanese/Chinese/code switch |  | Tokenization tax for the target workload. |
| Code identifier | `parseHTTPRequestBody` |  | Identifier splitting. |
| JSON boundary | `{"answer":"yes"}` |  | Structured-output overhead. |
| Whitespace | `line 1\n  line 2` |  | Formatting preservation. |
| Role-marker-like text | `<|assistant|>` or model-family marker |  | Normal text vs special token behavior. |

If two models have different token counts for the same text, compare latency by prompt tokens, not by characters.

## Lab 2: Render Then Count The Real Prompt

Take one chat request and count the exact sequence that the model sees.

| Component | Token count | Evidence |
|---|---:|---|
| System prompt |  |  |
| Chat template and role markers |  |  |
| User task |  |  |
| Chat history |  |  |
| Retrieved context |  |  |
| Tool schema or JSON mode instruction |  |  |
| Reserved output cap |  |  |
| Safety margin |  |  |
| Runtime context limit |  |  |

Pass signal: the full rendered request plus reserved output fits below the runtime limit with margin.

With Hugging Face Transformers, prefer counting `apply_chat_template(..., tokenize=True)` output when available because it includes role markers and special tokens. If you render first and tokenize later, make sure special tokens are not duplicated.

## Lab 3: RAG Packing Budget

Before adding retrieval to a local endpoint, calculate how many retrieved tokens can fit.

```text
available retrieval budget =
  runtime context limit
  - reserved output tokens
  - safety margin
  - system/template/user/history/tool tokens
```

Then choose a packing policy:

| Decision | Record |
|---|---|
| Chunk size in tokens |  |
| Top-k before rerank |  |
| Top-k packed into prompt |  |
| Citation metadata tokens |  |
| Delimiter/header overhead |  |
| Maximum packed context tokens |  |
| Truncation/drop policy |  |

Pass signal: the assistant can explain why a relevant chunk was included, excluded, or truncated without relying on vague "context is too long" language.

## Lab 4: Overflow And Truncation Test

Deliberately exceed the budget with harmless content. Record what the runtime does.

| Runtime | Over-budget request | Observed behavior | Safe policy |
|---|---|---|---|
|  |  | Error / truncates oldest / truncates newest / stalls / OOM / unknown |  |

Do not rely on a runtime's default truncation policy for important tasks. Silent truncation can remove the system instruction, current question, citation evidence, or output room.

## Lab 5: Prompt-Length Performance Test

Run the same answer task at three prompt lengths. Keep model, runtime, sampler settings, output cap, and endpoint route fixed.

| Run | Prompt tokens | Reserved output | Actual output tokens | TTFT | Total latency | Decode tokens/sec | Peak RAM/VRAM | Interpretation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Short |  |  |  |  |  |  |  |  |
| Medium |  |  |  |  |  |  |  |  |
| Long |  |  |  |  |  |  |  |  |

Interpretation:

- TTFT usually grows with prompt length because prefill processes the prefix first.
- Decode tokens/sec depends more on model size, backend, memory bandwidth, and active sequences.
- Memory growth on longer prompts points to KV-cache pressure, not just weight memory.

## Failure Triage

| Symptom | Likely cause | First fix |
|---|---|---|
| Context length exceeded | Prompt plus output reserve does not fit | Count rendered prompt and reduce history/RAG/tool text. |
| Answer cuts off | Output reserve or stop policy too small | Raise output cap after reducing prompt or context. |
| Important evidence ignored | Retrieval packing, rank order, or lost-in-the-middle effect | Reduce noise, rerank, place key evidence deliberately, or shorten chunks. |
| First token slow | Long prefill, queueing, or large context | Compare prompt tokens and TTFT across short/long runs. |
| OOM only on long prompts | KV-cache growth | Lower context, top-k, history, or concurrency. |
| Same text has different latency by model | Tokenizer difference | Compare prompt token counts by model tokenizer. |
| Role markers appear in output | Chat template or stop mismatch | Return to [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]]. |
| Tool/RAG prompt fails only after adding schemas | Tool schema or context overhead | Count schema tokens and reserve output before packing retrieval. |

## Benchmark Add-On

Add these fields to [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] whenever context length or prompt packing matters:

| Field | Why |
|---|---|
| Runtime context limit | Defines the hard or configured sequence budget. |
| Prompt tokens | Explains prefill and context pressure. |
| Reserved output tokens | Prevents long prompts from starving the answer. |
| Actual output tokens | Normalizes latency and stop behavior. |
| Chat-template overhead | Explains hidden prompt differences. |
| Shared prefix tokens | Explains whether a repeated-prefix cache can help. |
| RAG/context tokens | Separates retrieval cost from user prompt cost. |
| Tool/schema tokens | Makes tool-call overhead visible. |
| History turns included | Explains multi-turn drift and token growth. |
| Truncation policy tested? | Prevents silent data loss. |

## Completion Gate

This lab is complete when you have:

- [ ] tokenizer sanity counts for the served model
- [ ] one rendered chat prompt counted with template overhead
- [ ] one context budget table with output reserve and safety margin
- [ ] optional runner output from [[LLM/Study/Local LLM Context Window and Token Budgeting Runner|Local LLM Context Window and Token Budgeting Runner]] when the budget needs repeatable evidence
- [ ] one RAG or long-context packing policy if the workload uses external context
- [ ] one overflow/truncation observation for the runtime
- [ ] one short/medium/long prompt performance comparison
- [ ] one benchmark row updated with context-budget fields
- [ ] one written decision about what to drop first when the request does not fit

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Pre-2017 — Before Transformers/Tokenization]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Runner]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Prompt Cache and KV Reuse Lab]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/Local LLM Troubleshooting Decision Tree]]
- [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
- [[LLM/2023 — Open Models and Agents/Chunking Strategies]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
- [[LLM/_chunks/chunk-llm-119 PagedAttention Copy-on-Write Sharing|chunk-llm-119]]
- [[LLM/_chunks/chunk-llm-169 SentencePiece Processes Raw Unicode Without Pre-Tokenization|chunk-llm-169]]
- [[LLM/_chunks/chunk-llm-171 SentencePiece Guarantees Lossless Detokenization|chunk-llm-171]]
- [[LLM/_chunks/chunk-llm-214 KV Cache Memory Bandwidth Bottleneck|chunk-llm-214]]

Current external docs checked 2026-06-15:

- [Hugging Face Transformers chat templates](https://huggingface.co/docs/transformers/en/chat_templating)
- [Hugging Face Transformers tokenizer docs](https://huggingface.co/docs/transformers/en/main_classes/tokenizer)
- [Ollama context length](https://docs.ollama.com/context-length)
- [Ollama Modelfile reference](https://docs.ollama.com/modelfile)
- [vLLM engine arguments](https://docs.vllm.ai/en/stable/configuration/engine_args/)
- [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/v0.18.0/serving/openai_compatible_server/)
- [llama.cpp HTTP server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
