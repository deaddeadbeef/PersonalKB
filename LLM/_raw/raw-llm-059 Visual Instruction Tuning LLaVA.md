---
tags: [raw, llm]
id: "raw-llm-059"
title: "Visual Instruction Tuning"
author: "Liu et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2304.08485"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Visual Instruction Tuning (LLaVA)

## What Is This?
Introduces Large Language and Vision Assistant (LLaVA), connecting a CLIP vision encoder to a LLaMA language model via a simple projection layer, then instruction-tuning on GPT-4-generated visual conversation data.

## Why It Matters
Demonstrated that multimodal instruction following can be achieved by connecting pre-trained vision and language models with minimal additional parameters. LLaVA's simplicity and open-source nature spawned a large ecosystem of visual LLM research.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Architecture: CLIP ViT-L encoder → linear projection → LLaMA decoder
- [ ] GPT-4-generated multimodal instruction-following training data
- [ ] Two-stage training: feature alignment pre-training → visual instruction fine-tuning
