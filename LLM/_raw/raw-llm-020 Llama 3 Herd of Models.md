---
tags: [raw, llm]
id: "raw-llm-020"
title: "The Llama 3 Herd of Models"
author: "Dubey et al."
year: 2024
source_type: "paper"
url: "https://arxiv.org/abs/2407.21783"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# The Llama 3 Herd of Models

## What Is This?
Meta's Llama 3 family (8B, 70B, 405B) trained on 15T+ tokens, featuring a natively multimodal 405B model with text, image, video, and speech capabilities.

## Why It Matters
Llama 3 405B became the most capable open-weight model at release, competitive with GPT-4 on many benchmarks, proving that open models could reach frontier performance with sufficient scale and data.

## Key Takeaways
1. Trained on 15T+ multilingual tokens — a massive increase over Llama 2's 2T
2. 405B dense model competitive with GPT-4 and Claude 3.5 Sonnet on major benchmarks
3. Multimodal extensions: vision encoder, speech adapter, and video understanding added post-pretraining
4. Iterative post-training with DPO, rejection sampling, and synthetic data generation

## Chunk Candidates
- [ ] Training scale (15T tokens, 405B parameters) and infrastructure details
- [ ] Benchmark comparisons with closed-source frontier models
- [ ] Multimodal architecture: composition of vision, speech, and video modules
- [ ] Post-training recipe: DPO, rejection sampling, and synthetic data pipelines
