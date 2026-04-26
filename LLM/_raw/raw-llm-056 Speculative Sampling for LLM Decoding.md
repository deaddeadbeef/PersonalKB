---
tags: [raw, llm]
id: "raw-llm-056"
title: "Accelerating Large Language Model Decoding with Speculative Sampling"
author: "Chen et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2302.01318"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Speculative Sampling for LLM Decoding

## What Is This?
A method that uses a small draft model to propose multiple candidate tokens, then verifies them in parallel with the large target model — generating multiple tokens per forward pass of the large model while preserving its exact output distribution.

## Why It Matters
Achieved 2-3× decoding speedup with no quality loss, breaking the one-token-per-forward-pass bottleneck of autoregressive generation. Speculative decoding is now widely deployed in production LLM serving (vLLM, TensorRT-LLM, etc.).

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Draft-then-verify algorithm: small model proposes, large model accepts/rejects
- [ ] Acceptance probability and rejection sampling to preserve target distribution
- [ ] Speedup analysis: draft model size, acceptance rate, and tokens per step
