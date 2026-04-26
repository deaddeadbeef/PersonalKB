---
tags: [llm, chunk]
id: chunk-llm-241
source: "[[raw-llm-061]]"
supports: ["[[Reasoning Models and Test-Time Compute]]"]
confidence: verified
up: "[[LLM]]"
---

# Test-Time Compute Scaling Improves Performance by Allocating More Inference Tokens

## Context

Traditional LLM scaling improves performance by increasing model parameters and training data. Reasoning models introduced an orthogonal approach: spending more compute during inference by generating extended chains of thought.

## Claim

Test-time compute scaling allows models to improve output quality by generating more reasoning tokens at inference time, representing a new capability axis orthogonal to training-time scaling.

## Why It Matters

This opened a second frontier for capability improvement — models can "think harder" on difficult inputs without retraining, enabling variable compute allocation based on problem difficulty.

## QnA Seeds

- Q: How does test-time compute differ from training-time scaling? → A: Training scaling increases parameters/data before deployment; test-time scaling increases reasoning tokens during each inference call.
- Q: Why is variable compute allocation valuable? → A: Easy questions get fast answers while hard questions get deep reasoning, making compute spend proportional to difficulty.
