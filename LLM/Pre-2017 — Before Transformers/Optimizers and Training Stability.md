---
tags: [llm, pretraining]
up: "[[Pre-2017 — Before Transformers Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Optimizers and Training Stability

> **One-line summary** Large language models train successfully only when optimization speed is paired with techniques that prevent numerical instability and catastrophic divergence.

## 🎯 Intuition
**The Core Idea:** LLM training depends on adaptive optimization plus stability safeguards so huge models can converge quickly without blowing up numerically.

**Analogy:** The optimizer is cruise control for gradient descent, while warmup, clipping, mixed precision, and checkpoint recovery are the traction control, seatbelt, and brakes that keep a high-speed training run from crashing.

**Why It Matters:** Training stability separates successful LLM runs from wasted compute. A single unrecovered loss spike at 80% of training can ruin a multi-million-dollar run. AdamW, warmup, cosine decay, mixed precision, clipping, and checkpointing are not just helpful — they are essential, and together they make trillion-token training practical and routine.

---

## ⚙️ Core Mechanics
### How It Works
- **AdamW**: first moment `m = β₁m + (1-β₁)g`; second moment `v = β₂v + (1-β₂)g²`; update with decoupled weight decay.
- **Learning rate schedule**: linear warmup (`0 → max` over ~2000 steps), cosine decay (`max → 0.1×max` following a cosine curve).
- **Gradient clipping**: scale gradients if `||g|| > threshold`; `g ← g · threshold/||g||`; typical threshold = `1.0`.
- **Loss spike recovery**: skip batch, reload checkpoint (last 100-500 steps), continue training; reduce LR if persistent.
- **μP (Maximal Update Parameterization)**: scale weight init by `1/√fan_in`; scale LR by `1/width`; enables hyperparameter transfer.
- **Mixed precision (fp16)**: loss scaling to prevent underflow; gradient scaling; dynamic loss scaling common.
- **Mixed precision (bf16)**: wider exponent range (same as fp32); no loss scaling needed; preferred for large models.
- **Gradient accumulation**: accumulate gradients over `N` micro-batches before updating; simulate larger batch sizes.
- **Why bf16 > fp16**: bf16 has 8 exponent bits (vs 5 in fp16), reducing overflow/underflow; no loss scaling; simpler.

### Key Specifications

| Technique | Purpose | Typical Settings |
|-----------|---------|------------------|
| AdamW | Adaptive optimization | β₁=0.9, β₂=0.95-0.999, weight decay=0.1 |
| Learning rate warmup | Stabilize early training | Linear, 1-2% of total steps |
| Cosine decay | Gradual convergence | Decay to 10% of max LR |
| Gradient clipping | Prevent exploding gradients | Global norm = 1.0 |
| bf16 | Speed + stability | Preferred over fp16; no loss scaling |
| fp16 | Speed (older) | Requires dynamic loss scaling |

### Key Facts
- AdamW is the dominant optimizer for LLM pretraining.
- Warmup is especially important early in training when gradients are noisy and moment estimates are unreliable.
- Cosine decay is a standard large-scale schedule because it improves fine-grained convergence.
- Loss spikes can come from outlier batches, numerical instability, or gradient explosion.
- bf16 is preferred over fp16 because it preserves speedups while making training simpler and more stable.

---

## 🔬 Deep Dive
### Technical Details
**AdamW** (Adam with decoupled weight decay) is the dominant optimizer for LLM pretraining. Adam maintains first and second moment estimates (mean and variance of gradients) for adaptive per-parameter learning rates, converging faster than SGD on high-dimensional problems. Weight decay is decoupled from the gradient update:

`θₜ₊₁ = θₜ - η[αₜm̂ₜ/(√v̂ₜ + ε) + λθₜ]`

where `m̂ₜ` and `v̂ₜ` are bias-corrected moment estimates and `λ` is weight decay. Typical hyperparameters are `β₁=0.9`, `β₂=0.95-0.999`, `ε=10⁻⁸`, and `λ=0.1`.

**Learning rate schedules** are critical: warmup for the first ~1% of steps linearly increases LR from 0 to max, then **cosine decay** reduces it to ~10% of max. Warmup stabilizes early training when gradients are noisy and second moment estimates are unreliable. Cosine decay gradually reduces the learning rate, allowing fine-grained convergence. **Gradient clipping** by global norm, typically `1.0`, prevents exploding gradients that cause loss spikes.

**Loss spikes** are sudden, dramatic increases in loss during training. They are caused by outlier batches, numerical instability, or gradient explosion. Recovery strategies include skipping the bad batch, reloading from a recent checkpoint, and reducing the learning rate temporarily. **μP (Maximal Update Parameterization)** enables hyperparameter transfer across scales: tune hyperparameters on a small model, then transfer to large models with minimal retuning by scaling initialization and learning rates carefully. **Mixed precision** (`fp16` or `bf16` + `fp32` master weights) speeds training by roughly 2-3× by using lower precision for forward/backward passes while maintaining `fp32` precision for weight updates and sensitive operations.

### Limitations and Criticisms
- Even with strong safeguards, late-stage loss spikes can still waste enormous amounts of compute if recovery is slow or incomplete.
- fp16 improves speed but requires finicky dynamic loss scaling and is more vulnerable to overflow/underflow than bf16.
- μP is principled, but it is less widely adopted in practice than standard AdamW-plus-schedule recipes.

### Impact and Legacy
AdamW's adaptive learning rates handle the diverse scales of transformer parameters — including embeddings, attention, and feedforward layers — better than SGD, making it the standard optimizer for large models. Mixed precision, especially bf16 on hardware like A100 and H100 GPUs with dedicated Tensor Cores, is a major reason very large models fit and train efficiently at all. Combined stability techniques — gradient clipping, bf16, cosine decay, warmup, checkpointing, and sometimes μP — have turned billion-parameter and trillion-token training from a fragile stunt into a repeatable engineering process.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why is warmup especially important at the beginning of LLM training?
2. What practical advantage does bf16 have over fp16?
3. What is the purpose of gradient clipping during large-scale training?

### Core Problems
1. Walk through how AdamW updates a parameter using first and second moment estimates, and explain why decoupled weight decay differs from simply adding an L2 penalty to the gradient.
2. A training run shows sudden loss spikes late in training. Using the note's content, diagnose plausible causes and describe a recovery plan involving clipping, learning-rate changes, and checkpoint reloads.

### Challenge
1. Suppose you want to transfer hyperparameters from a small transformer to a much wider one. Explain how μP would guide initialization and learning-rate scaling, and what practical evidence you would want before trusting that transfer.

*See also:*
- [[AdamW]]
- [[Mixed Precision Training]]
- [[Gradient Clipping]]
- [[Checkpointing]]
- [[μP]]

## Supporting Chunks / References
### Supporting Chunks
*(To be populated as chunks are created)*

### References
- [[LLM/Sources/Sources Index]]
