---
tags: [study, llm, reasoning, inference, local-llm, test-time-compute]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
tier-coverage: [core, practice, deep-dive]
last-verified: 2026-06-15
---

# Local LLM Reasoning Budget and Test-Time Compute Lab

> **One-line summary** A reasoning model is not just a better chat model; it is a local inference experiment where thinking mode, reasoning parser, output budget, latency, trace visibility, and quality evidence must be controlled together.

Use this after [[LLM/2026 — Reasoning and Agents/Reasoning Models and Test-Time Compute|Reasoning Models and Test-Time Compute]], [[LLM/2026 — Reasoning and Agents/DeepSeek R1 and Open Reasoning|DeepSeek R1 and Open Reasoning]], [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]], [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]], and [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix|Local LLM Runtime and Model Compatibility Matrix]].

Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] to capture raw responses. Save timing in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], quality decisions in [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], and deployment consequences in [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]]. Use [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner|Local LLM Reasoning Budget and Test-Time Compute Runner]] when the saved effort sweep needs machine-checkable pass, hold, fail, CSV, Markdown, JSON, and JSONL evidence.

## What This Lab Decides

This lab answers four practical questions:

1. Does the selected local model support reasoning or thinking mode?
2. Can the runtime separate reasoning content from final answer content?
3. Does more reasoning effort improve the workload enough to justify added latency and tokens?
4. Should reasoning traces be shown, logged, hidden, redacted, or disabled for this use case?

Do not treat a visible chain of thought as ground truth. It is model output. Judge the final answer, the evidence used, and the measured behavior.

## Reasoning Control Model

| Layer | Question | Evidence |
|---|---|---|
| Model capability | Is this model trained to produce reasoning content or effort levels? | Model card, runtime metadata, smoke response. |
| Trigger | How is reasoning enabled, disabled, or budgeted? | `think`, `reasoning.effort`, parser flag, template setting, or UI setting. |
| Parser | Does the runtime split reasoning from final content? | `thinking`, `reasoning`, `reasoning_content`, or inline tags. |
| Budget | How many output tokens, how much latency, and which effort level are allowed? | Effort sweep, output-token cap, TTFT, total latency, tokens/sec. |
| Quality | Does extra reasoning improve correctness, planning, tool use, or verification? | Scored prompt-suite rows. |
| Privacy | Can traces expose sensitive data, hidden prompts, retrieved text, or unsafe instructions? | Log policy and redaction decision. |

Reasoning budget is part of the request contract. A benchmark that changes thinking mode is not comparable to one that does not.

## Runtime Support Map

| Runtime or UI | Reasoning control | Evidence to record |
|---|---|---|
| Ollama native API | `think` can be `true`, `false`, or effort strings for supported models. GPT-OSS uses `low`, `medium`, or `high`. | Request body, `thinking` field, final `response` or `message.content`, usage timings. |
| Ollama OpenAI-compatible API | Supports reasoning/thinking fields for thinking models, including `reasoning_effort` and `reasoning.effort` request fields. | `/v1/chat/completions` request, response shape, ignored-field behavior. |
| LM Studio OpenAI-compatible API | `/v1/responses` supports `reasoning.effort` for supported local models such as `openai/gpt-oss-20b`; `/v1/chat/completions` has separate reasoning fields for some models. | Base URL, endpoint choice, effort value, non-streaming and streaming response fields. |
| llama.cpp server | Some reasoning models may emit inline tags or parsed fields depending on template/server support. | Raw content, `timings`, `usage`, tags, template setting, parse result. |
| vLLM | Reasoning output requires the right reasoning parser for the model family. | Launch command with `--reasoning-parser`, response `reasoning` or reasoning-content field, chat template compatibility. |
| SGLang | Reasoning parser splits model-specific tags into `reasoning_content` and final `content`. | Launch command with `--reasoning-parser`, parser name, response fields, streaming behavior. |
| Open WebUI | UI has separate reasoning-tag parsing and Ollama `think` controls. | Provider response, UI parser setting, whether trace is hidden, shown, or forwarded during tool turns. |

If a runtime merges `<think>...</think>` into normal content, the answer has not passed the reasoning-separation gate.

## Lab 1: Capability And Parser Smoke Test

Pick one reasoning-capable model and one local runtime. Run a short prompt where reasoning should be useful but easy to verify.

| Field | Value |
|---|---|
| Runtime and version |  |
| Model id |  |
| Reasoning family | DeepSeek R1 / Qwen3 / GPT-OSS / other |
| Control field | `think` / `reasoning.effort` / parser flag / template / UI |
| Parser setting |  |
| Prompt |  |
| Reasoning field observed |  |
| Final-answer field observed |  |
| Inline tags observed | yes / no |
| Correct final answer | yes / no |
| Failure layer | model / trigger / parser / template / route / UI / quality |

Pass signal: the final answer is separate from the reasoning trace, or the note explicitly says the runtime only exposes inline reasoning tags.

## Lab 2: Effort Sweep

Use one prompt that benefits from reasoning, such as a small logic puzzle, math problem, planning task, or multi-step debugging scenario. Keep model, runtime, prompt, sampler, context, and output cap fixed. Change only the reasoning effort.

| Run | Reasoning setting | Reasoning tokens or trace length | TTFT | Total latency | Final-answer quality | Decision |
|---|---|---:|---:|---:|---|---|
| Off or none |  |  |  |  |  |  |
| Low |  |  |  |  |  |  |
| Medium |  |  |  |  |  |  |
| High |  |  |  |  |  |  |

Interpretation:

- If quality does not improve, prefer the lower-effort run.
- If quality improves only at high effort, decide whether the workload can tolerate the extra latency and output budget.
- If high effort rambles or exceeds output caps, tighten the prompt, cap, or task routing.
- If the runtime ignores the effort field, record it in the API contract card before comparing quality.

## Lab 3: Reasoning Visibility And Logging Policy

Decide how the local application should handle reasoning content.

| Policy choice | Use when | Risk |
|---|---|---|
| Show trace | Learning, debugging, transparency, local-only experiments. | Users may over-trust unverified reasoning. |
| Hide trace but keep final answer | Product UI, extraction, simple assistants. | Debugging is harder when failures occur. |
| Log trace locally | Private diagnostic harness with redaction and retention rules. | Traces may contain sensitive prompt or retrieved content. |
| Redact trace | Sharing benchmark or bug reports. | Redaction can remove failure evidence. |
| Disable thinking | Cheap/simple tasks where reasoning adds latency without quality gain. | Some reasoning models may degrade or ignore disable controls. |

Minimum safe policy: do not send reasoning traces outside the local boundary unless you explicitly reviewed what they contain and why they are needed.

## Lab 4: Reasoning Versus Sampling

Reasoning effort is not the same as sampling randomness. Run one deterministic setting and one normal workload setting.

| Run | Effort | Temperature | Top-p | Max output tokens | Final answer | Parse/quality result |
|---|---|---:|---:|---:|---|---|
| Deterministic low effort |  |  |  |  |  |  |
| Deterministic higher effort |  |  |  |  |  |  |
| Workload preset low effort |  |  |  |  |  |  |
| Workload preset higher effort |  |  |  |  |  |  |

Pass signal: you can say whether the improvement came from more reasoning effort, a different sampler, a larger output budget, or random variation.

## Lab 5: Reasoning With Tools Or RAG

Use this only after [[LLM/Study/Local RAG Minimal Python Harness|Local RAG Minimal Python Harness]] or [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] exists for the workload.

| Check | Evidence |
|---|---|
| Retrieved context or tool result entered the prompt |  |
| Reasoning trace did not override policy or cite unsupported facts |  |
| Tool call arguments were validated outside model reasoning |  |
| Final answer cites evidence or tool result, not only the trace |  |
| Trace retention policy is written |  |

Reasoning is not authorization. A model explaining why it wants a tool call does not make the tool call safe.

## Benchmark Row Add-On

Add these fields to [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] when using reasoning models:

| Field | Why |
|---|---|
| Reasoning-capable model | Separates ordinary instruct models from reasoning models. |
| Reasoning control field | `think`, `reasoning.effort`, parser flag, template, or UI control. |
| Effort value | Low/medium/high/off/none or runtime-specific value. |
| Reasoning-output shape | Separate field, inline tags, hidden, unavailable, or ignored. |
| Reasoning token or trace length | Explains added output cost and latency. |
| Final-answer tokens | Keeps reasoning and answer cost distinct. |
| TTFT and total latency | Shows the user-visible cost of extra thinking. |
| Trace logging policy | Prevents accidental private trace retention. |
| Quality delta versus low/off | Proves whether extra effort mattered. |

## Failure Triage

| Symptom | Likely layer | First check |
|---|---|---|
| No reasoning appears | Model is not reasoning-capable, trigger missing, or field ignored. | Model card, request body, API contract row. |
| Reasoning appears inside final answer | Parser/template/UI separation failure. | Raw response and parser settings. |
| Effort value has no effect | Runtime ignores the field or model does not support budget control. | Compare raw responses and usage/timing. |
| High effort is slower but not better | Task does not benefit, prompt is bad, or answer is already easy. | Quality row against low effort. |
| High effort cuts off final answer | Output cap spent on trace or stop policy is wrong. | Separate reasoning length from final-answer length. |
| Tool call follows unsafe reasoning | Policy boundary is missing. | Validate arguments and permissions outside the model. |
| RAG answer cites unsupported claims | Trace is substituting for evidence. | Check retrieved chunks and final answer support. |
| UI shows raw `<think>` tags | Reasoning tag parser is not configured. | UI reasoning-tag settings and provider response shape. |

## Decision Card

| Field | Value |
|---|---|
| Workload |  |
| Model/runtime |  |
| Reasoning support | separate field / inline tags / hidden / unsupported |
| Effort levels tested |  |
| Best effort level | off / low / medium / high / runtime-specific |
| Quality delta |  |
| Latency delta |  |
| Token/output-budget impact |  |
| Trace visibility policy | show / hide / log locally / redact / disable |
| Failure layer, if any | model / trigger / parser / template / route / UI / quality / policy |
| Decision | use reasoning / use low effort / use high effort only for hard prompts / disable / change runtime |
| Retest trigger | new model, new runtime, new parser, new workload, new privacy boundary |

## Completion Gate

This lab is complete when:

- [ ] one reasoning-capable model and runtime are identified
- [ ] the control field or parser setting is documented
- [ ] raw response evidence shows where reasoning and final answer appear
- [ ] an effort sweep compares off/low/medium/high or the closest supported alternatives
- [ ] benchmark rows separate reasoning cost from final-answer cost where possible
- [ ] quality rows prove whether added effort improves the workload
- [ ] the trace visibility and logging policy is written
- [ ] the reasoning budget runner output is linked before quality, runtime, result-synthesis, or deployment decisions depend on reasoning mode
- [ ] tool/RAG reasoning is evaluated against external evidence and policy, not the trace alone
- [ ] the deployment or model choice says when to use, reduce, disable, or reject reasoning mode

## References

Internal routes:

- [[LLM/Sources/Sources Index]]
- [[LLM/2026 — Reasoning and Agents/Reasoning Models and Test-Time Compute]]
- [[LLM/2026 — Reasoning and Agents/DeepSeek R1 and Open Reasoning]]
- [[LLM/2026 — Reasoning and Agents/Reasoning Distillation]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Runtime and Model Compatibility Matrix]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/Study/Local RAG Minimal Python Harness]]
- [[LLM/Study/LLM Deployment Decision Matrix]]

Current external docs checked 2026-06-15:

- [Ollama thinking capability](https://docs.ollama.com/capabilities/thinking)
- [Ollama generate endpoint](https://docs.ollama.com/api/generate)
- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [LM Studio Responses endpoint](https://lmstudio.ai/docs/developer/openai-compat/responses)
- [LM Studio API changelog](https://lmstudio.ai/docs/developer/api-changelog)
- [vLLM reasoning outputs](https://docs.vllm.ai/en/latest/features/reasoning_outputs/)
- [SGLang reasoning parser](https://docs.sglang.io/docs/advanced_features/separate_reasoning)
- [Open WebUI reasoning and thinking models](https://docs.openwebui.com/features/chat-conversations/chat-features/reasoning-models/)
