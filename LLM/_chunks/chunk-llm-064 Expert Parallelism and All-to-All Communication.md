---
tags: [chunk, llm]
id: "chunk-llm-064"
source: "[[LLM/_raw/raw-llm-016 Switch Transformers Trillion Parameter MoE]]"
source_loc: "What Is This, Chunk Candidates"
topic: "Expert parallelism"
claim: "Expert parallelism distributes experts across GPUs; tokens are routed via all-to-all communication to reach their assigned expert."
confidence: "verified"
supports: ["[[LLM/Architecture Variants/Mixture-of-Experts Models]]"]
up: "[[LLM/LLM]]"
---

# Expert Parallelism and All-to-All Communication

## Context
In a Switch Transformer with hundreds or thousands of experts, no single GPU can hold all expert parameters. Expert parallelism distributes experts across GPUs — each GPU holds a subset of experts and processes tokens routed to those experts. The critical communication primitive is all-to-all: after the router decides which expert each token should go to, tokens must be physically sent from the GPU where they reside to the GPU holding their assigned expert.

The all-to-all communication pattern is fundamentally different from the all-reduce used in data parallelism or tensor parallelism. In all-to-all, each GPU sends different data to every other GPU (each token goes to a different expert), creating a many-to-many communication pattern. After expert computation, a reverse all-to-all sends the processed tokens back to their originating GPUs. This communication overhead is the primary cost of expert parallelism and the reason why expert count, capacity factors, and batch sizing must be carefully tuned.

## Why It Matters
Expert parallelism is the fourth parallelism axis (alongside data, tensor, and pipeline) needed for MoE training. The all-to-all communication pattern creates unique challenges: it doesn't benefit from the same optimizations as all-reduce, and it scales with both the number of experts and the batch size. Understanding this communication pattern is essential for deploying MoE models at scale.

## QnA Seeds
- Q: How does expert parallelism differ from tensor parallelism in its communication pattern?
  A: Tensor parallelism uses all-reduce (every GPU sends the same aggregated data to all others). Expert parallelism uses all-to-all (each GPU sends different tokens to different GPUs based on routing decisions). All-to-all is a many-to-many pattern that's harder to optimize and scales with batch size.
- Q: What is the communication sequence for processing a batch of tokens through an MoE layer?
  A: (1) Router computes expert assignments for all tokens, (2) all-to-all sends each token to the GPU holding its assigned expert, (3) each GPU processes tokens through its local experts, (4) reverse all-to-all sends processed tokens back to their originating GPUs.
