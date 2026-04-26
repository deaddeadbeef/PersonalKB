---
tags: [raw, llm]
id: "raw-llm-016"
title: "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity"
author: "Fedus et al."
year: 2021
source_type: "paper"
url: "https://arxiv.org/abs/2101.03961"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

## What Is This?
Simplifies Mixture-of-Experts routing to a single-expert selection per token (top-1 routing), enabling stable training of sparse models up to 1.6 trillion parameters.

## Why It Matters
Demonstrated that sparse MoE models can scale parameter count massively while keeping per-token compute constant, achieving large quality gains with the same training FLOP budget as dense models.

## Key Takeaways
1. Top-1 routing: each token is sent to exactly one expert, simplifying load balancing and reducing communication
2. Auxiliary load-balancing loss encourages uniform expert utilization
3. 7× parameter increase over dense T5 with matched training FLOPs yields large quality improvements
4. Distillation from sparse Switch models into dense models retains ~30% of the quality gain

## Chunk Candidates
- [ ] Top-1 routing mechanism and gating function design
- [ ] Load-balancing loss and expert capacity factor
- [ ] Scaling results: sparse vs dense at matched FLOPs
- [ ] Distillation from sparse MoE to dense models
