---
tags: [chunk, llm]
id: "chunk-llm-051"
source: "[[LLM/_raw/raw-llm-013 FlashAttention IO-Aware Exact Attention]]"
source_loc: "Chunk Candidates"
topic: "FlashAttention 2 improvements"
claim: "FlashAttention 2 improved parallelism and work partitioning, achieving ~2× speedup over FlashAttention 1."
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Efficient Attention and Long-Context Variants]]"]
up: "[[LLM/LLM]]"
---

# FlashAttention 2 Parallelism Improvements

## Context
FlashAttention 1 demonstrated the tiling approach but left performance on the table due to suboptimal GPU occupancy and work distribution. FlashAttention 2 addressed these limitations with three key improvements: (1) reducing non-matmul FLOPs by restructuring the online softmax computation, (2) parallelizing across the sequence length dimension (not just batch and heads) to better utilize GPU SMs, and (3) partitioning work between warps within a thread block to reduce shared memory reads/writes and improve warp occupancy.

These changes enabled FlashAttention 2 to reach approximately 70% of the theoretical maximum FLOP/s on A100 GPUs, compared to ~50% for FlashAttention 1. The practical result was roughly a 2× wall-clock speedup over FlashAttention 1, making it fast enough to be used as the default attention implementation with negligible overhead compared to the rest of the transformer computation.

## Why It Matters
FlashAttention 2's improvements pushed attention from being a bottleneck to being a well-optimized primitive. The 2× speedup over v1 mattered because attention is computed at every layer, so improvements compound. This level of optimization made it practical to use exact attention even at very long context lengths where previous implementations would have been prohibitively slow.

## QnA Seeds
- Q: What were the main improvements in FlashAttention 2 over FlashAttention 1?
  A: Three key changes: (1) reduced non-matmul FLOPs in the softmax computation, (2) parallelized across the sequence length dimension for better GPU utilization, and (3) optimized warp-level work partitioning to minimize shared memory access. Together these achieved ~70% of peak A100 FLOP/s.
- Q: How much faster is FlashAttention 2 compared to FlashAttention 1?
  A: Approximately 2× faster in wall-clock time, primarily from better GPU occupancy and reduced overhead in the tiling loops. FlashAttention 2 achieves ~70% of theoretical peak FLOP/s compared to ~50% for v1.
