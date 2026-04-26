---
tags: [chunk, llm]
id: "chunk-llm-213"
source: "[[LLM/_raw/raw-llm-054 Fast Transformer Decoding One Write-Head MQA]]"
source_loc: "What Is This, Chunk Candidates"
topic: "multi-query attention mechanism"
claim: "Multi-Query Attention shares a single set of key-value projections across all attention heads while keeping separate query projections, drastically reducing KV cache size."
confidence: "verified"
supports: ["[[LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse]]", "[[LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants]]"]
qna_seeds:
  - q: "How does Multi-Query Attention differ from standard Multi-Head Attention?"
    a: "In MHA, each head has its own Q, K, V projections. In MQA, all heads share a single K and V projection while maintaining separate Q projections — reducing the KV cache by a factor equal to the number of heads."
  - q: "What is the KV cache reduction factor with MQA?"
    a: "For a model with H attention heads, MQA reduces the KV cache size by a factor of H (e.g., 32× for a 32-head model), because only one set of keys and values is stored instead of H sets."
up: "[[LLM/LLM]]"
---
# Multi-Query Attention Shares KV Projections Across All Heads

Multi-Query Attention (MQA), proposed by Shazeer in 2019, modifies the standard multi-head attention mechanism by sharing a single set of key and value projection matrices across all attention heads. Each head retains its own query projection, so heads still attend to different aspects of the input, but they all read from the same key-value representation.

This sharing reduces the KV cache memory requirement by a factor equal to the number of heads. For a 32-head model, MQA stores 1/32 of the key-value tensors during autoregressive decoding, dramatically reducing both memory footprint and the memory bandwidth consumed by loading the KV cache at each decoding step. The quality impact is modest — typically less than 1% degradation on benchmarks — because the queries still provide per-head specialization.
