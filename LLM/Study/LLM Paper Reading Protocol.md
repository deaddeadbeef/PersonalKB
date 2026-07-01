---
tags: [study, llm, papers, research-literacy]
up: "[[LLM/Study/LLM Study Index]]"
confidence: policy
freshness: stable
tier-coverage: [practice, deep-dive]
---

# LLM Paper Reading Protocol

> **One-line summary** Reading LLM papers well means extracting the problem, method, evidence, limitations, and deployment implication, then placing the paper inside the field map instead of memorizing isolated claims.

Use this with the 20-paper fast path in [[LLM/Study/LLM Study Index|LLM Study Index]], [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map|LLM 20-Paper Fast Path Synthesis Map]], [[LLM/Study/LLM Paper Claim Ledger|LLM Paper Claim Ledger]], and the research-literacy gate in [[LLM/Study/LLM Mastery Roadmap|LLM Mastery Roadmap]]. The goal is not to read every paper linearly. The goal is to learn how to interrogate papers until you can tell what changed, what evidence supports it, and whether it matters for local models, RAG systems, inference, or evaluation. Use [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] after the claim row exists and before treating the paper as applied knowledge.

## Reading Passes

| Pass | Timebox | Output |
| --- | --- | --- |
| Triage | 10-15 minutes | Problem, claimed contribution, where it sits in the timeline |
| Mechanism | 30-60 minutes | The actual method, architecture, objective, or system change |
| Evidence | 30-90 minutes | Baselines, metrics, ablations, limitations, and deployment implications |
| Vault capture | 10-20 minutes | A short paper card, internal links, and open questions |

Do not start by reading every equation. Start by locating the claim, then read equations, experiments, and appendices only where they prove or weaken that claim.

Use [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide|LLM Metrics and Evaluation Interpretation Guide]] whenever the evidence section depends on a loss curve, benchmark row, pairwise preference result, judge score, calibration claim, latency number, or memory measurement.

## Paper Card Template

Copy this into a dated reading note or a paper-specific wiki note.

| Field | Prompt |
| --- | --- |
| Citation | Title, authors, year, source note |
| One-line claim | What does the paper say changed? |
| Problem | What limitation in previous work is being addressed? |
| Prior baseline | What was the strongest prior method or assumption? |
| Method | What mechanism, objective, data recipe, architecture, or system design is new? |
| Evidence | Which metric family, benchmark, ablation, scaling curve, human study, or systems measurement supports the claim? |
| Baselines | Were the baselines strong, current, and fairly tuned? |
| Ablations | What component mattered most? What was not isolated? |
| Assumptions | What data, compute, hardware, context length, or evaluator assumptions matter? |
| Failure modes | Where does the method not transfer? |
| Deployment implication | Does this change local hosting, inference cost, RAG design, fine-tuning, evaluation, or only frontier training? |
| Vault links | Which existing notes should this update or support? |
| Open questions | What would you test before trusting it? |

## Claim Extraction

Every paper should reduce to one of these claim shapes:

| Claim type | Ask | Example source area |
| --- | --- | --- |
| Architecture | What changed inside the model? | [[LLM/2017 — The Transformer/Transformer Architecture|Transformer Architecture]], [[LLM/2020–2021 — The Scaling Era/Mixture-of-Experts Models|Mixture-of-Experts Models]] |
| Training recipe | What changed in objective, data, scale, or optimization? | [[LLM/2020–2021 — The Scaling Era/Scaling Laws|Scaling Laws]], [[LLM/2022 — Alignment and Chat/Compute Data and Parameter Trade-offs|Compute/Data trade-offs]] |
| Adaptation | How does the model change after pretraining? | [[LLM/2020–2021 — The Scaling Era/LoRA and QLoRA|LoRA and QLoRA]], [[LLM/2022 — Alignment and Chat/Direct Preference Optimization|DPO]] |
| Prompting/reasoning | What behavior appears at inference time? | [[LLM/2022 — Alignment and Chat/Chain-of-Thought Prompting|Chain-of-Thought Prompting]] |
| Retrieval/tools | What system is built around the model? | [[LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly|Retrieval Pipelines]], [[LLM/2023 — Open Models and Agents/Function Calling|Function Calling]] |
| Evaluation | How is model behavior measured? | [[LLM/2023 — Open Models and Agents/LLM-as-Judge|LLM-as-Judge]], [[LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies|Human Evaluation]] |
| Inference systems | What changes latency, throughput, memory, or serving cost? | [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs|Serving Architectures]], [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache]] |

If a paper claims multiple categories, separate them. A model paper often bundles architecture, data, training scale, evaluation, and inference cost into one headline result. Mastery means isolating which variable actually did the work.

## Evidence Checklist

Use this before accepting the headline.

- Are the baselines relevant and competitive?
- Are the evaluation tasks aligned with the paper's claim?
- Are there ablations that isolate the claimed mechanism?
- Could the gain come from more data, more compute, cleaner data, or better prompting instead?
- Are the metrics saturated, contaminated, or too narrow?
- Does the paper report cost, latency, memory, context length, or hardware when those affect the claim?
- Are failures and negative results shown, or only best-case examples?
- Would the result transfer to a smaller local model, a quantized model, or a RAG system?

Tie evaluation concerns back to [[LLM/2018–2019 — Pretrained Language Models/Knowledge and Reasoning Benchmarks|Knowledge and Reasoning Benchmarks]], [[LLM/2020–2021 — The Scaling Era/Contamination and Data Leakage|Contamination and Data Leakage]], and [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes|RAG Evaluation and Failure Modes]].

## 20-Paper Fast Path Lens

The fast path in [[LLM/Study/LLM Study Index|LLM Study Index]] is not just a list. Read each paper for a specific concept.

| Paper | Read for |
| --- | --- |
| Attention Is All You Need | Self-attention, parallel sequence modeling, encoder/decoder structure |
| BERT | Masked language modeling, bidirectional encoders, pretrain-then-fine-tune |
| GPT-1 | Decoder-only pretraining plus downstream adaptation |
| GPT-2 | Scaling decoder-only language models and zero-shot transfer |
| GPT-3 | In-context learning and scale as a capability driver |
| Scaling Laws | Predictable relationships among parameters, data, compute, and loss |
| Chinchilla | Compute-optimal training and the data-vs-parameter trade-off |
| Megatron-LM | Tensor/model parallelism for large-scale training |
| FlashAttention | IO-aware attention and why memory movement matters |
| LLaMA | Open-weight efficient pretraining and inference-oriented model design |
| T5 | Text-to-text framing and encoder-decoder transfer learning |
| InstructGPT | SFT, reward modeling, and RLHF for assistant behavior |
| Constitutional AI | AI feedback and principle-guided alignment |
| DPO | Preference optimization without a separate reward model/PPO loop |
| LoRA | Low-rank adaptation as parameter-efficient fine-tuning |
| QLoRA | Finetuning quantized models under memory constraints |
| Chain-of-Thought | Prompted intermediate reasoning and its scale dependence |
| RAG | Retrieval as a way to add external knowledge and attribution |
| ReAct | Interleaving reasoning traces with tool/action use |
| HELM | Holistic evaluation across scenarios, metrics, and trade-offs |

After each paper, write one sentence in the form:

```text
Before this paper, the field mostly assumed __; after this paper, the important new lever was __.
```

## Deployment Implication Matrix

Academic understanding should end in an engineering judgment.

| If the paper is about | Ask for local deployment |
| --- | --- |
| Architecture | Does it require new kernels, model weights, or runtime support? |
| Training scale | Can a smaller open model inherit the idea, or is it frontier-only? |
| Fine-tuning | Can LoRA/QLoRA reproduce the behavior on available hardware? |
| Retrieval | Does it change chunking, embedding choice, reranking, or citation checks? |
| Inference optimization | Does it reduce TTFT, decode speed, KV memory, or batch throughput? |
| Evaluation | Does it improve [[LLM/Study/Local LLM Quality Evaluation Harness|Local LLM Quality Evaluation Harness]] or benchmark design? |
| Agents/tools | Does it change schemas, tool routing, error recovery, or action evaluation? |

Use [[LLM/Study/Local LLM Hosting and Inference Lab|Local LLM Hosting and Inference Lab]], [[LLM/Study/Local LLM Model and Hardware Sizing Guide|Local LLM Model and Hardware Sizing Guide]], and [[LLM/Study/Local LLM Inference Benchmark Log|Local LLM Inference Benchmark Log]] to test deployment implications instead of leaving them as abstract notes.

## Red Flags

Treat these as prompts for deeper reading:

- The headline mixes model scale, data quality, architecture, and prompting without ablations.
- The benchmark is saturated or likely contaminated.
- The method beats weak or outdated baselines.
- The paper reports accuracy but hides latency, memory, context length, or inference cost.
- The examples are persuasive but not tied to a repeatable metric.
- The method depends on private data, private models, or undisclosed filtering.
- The result works on a benchmark but not on the workload you actually care about.

## Vault Capture Workflow

After reading:

1. Link the paper to [[LLM/Sources/Sources Index|Sources Index]] or its raw source note.
2. Link the concept to the relevant timeline note.
3. Add one durable claim to an existing wiki note only if the source supports it.
4. Create a chunk only when the claim is atomic, reusable, and source-backed.
5. Add a practice implication when it changes local inference, RAG, evaluation, or deployment decisions.
6. Route the claim through [[LLM/Study/LLM Paper-to-Local Proof Router|LLM Paper-to-Local Proof Router]] when the local proof artifact is not obvious.
7. Leave uncertain claims as open questions instead of smoothing them into prose.

## Completion Gate

You have actually read a paper when you can answer these without looking:

- What problem did it solve?
- What was the strongest prior baseline?
- What mechanism did it introduce?
- What evidence supports the claim?
- What are the main limitations?
- Which existing LLM note does it update?
- What would you test before applying it to a local model or RAG system?

The 20-paper fast path is complete when you can write a one-page map connecting architecture, scaling, alignment, retrieval, evaluation, and inference systems without treating them as separate subjects.

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/Study/LLM Study Index]]
- [[LLM/Study/LLM 20-Paper Fast Path Synthesis Map]]
- [[LLM/Study/LLM Paper Claim Ledger]]
- [[LLM/Study/LLM Paper-to-Local Proof Router]]
- [[LLM/Study/LLM Mastery Roadmap]]
- [[LLM/Study/LLM Architecture Cheatsheet]]
- [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]
- [[LLM/Study/Local LLM Hosting and Inference Lab]]
- [[LLM/Study/Local LLM Model and Hardware Sizing Guide]]
- [[LLM/Study/Local LLM Inference Benchmark Log]]
- [[LLM/Study/Local LLM Quality Evaluation Harness]]
- [[LLM/2017 — The Transformer/Transformer Architecture]]
- [[LLM/2020–2021 — The Scaling Era/Scaling Laws]]
- [[LLM/2022 — Alignment and Chat/Reinforcement Learning from Human Feedback]]
- [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]]
- [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]]
