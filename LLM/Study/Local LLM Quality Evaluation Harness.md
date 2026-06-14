---
tags: [study, llm, evaluation, local-llm, benchmark]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [practice]
---

# Local LLM Quality Evaluation Harness

> **One-line summary** A local model is not "good" just because it loads and answers quickly; it is good only when it passes a workload-specific quality gate with reproducible prompts, rubric scores, and latency/memory evidence.

Use this after [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]], [[LLM/Study/Local LLM Serving Runbook|Local LLM Serving Runbook]], and [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]]. The sizing guide chooses plausible model/runtime candidates, the runbook proves the endpoint, the benchmark log records performance, and this harness decides whether the output quality is acceptable.

Use [[LLM/Study/Local LLM Client Harness Lab|Local LLM Client Harness Lab]] when each prompt-suite case needs to run through the same client code and produce comparable output paths, latency fields, and error records. Use [[LLM/Study/Decoding and Sampling Controls Lab|Decoding and Sampling Controls Lab]] before judging two outputs if sampler settings, seeds, stop rules, or output caps differ.

## What This Harness Decides

The harness answers a narrow practical question:

> For this workload, on this hardware, with this runtime and sampling setup, is this local model good enough to keep using?

Do not turn this into a universal leaderboard. The same model can pass for private summarization, hold for coding, and fail for citation-heavy RAG.

## Evaluation Ladder

Run the ladder in order. Stop early only when a model clearly fails a required gate.

| Stage | Question | Pass signal |
| --- | --- | --- |
| 1. Smoke test | Does the model load and return the requested shape? | No crash, no empty output, correct route/API shape |
| 2. Known-answer tests | Can it answer locally verifiable facts or calculations? | Correct answer without invented details |
| 3. Instruction/schema tests | Can it obey exact format constraints? | Valid JSON, table, code block, or command shape as requested |
| 4. Pairwise comparison | Is it better than a baseline model/runtime on the same prompts? | Candidate wins, ties, or loses for explicit reasons |
| 5. RAG/citation tests | Does it use supplied evidence and cite only supported claims? | Relevant retrieval, faithful answer, correct citations, refusal when evidence is missing |
| 6. Long-context and multi-turn tests | Does it retain instructions and use the right context across turns? | Follow-up answers respect earlier constraints and cite the relevant context |
| 7. Safety/constraint tests | Does it respect the workload's boundaries? | It follows allowed constraints and avoids unsafe or out-of-scope help |
| 8. Human review plus optional LLM judge | Would a human accept the result for the target use? | Human rubric agrees with the pass decision; LLM judge is only supporting evidence |

This ladder connects local hosting practice to [[LLM/2023 — Open Models and Agents/LLM-as-Judge|LLM-as-Judge]], [[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies|Human Evaluation and Preference Studies]], and [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes|RAG Evaluation and Failure Modes]].

## Prompt Set

Use private or locally written prompts for decisions that matter. Public benchmark examples are useful for learning, but local acceptance should avoid memorized or contaminated prompts.

| Prompt id | Task class | What it tests | Minimum expected behavior |
| --- | --- | --- | --- |
| K-01 | Known fact or calculation | Factuality and basic reasoning | Correct answer, calibrated uncertainty, no invented support |
| S-01 | Structured output | Instruction following and schema control | Valid JSON/table/code shape, no extra prose if forbidden |
| X-01 | Summarization or extraction | Detail retention and compression | Keeps key facts, drops irrelevant material, preserves constraints |
| L-01 | Long context | Context use under KV-cache pressure | Finds the relevant span and does not overuse unrelated context |
| R-01 | RAG grounded answer | Retrieval use, faithfulness, citations | Every substantive claim is supported by retrieved evidence |
| M-01 | Multi-turn instruction retention | Conversation memory and follow-up behavior | Keeps prior constraints through a second or third turn |
| C-01 | Constraint/refusal | Boundary handling | Refuses or narrows the answer when required by the task policy |
| D-01 | Domain-specific work | Real workload fit | Solves the exact task class you plan to run locally |

For local model selection, the domain-specific prompt matters most. A model that wins broad chat prompts but fails your actual workload is not a pass.

## Rubric

Score each dimension from 0 to 2.

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Factuality | Wrong or hallucinated | Partly correct but has unsupported or shaky claims | Correct and appropriately qualified |
| Instruction following | Ignores key instruction | Follows the main request but misses a constraint | Follows all required constraints |
| Format validity | Invalid or unusable shape | Mostly valid with small repair needed | Valid on first use |
| Grounding/citations | Unsupported claims or fake citations | Some claims supported, some vague | Claims are tied to provided evidence |
| Completeness | Misses the core task | Covers the main task but omits useful detail | Complete enough for the workload |
| Concision | Too verbose or too terse to use | Usable but inefficient | Right level of detail for the task |
| Safety/constraint adherence | Violates the boundary | Avoids worst issue but needs review | Cleanly respects the boundary |
| Latency/memory acceptability | Too slow or unstable | Usable only with tuning | Meets the benchmark threshold |

Write the threshold before running. A strict gate might require all required dimensions at 2. A looser exploratory gate might pass with an average of 1.5 if no required dimension is 0.

## Pass / Hold / Fail Gate

| Decision | Use when | Next action |
| --- | --- | --- |
| Pass | Quality threshold is met, latency/memory constraints are met, and the run is reproducible | Keep the model/runtime for this workload and record the decision in the benchmark log |
| Hold | Quality is close, but one bottleneck needs another controlled run | Tune prompt, sampling, quantization, context assembly, runtime, or use [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide|LLM Adaptation and Fine-Tuning Decision Guide]] before training |
| Fail | The model hallucinates, breaks schema, invents citations, misses required constraints, crashes, or is too slow | Replace model/runtime, narrow the workload, or use the adaptation guide to decide whether RAG, SFT, LoRA, QLoRA, DPO, distillation, or no training is appropriate |

The pass decision must include both quality and operations evidence. A fast wrong model fails. A high-quality model that does not fit memory or latency constraints also fails for interactive local use.

Sampler settings are part of the quality condition. A model that passes only under a high-temperature creative preset has not passed a deterministic extraction gate, and a model that fails under one runtime may need an API-contract check before the failure is assigned to model capability.

## Pairwise Comparison Protocol

Use pairwise comparison when choosing between two local setups.

1. Pick a baseline model/runtime and one candidate.
2. Use the same prompts, system instructions, sampling settings, max output tokens, context, and retrieved passages.
3. Hide model identity from the reviewer when practical.
4. Randomize A/B order across prompts.
5. Record winner, tie, or loser with the rubric dimension that decided the judgment.
6. If using an LLM judge, run both AB and BA orderings and compare the verdicts.
7. Treat LLM-judge output as fast signal, not ground truth; validate important decisions with human review.

Bias controls matter because [[LLM/2023 — Open Models and Agents/LLM-as-Judge|LLM judges]] and humans can prefer position, verbosity, confidence, and familiar style over actual quality. The relevant source notes are [[LLM/_chunks/chunk-llm-237 MT-Bench Multi-Turn LLM Evaluation|MT-Bench multi-turn evaluation]], [[LLM/_chunks/chunk-llm-238 Chatbot Arena Elo Rating System|Chatbot Arena pairwise preference]], [[LLM/_chunks/chunk-llm-239 LLM Judge Agreement Rates and Biases|LLM judge bias]], and [[LLM/_chunks/chunk-llm-240 MT-Bench Chatbot Arena Evaluation Paradigms|modern evaluation paradigms]].

## RAG and Citation Checks

When the workload uses retrieval, evaluate retrieval and answer quality separately.

Use [[LLM/Study/Local RAG Assistant Lab|Local RAG Assistant Lab]] when you need the full build-and-diagnose workflow behind these checks.

| Check | Ask | Failure mode |
| --- | --- | --- |
| Retrieval relevance | Did the system retrieve passages that actually answer the question? | Retrieval miss |
| Context sufficiency | Did the retrieved context contain enough evidence? | Missing source or too-low top-k |
| Context cleanliness | Did irrelevant or contradictory passages enter the prompt? | Context poisoning |
| Answer support | Is every substantive claim supported by context? | Hallucination despite context |
| Citation correctness | Do citations point to the exact supporting passage? | Fake or loose citation |
| Missing-evidence behavior | Does the model refuse or say "not enough evidence" when needed? | Parametric-memory override |

This follows [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes|RAG Evaluation and Failure Modes]]. For self-checking patterns, review [[LLM/_chunks/chunk-llm-229 Self-RAG Reflection Tokens|Self-RAG reflection tokens]], [[LLM/_chunks/chunk-llm-230 Self-RAG Adaptive Retrieval|adaptive retrieval]], [[LLM/_chunks/chunk-llm-231 Self-RAG Hallucination Reduction|hallucination reduction]], and [[LLM/_chunks/chunk-llm-232 Self-RAG Toward Self-Correcting LLMs|self-correcting RAG limits]].

## Contamination Control

Public benchmarks are useful for shared vocabulary, but local acceptance should not rely only on them.

- Use private prompts you wrote yourself for pass/fail decisions.
- Include prompts based on your real documents, code, or workflows.
- Avoid copying examples from public benchmark pages into the acceptance suite.
- Refresh prompts when the model, corpus, or task changes.
- Keep a small held-out set that you do not tune prompts against.

This protects the decision from the failure mode described in [[LLM/2020–2021 — The Scaling Era/Contamination and Data Leakage|Contamination and Data Leakage]] and keeps broad benchmark results in the right role described by [[LLM/2018–2019 — Pretrained Language Models/Knowledge and Reasoning Benchmarks|Knowledge and Reasoning Benchmarks]].

## Log Template

Create one row per prompt per model/runtime.

| Run id | Model/runtime | Prompt id | Task class | Expected behavior | Output path/link | Fact | Instr | Format | Ground | Complete | Concise | Safe | Latency | Failure mode | Decision | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | 0/1/2 | 0/1/2 | 0/1/2 | 0/1/2 | 0/1/2 | 0/1/2 | 0/1/2 | 0/1/2 |  | Pass/Hold/Fail |  |

Record the final decision in [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] so quality evidence stays next to latency, memory, quantization, and hardware evidence.

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Serving Runbook]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Decoding and Sampling Controls Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge]]
- [[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
- [[LLM/2018–2019 — Pretrained Language Models/Knowledge and Reasoning Benchmarks]]
- [[LLM/2020–2021 — The Scaling Era/Contamination and Data Leakage]]
- [[LLM/_chunks/chunk-llm-237 MT-Bench Multi-Turn LLM Evaluation]]
- [[LLM/_chunks/chunk-llm-238 Chatbot Arena Elo Rating System]]
- [[LLM/_chunks/chunk-llm-239 LLM Judge Agreement Rates and Biases]]
- [[LLM/_chunks/chunk-llm-240 MT-Bench Chatbot Arena Evaluation Paradigms]]
- [[LLM/_chunks/chunk-llm-229 Self-RAG Reflection Tokens]]
- [[LLM/_chunks/chunk-llm-230 Self-RAG Adaptive Retrieval]]
- [[LLM/_chunks/chunk-llm-231 Self-RAG Hallucination Reduction]]
- [[LLM/_chunks/chunk-llm-232 Self-RAG Toward Self-Correcting LLMs]]
