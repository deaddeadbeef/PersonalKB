---
tags: [raw, llm]
id: "raw-llm-054"
title: "Fast Transformer Decoding: One Write-Head is All You Need"
author: "Shazeer"
year: 2019
source_type: "paper"
url: "https://arxiv.org/abs/1911.02150"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Fast Transformer Decoding: One Write-Head is All You Need (Multi-Query Attention)

## What Is This?
Proposes Multi-Query Attention (MQA), where all attention heads share a single set of key and value projections while maintaining separate query projections — dramatically reducing the KV cache size and memory bandwidth during autoregressive decoding.

## Why It Matters
Identified the KV cache memory bandwidth bottleneck as the primary inference cost for autoregressive Transformers and provided an elegant solution. MQA became foundational, adopted by PaLM and Falcon, and later refined into Grouped-Query Attention (GQA).

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Multi-Query Attention mechanism: shared K,V projections across heads
- [ ] KV cache memory bandwidth analysis during incremental decoding
- [ ] Quality vs. speed trade-off and adoption in PaLM, Falcon, and successors
