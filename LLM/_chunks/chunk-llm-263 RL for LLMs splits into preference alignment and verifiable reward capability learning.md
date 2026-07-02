---
tags: [llm, chunk]
id: chunk-llm-263
source: "[[LLM/_raw/raw-llm-071|raw-llm-071]]"
source_loc: "p. 133"
supports: ["[[LLM/2022 — Alignment and Chat/Reinforcement Learning from Human Feedback]]", "[[LLM/2022 — Alignment and Chat/Direct Preference Optimization]]", "[[LLM/Study/LLM Progressive Systems Route]]"]
confidence: verified
up: "[[LLM/LLM]]"
---

# RL For LLMs Splits Into Preference Alignment And Verifiable Reward Capability Learning

## Context

The survey describes two broad reinforcement-learning paradigms for language models: alignment from human preferences, such as RLHF and DPO, and capability improvement from verifiable rewards, especially for mathematics, code, and reasoning.

## Claim

Post-training should not be taught as one undifferentiated alignment step. Preference alignment and verifiable-reward capability learning solve different problems and produce different evidence requirements.

## Why It Matters

This helps the wiki keep RLHF, DPO, reward models, RLVR, DeepSeek-R1, reasoning models, and local reasoning-budget experiments in one map without flattening their differences.

## QnA Seeds

- Q: What does RLHF optimize? -> A: A policy toward preferences captured from human judgments, usually through a reward model or a direct preference objective.
- Q: What makes verifiable-reward RL different? -> A: The reward can be computed from an objective outcome, such as a correct answer or passing code test, without relying only on subjective preference labels.
