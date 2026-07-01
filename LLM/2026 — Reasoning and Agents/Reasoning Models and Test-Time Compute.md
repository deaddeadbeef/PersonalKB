---
tags: [llm, reasoning-agents]
up: "[[2026 — Reasoning and Agents Overview]]"
confidence: verified
freshness: current-sensitive
tier-coverage: [intuition, core, deep-dive, practice]
---

# Reasoning Models and Test-Time Compute

> **One-line summary** Reasoning models allocate additional compute at inference time to solve harder problems, representing a new scaling axis orthogonal to parameter count.

## 🎯 Intuition

### Core Idea

Traditional scaling improves models by making them bigger and training them more. Reasoning models add another lever: let the model spend more effort at inference time before it answers.

### Analogy

This is like spending more time on a harder exam question — bigger brain vs. thinking harder.

### Why It Matters

Instead of paying the cost of a larger model on every query, systems can answer easy questions quickly and spend extra compute only when a problem is hard.

---

## ⚙️ Core Mechanics

### How It Works

Reasoning models generate extended internal reasoning before producing an answer. OpenAI's **o1** (September 2024) was the first major model of this kind. It produced hidden reasoning tokens not shown to the user, allowing the model to decompose problems, check its work, and explore multiple solution paths.

This introduced **test-time compute** as a second scaling axis alongside model size and training compute. The **o3** and **o3-mini** models in early 2025 extended the idea with configurable thinking budgets that trade latency for accuracy.

### Key Specs

- First major release: **o1, September 2024**
- Reasoning visibility: **hidden chain-of-thought**
- Adjustable effort: **o3-mini low / medium / high reasoning effort**

### Key Facts

- **o1-preview** released September 2024; o1-mini followed as a faster, cheaper variant
- **Hidden chain-of-thought**: reasoning tokens are generated but not shown to the user
- **AIME 2024**: o1 scored 83.3% vs GPT-4o's 13.4%
- **GPQA Diamond**: o1 reached 78.0% (PhD-level science)
- **o3-mini** offers low/medium/high "reasoning effort" settings
- **Test-time compute** scales performance without retraining the model
- **Safety via reasoning**: CoT monitoring enables detecting harmful reasoning chains

| Concept | Traditional Scaling | Test-Time Compute |
|---------|-------------------|-------------------|
| When compute is spent | Training | Inference |
| How to improve | More parameters/data | More reasoning tokens |
| Cost profile | Fixed per query | Variable per query |
| Analogy | Bigger brain | Thinking harder |
| Scaling law axis | Chinchilla (train compute) | Inference compute |

---

## 🔬 Deep Dive

### Technical Details

OpenAI o1 posted dramatic benchmark gains: **83.3% on AIME 2024** versus **13.4% for GPT-4o**, **78.0% on GPQA Diamond**, and a **Codeforces rating of 1807**, placing it in the **93rd percentile** of competitive programmers. These results suggested that performance scales predictably with inference-time compute, producing new **inference scaling laws** analogous to training scaling laws.

### Limitations

- More reasoning tokens increase latency and per-query cost
- Hidden reasoning creates transparency trade-offs
- Better reasoning does not automatically remove hallucinations or guarantee correctness

### Impact

Test-time compute opened a second frontier for capability improvement and enabled new safety ideas, including monitoring chain-of-thought for deceptive or harmful reasoning.

### Related Notes

- [[Chain-of-Thought Prompting]] — the prompting technique that inspired reasoning models
- [[LLM/2020–2021 — The Scaling Era/Scaling Laws|Scaling Laws and Chinchilla]] — training-time scaling laws that reasoning models complement
- [[DeepSeek R1 and Open Reasoning]] — open-source replication of the reasoning paradigm
- [[LLM/Study/Local LLM Reasoning Budget and Test-Time Compute Lab]] — practical local harness for thinking mode, reasoning effort, parser separation, latency, quality, and trace policy.
- [[Frontier Models 2025-2026]] — the broader model generation context

---

## 🏋️ Practice

### Warm-Up

1. What is test-time compute?
2. Why is it called a new scaling axis?

### Core Problems

1. Compare training-time scaling with inference-time scaling.
2. Explain why hidden chain-of-thought can improve problem solving.
3. Describe how o3-mini's reasoning effort settings embody the test-time compute idea.

### Challenge

Argue whether future capability progress is more likely to come from larger base models or from better control over inference-time reasoning budgets.

---

## Supporting Chunks

- [[LLM/_chunks/chunk-llm-241 Test-time compute scaling improves performance by allocating more inference tokens to harder problems|chunk-llm-241]]
- [[LLM/_chunks/chunk-llm-242 OpenAI o1 scores 83 percent on AIME 2024 via hidden chain-of-thought reasoning|chunk-llm-242]]
- [[LLM/_chunks/chunk-llm-243 Inference scaling laws predict model performance as a function of thinking time|chunk-llm-243]]

## References

→ [[LLM/Sources/Sources Index|Sources Index]]
