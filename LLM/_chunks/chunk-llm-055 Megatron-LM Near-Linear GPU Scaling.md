---
tags: [chunk, llm]
id: "chunk-llm-055"
source: "[[LLM/_raw/raw-llm-014 Megatron-LM Model Parallelism]]"
source_loc: "Key Takeaways 3"
topic: "Megatron-LM scaling efficiency"
claim: "Megatron-LM demonstrated efficient training of models up to 8.3B parameters across 512 GPUs with near-linear scaling."
confidence: "verified"
supports: ["[[LLM/Pretraining/Training Infrastructure and Parallelism]]"]
up: "[[LLM/LLM]]"
---

# Megatron-LM Near-Linear GPU Scaling

## Context
The Megatron-LM paper demonstrated training of models up to 8.3 billion parameters (the largest at the time, 2019) across 512 NVIDIA V100 GPUs. The key result was near-linear scaling efficiency: using 8-way tensor parallelism within each node achieved 77% scaling efficiency (vs. ideal linear), and combining with data parallelism across nodes maintained strong throughput. The 8.3B model achieved 15.1 PetaFLOPs sustained performance across the cluster.

Near-linear scaling means that doubling the number of GPUs nearly doubles the training speed, with the gap attributable to communication overhead and reduced per-GPU batch sizes. This was a landmark demonstration that very large models could be trained efficiently on distributed hardware, validating tensor parallelism as a practical approach rather than a theoretical one.

## Why It Matters
Megatron-LM's scaling results established the engineering template that made GPT-3, PaLM, and all subsequent large models possible. Proving that 8-way tensor parallelism could scale to 8.3B parameters with near-linear efficiency on 2019-era hardware gave the field confidence that 100B+ parameter models were within reach — they just needed more GPUs and the right parallelism strategy.

## QnA Seeds
- Q: What scaling efficiency did Megatron-LM achieve with tensor parallelism?
  A: 77% scaling efficiency with 8-way tensor parallelism within a node on V100 GPUs. The full 8.3B parameter model trained across 512 GPUs achieved 15.1 PetaFLOPs sustained, demonstrating near-linear scaling when combining tensor and data parallelism.
- Q: Why was Megatron-LM's scaling demonstration significant for the field?
  A: It proved that multi-billion parameter models could be trained efficiently on distributed GPU clusters, validating tensor parallelism as practical infrastructure. This gave confidence that scaling to hundreds of billions of parameters was feasible, directly enabling subsequent models like GPT-3 and PaLM.
