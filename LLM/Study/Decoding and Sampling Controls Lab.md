---
tags: [study, llm, inference, local-llm, decoding, sampling, lab]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [core, practice]
last-verified: 2026-06-15
---

# Decoding and Sampling Controls Lab

> **One-line summary** Decoding controls turn model logits into the next token; local LLM runs are only reproducible when temperature, filters, penalties, seeds, stop rules, and output caps are treated as part of the experiment.

Use this after [[LLM/Study/LLM Inference Request Lifecycle Lab|LLM Inference Request Lifecycle Lab]] traces one request from prompt to response. That lab answers "where does sampling happen?" This lab answers "which controls changed the next-token distribution, format, reproducibility, and benchmark result?"

Use this before [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], and [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] whenever two local model runs need a fair comparison. Use [[LLM/Study/Decoding and Sampling Controls Runner|Decoding and Sampling Controls Runner]] when the sampler decisions should be saved as repeatable Python evidence. Use [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] when schema-constrained output must become an executed tool call or bounded agent loop.

Use [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab|Local LLM Reasoning Budget and Test-Time Compute Lab]] when the changed control is thinking mode, reasoning effort, or parser separation rather than temperature, token filtering, penalties, stopping, or structured-output constraints. Use [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner|Local LLM Reasoning Budget and Test-Time Compute Runner]] when that effort sweep must support quality, runtime, result-synthesis, or deployment evidence.

Use [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] when the changed control is draft-model, EAGLE, MTP, n-gram, or another speculative decoding path. Speculative decoding changes the decode loop and memory profile, so it needs a no-spec A/B rather than a sampler-only sweep.

## Outcome

After this lab you should be able to:

- explain the path from logits to filtered probabilities to selected token
- distinguish greedy decoding, random sampling, nucleus sampling, top-k filtering, min-p filtering, repetition penalties, and constrained decoding
- choose deterministic, factual, creative, schema-first, and self-consistency presets without guessing
- map common sampling controls across OpenAI-compatible/vLLM-style requests, Ollama, and llama.cpp
- record sampler settings in every benchmark and quality row
- diagnose format drift, repetition loops, truncation, unstable facts, ignored parameters, and non-reproducible comparisons

## Sampler Pipeline Mental Model

Autoregressive generation repeats this loop:

1. The model reads the current token prefix and emits logits for the next token.
2. Logit processors modify those logits with constraints, penalties, grammar/schema rules, bad-token masks, or runtime-specific policies.
3. Candidate filters keep or remove parts of the vocabulary, such as top-k, top-p, min-p, or typical sampling.
4. Temperature rescales the remaining logits before the probability distribution is sampled.
5. The selected token is appended, detokenized when needed, and checked against EOS, stop strings, schema/tool boundaries, or the output-token cap.
6. The loop repeats until a stop condition fires.

The exact order can differ by runtime. llama.cpp exposes sampler order explicitly; other runtimes may hide it behind request parameters. For serious comparisons, record both the runtime and the parameter values.

## Academic Control Map

| Control | Mechanism | Useful for | Watch out for |
| --- | --- | --- | --- |
| Greedy decoding | Always pick the highest-probability next token. | Deterministic baselines and simple smoke tests. | Can be brittle, repetitive, or overconfident. |
| Temperature | Divides logits before softmax; lower sharpens, higher flattens. | Moving between deterministic and diverse behavior. | High values amplify factual and format drift. |
| Top-k | Keeps only the `k` most likely tokens before sampling. | Hard shortlist control. | Too small can force awkward or wrong tokens. |
| Top-p / nucleus | Keeps the smallest token set whose cumulative probability reaches `p`. | Adaptive diversity for open-ended responses. | Low `p` can erase valid alternatives. |
| Min-p | Keeps tokens above a probability floor relative to the likely token. | Runtime-specific alternative to top-p/top-k for avoiding very unlikely tails. | Not supported everywhere; comparisons must record support. |
| Typical sampling | Favors tokens whose surprise is close to expected surprise. | Some creative writing or style experiments. | Less common in generic OpenAI-compatible clients. |
| Repetition penalty | Penalizes tokens seen in the recent context. | Reducing loops and repeated phrases. | Too strong can damage terms that must repeat, such as code, names, or citations. |
| Frequency/presence penalties | Penalize repeated token frequency or prior appearance. | Encouraging topic expansion or reducing repetition. | Hosted-provider semantics may not match local runtime semantics. |
| Beam search | Keeps multiple high-scoring partial sequences. | Translation-style tasks and some constrained generation. | Often worse for open-ended chat and expensive for local serving. |
| Self-consistency | Samples multiple answers and selects by voting or a verifier. | Reasoning checks when latency budget allows. | Must log each sample and the selection rule. |
| Constrained decoding | Masks invalid tokens according to grammar, schema, tool, or JSON constraints. | Structured output and tool calls. | A bad schema can force lossy or invalid answers. |
| Speculative decoding | Draft tokens are proposed by a faster model, MTP/EAGLE head, or n-gram proposer and verified by the target model. | Decode-latency optimization. | Run [[LLM/Study/Local LLM Speculative Decoding Lab|Local LLM Speculative Decoding Lab]] because acceptance, memory, and quality evidence decide whether it helps. |

Connect this to [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals|Language Model Fundamentals]] and [[LLM/Study/Tiny Decoder-Only Transformer Training Lab|Tiny Decoder-Only Transformer Training Lab]]: the same logits-to-token loop appears in toy models and production runtimes.

## Runtime Parameter Map

| Concept | OpenAI-compatible / vLLM-style | Ollama | llama.cpp / llama-server |
| --- | --- | --- | --- |
| Output cap | `max_tokens` | `num_predict` in Modelfile or runtime options | `max_tokens` or `n_predict` |
| Temperature | `temperature` | `temperature` | `temperature` |
| Top-p | `top_p` | `top_p` | `top_p` |
| Top-k | `top_k` when supported | `top_k` | `top_k` |
| Min-p | `min_p` when supported | `min_p` | `min_p` |
| Typical sampling | Runtime-specific | Not a common Ollama Modelfile control | `typical_p` or `typ_p` depending on interface |
| Seed | `seed` when supported | `seed` | `seed` |
| Stop strings | `stop` | `stop` | `stop` |
| Repetition penalty | `repetition_penalty` when supported | `repeat_penalty`, `repeat_last_n` | `repeat_penalty`, repeat window controls |
| Presence/frequency penalties | `presence_penalty`, `frequency_penalty` when supported | Runtime-specific or absent in common Modelfile path | `presence_penalty`, `frequency_penalty` in server settings |
| Streaming | `stream` | Native and compatibility routes vary | `stream` |
| Log probabilities | `logprobs` when supported | Not universal | Runtime/interface-specific |
| Context setting | Usually server/runtime configuration, not just request body | `num_ctx` | context/server startup setting |
| Speculative draft | Runtime/server feature | `draft_num_predict` for draft-token behavior | server/build/runtime-specific |

Do not assume an OpenAI-compatible endpoint supports every local sampler. Use [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|Local LLM OpenAI-Compatible API Contract Lab]] to record which parameters are accepted, ignored, translated, or rejected.

## Sampling Presets

These are starting policies, not universal defaults.

| Workload | Starting policy | Evidence to record |
| --- | --- | --- |
| Endpoint smoke test | `temperature=0`, explicit output cap, simple stop behavior. | Exact request and returned content. |
| Factual QA or RAG | Low temperature, stable top-p/default filter, explicit max tokens, citation/grounding check. | Prompt, retrieved context version, answer support, quality score. |
| Structured extraction | Low temperature, schema or grammar if supported, strict max tokens, parse validation. | Raw output, parser result, schema version, stop reason. |
| Coding helper | Low to moderate temperature, explicit stop strings for file boundaries, tests as judge. | Prompt id, output path, test result, failure mode. |
| Brainstorming | Higher temperature or broader top-p, multiple samples, larger but capped output. | Number of samples, chosen output, selection criteria. |
| Self-consistency reasoning | Multiple independent samples, fixed prompt, fixed scoring/voting rule. | Per-sample settings, final answer, verifier or vote. |
| Benchmark comparison | Same prompt, same context, same output cap, same sampler settings. | Full sampler config in the benchmark row. |

## Lab 1: Freeze The Baseline

Pick one local endpoint that already passed [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]]. Freeze a boring baseline.

| Field | Value |
| --- | --- |
| Runtime and version |  |
| Model id |  |
| Route |  |
| Prompt id |  |
| Prompt text or local path |  |
| Temperature |  |
| Top-p |  |
| Top-k |  |
| Min-p |  |
| Repetition/frequency/presence penalties |  |
| Seed support | supported / unsupported / unknown |
| Max output tokens |  |
| Stop strings |  |
| Structured output mode | none / JSON prompt / schema / grammar / tool |
| Streaming | on / off |

Pass signal: another run can reconstruct the same request without relying on runtime defaults.

## Lab 2: Temperature Sweep

Use the same prompt, model, endpoint, output cap, and filters. Change only temperature.

| Run | Temperature | Output summary | Correct? | Format valid? | Diversity change | Decision |
| --- | ---: | --- | --- | --- | --- | --- |
| T0 | 0 or lowest supported |  |  |  |  |  |
| T1 | 0.3 |  |  |  |  |  |
| T2 | 0.7 or 0.8 |  |  |  |  |  |

Interpretation:

- If factual answers drift as temperature rises, keep the workload low-temperature and move creativity elsewhere.
- If all outputs are identical, the prompt may be too constrained, the model may be deterministic, or the runtime may ignore the parameter.
- If JSON fails only at higher temperature, the issue is a sampling/structure boundary, not just a parser issue.

## Lab 3: Filter Sweep

Reset temperature to the baseline. Change one candidate filter at a time.

| Run | Top-p | Top-k | Min-p | Output summary | Difference from baseline | Decision |
| --- | ---: | ---: | ---: | --- | --- | --- |
| Baseline |  |  |  |  |  |  |
| Top-p test |  |  |  |  |  |  |
| Top-k test |  |  |  |  |  |  |
| Min-p test |  |  |  |  |  |  |

Pass signal: you can explain whether a filter changed diversity, correctness, format, or nothing observable.

## Lab 4: Penalty And Repetition Test

Use a prompt likely to trigger repetition, such as a long explanation, a list, or code comments. Compare no penalty, default penalty, and stronger penalty.

| Run | Penalty settings | Repetition observed | Required repeated terms damaged? | Decision |
| --- | --- | --- | --- | --- |
| No/default penalty |  |  |  |  |
| Stronger penalty |  |  |  |  |
| Workload preset |  |  |  |  |

Pass signal: you reduce loops without damaging names, code identifiers, citations, or required terms.

## Lab 5: Stop, Truncation, And Structured Output

Run one short delimited task and one structured-output task.

| Test | Expected boundary | Max tokens | Stop/schema setting | Actual stop reason | Parse result | Fix |
| --- | --- | ---: | --- | --- | --- | --- |
| Delimited answer |  |  |  |  |  |  |
| JSON object |  |  |  |  |  |  |

Use [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation|Structured Output and Constrained Generation]] when prompt-only JSON fails. Use [[LLM/Study/Local LLM Tool Calling and Structured Output Lab|Local LLM Tool Calling and Structured Output Lab]] when the structured output names a tool or triggers application code. Use [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]] when stop strings or role markers behave differently from the request body.

## Lab 6: Runtime Support Check

Send one harmless request with a parameter you plan to depend on, such as `seed`, `top_k`, `min_p`, `logprobs`, or a schema/grammar field.

| Parameter | Accepted? | Ignored? | Error behavior | Evidence |
| --- | --- | --- | --- | --- |
| Seed |  |  |  |  |
| Top-k |  |  |  |  |
| Min-p |  |  |  |  |
| Logprobs |  |  |  |  |
| Schema/grammar |  |  |  |  |

Pass signal: your [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab|API contract card]] says which sampler features are dependable for the workload.

## Benchmark Row Add-On

Every comparison row in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] should capture these fields:

| Field | Why |
| --- | --- |
| Sampler preset name | Makes the row readable later. |
| Temperature/top-p/top-k/min-p | Explains diversity and candidate filtering. |
| Output cap | Prevents accidental unbounded comparisons. |
| Stop strings and stop reason | Separates successful completion from truncation. |
| Seed support and value | Explains reproducibility limits. |
| Penalties and repeat window | Explains loops or loss of repeated terms. |
| Structured output mode | Explains parse validity. |
| Runtime version | Controls may change across releases. |
| Unsupported or ignored fields | Avoids false conclusions from no-op parameters. |
| Speculative decoding state | Captures off/on, draft method, accepted tokens, speed delta, memory cost, and quality result when a draft path is used. |

## Failure Triage

| Symptom | Likely cause | First check |
| --- | --- | --- |
| Same prompt gives different benchmark decisions | Sampling or seed changed. | Compare full sampler config and seed support. |
| Output is factual at low temperature but invents at high temperature | Temperature opened unstable alternatives. | Lower temperature or require retrieval/citations. |
| Output is bland or refuses useful alternatives | Filters too narrow or temperature too low. | Raise one control at a time. |
| Repetition loop | Penalty/window too weak, prompt loop, or model issue. | Tune repeat penalty/window and inspect prompt. |
| Required names disappear or mutate | Penalty too strong. | Lower penalty or protect exact terms in prompt/schema. |
| JSON fails intermittently | Prompt-only structure plus randomness. | Lower temperature, add validation, or use constrained decoding. |
| Response cuts off | Output cap too low or stop string too broad. | Inspect stop reason and max token setting. |
| Runtime accepts a field but behavior does not change | Field ignored or translated. | Add API contract feature-gap row. |
| Comparison favors one model unfairly | Sampler, output cap, or prompt changed. | Re-run with fixed settings and prompt ids. |

## Completion Gate

This lab is complete when you have:

- [ ] one frozen baseline with full sampler settings
- [ ] one temperature sweep with a written decision
- [ ] one top-p/top-k/min-p filter sweep where only one control changes at a time
- [ ] one repetition/penalty test
- [ ] one stop/truncation/structured-output test with parse result
- [ ] one runtime support row for the sampler features you plan to use
- [ ] one benchmark row updated with sampler fields
- [ ] one quality-harness comparison that fixes sampler settings before judging output
- [ ] one explanation linking observed behavior to logits, filters, penalties, stopping, or runtime support

## References

Internal:

- [[LLM/Sources/Sources Index]]
- [[LLM/Pre-2017 — Before Transformers/Language Model Fundamentals]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/Study/LLM Inference Request Lifecycle Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Runner]]
- [[LLM/Study/Decoding and Sampling Controls Runner]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab]]
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Runner]]
- [[LLM/Study/Local LLM Speculative Decoding Lab]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local LLM Tool Calling and Structured Output Lab]]
- [[LLM/2023 — Open Models and Agents/Structured Output and Constrained Generation]]
- [[LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding]]

Current external docs checked 2026-06-15:

- [Ollama OpenAI compatibility](https://docs.ollama.com/api/openai-compatibility)
- [OpenAI chat completions API reference](https://platform.openai.com/docs/api-reference/chat/create)
- [Hugging Face generation parameters](https://huggingface.co/docs/transformers/en/main_classes/text_generation)
- [Hugging Face generation strategies](https://huggingface.co/docs/transformers/en/generation_strategies)
- [vLLM sampling parameters](https://docs.vllm.ai/en/v0.6.4/dev/sampling_params.html)
- [Ollama Modelfile reference](https://docs.ollama.com/modelfile)
- [llama.cpp server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
