---
tags: [chunk, llm]
id: "chunk-llm-087"
source: "[[LLM/_raw/raw-llm-022 QLoRA Efficient Finetuning Quantized LLMs]]"
source_loc: "Key Takeaways 3"
topic: "Paged optimizers unified memory"
claim: "Paged optimizers in QLoRA use unified CPU/GPU memory to handle memory spikes during gradient checkpointing."
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/LoRA and QLoRA]]"]
up: "[[LLM/LLM]]"
---

# Paged Optimizers Handle Memory Spikes via Unified Memory

## Context
During fine-tuning with gradient checkpointing, GPU memory usage is not constant — it spikes when recomputing activations during the backward pass. These transient spikes can cause out-of-memory (OOM) errors even when average memory usage is well within GPU capacity. QLoRA addresses this with paged optimizers, which leverage NVIDIA's unified memory feature to automatically page optimizer states between CPU and GPU memory.

When a memory spike occurs, the least recently used optimizer state pages are automatically evicted to CPU memory and brought back when needed. This is conceptually identical to how operating systems handle virtual memory paging. The overhead is minimal because optimizer states are only needed during the parameter update step, and the CPU-GPU transfer can overlap with computation.

## Why It Matters
Paged optimizers eliminate the worst-case memory problem that makes fine-tuning unpredictable. Instead of sizing GPU memory for peak usage (which wastes capacity most of the time), the system gracefully handles spikes, allowing larger batch sizes and larger models to fit within a fixed memory budget.

## QnA Seeds
- Q: What problem do paged optimizers solve in QLoRA?
  A: They handle transient GPU memory spikes during gradient checkpointing by automatically paging optimizer states between CPU and GPU memory, preventing OOM errors.
- Q: How do paged optimizers work conceptually?
  A: They use NVIDIA unified memory to evict least-recently-used optimizer state pages to CPU RAM during memory spikes and bring them back when needed, similar to OS virtual memory paging.
