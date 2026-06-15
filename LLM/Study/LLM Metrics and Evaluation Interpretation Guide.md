---
tags: [study, llm, evaluation, metrics, perplexity, calibration, benchmark, local-llm]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
tier-coverage: [theory, practice]
---

# LLM Metrics and Evaluation Interpretation Guide

> **One-line summary** LLM metrics only help when you know which claim they prove: loss predicts text, benchmarks test task samples, pairwise scores measure preference, calibration measures probability trust, and local benchmark rows measure operations.

Use this after [[LLM/Study/LLM Math and Tensor Shape Primer|LLM Math and Tensor Shape Primer]], [[LLM/Study/LLM Training Pipeline Map|LLM Training Pipeline Map]], and [[LLM/Study/LLM Paper Reading Protocol|LLM Paper Reading Protocol]]. Those notes define logits/loss, training stages, and paper reading. This guide tells you how to interpret the numbers without confusing training progress, leaderboard performance, workload quality, and local serving evidence.

Use it before [[LLM/Study/Local LLM Evaluation Set Design Runner|Local LLM Evaluation Set Design Runner]], [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]], [[LLM/Study/Local LLM Judge Calibration Runner|Local LLM Judge Calibration Runner]], [[LLM/Study/Local LLM Inference Metrics Field Guide|Local LLM Inference Metrics Field Guide]], [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]], [[LLM/Study/Local LLM Runtime Comparison Lab|Local LLM Runtime Comparison Lab]], and [[LLM/Study/LLM Deployment Decision Matrix|LLM Deployment Decision Matrix]] when a decision depends on a metric.

## The Metric Rule

Every metric must answer four questions:

1. **What claim does it prove?**
2. **What data distribution produced it?**
3. **What failure mode can it miss?**
4. **What local decision should change because of it?**

If a metric cannot answer all four, keep it as context, not as a decision gate.

## Metric Families

| Metric family | What it measures | Good for | Does not prove |
| --- | --- | --- | --- |
| Cross-entropy / NLL | Probability assigned to true next tokens | Pretraining, validation loss, SFT target fitting | Assistant usefulness, citation faithfulness, tool safety |
| Perplexity | Exponentiated average NLL | Comparing language-model fit on the same tokenization/data | Chat quality across different tokenizers or tasks |
| Accuracy / exact match / F1 | Correctness on labeled tasks | Closed-form QA, classification, extraction, benchmark subsets | Robustness, calibration, reasoning path, deployment fit |
| pass@k | Chance at least one of k samples passes tests | Code generation and search-like generation | First-try reliability or safety of the selected answer |
| Pairwise win rate / Elo | Human or judge preference between outputs | Chat style and broad preference comparisons | Absolute truth, local workload success, absence of bias |
| Rubric score | Human-defined quality dimensions | Local acceptance, RAG, tools, style, safety | General model ability beyond the rubric |
| LLM-as-judge score | Model-based judgment under a prompt | Fast screening and pairwise triage | Ground truth, unbiased preference, calibrated risk |
| Calibration / ECE / Brier | Whether confidence matches correctness | Classification, abstention, routing, risk thresholds | Generative faithfulness or instruction following |
| Latency / TTFT / TPOT / throughput | Serving behavior | Runtime, hardware, batching, context, deployment choices | Model capability or answer correctness |
| Memory / VRAM / OOM rate | Resource fit | Quantization, context, concurrency, model size | Quality of the response |
| Safety / refusal / policy rate | Boundary behavior | Deployment and tool/RAG safety gates | General helpfulness without allowed-task checks |

One number is never the model. It is one measurement of a model, prompt, runtime, data distribution, and evaluation procedure.

## Loss, NLL, And Perplexity

For a token sequence with targets `x_1 ... x_N`, the average negative log-likelihood is:

```text
NLL = -1/N * sum_i log p_model(x_i | x_<i)
```

Cross-entropy is the same practical quantity when the target distribution is one-hot over the observed next token. Perplexity is:

```text
perplexity = exp(NLL)
```

Interpretation:

| Observation | Sensible interpretation | Unsafe interpretation |
| --- | --- | --- |
| Training loss falls | The model fits the training distribution better. | The assistant is ready. |
| Validation loss falls | The fit transfers to held-out text from a similar distribution. | The model will follow instructions. |
| Perplexity is lower on corpus A than corpus B | Corpus A is less surprising under this model/tokenizer. | Corpus A is objectively easier or better. |
| SFT loss falls | The model predicts demonstration responses more strongly. | Human preference or safety improved. |
| Loss improves but local answers worsen | The metric and workload diverged, or the data changed behavior. | The benchmark must be wrong. |

Perplexity is most meaningful when tokenization, evaluation corpus, preprocessing, and context length are comparable. It is weak evidence across different model families, chat templates, languages, tokenizers, or instruction-following tasks.

## Benchmark Scores

Benchmarks are samples from a task distribution. Treat each score as a claim about that sample, not a universal quality label.

| Benchmark-style metric | Ask before trusting it |
| --- | --- |
| MMLU-style multiple choice | Is the task saturated, contaminated, or too broad for the local workload? |
| GSM/math benchmark | Are solutions exact, robust to prompt changes, and comparable under the same sampling budget? |
| Code benchmark | Is the metric pass@1 or pass@k, and does it count hidden tests or public examples? |
| Long-context benchmark | Does it test retrieval from the middle, distractors, and context length used locally? |
| RAG evaluation | Are retrieval and generation scored separately? |
| Agent/tool benchmark | Are tool calls validated by execution, or only judged from text? |
| Safety benchmark | Does it include both unsafe refusal and allowed benign compliance? |

Benchmark red flags:

- the paper reports only a headline average
- the metric is saturated
- examples may be in pretraining data
- prompt format or few-shot examples differ from local use
- the private/local evaluation set has no design audit, held-out split, or contamination control
- sampling budget, pass@k, or self-consistency is hidden
- failure examples are absent
- latency, cost, and memory are missing even though deployment is the claim

## Preference And Judge Scores

Preference metrics answer "which answer did someone or something prefer under this judging setup?" They do not automatically answer "which answer is true?"

| Signal | Use it for | Control |
| --- | --- | --- |
| Human pairwise win | Overall usefulness/style preference | Blind order, fixed prompt, clear rubric, tie option |
| Chatbot Arena-style rating | Broad chat preference | Treat as broad signal, not workload proof |
| LLM-as-judge | Cheap triage, pairwise comparison, rubric draft | Run AB and BA order, inspect rationale, keep human review for important gates, then audit with [[LLM/Study/Local LLM Judge Calibration Runner|Local LLM Judge Calibration Runner]] |
| MT-Bench-style multi-turn score | Instruction and conversational follow-through | Check whether the judge rewards verbosity or familiar style |

Common bias patterns:

- position bias: first or second answer wins too often
- verbosity bias: longer answer looks more useful
- confidence bias: assertive false answers score well
- self-preference or family preference: judge favors familiar style
- rubric leakage: the answer optimizes the rubric wording rather than the task

Use [[LLM/Study/Local LLM Evaluation Set Design Runner|Local LLM Evaluation Set Design Runner]] before the quality harness when the prompt suite itself must support repeated decisions. Use [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] to keep preference scores as supporting evidence beside human rubric rows, not as a replacement for them. Use [[LLM/Study/Local LLM Judge Calibration Runner|Local LLM Judge Calibration Runner]] before trusting LLM-as-judge rows for repeated local model/runtime decisions.

## Calibration And Confidence

Calibration asks whether predicted confidence matches empirical correctness. A model is calibrated if events it marks as 80 percent likely happen about 80 percent of the time.

Useful calibration settings:

- classification and routing
- extraction with confidence thresholds
- abstention or escalation decisions
- retrieval hit confidence
- tool-use risk scoring
- batch triage where false positives and false negatives have costs

Weak calibration settings:

- open-ended chat answers with no explicit probability
- free-form explanations where the model's stated confidence is not tied to a measured probability
- RAG answers without claim-level citation checks

Practical rule: do not trust a model's prose confidence. Trust measured correctness by confidence bucket, or avoid confidence-based automation.

## Local Inference Metrics

Local hosting adds measurements that papers often hide.

| Local metric | What it tells you | First route |
| --- | --- | --- |
| Time to first token (TTFT) | Prefill, queueing, context length, cold load, scheduler effects | [[LLM/Study/LLM Inference Request Lifecycle Lab]] |
| Time per output token (TPOT) | Decode speed and memory bandwidth pressure | [[LLM/Study/Local LLM Serving Internals and Scheduler Lab]] |
| Output tokens/sec | User-visible decode rate | [[LLM/Study/Local LLM Inference Benchmark Log]] |
| Prompt tokens | Prefill work and KV-cache size | [[LLM/Study/Local LLM Context Window and Token Budgeting Lab]] |
| Peak VRAM/RAM | Weight, KV cache, runtime overhead, batching headroom | [[LLM/Study/Local LLM Model and Hardware Sizing Guide]] |
| OOM rate | Whether the workload fits under expected context/concurrency | [[LLM/Study/Local LLM Troubleshooting Decision Tree]] |
| Queue depth / active requests | Saturation and backpressure | [[LLM/Study/Local LLM Concurrency and Batch Throughput Lab]] |
| Quality pass/hold/fail | Whether speed is usable for the workload | [[LLM/Study/Local LLM Quality Evaluation Harness]] |

Fast is not good. Good but too slow may still fail the local deployment decision. A credible local decision needs both performance evidence and quality evidence.

## Paper Reading Metric Card

Copy this into a paper note when a result matters.

| Field | Value |
| --- | --- |
| Paper / section |  |
| Main claim |  |
| Metric used | loss / perplexity / accuracy / F1 / pass@k / win rate / calibration / latency / memory / other |
| Dataset or workload |  |
| Baseline |  |
| Controlled variables |  |
| Hidden or weak variables | prompt, samples, data contamination, tokenizer, compute, inference budget, judge bias |
| What the metric proves |  |
| What it cannot prove |  |
| Local inference implication |  |
| Follow-up proof needed | benchmark row / quality row / RAG row / API contract / security check / deployment memo |

## Local Decision Metric Card

Use this when selecting a local model/runtime.

| Field | Value |
| --- | --- |
| Workload | chat / coding / extraction / RAG / tool use / batch summarization / other |
| Required quality gate |  |
| Required latency gate |  |
| Required memory gate |  |
| Required security or privacy gate |  |
| Candidate model/runtime |  |
| Evidence row |  |
| Metric that passed |  |
| Metric that failed or is missing |  |
| Decision | keep / tune / rerun / reject / escalate to hosted / change workload |
| Reason |  |

## Failure Patterns

| Symptom | Likely mistake | Better next step |
| --- | --- | --- |
| Lower perplexity model fails instructions | Treating next-token fit as assistant behavior | Run chat/template and quality harness checks. |
| High benchmark score fails private workload | Benchmark distribution mismatch | Build local held-out prompts and audit them with the evaluation set design runner. |
| Fast model gives unsupported citations | Treating latency as quality | Run RAG retrieval and citation audit. |
| Pairwise judge prefers verbose wrong answer | Judge bias | Run human rubric and AB/BA order control. |
| Model passes with high temperature only | Sampling hides instability | Freeze sampler for deterministic gates. |
| pass@k looks strong but first answer fails | Search budget is hidden | Record pass@1 for interactive use. |
| Calibration claim comes from prose confidence | No measured buckets | Require confidence buckets or remove automation. |
| Runtime comparison changes prompt and model | Variables are mixed | Use runtime comparison lab with fixed prompt/model/sampler. |

## Completion Gate

This guide is complete for one paper or local decision when you can:

- [ ] name the exact claim a metric supports
- [ ] name the dataset, workload, prompt, or distribution behind the metric
- [ ] explain at least one failure mode the metric misses
- [ ] separate training loss, benchmark score, preference score, calibration, quality rubric, latency, and memory evidence
- [ ] fill either a paper metric card or a local decision metric card
- [ ] route the next proof to the correct lab: evaluation set design, benchmark, quality harness, RAG evaluation, runtime comparison, API contract, or deployment matrix

## References

Internal:

- [[LLM/Study/LLM Math and Tensor Shape Primer]]
- [[LLM/Study/Tiny Decoder-Only Transformer Training Lab]]
- [[LLM/Study/LLM Training Pipeline Map]]
- [[LLM/Study/Local LLM Inference Metrics Field Guide]]
- [[LLM/Study/LLM Paper Reading Protocol]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Mechanism-to-Inference Bridge Map]]
- [[LLM/Study/Local LLM Evaluation Set Design Runner]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/Study/Local LLM Judge Calibration Runner]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Runtime Comparison Lab]]
- [[LLM/Study/Local LLM Client Harness Lab]]
- [[LLM/Study/Local LLM OpenAI-Compatible API Contract Lab]]
- [[LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab]]
- [[LLM/Study/LLM Deployment Decision Matrix]]
- [[LLM/2018–2019 — Pretrained Language Models/Knowledge and Reasoning Benchmarks]]
- [[LLM/2020–2021 — The Scaling Era/Scaling Laws]]
- [[LLM/2020–2021 — The Scaling Era/Contamination and Data Leakage]]
- [[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies]]
- [[LLM/2023 — Open Models and Agents/LLM-as-Judge]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
- [[LLM/_chunks/chunk-llm-237 MT-Bench Multi-Turn LLM Evaluation]]
- [[LLM/_chunks/chunk-llm-238 Chatbot Arena Elo Rating System]]
- [[LLM/_chunks/chunk-llm-239 LLM Judge Agreement Rates and Biases]]
- [[LLM/_chunks/chunk-llm-240 MT-Bench Chatbot Arena Evaluation Paradigms]]
