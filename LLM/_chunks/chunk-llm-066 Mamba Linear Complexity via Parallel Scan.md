---
tags: [chunk, llm]
id: "chunk-llm-066"
source: "[[LLM/_raw/raw-llm-017 Mamba Selective State Spaces]]"
source_loc: "Key Takeaways 2"
topic: "Mamba linear-time complexity"
claim: "Mamba achieves linear O(n) complexity in sequence length via parallel scan, compared to attention's O(n²)."
confidence: "verified"
supports: ["[[LLM/Architecture Variants/State Space Models and Mamba]]"]
up: "[[LLM/LLM]]"
---

# Mamba Linear Complexity via Parallel Scan

## Context
Transformer attention computes all pairwise interactions between tokens, resulting in O(n²) time and memory complexity in sequence length n. This quadratic scaling is the fundamental bottleneck for long-sequence processing. Mamba's selective SSM processes sequences in O(n) time by formulating the computation as a linear recurrence that can be parallelized using the parallel scan (prefix sum) algorithm.

The parallel scan works because the SSM state update is an associative operation: the combined effect of processing tokens 1 through k can be composed from the effects of processing tokens 1 through j and j+1 through k. This associativity enables a divide-and-conquer parallelization that computes all n state updates in O(log n) parallel steps on a GPU, despite each update depending on the previous state. The total work is O(n) (linear scan) with O(log n) depth (parallel steps), making it both asymptotically and practically efficient.

## Why It Matters
Linear-time sequence processing is the holy grail that motivated years of efficient attention research (Linformer, Performer, etc.). Mamba achieved it not by approximating attention but by using a fundamentally different computation (selective SSM + parallel scan). For very long sequences (16K+), Mamba's throughput advantage over transformers becomes dramatic — 5× or more at 64K tokens.

## QnA Seeds
- Q: How does Mamba achieve O(n) complexity while attention requires O(n²)?
  A: Mamba uses a selective SSM formulated as a linear recurrence, parallelized with the parallel scan algorithm. Unlike attention which computes all pairwise token interactions (n² pairs), the SSM processes each token once with a fixed-size state, giving linear total work with O(log n) parallel depth.
- Q: What makes the parallel scan algorithm applicable to Mamba's SSM computation?
  A: The SSM state update is an associative operation — combining updates from non-overlapping sequence segments is equivalent to processing the full segment. This associativity enables divide-and-conquer parallelization, computing all n state updates in O(log n) parallel GPU steps.
