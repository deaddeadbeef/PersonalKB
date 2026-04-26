---
tags: [llm, chunk]
id: chunk-llm-242
source: "[[raw-llm-061]]"
supports: ["[[Reasoning Models and Test-Time Compute]]"]
confidence: verified
up: "[[LLM]]"
---

# OpenAI o1 Scores 83.3% on AIME 2024 via Hidden Chain-of-Thought

## Context

OpenAI released o1-preview in September 2024 as the first major reasoning model. It generates internal reasoning tokens that are hidden from the user, allowing step-by-step problem decomposition.

## Claim

OpenAI o1 achieved 83.3% on AIME 2024 (vs GPT-4o's 13.4%) by generating hidden chain-of-thought tokens that decompose problems and self-verify before producing a final answer.

## Why It Matters

A 6× improvement on competition mathematics demonstrated that inference-time reasoning could yield gains comparable to orders-of-magnitude increases in model scale.

## QnA Seeds

- Q: What is the key mechanism behind o1's performance? → A: Hidden chain-of-thought reasoning tokens that allow multi-step decomposition and self-verification before the final answer.
- Q: How much did o1 improve over GPT-4o on AIME? → A: From 13.4% to 83.3% — roughly a 6× improvement.
