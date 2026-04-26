---
tags: [raw, llm]
id: "raw-llm-010"
title: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
author: "Rafailov et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2305.18290"
status: "processed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Direct Preference Optimization

## What Is This?
Reformulates RLHF as a simple classification loss, eliminating the need for a separate reward model and PPO training.

## Why It Matters
Dramatically simplified alignment training. Made preference-based alignment accessible to smaller teams without RL expertise.

## Key Takeaways
1. Closed-form relationship between optimal policy and reward function
2. DPO loss: binary cross-entropy on (preferred, rejected) pairs
3. No reward model, no PPO, no RL instabilities
4. Comparable results to RLHF with simpler implementation

## Chunk Candidates
- [ ] DPO loss derivation and intuition
- [ ] Comparison with RLHF pipeline
- [ ] Offline vs online preference data
- [ ] Variants (IPO, KTO, ORPO)
