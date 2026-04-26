---
tags: [raw, llm]
id: "raw-llm-036"
title: "PaLM: Scaling Language Modeling with Pathways"
author: "Chowdhery et al."
year: 2022
source_type: "paper"
url: "https://arxiv.org/abs/2204.02311"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# PaLM: Scaling Language Modeling with Pathways

## What Is This?
Google's 540 B parameter dense decoder-only Transformer trained on the Pathways system across 6144 TPU v4 chips, demonstrating breakthrough performance and discontinuous improvements on reasoning tasks at scale.

## Why It Matters
Provided the strongest evidence at its time for emergent abilities in LLMs — certain capabilities (multi-step reasoning, code generation, joke explanation) appeared only at the 540 B scale, fueling the scaling debate and motivating chain-of-thought prompting research.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Pathways system: efficient training across 6144 TPU v4 chips with high utilization
- [ ] Emergent abilities observed only at 540 B scale (BIG-Bench discontinuities)
- [ ] Architecture choices: SwiGLU, parallel attention/FFN, multi-query attention, RoPE
