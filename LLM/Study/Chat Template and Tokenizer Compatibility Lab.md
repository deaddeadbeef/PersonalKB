---
tags: [study, llm, inference, local-llm, tokenizer, chat-template]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [core, practice]
---

# Chat Template and Tokenizer Compatibility Lab

> **One-line summary** A local chat model only behaves like the model you chose when the model weights, tokenizer, special tokens, chat template, client messages, and stop conditions all match.

Use this after [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] when a local endpoint works but the output feels wrong: it continues the prompt, speaks as the user, ignores the system prompt, leaks role markers, or fails structured output.

## Outcome

After this lab you should be able to:

- explain why a base model, instruct model, and chat model can behave differently even with similar weights
- identify the tokenizer and special tokens used by a local model package
- verify that chat messages are rendered with the intended role template before generation
- detect duplicate or missing BOS/EOS tokens, assistant prefixes, stop strings, and role markers
- record template/tokenizer evidence in a benchmark or quality evaluation run

## Mental Model

Tokenization turns text into token IDs. Instruction tuning teaches a model the patterns it should follow. A chat template is the bridge between the two: it serializes structured messages such as system, user, assistant, and tool content into the token sequence the model was trained to treat as conversation.

If that bridge is wrong, the model may not be "bad"; the request may be malformed. A strong instruct model can look weak if the runtime sends the wrong role markers, uses the wrong tokenizer, omits the assistant-generation prefix, duplicates special tokens, or stops on the wrong sequence.

## Compatibility Chain

| Layer | Question | Evidence |
|---|---|---|
| Model type | Is this base, instruct, chat, code, tool, or embedding oriented? | Model id, filename, model card, runtime metadata. |
| Tokenizer | Which vocabulary and text-normalization rules map text to token IDs? | Tokenizer file, GGUF metadata, runtime tokenizer info, token counts. |
| Special tokens | What IDs represent BOS, EOS, padding, unknown, role markers, or tool boundaries? | Tokenizer config, model metadata, rendered prompt. |
| Chat template | How are system/user/assistant/tool messages serialized? | Rendered prompt or template string if visible. |
| Client request | Are messages, prompt, sampling, max tokens, and stop rules sent as intended? | Request body or client code. |
| Runtime adapter | Does the runtime apply its own template or expect a pre-rendered prompt? | Runtime setting, API route, server log, generated prompt. |
| Stop conditions | What ends the response? | EOS token, stop strings, max output tokens, parser/schema boundary. |

## Lab 1: Model Package Card

Record the package you actually served:

| Field | Value |
|---|---|
| Model id or file |  |
| Base/instruct/chat/tool/code classification |  |
| Runtime |  |
| Quantization or format |  |
| Tokenizer source |  |
| Context limit used |  |
| BOS token |  |
| EOS token |  |
| Additional special tokens |  |
| Chat template source |  |
| Stop strings or stop token IDs |  |
| Evidence link/path |  |

Pass signal: someone else can tell whether the endpoint is serving the intended model family and prompt format.

## Lab 2: Rendered Prompt Check

Use a harmless, short request. If the runtime exposes the rendered prompt, save a redacted excerpt showing only the role markers and boundaries.

| Check | Expected | Observed |
|---|---|---|
| System message appears before user message |  |  |
| User content is inside the user role boundary |  |  |
| Assistant-generation marker is present, if the template needs one |  |  |
| BOS/EOS tokens are not duplicated |  |  |
| Tool or JSON instruction is in the intended role |  |  |
| Stop string does not appear inside ordinary content |  |  |

Do not paste private prompts into the vault. Save only the minimal evidence needed to prove the template shape.

## Lab 3: Base Versus Chat Behavior

Run the same simple task through the intended chat route and, if safe, through a raw completion route or template-disabled route.

Prompt:

```text
Reply with exactly: template ok
```

| Route | Template applied? | Output | Interpretation |
|---|---|---|---|
| Chat/messages route | Yes |  |  |
| Raw prompt/completion route | No or manual |  |  |

Pass signal: you can explain whether the model is following instructions because of instruction tuning, because of a correct chat template, or because the prompt was simple enough to work either way.

## Lab 4: Tokenizer Sanity Set

Count tokens for short examples that stress different tokenizer behavior.

| Text class | Example | Token count | What to notice |
|---|---|---:|---|
| Plain English | `The model answered correctly.` |  | Baseline compression. |
| Non-English or mixed script |  |  | Tokenization tax and context cost. |
| Code identifier | `parseHTTPRequestBody` |  | Identifier splitting. |
| JSON boundary | `{"answer":"yes"}` |  | Structured-output boundary tokens. |
| Whitespace-sensitive text | `line 1\n  line 2` |  | Lossless spacing and detokenization. |
| Special-token-looking text |  |  | Whether the tokenizer treats it as normal text or a control token. |

Use [[LLM/Pre-2017 — Before Transformers/Tokenization|Tokenization]] for the academic explanation. Use the counts in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] when comparing models with different tokenizers.

## Lab 5: Stop And Role Boundary Test

Create a short answer with a stop condition and then test a multi-turn prompt.

| Test | Expected boundary | Observed output | Fix |
|---|---|---|---|
| Stop after sentinel | Model stops after sentinel and does not include following text |  |  |
| Multi-turn role order | Assistant answers as assistant, not user/system |  |  |
| JSON-only response | Output parses and does not include role markers |  |  |
| Tool-call-like response | Arguments stay inside the expected schema |  |  |

If JSON or tool arguments matter, pair this lab with [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation|Structured Output and Constrained Generation]] and [[LLM/2023 — Open Models and Agents/Function Calling|Function Calling]].

## Failure Triage

| Symptom | Likely cause | First fix |
|---|---|---|
| Model continues the prompt instead of answering | Base model, raw completion route, or missing chat template | Use an instruct/chat model and the messages/chat route. |
| Model speaks as `user` or prints role labels | Wrong role serialization or missing assistant prefix | Inspect rendered prompt and template. |
| System prompt seems ignored | Template does not include system role, or model was not tuned for that hierarchy | Try the model's documented chat template and test with a minimal system rule. |
| Output includes special-token strings | Stop strings or detokenization boundary mismatch | Add correct stops and inspect EOS handling. |
| JSON is almost valid but has wrapper text | Prompt-only structure without enforcement | Use schema validation or constrained decoding. |
| Same prompt is much longer on one model | Tokenizer difference | Record prompt tokens before comparing latency. |
| Non-English prompt is slow or truncated | Tokenization tax and context pressure | Count tokens and reduce context or choose a better tokenizer/model family. |
| Tool call appears in prose | Client route does not support tool schema or template is wrong | Use a tool-aware route or explicit structured-output validation. |

## Benchmark Add-On

Add these fields to any local inference benchmark or quality harness run where prompt format may affect the result:

| Field | Why |
|---|---|
| Model type | Separates base/completion behavior from chat/instruct behavior. |
| Tokenizer source | Explains token count, context pressure, and detokenization behavior. |
| Chat template source | Makes role serialization reproducible. |
| Rendered prompt checked? | Prevents hidden adapter bugs. |
| Stop/EOS policy | Explains truncation, role-marker leakage, or runaway output. |
| Prompt token count by text class | Makes cross-model latency comparisons fairer. |

## Completion Gate

This lab is complete when you have:

- [ ] a model package card with tokenizer, special-token, template, and stop evidence
- [ ] a rendered prompt check or a clear note that the runtime does not expose it
- [ ] a base-vs-chat or raw-vs-messages behavior comparison
- [ ] a tokenizer sanity set with token counts
- [ ] a stop/role boundary test
- [ ] one benchmark or quality-harness row updated with template/tokenizer fields
- [ ] one failure diagnosis that distinguishes model quality from request formatting

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Pre-2017 — Before Transformers/Tokenization]]
- [[LLM/Pre-2017 — Before Transformers/Perplexity and Intrinsic Metrics]]
- [[LLM/2022 — Alignment and Chat/Instruction Tuning]]
- [[LLM/2022 — Alignment and Chat/System Prompts and Role Conditioning]]
- [[LLM/2023 — Open Models and Agents/Function Calling]]
- [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[chunk-llm-092 Instruction Tuning Bridges to Following]]
- [[chunk-llm-119 PagedAttention Copy-on-Write Sharing]]
- [[chunk-llm-169 SentencePiece Processes Raw Unicode Without Pre-Tokenization]]
- [[chunk-llm-171 SentencePiece Guarantees Lossless Detokenization]]
