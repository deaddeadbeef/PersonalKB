---
tags: [raw, llm]
id: "raw-llm-045"
title: "PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel"
author: "Zhao et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2304.11277"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# PyTorch FSDP: Fully Sharded Data Parallel

## What Is This?
Describes PyTorch's native implementation of Fully Sharded Data Parallel training, which shards model parameters, gradients, and optimizer states across GPUs — a ZeRO-3 equivalent integrated into the PyTorch ecosystem.

## Why It Matters
Made trillion-parameter-scale training accessible through a native PyTorch API, eliminating the need for external frameworks like DeepSpeed for many workloads. FSDP is now the default distributed training strategy for LLM fine-tuning and pre-training in the PyTorch ecosystem.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Sharding strategy: parameters, gradients, and optimizer states across ranks
- [ ] Communication primitives: all-gather for forward, reduce-scatter for backward
- [ ] Memory vs. communication trade-offs and mixed-precision integration
