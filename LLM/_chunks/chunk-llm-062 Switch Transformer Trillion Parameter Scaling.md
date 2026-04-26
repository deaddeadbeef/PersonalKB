---
tags: [chunk, llm]
id: "chunk-llm-062"
source: "[[LLM/_raw/raw-llm-016 Switch Transformers Trillion Parameter MoE]]"
source_loc: "Key Takeaways 3"
topic: "Switch Transformer scaling results"
claim: "Switch Transformer demonstrated scaling to 1.6 trillion parameters with the same FLOPs as a much smaller dense model."
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Mixture-of-Experts Models]]"]
up: "[[LLM/LLM]]"
---

# Switch Transformer Trillion Parameter Scaling

## Context
The Switch Transformer's key scaling result was training a 1.6 trillion parameter sparse model that used the same per-token FLOPs as a dense T5-Base model (~220M parameters). Despite having 7,000× more parameters, the sparse model's computational cost per token was identical because only one expert (out of thousands) activates per token. The result was substantially better quality on language understanding and generation tasks compared to the dense baseline at matched training compute.

This demonstrated the fundamental MoE value proposition: parameters and compute can be decoupled. A dense model's quality is limited by both its parameter count and compute budget, but an MoE model can have a massive parameter count (providing capacity) while keeping compute fixed (providing efficiency). The Switch Transformer showed improvements of 4-7× in pre-training speed to reach the same quality as dense T5 models.

## Why It Matters
The 1.6T parameter result proved that trillion-parameter models were achievable with existing hardware budgets by using sparsity. This validated the MoE approach for extreme-scale models and influenced the design of subsequent frontier models — GPT-4 is widely reported to use MoE, and Mixtral explicitly adopted the sparse MoE architecture for its efficiency advantages.

## QnA Seeds
- Q: How did Switch Transformer achieve 1.6 trillion parameters with the same FLOPs as T5-Base?
  A: By using sparse MoE with top-1 routing: each token activates only one expert out of thousands, so per-token compute equals one expert's cost regardless of total parameter count. The 1.6T parameters provide capacity, while compute stays constant at ~220M parameter equivalent per token.
- Q: What speedup did Switch Transformer achieve over dense models at equivalent quality?
  A: 4-7× improvement in pre-training speed to reach the same quality as dense T5 models. This means a sparse Switch model reaches a given loss level in 4-7× fewer training steps/FLOPs than a dense model of comparable quality.
