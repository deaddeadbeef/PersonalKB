---
tags: [raw, llm]
id: "raw-llm-013"
title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
author: "Dao et al."
year: 2022
source_type: "paper"
url: "https://arxiv.org/abs/2205.14135"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

## What Is This?
An IO-aware algorithm that computes exact attention by tiling the computation to exploit GPU SRAM, avoiding materializing the full N×N attention matrix in HBM.

## Why It Matters
FlashAttention made long-context training practical by reducing attention memory from O(N²) to O(N) and delivering 2-4× wall-clock speedups. It became the default attention kernel in nearly all modern training stacks.

## Key Takeaways
1. Tiles Q, K, V blocks to fit in fast SRAM; never materializes the full attention matrix in HBM
2. Uses online softmax (log-sum-exp rescaling) to compute exact attention incrementally
3. Achieves O(N) memory instead of O(N²) with no approximation
4. Backward pass uses recomputation from stored O, ℓ, m statistics instead of saving the attention matrix

## Chunk Candidates
- [ ] Tiling algorithm and SRAM/HBM memory hierarchy exploitation
- [ ] Online softmax trick for incremental exact computation
- [ ] Memory and speed benchmarks vs standard and sparse attention
- [ ] FlashAttention-2 improvements and kernel fusion extensions
