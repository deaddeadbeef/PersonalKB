---
tags: [raw, llm]
id: "raw-llm-009"
title: "LLaMA: Open and Efficient Foundation Language Models"
author: "Touvron et al."
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2302.13971"
status: "processed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# LLaMA: Open and Efficient Foundation Language Models

## What Is This?
Meta's family of open foundation models (7B-65B) trained on publicly available data, showing open models can match proprietary ones.

## Why It Matters
Sparked the open-source LLM revolution. LLaMA-13B matched GPT-3 (175B). Led to an explosion of fine-tuned variants (Alpaca, Vicuna, etc.).

## Key Takeaways
1. Trained only on publicly available data (1.4T tokens)
2. Applied Chinchilla-optimal training: smaller model, more data
3. LLaMA-13B competitive with GPT-3 175B on most benchmarks
4. Architecture: pre-norm, RoPE, SwiGLU, no bias terms

## Chunk Candidates
- [ ] Training data composition and size
- [ ] Chinchilla-optimal training application
- [ ] Architecture choices (RoPE, SwiGLU, pre-norm)
- [ ] Impact on open-source ecosystem
