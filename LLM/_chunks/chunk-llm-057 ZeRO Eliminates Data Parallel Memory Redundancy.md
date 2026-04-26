---
tags: [chunk, llm]
id: "chunk-llm-057"
source: "[[LLM/_raw/raw-llm-015 ZeRO Memory Optimizations]]"
source_loc: "Key Takeaways 1-3"
topic: "ZeRO memory partitioning"
claim: "ZeRO eliminates memory redundancy in data parallelism by sharding optimizer states (Stage 1), gradients (Stage 2), and parameters (Stage 3) across GPUs."
confidence: "verified"
supports: ["[[LLM/Pretraining/Training Infrastructure and Parallelism]]"]
up: "[[LLM/LLM]]"
---

# ZeRO Eliminates Data Parallel Memory Redundancy

## Context
In standard data parallelism, every GPU holds a complete copy of the model parameters, gradients, and optimizer states (e.g., Adam's first and second moment estimates). For a model with Ψ parameters in fp16, each GPU stores: 2Ψ bytes for parameters + 2Ψ bytes for gradients + 12Ψ bytes for Adam optimizer states (fp32 copy + momentum + variance) = 16Ψ bytes. With N GPUs, this means 16NΨ total bytes across the cluster for what is logically one model.

ZeRO (Zero Redundancy Optimizer) eliminates this redundancy in three progressive stages. Stage 1 partitions optimizer states across GPUs (each GPU stores 1/N of Adam states), reducing per-GPU optimizer memory by N×. Stage 2 additionally partitions gradients. Stage 3 additionally partitions parameters themselves. At Stage 3, each GPU stores only 1/N of the complete model state, and the full parameter set is reconstructed on-the-fly via all-gather operations when needed for computation.

## Why It Matters
ZeRO fundamentally changed the memory economics of training. A 10B parameter model that would require ~160GB per GPU under standard data parallelism can be trained on 16GB GPUs with enough ZeRO Stage 3 workers. This democratized large model training and is the core technology behind DeepSpeed, the most widely used distributed training library.

## QnA Seeds
- Q: What are the three stages of ZeRO and what does each partition?
  A: Stage 1 partitions optimizer states (e.g., Adam moments) across GPUs. Stage 2 additionally partitions gradients. Stage 3 additionally partitions model parameters. Each stage progressively reduces per-GPU memory by sharding more of the training state across N data-parallel workers.
- Q: How much memory does standard data parallelism waste compared to ZeRO Stage 3?
  A: In standard DP, each of N GPUs stores the full 16Ψ bytes (parameters + gradients + optimizer states). ZeRO Stage 3 stores only 16Ψ/N per GPU — an N× reduction. For a 10B parameter model on 64 GPUs, this is the difference between ~160GB/GPU and ~2.5GB/GPU for model state.
