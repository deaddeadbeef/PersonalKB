---
tags: [raw, llm]
id: "raw-llm-053"
title: "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration"
author: "Lin et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2306.00978"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# AWQ: Activation-aware Weight Quantization

## What Is This?
A quantization method that identifies salient weight channels by observing activation magnitudes (not weight magnitudes), then protects those channels via per-channel scaling before uniform quantization — no backpropagation or reconstruction needed.

## Why It Matters
Achieved better quality than GPTQ at the same bit-width with a simpler, faster algorithm. AWQ's insight — that 1% of weights critical for quality can be identified via activations — became a key principle for efficient LLM quantization and on-device deployment.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Activation-aware salient channel identification (1% critical weights)
- [ ] Per-channel scaling trick to protect salient weights before quantization
- [ ] INT4 quantization speedup on edge devices and comparison with GPTQ/RTN
