---
tags: [llm, chunk]
id: chunk-llm-264
source: "[[LLM/_raw/raw-llm-071|raw-llm-071]]"
source_loc: "p. 251"
supports: ["[[LLM/2026 — Reasoning and Agents/Reasoning Models and Test-Time Compute]]", "[[LLM/2026 — Reasoning and Agents/DeepSeek R1 and Open Reasoning]]", "[[LLM/Study/LLM Progressive Systems Route]]"]
confidence: verified
up: "[[LLM/LLM]]"
---

# Reasoning RL Treats Multi-Step Reasoning As Verifiable Search Under Sparse Rewards

## Context

The reasoning chapter argues that ordinary response-level RL is weak for multi-step reasoning because reasoning tasks involve sparse rewards, long horizons, combinatorial paths, and often objectively checkable final answers.

## Claim

Reasoning models should be understood as search-and-verification systems that spend more inference-time computation exploring and checking intermediate steps, not merely as larger chat models.

## Why It Matters

This gives the wiki a clean bridge from RL foundations to test-time compute, reasoning distillation, and local reasoning-budget probes.

## QnA Seeds

- Q: Why are reasoning rewards sparse? -> A: A final answer may be right or wrong even though many intermediate steps contributed to the outcome.
- Q: What makes math and code useful for reasoning RL? -> A: They often provide automatically verifiable outcomes, such as exact answers, proof checks, or passing tests.
