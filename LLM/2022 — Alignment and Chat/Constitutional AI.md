---
tags: [llm, alignment]
up: "[[2022 — Alignment and Chat Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Constitutional AI

> **One-line summary** Constitutional AI aligns models by having them critique and revise their own outputs using explicit natural-language principles instead of relying only on human feedback.

## 🎯 Intuition
**The Core Idea:** Constitutional AI (Bai et al., 2022) replaces human feedback with AI feedback, using a set of natural-language principles — the constitution — to guide self-critique and revision. The model generates responses, critiques them against the constitution, revises them, and then trains on the revised outputs. This process scales alignment without requiring expensive human annotation for every example, introducing the concept of RLAIF (Reinforcement Learning from AI Feedback) and advancing the idea of scalable oversight.

The Constitutional AI pipeline has two main phases. In the **critique-revision phase** (also called the "SL-CAI" stage), the model is prompted to generate a response to a potentially harmful query. It is then prompted to critique its own response against a specific constitutional principle (e.g., "Choose the response that is least likely to be used for harmful purposes"). Based on the critique, it generates a revised response. This (prompt, revised-response) pair becomes training data for supervised fine-tuning. The process is repeated across many principles and many prompts, generating a large dataset of constitutionally-revised outputs.

**Analogy:** Constitutional AI is like giving a student an answer key with values and asking them to grade and rewrite their own homework before the teacher sees it. The teacher still wrote the rules, but the student does much more of the correction work.

**Why It Matters:** Constitutional AI addresses the scalability bottleneck of RLHF. As models become more capable, the volume of feedback needed to align them grows, but human annotation capacity doesn't scale at the same rate. By having AI provide the feedback, Constitutional AI decouples alignment from human labor — at least partially. The constitution also makes alignment criteria transparent and editable, which is important for governance and auditability.

The concept of scalable oversight — how to supervise systems that are more capable than their supervisors — is one of the central challenges in alignment. Constitutional AI is an early practical approach: the model supervises itself according to human-specified principles. This is imperfect (the model may not catch its own subtle failures), but it demonstrates that the oversight loop doesn't require a human in every iteration.

---

## ⚙️ Core Mechanics
### How It Works
- **Critique-revision loop**: Generate → critique against principle → revise. Each constitutional principle produces a different critique angle. Multiple principles can be applied sequentially to the same response.
- **Constitution design**: 15–20 natural-language principles covering helpfulness, harmlessness, honesty, and specific safety concerns. Principles are written to be clear and actionable by the model.
- **SL-CAI (Supervised Learning from Constitutional AI)**: The SFT stage trained on revised outputs. This produces a model that is already somewhat aligned before any RL.
- **RLAIF (Reinforcement Learning from AI Feedback)**: The model itself provides preference labels for reward model training. The RM is then used in standard PPO, identical to the RLHF pipeline.
- **Chain-of-thought in feedback**: The AI annotator is asked to reason through its preference before stating it. This improves the quality and consistency of AI-generated labels.
- **Scalability**: The main advantage. Human annotation costs scale linearly with dataset size; AI annotation costs scale with compute, which is cheaper and faster. A single model can generate millions of preference pairs.
- **Iterated distillation**: The revised outputs from a stronger model can be used to train a weaker model, or the process can be applied iteratively — each round produces a better model that generates better critiques and revisions.
- **Limitations**: The constitution must be written by humans, so the approach still depends on human judgment at the meta-level. AI feedback can inherit biases from the model. The critique-revision process may not catch subtle alignment failures that the model itself doesn't recognize.

### Key Specifications
- **Two main phases**: critique-revision (SL-CAI) and RLAIF
- **Constitution size**: 15–20 natural-language principles
- **Preference training pipeline**: AI pairwise comparisons → reward model → PPO

### Key Facts
- Constitutional AI keeps the alignment criteria explicit in natural language.
- The revised outputs from self-critique become supervised training data.
- RLAIF swaps human preference labels for AI-generated preference labels.
- The main scalability benefit comes from replacing linear human-labeling costs with cheaper compute.

### Common Distinctions

| Aspect | RLHF | Constitutional AI |
|---|---|---|
| Feedback source | Human annotators | AI self-critique + constitution |
| Preference labels | Human pairwise comparisons | AI pairwise comparisons (RLAIF) |
| Scaling cost | Linear in annotations (expensive) | Linear in compute (cheaper) |
| Alignment criteria | Implicit in annotator guidelines | Explicit in constitution (auditable) |
| SFT data source | Human demonstrations | Model-generated revised outputs |
| Bottleneck | Annotator availability and quality | Constitution quality and model self-knowledge |

---

## 🔬 Deep Dive
### Technical Details
In the **RLAIF phase**, the model acts as its own preference annotator. Given two responses to the same prompt, the model is asked which response better adheres to the constitutional principles. These AI-generated preferences replace the human-generated preferences used in standard RLHF. A reward model is trained on these AI preferences, and the policy is optimized via PPO against that reward model — exactly as in RLHF, but with the human annotation step replaced by model self-evaluation.

The constitution itself is a set of natural-language principles that encode desired behavior. Examples include "Choose the response that is most helpful while being safe," "Choose the response that is least likely to contain harmful content," and "Choose the response that is most honest and transparent." The principles are intentionally human-readable and modifiable — changing the model's behavior is as simple as editing the constitution. This is philosophically significant: alignment criteria are made explicit and auditable rather than being implicit in a dataset of human preferences.

### Limitations and Criticisms
- The constitution must still be written by humans, so the method depends on human judgment at the meta-level.
- AI feedback can inherit biases already present in the model.
- The critique-revision process may fail to catch subtle alignment failures that the model itself cannot recognize.
- Scalable oversight is improved, not solved.

### Impact and Legacy
Constitutional AI helped formalize the idea that alignment criteria can be explicit, editable, and auditable. It also pushed the field toward scalable oversight and made RLAIF a practical alternative to fully human-labeled preference pipelines.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What role does the constitution play in Constitutional AI?
2. What is the difference between the critique-revision stage and the RLAIF stage?
3. Why is Constitutional AI considered more scalable than standard RLHF?

### Core Problems
1. Explain how Constitutional AI can reduce human-labeling costs while still depending on human judgment.
2. Compare RLHF and Constitutional AI in terms of where their supervision signal comes from and how transparent that signal is.

### Challenge
1. Draft three constitutional principles for a domain-specific assistant and explain how weaknesses in those principles could still produce misalignment.

## Supporting Chunks
*(To be populated as chunks are created)*

## References
- [[LLM/Sources/Sources Index]]
