---
tags: [llm, chunk]
id: chunk-llm-250
source: "[[raw-llm-069]]"
supports: ["[[Frontier Models 2025-2026]]"]
confidence: verified
up: "[[LLM]]"
---

# Llama 4 Adopts Mixture-of-Experts for Frontier Performance with Open Weights

## Context

Meta's Llama family has been the cornerstone of the open-weights ecosystem, scaling from Llama 1 (2023) through Llama 3.1 405B (2024) with increasingly competitive performance.

## Claim

Meta's Llama 4 adopted a mixture-of-experts (MoE) architecture, achieving competitive performance with closed frontier models while maintaining open weights, continuing to narrow the open-closed capability gap.

## Why It Matters

MoE enables frontier-level capability at reduced inference cost (only a subset of experts activate per token), making open-source frontier models more practical to deploy.

## QnA Seeds

- Q: Why did Llama 4 switch to MoE? → A: MoE activates only a subset of parameters per token, enabling frontier-scale capability at lower per-token inference cost.
- Q: Under what license are Llama 4 weights released? → A: Meta's community license, which is permissive for most uses including commercial applications.
