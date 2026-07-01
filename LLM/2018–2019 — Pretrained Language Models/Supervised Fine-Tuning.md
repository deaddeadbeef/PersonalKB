---
tags: [llm, fine-tuning]
up: "[[2018–2019 — Pretrained Language Models Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Supervised Fine-Tuning

> **Supervised fine-tuning teaches a pretrained model to follow desired input-output patterns by training on labeled prompt-completion examples.**

## 🎯 Intuition
**The Core Idea:** Supervised fine-tuning adapts a pretrained language model by showing it labeled examples of the exact behavior you want.
**Analogy:** Like teaching a know-it-all to follow instructions instead of just knowing a lot of facts.
**Why It Matters:** SFT is the foundational technique that turns a generic base model into a useful assistant, domain model, or style-specific responder. It is simple, effective, and central to pipelines like RLHF, but it is also compute-heavy and can overfit quickly when data is limited.

---

## ⚙️ Core Mechanics
### How It Works
**Supervised Fine-Tuning (SFT)** is the process of training a pre-trained language model on labeled (prompt, completion) pairs to adapt its behavior for specific tasks or response styles. Unlike continued pretraining (which uses raw text), SFT uses structured examples that demonstrate the desired input-output mapping.

Full-parameter updates are performed—all model weights are adjusted based on the supervised training signal. This makes SFT powerful but resource-intensive and prone to overfitting on small datasets.

**Training Process:**
- Start with a pre-trained base model (e.g., LLaMA, GPT)
- Prepare labeled dataset: pairs of prompts and target completions
- Fine-tune using standard supervised learning (cross-entropy loss on completions)
- All model parameters updated via gradient descent

**Data Formatting:**
- **Instruction format**: System prompt + user instruction + assistant response
- **Chat templates**: Structured conversation format with role markers
- Quality over quantity: clean, diverse examples beat large noisy datasets
- Typical dataset sizes: 1K–100K examples (though highly variable)

**Overfitting Risks:**
- Small datasets (<10K examples) risk memorizing training data
- Model loses general capabilities, becomes brittle
- Mitigations: early stopping, dropout, mix in general data, use PEFT methods

**When SFT Helps:**
- Teaching specific response formats or styles
- Domain adaptation with labeled examples
- First stage of RLHF pipeline (before RL)
- Creating instruction-following from base models

**When SFT Is Insufficient:**
- Subjective preferences (RLHF needed)
- Complex reasoning (may need chain-of-thought data)
- Retrieval tasks (RAG may be better)
- New factual knowledge (continued pretraining needed)

**The SFT Stage in RLHF:**
1. SFT: Train on high-quality human demonstrations
2. Reward Model: Train preference model on comparisons
3. RL: Optimize against reward model via PPO/DPO

### Key Specifications

| Dimension | SFT | Continued Pretraining | PEFT (e.g., LoRA) |
|-----------|-----|----------------------|-------------------|
| **Data format** | (Prompt, completion) pairs | Raw text corpus | Same as SFT |
| **Parameters updated** | All weights | All weights | Small adapter subset |
| **Typical dataset size** | 1K–100K examples | Millions–billions of tokens | 1K–100K examples |
| **Primary use** | Task/style adaptation | Domain knowledge injection | Efficient task adaptation |
| **Overfitting risk** | High on small data | Low (large data) | Lower (fewer parameters) |
| **Compute cost** | High | Very high | Low–medium |

### Key Facts
- SFT uses labeled prompt-completion pairs rather than raw text.
- Standard SFT updates all model weights, making it more expensive than PEFT approaches such as LoRA.
- Small datasets can cause memorization and loss of general capabilities.
- SFT is the first stage of the RLHF pipeline.
- SFT is often the baseline against which parameter-efficient adaptation methods are compared.

---

## 🔬 Deep Dive
### Technical Details
SFT is the foundational technique that transforms base models into useful assistants. It's the most straightforward fine-tuning approach and serves as the baseline against which parameter-efficient methods are compared.

From an optimization perspective, SFT is standard supervised learning on completions, usually using cross-entropy loss over target tokens. The dataset is structured rather than raw: instead of continuing general language modeling, the model sees prompt-completion pairs or chat-formatted turns with explicit role markers. This makes the desired mapping much more direct than in continued pretraining.

The method is flexible: it can teach response format, domain-specific behavior, and instruction following. It is also the first stage in the RLHF pipeline, where a model is first trained on high-quality demonstrations, then used to support reward-model training, and finally optimized further with RL methods such as PPO or preference-optimization approaches such as DPO.

But full-parameter SFT is expensive and can overfit. On small datasets—especially below roughly 10K examples—the model can memorize the training distribution, become brittle, and lose broader general capabilities. Common mitigations include early stopping, dropout, mixing in more general data, or shifting to parameter-efficient fine-tuning methods instead of updating all weights.

SFT is also not a universal solution. If the goal is subjective preference alignment, RLHF-style preference learning is usually needed. If the goal is harder reasoning, chain-of-thought exemplars may be necessary. If the goal is retrieval performance, RAG may outperform pure SFT. If the goal is adding new factual knowledge, continued pretraining is often a better fit.

Understanding SFT's strengths (flexibility, effectiveness) and limitations (data requirements, overfitting) is essential for choosing the right adaptation strategy.

### Limitations and Criticisms
- Full-parameter SFT is resource-intensive because all model weights are updated.
- Small labeled datasets can cause overfitting, memorization, brittleness, and loss of general capabilities.
- SFT alone is often insufficient for subjective preference alignment, retrieval-heavy tasks, difficult reasoning, or injecting large amounts of new factual knowledge.

### Impact and Legacy
SFT became the standard bridge between pretrained base models and useful downstream assistants. It underpins instruction-following systems, anchors the first stage of RLHF, and provides the conceptual baseline from which LoRA, QLoRA, and other parameter-efficient methods are evaluated.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What is the main difference between SFT data and continued pretraining data?
2. Why does updating all weights make SFT both powerful and risky?
3. Why is SFT considered the first stage rather than the whole RLHF pipeline?

### Core Problems
1. Compare SFT, continued pretraining, and PEFT along the dimensions in the table, and explain when each is the better adaptation strategy.
2. A team has only 5,000 labeled examples and wants a model to answer in a specific format without losing general ability. What risks arise with full SFT, and what mitigations from the note would you apply?

### Challenge
1. Argue for or against the claim that SFT is the single most important adaptation method in practical LLM engineering, even though it is often replaced by PEFT or supplemented by RLHF and RAG.

---

*See also:* [[Language Model Fundamentals]], [[LoRA and QLoRA]], [[Instruction Tuning]], [[Reinforcement Learning from Human Feedback]], [[Open-Weight Model Ecosystem]]

## References
- [[Instruction Tuning]] — Scaling SFT across diverse tasks for generalization
- [[LoRA and QLoRA]] — Efficient alternative to full SFT
- [[Domain Adaptation]] — Combining continued pretraining with SFT
- [[Continual Fine-Tuning and Catastrophic Forgetting]] — Challenges of sequential SFT

See [[LLM/Sources/Sources Index|LLM Sources Index]] for papers on:
- InstructGPT (Ouyang et al. 2022) — RLHF pipeline starting with SFT
- FLAN papers (Wei et al. 2021, Chung et al. 2022) — Instruction tuning methodology
- Alpaca (Taori et al. 2023) — Low-cost SFT demonstration

## References
- [[LLM/Sources/Sources Index|LLM Sources Index]]
