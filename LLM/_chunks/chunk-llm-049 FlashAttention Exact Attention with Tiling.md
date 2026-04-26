---
tags: [chunk, llm]
id: "chunk-llm-049"
source: "[[LLM/_raw/raw-llm-013 FlashAttention IO-Aware Exact Attention]]"
source_loc: "Key Takeaways 1-2"
topic: "FlashAttention tiling algorithm"
claim: "FlashAttention computes exact attention (not approximate) but reorganizes computation to minimize HBM reads/writes using tiling in SRAM."
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Efficient Attention and Long-Context Variants]]"]
up: "[[LLM/LLM]]"
---

# FlashAttention Exact Attention with Tiling

## Context
Prior to FlashAttention, most approaches to making attention more efficient relied on approximations — sparse attention patterns, low-rank projections, or kernel-based linearizations. These methods sacrificed mathematical exactness for speed. FlashAttention took a fundamentally different approach: it computes mathematically exact standard attention but reorganizes the computation order to be IO-aware.

The key technique is tiling: Q, K, and V matrices are divided into blocks that fit in GPU SRAM (the fast on-chip memory), and the attention computation proceeds block by block. An online softmax algorithm (maintaining running log-sum-exp statistics) enables computing exact softmax incrementally without ever materializing the full N×N attention matrix in slow HBM (high-bandwidth memory). The result is mathematically identical to standard attention but with dramatically fewer memory read/write operations.

## Why It Matters
FlashAttention proved that the bottleneck in attention was not computation but memory bandwidth. By making attention IO-aware rather than approximate, it offered the best of both worlds: exact results with significant speedups (2-4×) and reduced memory usage. This insight — that hardware-aware algorithm design matters as much as algorithmic complexity — reshaped how the field thinks about efficiency.

## QnA Seeds
- Q: How does FlashAttention achieve speedups without approximating attention?
  A: It reorganizes the computation to minimize reads/writes to slow GPU HBM by tiling Q, K, V into blocks that fit in fast SRAM. An online softmax algorithm computes exact attention incrementally block-by-block, never materializing the full N×N attention matrix in HBM.
- Q: What is the "online softmax" trick used in FlashAttention?
  A: It maintains running log-sum-exp statistics (maximum value and cumulative sum) as blocks are processed, then rescales partial results to produce exact softmax outputs. This avoids needing the full attention matrix in memory to compute the softmax normalization.
