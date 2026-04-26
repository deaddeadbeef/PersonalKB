---
tags: [chunk, llm]
id: "chunk-llm-052"
source: "[[LLM/_raw/raw-llm-013 FlashAttention IO-Aware Exact Attention]]"
source_loc: "Why It Matters"
topic: "FlashAttention universal adoption"
claim: "FlashAttention is now the default attention implementation in virtually all LLM training and inference frameworks."
confidence: "verified"
supports: ["[[LLM/Inference and Serving/KV Cache and Context Reuse]]"]
up: "[[LLM/LLM]]"
---

# FlashAttention as Default Implementation

## Context
FlashAttention has been integrated as the default attention kernel in all major LLM frameworks: PyTorch (via `torch.nn.functional.scaled_dot_product_attention`), Hugging Face Transformers, vLLM, TensorRT-LLM, DeepSpeed, Megatron-LM, and JAX/XLA-based training stacks. When users train or run inference with any modern LLM, they are almost certainly using FlashAttention or a derivative under the hood.

This universal adoption happened because FlashAttention provides strictly better performance with no accuracy trade-off — it computes mathematically exact attention faster and with less memory. There is no reason to use the naive implementation. The integration also benefits inference serving: frameworks like vLLM combine FlashAttention with PagedAttention for KV cache management, enabling efficient batched serving of long-context models.

## Why It Matters
FlashAttention's ubiquity means it has effectively become part of the transformer's "standard implementation" rather than an optional optimization. This has downstream implications: inference serving systems, quantization toolkits, and custom architectures all assume FlashAttention-style kernels are available, and new attention variants (like sliding window attention in Mistral) are implemented as FlashAttention extensions.

## QnA Seeds
- Q: Which major frameworks use FlashAttention as their default attention implementation?
  A: PyTorch (via scaled_dot_product_attention), Hugging Face Transformers, vLLM, TensorRT-LLM, DeepSpeed, and Megatron-LM all default to FlashAttention. It is also used in JAX/XLA training stacks. Essentially all modern LLM frameworks have adopted it.
- Q: How does FlashAttention integration benefit inference serving systems?
  A: Inference frameworks like vLLM combine FlashAttention's efficient tiled computation with PagedAttention for KV cache management. This enables serving long-context models with high throughput by minimizing both computation overhead and memory usage during batched decoding.
