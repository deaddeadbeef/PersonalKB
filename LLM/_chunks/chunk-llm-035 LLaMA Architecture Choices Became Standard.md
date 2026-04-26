---
tags: [chunk, llm]
id: "chunk-llm-035"
source: "[[LLM/_raw/raw-llm-009 LLaMA Open Foundation Language Models]]"
source_loc: "Section 2.2"
topic: "decoder architecture"
claim: "LLaMA architecture choices that became standard: pre-norm with RMSNorm, RoPE positional embeddings, SwiGLU activation, no bias terms"
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Decoder-Only Models]]"]
up: "[[LLM/LLM]]"
---

# LLaMA Architecture Choices Became Standard

## Context

LLaMA adopted several architectural modifications from recent research that departed from the original GPT architecture. Pre-normalization with RMSNorm (Zhang & Sennrich, 2019) replaced post-norm LayerNorm, improving training stability. Rotary Position Embeddings (RoPE, Su et al., 2021) replaced absolute or learned positional embeddings, providing better length generalization and relative position encoding. SwiGLU activation (Shazeer, 2020) replaced ReLU in the feed-forward network, improving representational capacity. Finally, all bias terms were removed from linear layers.

Each of these choices had been independently validated in prior work: RMSNorm is computationally cheaper than LayerNorm (no mean subtraction) and equally effective; RoPE naturally encodes relative positions and extrapolates well to longer sequences; SwiGLU provides smoother gradients and better expressiveness than ReLU or GELU; and removing biases reduces parameter count and was empirically shown to have no negative impact on performance.

## Why It Matters

LLaMA's architecture became the de facto template for nearly all subsequent open-weight decoder-only models. LLaMA-2, Mistral, Qwen, Yi, DeepSeek, and many others adopted the same combination of pre-norm RMSNorm, RoPE, SwiGLU, and no biases. By consolidating several best practices from the research community into one successful open model, LLaMA created an architectural standard that unified the open LLM ecosystem and simplified development of new models.

## QnA Seeds
- Q: Why is pre-normalization with RMSNorm preferred over post-norm LayerNorm?
  A: Pre-norm places normalization before the sub-layer (x + Sublayer(RMSNorm(x))) rather than after (LayerNorm(x + Sublayer(x))). This keeps the residual stream unnormalized, providing a cleaner gradient highway that improves training stability at scale. RMSNorm is cheaper than LayerNorm because it skips mean centering — it only normalizes by root-mean-square of activations. At large scale, pre-norm + RMSNorm trains more stably and slightly faster.
- Q: What advantage does RoPE have over absolute positional embeddings?
  A: RoPE encodes position information by rotating the query and key vectors, making the dot-product attention naturally depend on relative position (the rotation angle difference). This means the model learns relative position patterns that generalize to longer sequences than seen during training. Absolute embeddings are fixed-length and don't capture relative positions natively, requiring the model to learn these relationships indirectly.
