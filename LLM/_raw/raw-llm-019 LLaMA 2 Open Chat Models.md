---
tags: [raw, llm]
id: "raw-llm-019"
title: "LLaMA 2: Open Foundation and Fine-Tuned Chat Models"
author: "Touvron et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2307.09288"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# LLaMA 2: Open Foundation and Fine-Tuned Chat Models

## What Is This?
Meta's second-generation open-weight LLMs (7B-70B) with both pretrained and chat-optimized variants, trained on 2T tokens and fine-tuned with RLHF for dialogue safety and helpfulness.

## Why It Matters
LLaMA 2 was the first truly open-weight model competitive with closed-source chat models, establishing the template for open-source RLHF alignment and catalyzing the open-weight ecosystem.

## Key Takeaways
1. Pretrained on 2T tokens with 40% more data than LLaMA 1; context length extended to 4096
2. RLHF alignment pipeline: SFT → reward modeling → rejection sampling + PPO
3. Ghost Attention (GAtt) technique maintains system prompt adherence across multi-turn conversations
4. Extensive safety evaluations with human raters showing competitive safety vs closed models

## Chunk Candidates
- [ ] Training data scale and pretraining recipe changes from LLaMA 1
- [ ] RLHF pipeline details (SFT → reward model → rejection sampling → PPO)
- [ ] Ghost Attention (GAtt) for multi-turn system prompt adherence
- [ ] Safety evaluation methodology and human preference results
