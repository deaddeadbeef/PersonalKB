---
tags: [chunk, llm]
id: "chunk-llm-015"
source: "[[LLM/_raw/raw-llm-004 Scaling Laws for Neural Language Models]]"
source_loc: "Section 5"
topic: "sample efficiency"
claim: "Larger models are more sample-efficient — they achieve the same loss with fewer training tokens"
confidence: "verified"
supports: ["[[LLM/Pretraining/Compute Data and Parameter Trade-offs]]"]
up: "[[LLM/LLM]]"
---

# Larger Models Are More Sample-Efficient

## Context

Kaplan et al. observed that larger language models reach any given loss value with significantly fewer training tokens than smaller models. For example, a 10× larger model might reach a specific loss after seeing only 2× more data rather than 10×. This means the per-token learning rate (in terms of loss reduction) increases with model size — each training example provides more useful gradient signal to a larger model.

This sample efficiency arises because larger models have more parameters to represent the structure of language, so each training example can simultaneously improve many aspects of the model's internal representation. A small model may need to see many examples of a pattern to robustly learn it, while a large model can generalize from fewer instances because its richer representational capacity allows better interpolation and pattern extraction.

## Why It Matters

Sample efficiency has profound implications for optimal training strategies. It means that when you have a fixed compute budget, you should allocate more of it to model size and less to training duration than naïve intuition suggests. This finding was a key input to the Kaplan scaling recommendations (which favored larger models trained for fewer steps) and was later revised by the Chinchilla paper, which found the optimal balance favors more data than Kaplan initially suggested.

## QnA Seeds
- Q: How does sample efficiency relate to the compute-optimal training debate?
  A: Sample efficiency says larger models extract more learning per token. Kaplan interpreted this as evidence to scale parameters aggressively — train a very large model for fewer steps. But Chinchilla later showed that Kaplan underweighted the benefits of more data. The resolution is nuanced: larger models are more sample-efficient, but you still need enough data to fully realize that efficiency. The optimal balance scales both together.
- Q: Does sample efficiency mean small models can never match large models given enough data?
  A: Not exactly. Given infinite data, a small model will eventually converge to its capacity limit — the best loss it can achieve given its parameter budget. A larger model has a lower capacity limit. So while a small model can improve with more data, there's a floor it cannot breach. Sample efficiency is about the rate of approach to this floor, not the floor itself.
