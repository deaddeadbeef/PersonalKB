---
tags: [chunk, llm]
id: "chunk-llm-059"
source: "[[LLM/_raw/raw-llm-015 ZeRO Memory Optimizations]]"
source_loc: "Chunk Candidates"
topic: "ZeRO-Offload CPU extension"
claim: "ZeRO-Offload extends ZeRO by offloading optimizer states and computation to CPU, enabling training of larger models on fewer GPUs."
confidence: "verified"
supports: ["[[LLM/Pretraining/Training Infrastructure and Parallelism]]"]
up: "[[LLM/LLM]]"
---

# ZeRO-Offload to CPU Memory

## Context
Even with ZeRO Stage 3, per-GPU memory can be insufficient for very large models on limited hardware. ZeRO-Offload addresses this by offloading optimizer states and optimizer computation to CPU memory and CPU compute. Since optimizer updates (Adam step) are less compute-intensive than forward/backward passes, the CPU can handle them without becoming a bottleneck, while the GPU focuses on the matrix multiplications.

ZeRO-Offload achieves this by keeping fp16 parameters and gradients on GPU for forward/backward computation, then transferring gradients to CPU where the Adam optimizer updates the fp32 master weights. Updated fp16 parameters are then transferred back to GPU. With careful overlap of CPU computation and GPU-CPU data transfer, the throughput penalty is surprisingly small — typically 10-30% slowdown compared to GPU-only training, while enabling training of models 10× larger than GPU memory would otherwise allow.

## Why It Matters
ZeRO-Offload democratized large model training by making it possible to train billion-parameter models on just a single GPU with sufficient CPU RAM. This was particularly impactful for researchers and small teams who couldn't access large GPU clusters. The follow-up work, ZeRO-Infinity, extended offloading to NVMe SSDs, further expanding the accessible model size.

## QnA Seeds
- Q: How does ZeRO-Offload enable training models larger than GPU memory?
  A: It offloads optimizer states and the optimizer step computation to CPU memory and CPU compute. The GPU handles forward and backward passes with fp16 parameters, then gradients are transferred to CPU for the Adam update. Updated parameters are sent back to GPU, with overlapping to minimize the throughput penalty.
- Q: What is the typical throughput penalty for using ZeRO-Offload?
  A: 10-30% wall-clock slowdown compared to GPU-only training, depending on model size and CPU-GPU bandwidth. This is modest given that it enables training models 10× larger than GPU memory alone would support, making it practical for single-GPU or few-GPU setups.
