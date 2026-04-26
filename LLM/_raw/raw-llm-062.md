---
tags: [llm, raw]
source_type: technical_paper
source_title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
authors: [DeepSeek AI]
year: 2025
up: "[[Sources Index]]"
---

# DeepSeek R1 — Open-Source Reasoning

## Summary

DeepSeek AI released R1 in January 2025 as an open-weights reasoning model matching OpenAI o1 on multiple benchmarks. R1-Zero was trained with pure reinforcement learning (no supervised fine-tuning), and spontaneously developed chain-of-thought reasoning, self-verification, and introspective "aha moments." The full R1 model combined RL with cold-start SFT and used Group Relative Policy Optimization (GRPO). Released under MIT license with distilled variants from 1.5B to 70B parameters, the 14B distilled model outperformed o1-mini on several benchmarks.

## Key Claims

1. Pure RL without SFT can produce structured chain-of-thought reasoning (R1-Zero)
2. GRPO eliminates the need for a separate critic model, reducing training cost
3. Reasoning capabilities transfer effectively through distillation to much smaller models
4. Open-weights release under MIT license makes frontier reasoning universally accessible
5. Training cost of approximately $5.6M demonstrates reasoning can be developed affordably

## Atomic Facts

1. R1 released January 2025 under MIT license
2. AIME 2024: R1 scored 79.8%
3. MATH-500: R1 scored 97.3%
4. Distilled variants: 1.5B, 7B, 8B, 14B, 32B, 70B parameters
5. 14B distilled model outperformed o1-mini on multiple benchmarks
6. Training used Group Relative Policy Optimization (GRPO)

## Significance

R1 proved reasoning models can be developed affordably with open methods, democratizing advanced AI capabilities and challenging the assumption that frontier AI requires massive proprietary investment.

## Chunks Extracted

*Pending*