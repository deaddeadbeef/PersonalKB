---
tags: [llm, chunk]
source: "[[raw-llm-038]]"
confidence: high
supports:
  - "[[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]"
qna_seeds:
  - "Q: Why does Mistral 7B use grouped-query attention? A: Mistral 7B uses grouped-query attention (GQA) with 8 KV heads shared across 32 query heads, reducing the KV cache size by 4× compared to standard multi-head attention, which directly lowers memory requirements and speeds up autoregressive decoding."
---

# Mistral 7B Uses GQA for 4× KV Cache Reduction

Mistral 7B employs grouped-query attention (GQA) with 8 key-value heads shared across 32 query heads, meaning every 4 query heads share a single KV head. This reduces the KV cache memory by 4× compared to standard multi-head attention (which would require 32 KV heads), directly lowering GPU memory requirements during inference and speeding up autoregressive decoding. Combined with sliding window attention, GQA makes Mistral 7B significantly more deployment-friendly than models of similar quality that use full multi-head attention.