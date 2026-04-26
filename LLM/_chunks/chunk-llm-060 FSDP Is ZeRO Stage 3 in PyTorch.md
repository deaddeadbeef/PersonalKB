---
tags: [chunk, llm]
id: "chunk-llm-060"
source: "[[LLM/_raw/raw-llm-015 ZeRO Memory Optimizations]]"
source_loc: "Chunk Candidates"
topic: "FSDP and ZeRO equivalence"
claim: "FSDP (Fully Sharded Data Parallel) in PyTorch is essentially ZeRO Stage 3 integrated into the framework."
confidence: "verified"
supports: ["[[LLM/Pretraining/Training Infrastructure and Parallelism]]"]
up: "[[LLM/LLM]]"
---

# FSDP Is ZeRO Stage 3 in PyTorch

## Context
PyTorch's Fully Sharded Data Parallel (FSDP) implements the same core algorithm as ZeRO Stage 3: model parameters, gradients, and optimizer states are all sharded across data-parallel workers. During forward and backward passes, parameters are gathered (all-gather) just before they're needed and released (reduce-scatter for gradients) immediately after. This produces the same N× memory reduction as ZeRO Stage 3.

The key difference is integration: FSDP is a native PyTorch module wrapper (`torch.distributed.fsdp.FullyShardedDataParallel`), while ZeRO Stage 3 is implemented in DeepSpeed as an external library. FSDP offers tighter integration with PyTorch's autograd, composability with other PyTorch features (activation checkpointing, mixed precision), and a simpler API. FSDP2 (PyTorch 2.x) further improved this with per-parameter sharding and DTensor integration.

## Why It Matters
FSDP's integration into PyTorch means that ZeRO-style memory optimization is now a first-class citizen of the dominant deep learning framework. Practitioners no longer need to choose between DeepSpeed and native PyTorch — they get equivalent memory efficiency through FSDP with the full PyTorch ecosystem. This has made sharded data parallelism the default approach for distributed training in most modern LLM projects.

## QnA Seeds
- Q: What is the relationship between PyTorch FSDP and DeepSpeed ZeRO?
  A: FSDP implements the same algorithm as ZeRO Stage 3 — sharding parameters, gradients, and optimizer states across GPUs with all-gather for computation and reduce-scatter for gradients. The difference is that FSDP is a native PyTorch module wrapper with tighter framework integration, while ZeRO is an external DeepSpeed library.
- Q: What practical advantage does FSDP have over using DeepSpeed ZeRO?
  A: FSDP is natively integrated into PyTorch, composing naturally with autograd, activation checkpointing, mixed precision, and other PyTorch features. It requires no external library and has a simpler API. FSDP2 adds per-parameter sharding and DTensor integration for even more flexibility.
