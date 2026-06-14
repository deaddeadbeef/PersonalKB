---
tags: [study, llm, fine-tuning, adaptation, peft, local-llm, decision]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [core, deep-dive, practice]
---

# LLM Adaptation and Fine-Tuning Decision Guide

> **One-line summary** Fine-tuning is only one adaptation tool; choose prompting, RAG, SFT, LoRA, QLoRA, DPO, distillation, or continued pretraining from the failure mode, data, evaluation evidence, compute budget, and deployment boundary.

Use this after [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] identifies a quality gap, or before collecting a capstone adaptation decision in [[LLM/Study/LLM Mastery Capstone Workbook|LLM Mastery Capstone Workbook]]. Pair it with [[LLM/2018–2019 — Pretrained Language Models/Supervised Fine-Tuning|Supervised Fine-Tuning]], [[LLM/2020–2021 — The Scaling Era/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]], [[LLM/2020–2021 — The Scaling Era/LoRA and QLoRA|LoRA and QLoRA]], and [[LLM/2018–2019 — Pretrained Language Models/Domain Adaptation|Domain Adaptation]].

The core mistake is treating "fine-tune it" as the default response to every bad answer. Adaptation should start by naming the failure. If the model lacks current documents, use retrieval. If it ignores a response format, try prompts, examples, constrained decoding, or SFT. If it needs stable task behavior on private examples, consider LoRA or QLoRA. If it needs preference ranking, use preference optimization. If it lacks a broad domain language, continued pretraining may be justified.

## Outcome

After filling this out, you should be able to:

- distinguish prompt, RAG, SFT, LoRA, QLoRA, DPO, distillation, and continued-pretraining use cases
- decide whether a model should be adapted at all
- identify the minimum dataset and evaluation proof needed before training
- explain how adaptation changes deployment, privacy, cost, and rollback
- reject fine-tuning when retrieval, prompting, tool design, or model choice is the better fix

## Adaptation Ladder

Use the cheapest reversible change that fixes the measured failure.

| Step | Try when | Evidence that it worked |
|---|---|---|
| Prompt or system instruction | The model can do the task but misses framing, tone, or constraints | Quality harness passes with stable prompt template |
| Few-shot examples | The desired behavior is easy to demonstrate in-context | Held-out examples pass without overfitting to the examples |
| Structured output or tool design | The failure is format, schema, or action selection | Valid outputs and tool calls pass parser/policy checks |
| RAG | The answer needs private, current, or inspectable source material | Retrieval and citation checks pass separately from generation |
| Model/runtime swap | The local model lacks capability or is too slow | Benchmark and quality rows improve under the same prompt suite |
| SFT | The task needs repeated input-output behavior that examples can demonstrate | Held-out prompt-completion examples pass after training |
| LoRA | SFT behavior is needed, but full fine-tuning is too expensive or risky | Adapter improves held-out quality while preserving base capability |
| QLoRA | Adapter training is needed but memory is the blocker | Adapter trains on quantized base model and passes the same eval gate |
| DPO or preference optimization | The target behavior is better captured by chosen/rejected pairs than single answers | Pairwise eval improves without regressions on safety or format |
| Continued pretraining | The model needs broad domain language or terminology, not just response style | Domain eval improves and general capability regression is measured |
| Distillation | A smaller or cheaper model should imitate a stronger teacher | Student passes workload eval at lower cost or latency |

## Decision Inputs

| Input | Question to answer |
|---|---|
| Failure mode | Is the issue knowledge, retrieval, format, style, reasoning, preference, safety, latency, or cost? |
| Baseline model | Which model/runtime/quantization produced the failing evidence? |
| Workload | Is this chat, coding, extraction, RAG, agent tool use, summarization, or batch processing? |
| Data format | Do you have raw text, prompt-completion pairs, conversations, chosen/rejected pairs, or teacher traces? |
| Data volume | Is there enough clean data for the method, or only enough for prompting/evaluation? |
| Held-out set | What examples will be untouched until final evaluation? |
| Privacy boundary | Can the training data leave the machine or provider? |
| Compute budget | Can you train full weights, adapters, quantized adapters, or only prompt/RAG? |
| Deployment path | Will the result be local CPU, local GPU, self-hosted server, hosted API, hybrid, or batch? |
| Rollback | Can you remove the adapter, revert the prompt, switch model, or rebuild the index? |

## Problem To Method Matrix

| Problem | Prefer | Avoid as first move |
|---|---|---|
| Missing private documents | RAG | Fine-tuning private text into weights |
| Current or frequently changing facts | RAG or tool call | Continued pretraining |
| Wrong output format | Prompt, examples, constrained output, SFT if repeated | Bigger model alone |
| Domain terminology weakness | RAG, continued pretraining, or domain SFT depending on scale | Tiny SFT set pretending to add knowledge |
| Repeated task style | SFT, LoRA, or QLoRA | RAG if no external evidence is needed |
| Subjective preference | DPO, RLHF-style pipeline, or rubric-guided selection | Single-answer SFT only |
| Cost or latency too high | Distillation, smaller model, quantization, or deployment tuning | More training on the same oversized model |
| Catastrophic forgetting risk | LoRA, QLoRA, replay, or multi-adapter strategy | Full sequential fine-tuning without regression eval |
| Tool misuse | Tool policy, schemas, sandbox, and eval | Fine-tuning without external execution guardrails |
| RAG hallucination | Retrieval eval, citation gate, prompt/context assembly | Blind SFT on generated answers |

## Method Trade-Offs

| Method | Changes | Data needed | Strength | Main risk |
|---|---|---|---|---|
| Prompting | No weights | Task instructions and examples | Fast and reversible | Brittle prompt dependence |
| RAG | Context at inference | Corpus, chunking, retrieval eval | Fresh and inspectable knowledge | Retrieval miss, citation drift, prompt injection |
| SFT | Model weights or adapter | Prompt-completion examples | Stable behavior and format | Overfitting, forgetting, leakage |
| LoRA | Low-rank adapter | Same as SFT | Efficient, swappable, low storage | Underfitting if rank/data too small |
| QLoRA | Low-rank adapter on quantized base | Same as SFT | Fits larger models on less VRAM | Slower training, quantization artifacts |
| DPO | Policy preference objective | Chosen/rejected pairs | Preference alignment without reward model serving | Preference data quality dominates |
| Continued pretraining | All weights | Large raw domain corpus | Broad domain fluency | Very high compute, forgetting, stale knowledge |
| Distillation | Student model | Teacher outputs or traces | Lower latency/cost deployment | Teacher errors and style copied |

## Evidence Gate Before Training

Do not train until these are true:

- The baseline failure is captured in [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]].
- The intended method matches the failure mode in the matrix above.
- Training data and held-out evaluation data are separated.
- Duplicates, near-duplicates, private secrets, and unsafe examples are handled deliberately.
- Chat template, role markers, stop tokens, and tokenizer behavior are known from [[LLM/Study/Chat Template and Tokenizer Compatibility Lab|Chat Template and Tokenizer Compatibility Lab]].
- The evaluation suite includes at least one regression check for general behavior, safety, and format.
- The deployment path can load the resulting prompt, retrieval index, adapter, merged model, or student model.
- Rollback is explicit.

## Dataset Checklist

| Dataset piece | Required checks |
|---|---|
| Training examples | Clean input/output shape, no accidental labels, no benchmark leakage |
| Validation examples | Same distribution as task, not copied from training |
| Held-out examples | Untouched until final comparison |
| Negative examples | Useful for preference optimization, refusal, or format boundaries |
| RAG corpus | Versioned source folder, chunking policy, metadata, deletion policy |
| Synthetic data | Teacher identity, generation prompt, filter rules, failure examples |
| Private data | Storage location, access boundary, redaction, retention policy |

Quality matters more than row count. A small clean set that captures the task beats a larger pile of duplicated, mislabeled, or prompt-contaminated examples.

## Mini-Lab

Use this as the applied proof for adaptation literacy.

1. Choose one workload from the quality harness that currently passes, holds, or fails.
2. Save the baseline model/runtime/prompt row from [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]].
3. Name the failure mode: knowledge, retrieval, format, style, reasoning, preference, safety, latency, or cost.
4. Choose one adaptation path from the ladder and reject at least one alternative.
5. Create or point to the smallest dataset that can prove the decision.
6. Run the adapted setup or write a no-train decision memo if prompting/RAG/model swap is the correct fix.
7. Re-run the same held-out prompt suite.
8. Record whether quality improved, latency changed, privacy risk changed, and rollback remains possible.

Passing the mini-lab does not require training a model every time. A correct decision to avoid fine-tuning is part of mastery.

## Decision Memo Template

| Field | Value |
|---|---|
| Workload |  |
| Baseline evidence | benchmark / quality / RAG / safety links |
| Failure mode | knowledge / retrieval / format / style / reasoning / preference / safety / latency / cost |
| Candidate methods | prompting / examples / RAG / model swap / SFT / LoRA / QLoRA / DPO / continued pretraining / distillation |
| Selected method |  |
| Rejected alternatives |  |
| Data source and boundary |  |
| Held-out eval |  |
| Expected deployment impact | adapter, merged model, index, prompt, hosted model, or student model |
| Privacy and security impact |  |
| Rollback plan |  |
| Final decision | train / do not train / collect data first / change deployment |

## Completion Gate

An adaptation decision is complete when:

- the baseline failure is reproducible
- the adaptation method matches the failure mode
- training/evaluation data boundaries are explicit
- held-out evaluation shows improvement or the no-train decision is justified
- regressions in general behavior, safety, and format are checked
- deployment and rollback are written down

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Mastery Capstone Workbook]]
- [[LLM/Study/LLM Mastery Self-Assessment Exam]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/Study/Chat Template and Tokenizer Compatibility Lab]]
- [[LLM/Study/Local RAG Assistant Lab]]
- [[LLM/2018–2019 — Pretrained Language Models/Supervised Fine-Tuning]]
- [[LLM/2018–2019 — Pretrained Language Models/Domain Adaptation]]
- [[LLM/2018–2019 — Pretrained Language Models/Data Curation and Deduplication]]
- [[LLM/2018–2019 — Pretrained Language Models/Distillation and Model Compression]]
- [[LLM/2020–2021 — The Scaling Era/Parameter-Efficient Fine-Tuning]]
- [[LLM/2020–2021 — The Scaling Era/LoRA and QLoRA]]
- [[LLM/2020–2021 — The Scaling Era/Continual Fine-Tuning and Catastrophic Forgetting]]
- [[LLM/2022 — Alignment and Chat/Instruction Tuning]]
- [[LLM/2022 — Alignment and Chat/Reinforcement Learning from Human Feedback]]
- [[LLM/2022 — Alignment and Chat/Direct Preference Optimization]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
- [[LLM/2026 — Reasoning and Agents/Reasoning Distillation]]
