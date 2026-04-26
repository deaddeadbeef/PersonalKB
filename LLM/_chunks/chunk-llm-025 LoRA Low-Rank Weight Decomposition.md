---
tags: [chunk, llm]
id: "chunk-llm-025"
source: "[[LLM/_raw/raw-llm-007 LoRA Low-Rank Adaptation]]"
source_loc: "Section 4"
topic: "LoRA formulation"
claim: "LoRA decomposes weight updates as W = W_0 + BA where B∈ℝ^(d×r), A∈ℝ^(r×d), with rank r << d (typically 4-64)"
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/LoRA and QLoRA]]"]
up: "[[LLM/LLM]]"
---

# LoRA Low-Rank Weight Decomposition

## Context

LoRA (Low-Rank Adaptation) modifies the standard fine-tuning approach by freezing the pre-trained weight matrix W_0 and introducing a low-rank update: W = W_0 + BA, where B ∈ ℝ^(d×r) and A ∈ ℝ^(r×d), with rank r much smaller than d (typically 4, 8, 16, or 64, while d is often 4096+). During fine-tuning, only B and A are updated via gradient descent while W_0 remains frozen. Matrix A is initialized with a random Gaussian and B is initialized to zero, so the update BA starts as zero and the model begins from the pre-trained weights.

The key insight is that fine-tuning updates to large weight matrices tend to have low intrinsic rank — the actual weight change ΔW occupies a low-dimensional subspace. LoRA explicitly parameterizes this low-rank structure, reducing the number of trainable parameters from d² (full matrix) to 2dr (two thin matrices). For d=4096 and r=8, this is a 256× reduction in trainable parameters per adapted weight matrix.

## Why It Matters

LoRA made fine-tuning of billion-parameter models practical on consumer hardware. Instead of storing and updating all 7B+ parameters, you train only millions of adapter parameters. This democratized fine-tuning — researchers and hobbyists could adapt LLaMA, Mistral, and other open models to specialized tasks using a single GPU. LoRA also became the foundation for QLoRA and other efficient adaptation methods.

## QnA Seeds
- Q: Why does fine-tuning have low intrinsic rank?
  A: During fine-tuning, the model only needs to make small adjustments to its pre-trained behavior — adapting general language capabilities to a specific task. These adjustments tend to be structured and low-dimensional relative to the full parameter space. Empirically, Aghajanyan et al. (2020) showed that fine-tuning can be projected to very low-dimensional subspaces while retaining 90% of performance, motivating LoRA's approach.
- Q: How do you choose the rank r in LoRA?
  A: Rank r is a hyperparameter trading off expressiveness against efficiency. r=4 or r=8 works well for focused tasks like classification or single-domain adaptation. More complex tasks (multi-task, creative generation) may benefit from r=16-64. Empirically, performance gains from increasing r show diminishing returns — r=8 often achieves 95%+ of the quality of r=64 with 8× fewer parameters. Start low and increase only if quality is insufficient.
