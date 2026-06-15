---
tags: [study, llm, inference, local-llm, mental-model, serving, systems]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [intuition, core, practice]
last-verified: 2026-06-15
---

# Local LLM End-to-End Mental Model

> **One-line summary** A local LLM answer is not just "the model ran": it is a chain from model artifact, tokenizer, prompt template, runtime, prefill, decode, sampler, API route, client, evaluation, and operations evidence.

Use this before [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] when the system still feels like a black box. The lifecycle lab traces one request in detail. [[LLM/Study/LLM Mechanism-to-Inference Bridge Map|LLM Mechanism-to-Inference Bridge Map]] translates mechanisms into controls. This note is the end-to-end story: what must be true for bytes on disk to become a useful answer in an application.

## The Whole Loop

```text
workload -> client -> API route -> runtime -> model artifact -> tokenizer/template
-> prompt tokens -> prefill -> KV cache -> decode loop -> sampler/stops
-> text or structured output -> client handling -> evaluation -> operations decision
```

If any link is unproven, the answer may still appear in a chat UI, but the setup is not yet understood.

## One Request, Three Stories

| Story | What it says | Failure if ignored |
|---|---|---|
| Academic story | The model estimates a next-token distribution from tokenized context, learned weights, attention, and post-training behavior. | You can run commands but cannot explain why context, quantization, sampler, or chat template changed the result. |
| Systems story | A runtime loads model bytes, manages memory, builds KV cache during prefill, repeats decode steps, and serves results through a process and route. | You blame "model quality" for listener, memory, route, queue, or cache failures. |
| Product story | A client sends a workload-specific request, receives text or structured output, validates it, logs evidence, and decides whether the result is good enough. | You have a response but no pass/hold/fail decision, safety boundary, or reproducible path. |

Mastery means holding all three stories at once.

## Stack Layers

| Layer | Question to answer | Evidence route |
|---|---|---|
| Workload | What job is the model being asked to do, and what does success mean? | [[LLM/Study/Local LLM Workload to Model Selection Playbook]] |
| Client or UI | What program sends the request, receives the stream, handles errors, and stores evidence? | [[LLM/Study/Local LLM Client Harness Lab]] |
| API route | Which base URL, endpoint, model id, streaming mode, and error shape are being used? | [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]] |
| Runtime process | Which server loaded the model, on which boundary, with which launch flags and logs? | [[LLM/Study/Local LLM Serving Runbook]] |
| Hardware and boundary | Is the model running on CPU, GPU, WSL, Docker, or another boundary, and what can it access? | [[LLM/Study/Local LLM Environment Preflight Lab]] |
| Model artifact | Which exact weights, format, revision, quantization, and license are under test? | [[LLM/Study/Local LLM Model Acquisition and Provenance Checklist]] |
| Tokenizer and template | How do messages become token IDs, special tokens, role markers, and stop conditions? | [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]] |
| Prompt assembly | Which system prompt, history, RAG chunks, tool schemas, and output reserve fit in context? | [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]] |
| Prefill | How much input must be processed before the first generated token appears? | [[LLM/Study/LLM Inference Request Lifecycle Lab]] |
| Decode loop | How fast can the runtime generate one token at a time after prefill? | [[LLM/Study/Local LLM Inference Benchmark Log]] |
| Sampler and stops | How do logits become the returned text or schema, and where does generation stop? | [[LLM/Study/Decoding and Sampling Controls Lab]] |
| Scheduler and cache | What happens when requests, context length, or repeated prefixes compete for memory? | [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]] |
| Quality gate | Did the answer solve the workload under a known rubric, not just return quickly? | [[LLM/Study/Local LLM Quality Evaluation Harness]] |
| Operations boundary | Can the service be observed, secured, restarted, upgraded, and rolled back? | [[LLM/Study/Local LLM Observability and Operations Runbook]] |

## Academic Mechanism To Hosting Consequence

| Mechanism | Hosting consequence |
|---|---|
| Tokenization | A short-looking prompt can be many tokens, and a model-specific template can change the real input. |
| Decoder-only autoregression | The answer is produced by repeated next-token steps, so output length directly affects latency. |
| Attention | Long context increases prefill work and KV-cache memory; retrieval quality is not free just because context is large. |
| KV cache | More context and active sequences use memory even after the weights fit. |
| Quantization | Lower-bit artifacts can make a model loadable while changing quality, formatting, or rare-token behavior. |
| Sampling | Temperature, top-p, penalties, stops, seeds, and schema controls define the actual generation process. |
| Chat template | Instruction following can fail because messages were rendered incorrectly, not because the model is weak. |
| Batching and scheduling | Multi-user serving is a queue and cache problem, not only a "bigger GPU" problem. |
| RAG | The model can only use evidence that retrieval and context assembly actually provide. |
| Tools | The model proposes an action; the application validates, authorizes, executes, and feeds back the result. |
| Evaluation | A fast response is not a good response until it passes the workload rubric. |
| Deployment | Local ownership buys privacy and control only if the endpoint, logs, data, and update path are governed. |

## Request Narrative

1. The user asks for a task in a client or UI.
2. The client turns that task into a request body: model id, messages or prompt, sampler settings, output cap, and streaming choice.
3. The server route accepts the request and maps the model id to a loaded or loadable artifact.
4. The runtime locates model bytes, tokenizer files, chat template, quantization metadata, and hardware execution path.
5. The prompt is rendered into tokens, including role markers, special tokens, history, RAG context, tool schemas, and stop policy.
6. Prefill processes the full input and builds hidden states plus KV cache for the context.
7. Decode repeats: read current cache, compute logits for the next token, apply sampler or schema constraints, append token, update cache.
8. Detokenization turns token IDs back into text or structured output until a stop condition or token cap is reached.
9. The client receives the full response or stream, validates shape and policy, records timing and errors, and saves the run evidence.
10. The result is judged against the workload, then the next decision is made: keep, tune, shorten context, change runtime, change model, add RAG, add tools, or reject.

## Failure Ownership Ladder

Use this order before changing the model:

| Step | Ask | Evidence |
|---|---|---|
| 1 | Is the server process alive and bound to the expected host and port? | Process, port, listener, and log check. |
| 2 | Is the client calling the route and model id the server actually exposes? | `/v1/models` or equivalent route proof. |
| 3 | Did the intended artifact load with the intended quantization and hardware path? | Load log, model path, quantization, memory row. |
| 4 | Did the request use the correct tokenizer and chat template? | Rendered prompt and special-token check. |
| 5 | Did the prompt fit with enough output headroom? | Token budget row and context margin. |
| 6 | Did prefill, decode, queueing, or cache pressure explain the timing? | TTFT, tokens/sec, queue, memory, and context measurements. |
| 7 | Did sampler, stops, or schema controls explain the shape of output? | Frozen decoding settings and A/B sweep. |
| 8 | Did the answer pass the workload rubric? | Quality harness row. |
| 9 | Is the endpoint safe and maintainable for repeated use? | Security, observability, lifecycle, and rollback rows. |

Only after this ladder should "use a different model" become the default next action.

## A Good Local Inference Explanation

Use this as a verbal proof:

```text
The workload is:
The served model artifact is:
The runtime and route are:
The tokenizer/template renders the request as:
The context and output budget are:
Prefill cost should be high/low because:
Decode speed should be high/low because:
The sampler and stop policy are:
The response passed or failed because:
The next controlled change is:
```

If any line is blank, route to the matching lab before claiming understanding.

## What A First Endpoint Proves And Does Not Prove

| Evidence | Proves | Does not prove |
|---|---|---|
| CLI response | Runtime can load and generate for one request. | API compatibility, reproducibility, workload quality, or security. |
| HTTP smoke response | A route can accept a request and return text. | Correct tokenizer/template, quality, streaming behavior, or feature parity. |
| `/v1/models` response | A local server exposes a model list through an API contract. | The model is loaded, fast, safe, or suitable. |
| Benchmark row | Speed and memory under one controlled condition. | General quality or robustness. |
| Quality row | Performance against one workload rubric. | Operational readiness, safety, or future upgrade stability. |
| Security row | The endpoint exposure and data boundary are understood. | Model correctness or user value. |

## Completion Gate

You understand the end-to-end path when you can answer these without notes:

- [ ] How do bytes on disk become a served model id?
- [ ] How do chat messages become token IDs?
- [ ] Why does time to first token differ from tokens per second?
- [ ] Why can a model fit in memory but fail on a long RAG prompt?
- [ ] Why can an OpenAI-compatible endpoint still have feature gaps?
- [ ] Why is a fast local answer not automatically a good answer?
- [ ] Which layer owns the next failure you observe?
- [ ] What one controlled change would you make next, and what evidence would prove it worked?

## References

- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Local LLM Runtime Stack Anatomy]]
- [[LLM/Study/Local LLM First Endpoint Run Sheet]]
- [[LLM/Study/Local LLM Command Cookbook]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]]
- [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Security and Privacy Runbook]]
