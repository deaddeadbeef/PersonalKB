---
tags: [llm, chunk]
source: "[[raw-llm-038]]"
confidence: high
supports:
  - "[[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants]]"
qna_seeds:
  - "Q: What is sliding window attention in Mistral 7B? A: Sliding window attention limits each token's attention to a fixed window of W=4,096 preceding tokens rather than the full sequence, reducing attention complexity from O(n²) to O(n·W) while allowing information to propagate across the full context through stacked layers."
---

# Mistral 7B Uses Sliding Window Attention for Efficiency

Mistral 7B employs sliding window attention (SWA) with a window size W=4,096, where each token attends only to the preceding 4,096 tokens rather than the entire sequence. This reduces the quadratic attention complexity from O(n²) to O(n·W), making long-context processing more memory-efficient. Information beyond the window still propagates through the model because stacked Transformer layers allow each layer's window to "see through" the previous layer's window — after L layers, the effective receptive field spans L×W tokens. This enables a theoretical attention span of ~131K tokens with 32 layers.