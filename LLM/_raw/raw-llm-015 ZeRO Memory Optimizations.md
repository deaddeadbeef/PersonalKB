---
tags: [raw, llm]
id: "raw-llm-015"
title: "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models"
author: "Rajbhandari et al."
year: 2019
source_type: "paper"
url: "https://arxiv.org/abs/1910.02054"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# ZeRO: Memory Optimizations Toward Training Trillion Parameter Models

## What Is This?
Introduces Zero Redundancy Optimizer (ZeRO), which partitions optimizer states, gradients, and parameters across data-parallel ranks to eliminate memory redundancy without sacrificing training efficiency.

## Why It Matters
ZeRO is the memory optimization engine behind DeepSpeed and enabled training models with hundreds of billions of parameters on commodity GPU clusters by dramatically reducing per-GPU memory.

## Key Takeaways
1. ZeRO Stage 1: partition optimizer states (e.g., Adam moments) — ~4× memory reduction
2. ZeRO Stage 2: also partition gradients — ~8× memory reduction
3. ZeRO Stage 3: also partition parameters — memory scales linearly with number of GPUs
4. Communication volume matches standard data parallelism (Stage 1-2) or adds modest overhead (Stage 3)

## Chunk Candidates
- [ ] Three-stage memory partitioning scheme (optimizer states → gradients → parameters)
- [ ] Memory consumption analysis per stage vs standard data parallelism
- [ ] Communication overhead analysis and trade-offs
- [ ] ZeRO-Offload and ZeRO-Infinity extensions for CPU/NVMe offloading
