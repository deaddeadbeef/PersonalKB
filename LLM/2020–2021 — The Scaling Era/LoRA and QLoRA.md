---
tags: [llm, fine-tuning]
up: "[[2020–2021 — The Scaling Era Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# LoRA and QLoRA

> **Low-rank adapters and 4-bit quantization make high-quality LLM fine-tuning dramatically cheaper without changing the base model’s core architecture.**

## 🎯 Intuition
**The Core Idea:** LoRA adapts a frozen model by learning low-rank weight updates, and QLoRA pushes that idea further by combining those adapters with 4-bit quantization of the base model.
**Analogy:** LoRA is like adding sticky-note corrections to a textbook instead of rewriting every page, while QLoRA is doing that on a compressed travel edition you can actually carry around.
**Why It Matters:** LoRA democratized LLM fine-tuning by matching full fine-tuning quality on many tasks while training only a tiny fraction of parameters. It became the default PEFT method because it has zero inference overhead after merging, reduces trainable parameters by 10–10,000×, and is simple to implement with strong tooling support. QLoRA extended that breakthrough further by making 65B+ model fine-tuning feasible on a single 48GB GPU instead of a multi-GPU cluster.

---

## ⚙️ Core Mechanics
### How It Works
**Training setup:**
- **LoRA (Low-Rank Adaptation)** adapts large models by representing weight updates as low-rank decompositions: **W = W₀ + BA**, where W₀ is the frozen pretrained weight matrix, and B, A are small trainable matrices with rank r ≪ min(d_in, d_out).
- Only the low-rank matrices A and B are trained—the base model stays frozen.
- At inference, BA can be merged into W₀ for **zero computational overhead**.
- **QLoRA (Quantized LoRA)** combines 4-bit quantization of the base model with LoRA adapters, enabling fine-tuning of 65B parameter models on a single 48GB GPU—previously impossible without multi-GPU clusters.

**Which layers to adapt:**
- Original LoRA paper: Query and Value projection matrices (Q, V)
- Common practice: Q, K, V, and output projection (4 matrices per attention layer)
- Aggressive: All linear layers including feed-forward networks
- Trade-off: More matrices → better performance, more parameters

**Rank selection:**
- **r = 1–4**: Extremely efficient, may underfit
- **r = 8**: Sweet spot for many tasks
- **r = 16–32**: Better for complex tasks, diminishing returns
- **r = 64+**: Approaching full fine-tuning cost/performance
- Task complexity and model size influence optimal rank

**Initialization:**
- A: Random Gaussian initialization (mean 0, small std)
- B: Zero initialization → ΔW = 0 at start (preserves pretrained behavior)
- Scaling: ΔWx scaled by α/r (α typically = r, sometimes 2r)

**Merging at inference:**
- Training: Keep W₀ and BA separate
- Deployment: Compute W_merged = W₀ + BA once
- Result: No inference overhead—same speed as base model

**QLoRA innovations (Dettmers et al. 2023):**
1. **4-bit NormalFloat quantization** of base model weights
   - Information-theoretically optimal for normally distributed weights
   - Block-wise quantization (64–128 elements per block)
2. **Double quantization**: Quantize the quantization constants themselves
3. **Paged Optimizers**: Use CPU RAM for optimizer states via unified memory
4. **LoRA adapters**: Remain in 16-bit for training quality

**QLoRA memory savings:**
- 16-bit (FP16/BF16): ~2 bytes per parameter
- 4-bit (NF4): ~0.5 bytes per parameter
- Example: 65B model → 130GB (FP16) vs 33GB (4-bit)
- Plus LoRA adapters (~1% extra) + gradients + optimizer states fit in 48GB

**Multi-adapter serving:**
- One base model in GPU memory (quantized or full precision)
- Swap LoRA adapters (BA matrices) per request/task
- Adapter size: 10–100MB vs multi-GB base model
- Latency: Minimal (just memory load, no recomputation)
- Use case: Personalization, multi-tenant serving, A/B testing

### Key Specifications

| Dimension | Full Fine-Tuning | LoRA | QLoRA |
|-----------|-----------------|------|-------|
| **Trainable params** | 100% | 0.1–1% | 0.1–1% |
| **Base model precision** | FP16/BF16 | FP16/BF16 | 4-bit NF4 |
| **GPU memory (65B)** | ~260GB (4×A100) | ~130GB (2×A100) | ~48GB (1×A6000) |
| **Inference overhead** | None | None (merged) | Minimal (dequant) |
| **Quality vs full FT** | 100% (baseline) | 95–100% | 95–100% |
| **Training speed** | 1× | 1.2–1.5× | 0.6–0.8× |

| Method | Inference Overhead | Memory Savings | Quality | Flexibility |
|--------|-------------------|----------------|---------|-------------|
| **LoRA** | None | High | Excellent | High |
| **Adapters** | 5–10% latency | High | Excellent | High |
| **Prefix Tuning** | Minimal | Very high | Good | Medium |
| **Prompt Tuning** | Minimal | Extreme | Good (large models) | Low |

### Key Facts
- LoRA trains only low-rank matrices while keeping the pretrained base weights frozen.
- Typical LoRA ranks are 4, 8, 16, or 32 instead of full hidden sizes around 4096.
- QLoRA’s NF4 quantization cuts base-model memory from roughly 2 bytes per parameter to about 0.5 bytes per parameter.
- A 65B model that needs about 130GB in FP16 can fit in about 33GB in 4-bit before adding adapters and optimizer state management.
- Multi-adapter serving lets one base model support many small task-specific adapters with minimal latency.

---

## 🔬 Deep Dive
### Technical Details
**LoRA mathematics (Hu et al. 2021):**
- Original weight matrix: W ∈ ℝ^(d_out × d_in)
- LoRA decomposition: ΔW = BA, where B ∈ ℝ^(d_out × r), A ∈ ℝ^(r × d_in)
- Forward pass: h = W₀x + BAx = W₀x + ΔWx
- Trainable parameters: r(d_in + d_out) instead of d_in × d_out
- Typical rank: r = 4, 8, 16, 32 (vs d_in, d_out ~ 4096)

### Limitations and Criticisms
- Very low ranks such as **r = 1–4** can be extremely efficient but may underfit harder tasks.
- Increasing the rank to **r = 64+** starts to approach the cost/performance regime of full fine-tuning, reducing the efficiency advantage.
- QLoRA gains major memory savings, but it accepts minimal dequantization overhead at inference and slower training speed than standard LoRA.

### Impact and Legacy
LoRA is the default PEFT method because it matches full fine-tuning quality on many tasks, has zero inference overhead after merging, reduces trainable parameters by 10–10,000×, and is simple to implement and well-supported (HuggingFace PEFT, etc.). QLoRA transformed 65B-scale adaptation from a data-center operation into something feasible on consumer or prosumer hardware. It also helped normalize multi-adapter deployment patterns for personalization, multi-tenant serving, and A/B testing.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does training only A and B let LoRA preserve the pretrained model’s original behavior at initialization?
2. What practical advantage does merging BA into W₀ give LoRA at deployment time?
3. Why does QLoRA keep LoRA adapters in 16-bit even though the base model is quantized to 4-bit?

### Core Problems
1. Suppose an attention projection has shape d_out = d_in = 4096 and LoRA rank r = 8. Compare the trainable parameter count of LoRA with full fine-tuning for that matrix, and explain why the savings are so large.
2. You are deploying one base model for many customers with slightly different behaviors. Design a serving strategy using multi-adapter serving, and explain when you would choose LoRA versus QLoRA.

### Challenge
1. If a 65B model must be fine-tuned on a single 48GB GPU, explain how NF4 quantization, double quantization, paged optimizers, and low-rank adapters work together to make that feasible—and where the remaining bottlenecks still are.

*See also:* [[LLM/Inference and Serving/Quantization|Quantization]] — QLoRA combines quantization with LoRA; [[LLM/Fine-Tuning and Adaptation/Continual Fine-Tuning and Catastrophic Forgetting|Catastrophic Forgetting]] — LoRA mitigates forgetting by freezing base weights

## Supporting Chunks / References
### Supporting Chunks
- [[Parameter-Efficient Fine-Tuning]] — PEFT landscape overview
- [[Quantization Techniques]] — 4-bit NF4, GPTQ, AWQ details
- [[Multi-Adapter Serving]] — Deployment architectures
- [[Supervised Fine-Tuning]] — Full fine-tuning baseline

### References to Sources Index
See [[LLM/Sources/Sources Index|LLM Sources Index]] for papers:
- Hu et al. 2021: LoRA original paper
- Dettmers et al. 2023: QLoRA (4-bit quantization + LoRA)
- Dettmers et al. 2022: 8-bit optimizers and quantization
- HuggingFace PEFT library documentation
- Practical guides: rank selection, layer targeting, hyperparameters
