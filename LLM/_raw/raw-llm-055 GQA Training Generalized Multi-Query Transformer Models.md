---
tags: [raw, llm]
id: "raw-llm-055"
title: "GQA: Training Generalized Multi-Query Attention Models from Multi-Head Checkpoints"
author: "Ainslie et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2305.13245"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# GQA: Training Generalized Multi-Query Transformer Models

## What Is This?
Introduces Grouped-Query Attention, an interpolation between Multi-Head Attention and Multi-Query Attention where key-value heads are shared among groups of query heads, plus an uptraining recipe to convert existing MHA checkpoints to GQA.

## Why It Matters
Found the sweet spot between MHA quality and MQA speed — GQA achieves near-MHA accuracy with near-MQA inference speed. Adopted by LLaMA 2 70B, Mistral, and most modern LLMs as the default attention configuration.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] GQA mechanism: G key-value head groups shared among H query heads
- [ ] Uptraining recipe: converting MHA checkpoints to GQA with minimal fine-tuning
- [ ] Speed-quality Pareto curve: MHA vs. GQA vs. MQA on inference throughput
