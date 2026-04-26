---
tags: [llm, chunk]
id: chunk-llm-243
source: "[[raw-llm-061]]"
supports: ["[[Reasoning Models and Test-Time Compute]]"]
confidence: verified
up: "[[LLM]]"
---

# Inference Scaling Laws Predict Performance as a Function of Thinking Time

## Context

Chinchilla scaling laws predict training performance as a function of compute budget. Reasoning models revealed analogous laws for inference: performance scales predictably with the number of reasoning tokens generated.

## Claim

Inference scaling laws show that reasoning model performance improves predictably with additional compute at inference time, analogous to how Chinchilla laws predict training-time scaling.

## Why It Matters

Predictable inference scaling enables principled cost-performance trade-offs: allocate more thinking time for high-stakes queries, less for routine ones.

## QnA Seeds

- Q: What are inference scaling laws? → A: Empirical relationships showing that reasoning model accuracy improves predictably as more tokens are allocated for chain-of-thought reasoning.
- Q: How do inference scaling laws relate to training scaling laws? → A: They are complementary — training laws govern pre-deployment capability, inference laws govern per-query capability.
