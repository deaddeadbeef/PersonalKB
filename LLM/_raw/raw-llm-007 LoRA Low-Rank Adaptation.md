---
tags: [raw, llm]
id: "raw-llm-007"
title: "LoRA: Low-Rank Adaptation of Large Language Models"
author: "Hu et al."
year: 2021
source_type: "paper"
url: "https://arxiv.org/abs/2106.09685"
status: "processed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# LoRA: Low-Rank Adaptation of Large Language Models

## What Is This?
Freezes pretrained weights and injects trainable low-rank decomposition matrices into transformer layers.

## Why It Matters
Made fine-tuning practical for everyone. Train <1% of parameters with comparable quality to full fine-tuning. Enables multiple task-specific adapters on one base model.

## Key Takeaways
1. W = W_0 + BA where B is d×r and A is r×d (r << d)
2. Only A and B are trained; W_0 is frozen
3. At inference, merge BA into W_0 — no additional latency
4. Rank r is typically 4-64; higher rank = more capacity

## Chunk Candidates
- [ ] Low-rank decomposition formulation
- [ ] Which layers to adapt (attention vs FFN)
- [ ] Rank selection trade-offs
- [ ] Comparison with full fine-tuning and other PEFT methods
