---
tags: [llm, architecture, efficient-attention, long-context]
up: "[[LLM/LLM]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive]
---

# Efficient Attention and Long-Context Variants

> **One-line summary** Efficient attention is the family of implementation and architecture tricks that makes long-context transformer work practical instead of collapsing under naive quadratic memory traffic.

This is a bridge page for architecture navigation. The fuller era chapter is [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants|Efficient Attention and Long-Context Variants in the frontier-efficiency era]].

## Why This Exists

Standard self-attention compares every token with every other token. That gives transformers their expressive power, but it also creates the familiar $O(n²)$ attention matrix. Long-context models therefore need help from several directions:

- **IO-aware exact attention**, especially FlashAttention, which computes the same mathematical result while reducing GPU memory traffic.
- **Sparse or local patterns**, such as sliding-window attention, which restrict the attention graph to reduce cost.
- **KV-cache and serving optimizations**, which make repeated decoding over long contexts feasible.
- **Distributed long-context methods**, such as ring attention, which spread sequence work across devices.

## Reading Route

1. Start with [[LLM/2017 — The Transformer/Attention Mechanism|Attention Mechanism]] to understand the baseline operation.
2. Read [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants|Efficient Attention and Long-Context Variants]] for the full technical treatment.
3. Connect it to [[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse|KV Cache and Context Reuse]] for inference-time memory behavior.
4. Use [[LLM/Study/Attention Implementation Lab|Attention Implementation Lab]] to verify tensor shapes and masking behavior by implementation.

## Key Distinctions

| Method family | What changes | Main tradeoff |
|---|---|---|
| FlashAttention | Memory layout and kernel schedule | Exact result, but still quadratic compute |
| Sliding-window attention | Which tokens can attend to which other tokens | Lower cost, weaker global connectivity |
| Sparse global patterns | Adds global and random links to local windows | More design complexity |
| KV-cache reuse | Avoids recomputing past keys and values during decoding | Cache memory becomes the bottleneck |

## References

- [[LLM/Sources/Sources Index]]
- [[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants]]
- [[LLM/Study/Attention Implementation Lab]]
