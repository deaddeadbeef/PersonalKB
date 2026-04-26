---
tags: [chunk, llm]
id: "chunk-llm-050"
source: "[[LLM/_raw/raw-llm-013 FlashAttention IO-Aware Exact Attention]]"
source_loc: "Key Takeaways 3"
topic: "FlashAttention memory reduction"
claim: "FlashAttention achieves O(n) memory instead of O(n²) by never materializing the full attention matrix."
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Efficient Attention and Long-Context Variants]]"]
up: "[[LLM/LLM]]"
---

# FlashAttention O(n) Memory Complexity

## Context
Standard attention computes and stores the full N×N attention score matrix (where N is sequence length), requiring O(N²) memory. For long sequences, this becomes the dominant memory cost — a 16K context with 128 attention heads at float16 requires ~64GB just for the attention matrices. This quadratic memory scaling was the primary barrier to training and running models on long sequences.

FlashAttention eliminates this by never materializing the full attention matrix. The tiling approach processes one block of queries against one block of keys at a time, accumulating the output incrementally. Only the final output matrix O (size N × d) and small auxiliary statistics (log-sum-exp values, one per query row) need to be stored, reducing peak memory to O(N). For the backward pass, the attention matrix is recomputed from stored Q, K, V, and the auxiliary statistics rather than being saved.

## Why It Matters
The reduction from O(N²) to O(N) memory is what made long-context models practical. Without FlashAttention, training with 32K-128K context lengths would be infeasible due to GPU memory limits. This memory saving directly enabled the wave of long-context models (GPT-4 Turbo 128K, Claude 100K, Gemini 1M) that define the current generation of LLMs.

## QnA Seeds
- Q: Why does standard attention require O(N²) memory and how does FlashAttention reduce it to O(N)?
  A: Standard attention materializes the full N×N score matrix in HBM. FlashAttention processes attention block-by-block in SRAM, only storing the final output (N × d) and small per-query statistics. The attention matrix is never fully instantiated, and is recomputed during the backward pass from Q, K, V and stored statistics.
- Q: How does FlashAttention handle the backward pass without storing the attention matrix?
  A: It stores Q, K, V and small auxiliary statistics (per-row log-sum-exp values) from the forward pass. During backpropagation, it recomputes the attention matrix block-by-block from these stored values, trading extra computation for O(N) memory instead of O(N²).
