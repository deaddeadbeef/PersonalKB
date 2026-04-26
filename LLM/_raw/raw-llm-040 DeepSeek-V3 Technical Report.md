---
tags: [raw, llm]
id: "raw-llm-040"
title: "DeepSeek-V3 Technical Report"
author: "DeepSeek-AI"
year: 2024
source_type: "paper"
url: "https://arxiv.org/abs/2412.19437"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# DeepSeek-V3 Technical Report

## What Is This?
A 671 B parameter MoE model (37 B active) using Multi-head Latent Attention (MLA) and DeepSeekMoE architecture, trained on 14.8 T tokens with an auxiliary-loss-free load balancing strategy and FP8 mixed-precision training.

## Why It Matters
Achieved GPT-4o and Claude 3.5-class performance at a reported training cost of ~$5.5 M — dramatically lower than comparable models — demonstrating that architectural innovation (MLA, auxiliary-loss-free balancing) and training efficiency can close the gap with frontier labs.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Multi-head Latent Attention (MLA) for compressed KV cache
- [ ] Auxiliary-loss-free expert load balancing strategy
- [ ] FP8 mixed-precision training and $5.5 M training cost efficiency
