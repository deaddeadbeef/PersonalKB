---
tags: [chunk, llm]
id: "chunk-llm-004"
source: "[[LLM/_raw/raw-llm-001 Attention Is All You Need]]"
source_loc: "Section 3.1"
topic: "transformer architecture"
claim: "Transformer encoder-decoder uses residual connections + layer normalization around each sub-layer"
confidence: "verified"
supports: ["[[LLM/Foundations/Transformer Architecture]]"]
up: "[[LLM/LLM]]"
---

# Residual Connections and Layer Normalization

## Context

Each sub-layer in the Transformer (whether self-attention or feed-forward) is wrapped with a residual connection followed by layer normalization. The output of each sub-layer is LayerNorm(x + Sublayer(x)), where x is the sub-layer input. This means the sub-layer only needs to learn the residual — the difference from the identity function — rather than the entire transformation.

The original Transformer used "post-norm" placement (normalization after the residual addition). This pattern enables training of deep networks by providing gradient shortcuts through the residual connections and stabilizing activations through normalization. The encoder stacks 6 layers of [self-attention + FFN], and the decoder stacks 6 layers of [masked self-attention + cross-attention + FFN], all with this residual + LayerNorm wrapper.

## Why It Matters

Residual connections and layer normalization are what make deep Transformers trainable. Without residual connections, gradients vanish in deep stacks; without normalization, activation magnitudes drift. Modern variants (pre-norm, RMSNorm) have refined this pattern, but the core principle — skip connections plus normalization around every sub-layer — remains universal across all Transformer architectures.

## QnA Seeds
- Q: What is the difference between pre-norm and post-norm in Transformers?
  A: Post-norm (original Transformer) applies normalization after the residual addition: LayerNorm(x + Sublayer(x)). Pre-norm applies normalization before the sub-layer: x + Sublayer(LayerNorm(x)). Pre-norm is more stable during training (especially at scale) because the residual path remains unnormalized, providing a cleaner gradient highway. Most modern LLMs use pre-norm.
- Q: Why are residual connections essential for deep Transformer training?
  A: Residual connections provide a direct gradient path from output to input, bypassing the sub-layer transformations. Without them, gradients must flow through many sequential nonlinear transformations, causing them to vanish or explode. The residual path ensures that each layer only needs to learn a small perturbation from the identity, making optimization much easier.
