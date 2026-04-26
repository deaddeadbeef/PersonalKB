---
tags: [llm, chunk]
id: chunk-llm-245
source: "[[raw-llm-062]]"
supports: ["[[DeepSeek R1 and Open Reasoning]]"]
confidence: verified
up: "[[LLM]]"
---

# DeepSeek R1 Uses GRPO to Eliminate the Critic Model

## Context

Standard RLHF uses PPO, which requires training a separate critic (value) model alongside the policy model, roughly doubling memory and compute requirements.

## Claim

DeepSeek R1 uses Group Relative Policy Optimization (GRPO), a PPO variant that eliminates the separate critic model, reducing training infrastructure requirements and overall cost to approximately .6M.

## Why It Matters

Lower training cost makes frontier reasoning model development accessible to more labs and demonstrates that reasoning doesn't require billion-dollar compute budgets.

## QnA Seeds

- Q: What is GRPO and how does it differ from PPO? → A: GRPO estimates baselines from group statistics rather than a learned critic model, eliminating the need for a separate value network.
- Q: What was DeepSeek R1's reported training cost? → A: Approximately .6 million — a fraction of typical frontier model budgets.
