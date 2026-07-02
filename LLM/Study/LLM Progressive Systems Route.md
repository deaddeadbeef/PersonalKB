---
tags: [study, llm, route, agentic-ai]
up: "[[LLM/Study/LLM Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
source: "[[LLM/_raw/raw-llm-071|raw-llm-071]]"
---

# LLM Progressive Systems Route

> **One-line summary** A PDF-aligned route for revealing the LLM stack in order: model mechanics, systems constraints, post-training, reasoning, evaluation, agent loops, harnesses, and proof artifacts.

Use this when the LLM wiki feels too wide. The route follows the teaching shape extracted from [[LLM/_raw/raw-llm-071|The Hitchhiker's Guide to Agentic AI]]: do not begin with agent frameworks. Begin with the model pipeline, then reveal the layers that make agents work.

## Progressive Reveal Rule

Open one layer at a time:

1. Read the overview and at most three linked notes.
2. Explain the mechanism without looking.
3. Leave one proof artifact or one missing-evidence row.
4. Move to the next layer only when the current layer can explain a real failure, tradeoff, or design decision.

Do not open raw notes, chunks, runners, or implementation labs first. Those are evidence and proof layers, not the initial reading path.

## Route Map

| Stage | Reveal | Open first | Then deepen | Leave behind |
|---:|---|---|---|---|
| 0 | Orientation | [[LLM/LLM Book Reading Spine]] | [[LLM/LLM — Learning Path]], [[LLM/LLM Corpus Index]] | One chosen stage and one stop condition |
| 1 | Model pipeline | [[LLM/Pre-2017 — Before Transformers/Tokenization]], [[LLM/2017 — The Transformer/Transformer Architecture]] | [[LLM/Study/LLM Math and Tensor Shape Primer]], [[LLM/Study/Attention Implementation Lab]] | A text -> tokens -> representations -> logits -> text explanation |
| 2 | Training and systems constraints | [[LLM/Study/LLM Training Pipeline Map]], [[LLM/2020–2021 — The Scaling Era/Training Infrastructure and Parallelism]] | [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]], [[LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs]] | A claim tying quality, memory, latency, and training or serving cost together |
| 3 | Adaptation and alignment | [[LLM/2018–2019 — Pretrained Language Models/Supervised Fine-Tuning]], [[LLM/2022 — Alignment and Chat/Reinforcement Learning from Human Feedback]] | [[LLM/2022 — Alignment and Chat/Direct Preference Optimization]], [[LLM/Study/LLM Adaptation and Fine-Tuning Decision Guide]] | A no-train, RAG, SFT, LoRA, DPO, or distillation decision row |
| 4 | Reasoning and test-time compute | [[LLM/2026 — Reasoning and Agents/Reasoning Models and Test-Time Compute]], [[LLM/2026 — Reasoning and Agents/DeepSeek R1 and Open Reasoning]] | [[LLM/2026 — Reasoning and Agents/Reasoning Distillation]], [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab]] | A reasoning-budget hypothesis and what evidence would prove it |
| 5 | Evaluation | [[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]], [[LLM/2023 — Open Models and Agents/LLM-as-Judge]] | [[LLM/Study/Local LLM Evaluation Set Design Runner]], [[LLM/Study/Local LLM Quality Evaluation Runner]], [[LLM/Study/Local LLM Judge Calibration Runner]] | A pass, hold, or fail decision whose evidence is named |
| 6 | Agentic systems | [[LLM/2023 — Open Models and Agents/Tool Selection and Execution Loops]], [[LLM/2024–2025 — Frontier and Efficiency/Memory and State Management]] | [[LLM/2023 — Open Models and Agents/RAG Evaluation and Failure Modes]], [[LLM/2026 — Reasoning and Agents/Model Context Protocol]], [[LLM/2024–2025 — Frontier and Efficiency/Multi-Agent Systems]] | An observation -> reason -> action -> observation loop diagram with state and safety boundaries |
| 7 | Harness and local proof | [[LLM/Study/Local LLM End-to-End Mental Model]], [[LLM/Study/Local LLM Runtime Stack Anatomy]] | [[LLM/Study/Local LLM Hands-On Practicum Sequence]], [[LLM/Study/Local LLM First Endpoint Evidence Audit Runner]], [[LLM/Study/Local LLM Security and Privacy Runbook]] | One saved local endpoint, request lifecycle, benchmark, quality, privacy, or integration proof |
| 8 | Defense and capstone | [[LLM/Study/LLM Paper Reading Protocol]], [[LLM/Study/LLM Mastery Self-Assessment Exam]] | [[LLM/Study/LLM Paper Claim Ledger]], [[LLM/Study/LLM Mastery Capstone Workbook]], [[LLM/Study/LLM Mastery Evidence Audit Runner]] | One defended paper claim or capstone evidence row |

## What Each Stage Unlocks

### 1. Model Pipeline

Start with the pipeline because every later system still calls a model. The minimum mental model is: text becomes tokens, tokens become vectors, transformer layers build contextual representations, logits rank possible next tokens, and decoding turns selected tokens back into text.

Evidence: [[LLM/_chunks/chunk-llm-262 LLM foundations start with text to tokens to representations to logits|chunk-llm-262]]

### 2. Training And Systems Constraints

Once the pipeline is visible, add the cost model. Training requires data, optimizer stability, parallelism, and hardware throughput. Inference requires memory for weights and KV cache, scheduler choices, batching, latency targets, and quality measurement.

Evidence: [[LLM/_chunks/chunk-llm-261 Agentic AI requires a full-stack first-principles-to-production curriculum|chunk-llm-261]]

### 3. Adaptation And Alignment

Post-training splits into different jobs. SFT teaches imitation and format. RLHF and DPO move behavior toward preferences. Verifiable rewards can train capability when outcomes can be checked. Adaptation choices need baseline failure evidence before training.

Evidence: [[LLM/_chunks/chunk-llm-263 RL for LLMs splits into preference alignment and verifiable reward capability learning|chunk-llm-263]]

### 4. Reasoning

Reasoning models are not just larger chat models. Treat them as inference-time search and verification systems where sparse rewards, long horizons, and verifiable answers matter. This layer connects DeepSeek-R1, reasoning distillation, and local reasoning-budget controls.

Evidence: [[LLM/_chunks/chunk-llm-264 Reasoning RL treats multi-step reasoning as verifiable search under sparse rewards|chunk-llm-264]]

### 5. Evaluation

Evaluation comes before agent claims. For LLMs, there may be many plausible outputs, several quality axes, contamination risks, and model-judge biases. A model or agent is not "good" until the workload, rubric, evidence, and failure owner are explicit.

Evidence: [[LLM/_chunks/chunk-llm-265 LLM evaluation must handle open-ended multidimensional language outputs|chunk-llm-265]]

### 6. Agentic Systems

Only now open the agent layer. An agent is a loop that observes, reasons, acts, receives new observations, and repeats. RAG gives grounding, memory gives state, tools give action, protocols reduce integration cost, and safety/handoff rules keep autonomy bounded.

Evidence: [[LLM/_chunks/chunk-llm-266 Agentic AI is an observation reason action loop with memory grounding action and safety|chunk-llm-266]]

### 7. Harness And Local Proof

The harness is the runtime shell around the model. Keep reasoning, execution, memory, communication, and observability separate. Then prove the stack locally with a saved endpoint run, request lifecycle trace, benchmark row, quality gate, privacy check, or integration artifact.

Evidence: [[LLM/_chunks/chunk-llm-267 Agent harness design separates reasoning execution memory communication and observability|chunk-llm-267]]

### 8. Defense And Capstone

Finish with assessment. A good LLM wiki should make the reader able to answer, build, evaluate, and defend. The terminal artifact is not another reading list; it is a paper claim, local proof, exam score, or capstone evidence ledger.

Evidence: [[LLM/_chunks/chunk-llm-268 Agentic AI learning should end in self-assessment and proof artifacts|chunk-llm-268]]

## Minimal First Session

If you have one hour, do this:

1. Read [[LLM/2017 — The Transformer/Transformer Architecture]] and [[LLM/Pre-2017 — Before Transformers/Tokenization]].
2. Write the pipeline from memory: text -> tokens -> representations -> logits -> text.
3. Open [[LLM/Study/Local LLM End-to-End Mental Model]] only long enough to connect the same pipeline to a real request.
4. Stop with one gap: the phase you cannot explain yet.

## References

- [[LLM/_raw/raw-llm-071|The Hitchhiker's Guide to Agentic AI]]
- [[LLM/Sources/Sources Index]]
- [[LLM/LLM Book Reading Spine]]
- [[LLM/Study/LLM Study Index]]
