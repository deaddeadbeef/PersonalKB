---
tags: [llm, chunk]
source: "[[raw-llm-036]]"
confidence: high
supports:
  - "[[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants]]"
  - "[[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]"
qna_seeds:
  - "Q: What architectural choices did PaLM use? A: PaLM adopted SwiGLU activation, parallel attention and FFN computation (running attention and feedforward layers simultaneously rather than sequentially), multi-query attention (MQA), RoPE position embeddings, and no biases — choices that collectively improved training efficiency by ~15%."
---

# PaLM Adopted SwiGLU, Parallel Layers, MQA, and RoPE

PaLM made several architectural choices that became influential: SwiGLU activation functions, parallel computation of attention and feedforward layers (rather than sequential), multi-query attention (MQA) for efficient inference, RoPE position embeddings, and removal of all bias terms. The parallel attention/FFN formulation — computing both sublayers simultaneously and summing their outputs — increased training throughput by approximately 15% with no quality degradation at scale. Many of these choices (SwiGLU, RoPE, no biases) became standard in subsequent models including LLaMA and Mistral.