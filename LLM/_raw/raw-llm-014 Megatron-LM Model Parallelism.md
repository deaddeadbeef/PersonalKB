---
tags: [raw, llm]
id: "raw-llm-014"
title: "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism"
author: "Shoeybi et al."
year: 2019
source_type: "paper"
url: "https://arxiv.org/abs/1909.08053"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism

## What Is This?
Presents efficient intra-layer model parallelism techniques for training very large transformers by partitioning attention heads and MLP columns across GPUs with minimal communication.

## Why It Matters
Megatron-LM established the blueprint for tensor parallelism that all large-scale training frameworks now use, enabling models too large to fit on a single GPU to train efficiently across many.

## Key Takeaways
1. Tensor parallelism splits MLP columns and attention heads across GPUs within a single layer
2. Only two all-reduce operations per transformer layer are needed (forward + backward)
3. Scaled up to 8.3B parameters with near-linear scaling efficiency on 512 GPUs
4. Combined with data parallelism for the full 3D parallelism strategy (later extended with pipeline parallelism)

## Chunk Candidates
- [ ] Tensor parallelism partitioning scheme for MLP and attention layers
- [ ] Communication cost analysis (all-reduce placement and volume)
- [ ] Scaling efficiency results across GPU counts
- [ ] Integration with pipeline parallelism and data parallelism (3D parallelism)
