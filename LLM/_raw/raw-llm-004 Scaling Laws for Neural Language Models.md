---
tags: [raw, llm]
id: "raw-llm-004"
title: "Scaling Laws for Neural Language Models"
author: "Kaplan et al."
year: 2020
source_type: "paper"
url: "https://arxiv.org/abs/2001.08361"
status: "processed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Scaling Laws for Neural Language Models

## What Is This?
Empirical study showing power-law relationships between compute, dataset size, model parameters, and language model loss.

## Why It Matters
Provided a quantitative framework for predicting model performance based on resources. Drove the "scaling hypothesis" that guided billion-dollar training runs.

## Key Takeaways
1. Loss follows power laws: L(N) ≈ (N_c/N)^α for parameters, similar for data and compute
2. Performance is predictable: small runs can forecast large model performance
3. Larger models are more sample-efficient
4. Architecture details (depth vs width) matter less than scale

## Chunk Candidates
- [ ] Power-law relationships and exponents
- [ ] Compute-optimal allocation (Kaplan vs Chinchilla)
- [ ] Sample efficiency of larger models
- [ ] Predictability of scaling
