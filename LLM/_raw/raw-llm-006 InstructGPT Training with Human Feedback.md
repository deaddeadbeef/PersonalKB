---
tags: [raw, llm]
id: "raw-llm-006"
title: "Training language models to follow instructions with human feedback"
author: "Ouyang et al."
year: 2022
source_type: "paper"
url: "https://arxiv.org/abs/2203.02155"
status: "processed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Training language models to follow instructions with human feedback (InstructGPT)

## What Is This?
Introduced the RLHF pipeline: SFT → reward model → PPO, to align language models with human intent.

## Why It Matters
Made GPT-3 actually useful. The 1.3B InstructGPT was preferred over the 175B GPT-3. Directly led to ChatGPT.

## Key Takeaways
1. Three-stage pipeline: supervised fine-tuning → reward model training → PPO optimization
2. Human labelers write demonstrations and rank outputs
3. Small aligned model preferred over large unaligned model
4. KL penalty prevents divergence from SFT model

## Chunk Candidates
- [ ] RLHF three-stage pipeline
- [ ] Reward model training from preferences
- [ ] PPO with KL penalty
- [ ] Human evaluation methodology
