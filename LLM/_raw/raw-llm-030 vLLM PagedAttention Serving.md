---
tags: [raw, llm]
id: "raw-llm-030"
title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
author: "Kwon et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2309.06180"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Efficient Memory Management for Large Language Model Serving with PagedAttention

## What Is This?
Introduces PagedAttention, a KV cache management technique inspired by OS virtual memory that stores attention keys/values in non-contiguous blocks, enabling near-zero waste in GPU memory for LLM serving.

## Why It Matters
vLLM with PagedAttention became the de facto open-source LLM serving engine by solving KV cache memory fragmentation, achieving 2-4× higher throughput than HuggingFace and up to 24× vs naive implementations.

## Key Takeaways
1. KV cache is allocated in fixed-size blocks (pages) mapped via a block table, eliminating fragmentation
2. Copy-on-write sharing enables efficient parallel sampling (beam search, parallel decoding) without duplicating KV data
3. Reduces KV cache memory waste from 60-80% to near zero, enabling larger batch sizes
4. Integrates with continuous batching for maximum GPU utilization during serving

## Chunk Candidates
- [ ] PagedAttention block table and non-contiguous KV cache allocation
- [ ] Copy-on-write mechanism for parallel sampling efficiency
- [ ] Memory waste analysis: PagedAttention vs pre-allocated contiguous caches
- [ ] Throughput benchmarks and integration with continuous batching
