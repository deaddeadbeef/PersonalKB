---
tags: [raw, llm]
id: "raw-llm-002"
title: "Language Models are Few-Shot Learners"
author: "Brown et al."
year: 2020
source_type: "paper"
url: "https://arxiv.org/abs/2005.14165"
status: "processed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Language Models are Few-Shot Learners (GPT-3)

## What Is This?
The GPT-3 paper demonstrating that a 175B parameter language model can perform tasks via in-context learning without any gradient updates.

## Why It Matters
Established the in-context learning paradigm. Showed that scale alone produces qualitative capability jumps. Launched the "prompt engineering" era.

## Key Takeaways
1. 175B parameter autoregressive transformer trained on 300B tokens
2. Few-shot prompting: provide examples in the prompt, model generalizes
3. Performance scales smoothly with model size across diverse tasks
4. Zero-shot, one-shot, and few-shot evaluated systematically

## Chunk Candidates
- [ ] In-context learning as emergent capability
- [ ] Scaling behavior across model sizes
- [ ] Few-shot vs fine-tuning comparison
- [ ] Dataset and training details
