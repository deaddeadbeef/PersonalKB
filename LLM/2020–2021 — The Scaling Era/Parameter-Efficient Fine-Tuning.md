---
tags: [llm, fine-tuning]
up: "[[2020–2021 — The Scaling Era Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Parameter-Efficient Fine-Tuning

> **PEFT adapts large models by updating only a tiny, carefully chosen subset of parameters instead of retraining the whole network.**

## 🎯 Intuition
**The Core Idea:** Most task adaptation does not require changing every parameter in a large model—training a small, well-designed subset is often enough.
**Analogy:** PEFT is like tuning a few key knobs on a studio mixing board instead of rebuilding the entire recording studio every time you want a new sound.
**Why It Matters:** PEFT democratizes fine-tuning by slashing compute, memory, and storage requirements while still reaching performance comparable to full fine-tuning. Before PEFT, adapting a 70B model required expensive multi-GPU clusters; with methods like QLoRA, that work can happen on a single consumer GPU. It also enables multi-tenant serving, faster experimentation, and much lower storage overhead because the base model can be reused across many tasks.

---

## ⚙️ Core Mechanics
### How It Works
- **Parameter-Efficient Fine-Tuning (PEFT)** methods adapt large language models by training only a small fraction of parameters (<1–5%) while keeping the base model frozen. This dramatically reduces compute, memory, and storage costs while achieving comparable performance to full fine-tuning.

**Adapters (Houlsby et al. 2019):**
- Insert small trainable modules between transformer layers
- Typical structure: down-projection (d → r) → nonlinearity → up-projection (r → d)
- Bottleneck dimension r ≪ d (e.g., r=64 for d=768)
- Base model weights frozen, only adapter parameters trained
- Overhead: Small latency increase due to sequential computation

**Prefix Tuning (Li & Liang 2021):**
- Prepend trainable "virtual tokens" to each layer's key-value pairs
- Prefix length: typically 10–200 tokens
- These aren't real tokens—they're continuous embeddings optimized during training
- Base model frozen; only prefix parameters updated
- Inference: Prefix stored and reused for all inputs

**Prompt Tuning (Lester et al. 2021):**
- Simplification of prefix tuning: only tune soft prompts at input layer
- "Soft prompt": trainable continuous embeddings (vs discrete text tokens)
- Typically 20–100 soft tokens prepended to input
- Works well on T5-XXL (11B) and larger; struggles on smaller models
- Extremely lightweight: ~0.01% parameters

**P-Tuning v2 (Liu et al. 2022):**
- Combines ideas: trainable prompts at every layer (like prefix tuning)
- Optimization improvements for better convergence
- Shown to match full fine-tuning on SuperGLUE benchmarks
- Works across model scales (from 300M to 10B+)

**The PEFT landscape:**
- **Adapters**: Most general, small latency cost
- **LoRA**: No inference overhead, most popular (see [[LoRA and QLoRA]])
- **Prefix/Prompt Tuning**: Extremely parameter-efficient, best for large models
- **(IA)³ (Infused Adapter by Inhibiting and Amplifying Inner Activations)**: Element-wise scaling, minimal parameters

**When to use which:**
- **Full fine-tuning**: Abundant compute, need maximum performance
- **LoRA**: Best balance of efficiency and performance (default choice)
- **Adapters**: Need to swap tasks frequently, can tolerate latency
- **Prompt tuning**: Massive models (10B+), extremely limited resources
- **Multiple adapters**: Serving many tasks from one base model

### Key Specifications

| Method | Trainable Params | Inference Overhead | Complexity | When to Use |
|--------|-----------------|-------------------|------------|-------------|
| **Full Fine-Tuning** | 100% | None | Simple | Max performance, abundant resources |
| **Adapters** | 0.5–5% | Small latency | Medium | Multi-task serving, ok with latency |
| **LoRA** | 0.1–1% | None (merged) | Low | General-purpose PEFT (default) |
| **Prefix Tuning** | 0.1–1% | Minimal | Medium | Large models, need flexibility |
| **Prompt Tuning** | <0.01% | Minimal | Low | Massive models (10B+), minimal resources |

### Key Facts
- PEFT usually trains less than 1–5% of model parameters while freezing the base model.
- Adapters insert bottleneck modules into transformer layers and add a small inference latency cost.
- Prompt tuning can be extremely lightweight at around ~0.01% trainable parameters.
- P-Tuning v2 was shown to match full fine-tuning on SuperGLUE and works from roughly 300M to 10B+ model scales.
- LoRA is the default choice when you want the best balance between efficiency and performance.

---

## 🔬 Deep Dive
### Technical Details
- The core insight: full-parameter updates are often redundant—most adaptation can be achieved by modifying a small, carefully designed subset of the model.
- Adapter modules use a bottleneck architecture: down-projection (d → r), nonlinearity, then up-projection (r → d), where r ≪ d.
- Prefix tuning adds trainable continuous vectors to each layer’s key-value pairs rather than adding literal text tokens.
- Prompt tuning simplifies this further by learning soft prompts only at the input layer.
- P-Tuning v2 extends prompt-like adaptation to every layer and improves optimization for convergence across a wide range of model sizes.
- (IA)³ uses element-wise scaling to inhibit or amplify inner activations with very few trainable parameters.

### Limitations and Criticisms
- Adapters introduce a small latency increase because the inserted modules add sequential computation at inference time.
- Prompt tuning works well on very large models but struggles on smaller ones.
- Full fine-tuning can still be preferable when compute is abundant and absolute maximum performance is required.

### Impact and Legacy
PEFT changed fine-tuning from an expensive, cluster-heavy workflow into something far more accessible. It created a practical ecosystem of methods—adapters, LoRA, prefix tuning, prompt tuning, P-Tuning v2, and (IA)³—that support different trade-offs in latency, flexibility, and parameter count. It also enabled one base model to support many task-specific adaptations, making multi-tenant serving, rapid experimentation, and low-storage deployment strategies much more practical.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why can PEFT often match full fine-tuning even though it updates only a small fraction of parameters?
2. What is the difference between prefix tuning and prompt tuning?
3. Why is LoRA usually treated as the default PEFT choice?

### Core Problems
1. You need to serve many task-specific variants of the same base model. Compare adapters, LoRA, and prompt tuning for this scenario in terms of latency, storage, and ease of swapping tasks.
2. A team has extremely limited GPU memory but needs to adapt a 10B+ model quickly. Choose a PEFT strategy and justify it using the trade-offs in the note.

### Challenge
1. Develop a decision framework for choosing among full fine-tuning, adapters, LoRA, prefix tuning, prompt tuning, P-Tuning v2, and (IA)³ for a new LLM product, and explain how model scale, latency budget, and deployment style affect the choice.

*See also:* [[LoRA and QLoRA]]; [[Adapter Architectures]]; [[Multi-Adapter Serving]]; [[Supervised Fine-Tuning]]

## Supporting Chunks / References
### Supporting Chunks
- [[LoRA and QLoRA]] — Most popular PEFT method (detailed breakdown)
- [[Supervised Fine-Tuning]] — Full fine-tuning baseline
- [[Adapter Architectures]] — Deep dive into adapter design patterns
- [[Multi-Adapter Serving]] — Deploying many PEFT adapters efficiently

### References to Sources Index
See [[LLM/Sources/Sources Index|LLM Sources Index]] for papers:
- Houlsby et al. 2019: Adapter modules
- Li & Liang 2021: Prefix tuning
- Lester et al. 2021: Prompt tuning
- Liu et al. 2022: P-Tuning v2
- Hu et al. 2021: LoRA (see [[LoRA and QLoRA]])
- He et al. 2021: (IA)³
