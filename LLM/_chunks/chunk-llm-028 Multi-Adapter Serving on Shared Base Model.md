---
tags: [chunk, llm]
id: "chunk-llm-028"
source: "[[LLM/_raw/raw-llm-007 LoRA Low-Rank Adaptation]]"
source_loc: "Section 4.3, Section 7"
topic: "LoRA adapter serving"
claim: "Multiple LoRA adapters can serve different tasks on a shared base model by swapping the small adapter matrices"
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/LoRA and QLoRA]]"]
up: "[[LLM/LLM]]"
---

# Multi-Adapter Serving on Shared Base Model

## Context

Because LoRA adapters are small (typically a few MB to a few hundred MB compared to the multi-GB base model), multiple task-specific adapters can share a single copy of the base model in memory. At serving time, the appropriate adapter is selected based on the request and either merged into the weights or applied as a separate computation. This enables multi-tenant serving where one GPU hosts a single base model serving dozens of specialized tasks.

In practice, two serving strategies exist: (1) pre-merge, where you create separate merged model copies for each adapter (simple but memory-intensive), or (2) dynamic adapter loading, where the base model stays in memory and adapters are swapped per-request. Systems like LoRAX and Punica implement efficient batched inference where requests using different adapters can be processed in the same batch, with the adapter computation handled via custom CUDA kernels that apply different BA matrices to different sequences in the batch.

## Why It Matters

Multi-adapter serving transforms the economics of serving specialized models. Instead of deploying N separate fine-tuned models (each consuming tens of GB of GPU memory), you deploy one base model plus N tiny adapters. This reduces GPU memory requirements by an order of magnitude and enables personalized or task-specific models that would be prohibitively expensive to serve individually. It's a key enabler for platforms offering customized AI services.

## QnA Seeds
- Q: How does batched multi-adapter inference work efficiently?
  A: Systems like Punica and S-LoRA use custom CUDA kernels to apply different LoRA adapters to different sequences within the same batch. The base model forward pass is shared (one large matrix multiplication), and only the adapter computation is differentiated per-sequence. Since adapters are small (low-rank), the per-adapter computation adds minimal overhead. This approach achieves near-linear scaling with the number of concurrent adapters.
- Q: What is the memory overhead of storing many LoRA adapters alongside a base model?
  A: Minimal. A LoRA adapter for a 7B model at r=8 is typically 10-30MB, compared to ~14GB for the base model in fp16. You could store 100 different adapters for less memory than a second copy of the base model. In dynamic serving setups, only the base model and currently active adapters need to be in GPU memory — inactive adapters can be stored in CPU memory or disk and loaded in milliseconds.
