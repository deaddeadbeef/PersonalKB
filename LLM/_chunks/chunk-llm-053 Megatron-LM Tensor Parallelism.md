---
tags: [chunk, llm]
id: "chunk-llm-053"
source: "[[LLM/_raw/raw-llm-014 Megatron-LM Model Parallelism]]"
source_loc: "Key Takeaways 1"
topic: "Tensor parallelism in Megatron-LM"
claim: "Megatron-LM introduced tensor parallelism: splitting individual transformer layers across GPUs by partitioning the attention and FFN weight matrices."
confidence: "verified"
supports: ["[[LLM/Pretraining/Training Infrastructure and Parallelism]]"]
up: "[[LLM/LLM]]"
---

# Megatron-LM Tensor Parallelism

## Context
When a single transformer layer's parameters exceed the memory of one GPU, the model must be split across devices. Megatron-LM introduced tensor parallelism (also called intra-layer model parallelism), which partitions the weight matrices within individual layers across multiple GPUs. Specifically, the MLP's first linear layer is split column-wise (each GPU holds a subset of output features), and the second linear layer is split row-wise (each GPU holds a subset of input features). Similarly, attention heads are distributed across GPUs.

This partitioning is designed so that each GPU can compute its portion of the layer independently, with only two all-reduce communication operations needed per transformer layer to synchronize results. The column-parallel layer produces partial outputs that don't need synchronization until the row-parallel layer aggregates them, minimizing the communication-to-computation ratio.

## Why It Matters
Tensor parallelism is one of the three fundamental parallelism strategies (along with data and pipeline parallelism) used to train all large language models. Megatron-LM's specific partitioning scheme — column-parallel MLP first, row-parallel MLP second — became the standard approach adopted by all major training frameworks, making it foundational infrastructure for modern LLM training.

## QnA Seeds
- Q: How does Megatron-LM's tensor parallelism partition a transformer MLP across GPUs?
  A: The first MLP linear layer is split column-wise (each GPU gets a subset of output features), and the second is split row-wise (each GPU gets a subset of input features). This allows independent computation on each GPU with only an all-reduce at the end to aggregate results.
- Q: How are attention heads distributed in Megatron-LM's tensor parallelism?
  A: Attention heads are partitioned across GPUs, with each GPU computing a subset of the heads. Since heads operate independently, this requires no communication until the output projection, where an all-reduce synchronizes the results.
