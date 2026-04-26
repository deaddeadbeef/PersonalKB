---
tags: [raw, llm]
id: "raw-llm-039"
title: "Mixtral of Experts"
author: "Jiang et al."
year: 2024
source_type: "paper"
url: "https://arxiv.org/abs/2401.04088"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Mixtral of Experts

## What Is This?
A sparse Mixture-of-Experts model with 8 expert FFN blocks per layer (2 active per token), totaling 46.7 B parameters but using only 12.9 B per forward pass. Matches or beats LLaMA 2 70B and GPT-3.5 on most benchmarks.

## Why It Matters
Proved that open-weight MoE models are practical and competitive, achieving 70 B-class quality at a fraction of the inference cost — validating the sparse expert paradigm for production deployment at scale.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Sparse MoE architecture: 8 experts per layer, top-2 routing per token
- [ ] 46.7 B total / 12.9 B active parameter efficiency trade-off
- [ ] Comparison with LLaMA 2 70B and GPT-3.5 across reasoning and code benchmarks
