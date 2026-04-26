---
tags: [chunk, llm]
id: "chunk-llm-056"
source: "[[LLM/_raw/raw-llm-014 Megatron-LM Model Parallelism]]"
source_loc: "Key Takeaways 4"
topic: "3D parallelism strategy"
claim: "3D parallelism (data + tensor + pipeline) became the standard recipe for training models beyond single-GPU memory capacity."
confidence: "verified"
supports: ["[[LLM/Pretraining/Training Infrastructure and Parallelism]]"]
up: "[[LLM/LLM]]"
---

# 3D Parallelism Standard Training Recipe

## Context
Megatron-LM originally combined tensor parallelism with data parallelism. Subsequent work (Megatron-LM v2, DeepSpeed) added pipeline parallelism as a third axis, creating "3D parallelism." In this scheme: tensor parallelism splits layers across GPUs within a node (high bandwidth needed), pipeline parallelism assigns different layer groups to different nodes (lower communication frequency), and data parallelism replicates the full model across groups for throughput scaling.

The typical configuration for a large model: 8-way tensor parallelism within a node (one layer split across 8 GPUs), 8-16 pipeline stages across nodes (each stage holds a subset of layers), and 64-128 way data parallelism across pipeline replicas. This decomposition allows training models with hundreds of billions of parameters across thousands of GPUs, with each parallelism axis matched to the appropriate level of interconnect bandwidth.

## Why It Matters
3D parallelism is the recipe used for all frontier model training: GPT-3, PaLM, LLaMA, and every other model over ~10B parameters. Understanding this decomposition — and how it maps to hardware topology — is essential for anyone involved in large-scale training. The choice of parallelism dimensions directly affects training speed, memory efficiency, and hardware utilization.

## QnA Seeds
- Q: What are the three axes of 3D parallelism and where is each typically applied?
  A: Tensor parallelism splits individual layers across GPUs within a node (requires high-bandwidth NVLink), pipeline parallelism splits groups of layers across nodes (tolerates lower bandwidth), and data parallelism replicates the full pipeline across groups for throughput. Each axis matches a level of interconnect bandwidth.
- Q: What's a typical 3D parallelism configuration for training a 175B parameter model?
  A: 8-way tensor parallelism within each node, 8-16 pipeline stages across nodes (each stage holds a subset of layers), and 64-128 way data parallelism across pipeline replicas. This distributes the model across thousands of GPUs while matching each parallelism type to the available interconnect bandwidth.
