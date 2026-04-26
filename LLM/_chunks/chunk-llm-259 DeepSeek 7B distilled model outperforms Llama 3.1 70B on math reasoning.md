---
tags: [llm, chunk]
id: chunk-llm-259
source: "[[raw-llm-070]]"
supports: ["[[Reasoning Distillation]]"]
confidence: verified
up: "[[LLM]]"
---

# DeepSeek 7B Distilled Model Outperforms Llama 3.1 70B on Math Reasoning

## Context

A key question for reasoning distillation is how much capability can be preserved as model size decreases. DeepSeek's distillation results provide a dramatic answer.

## Claim

DeepSeek's 7B-parameter model distilled from R1 outperformed Llama 3.1 70B (10 times larger) on mathematical reasoning tasks, demonstrating that reasoning style transfers across model scales more effectively than raw knowledge.

## Why It Matters

A 10x smaller model outperforming a 10x larger one proves that reasoning capability is more about learned reasoning patterns than about parameter count, fundamentally changing the economics of AI deployment.

## QnA Seeds

- Q: How can a 7B model outperform a 70B model? → A: The 7B model learned efficient reasoning patterns from R1's traces, while the 70B base model lacks these patterns despite having more parameters.
- Q: What does this imply for deployment costs? → A: 10-100x cheaper inference for reasoning tasks, making advanced AI accessible without frontier-scale infrastructure.
