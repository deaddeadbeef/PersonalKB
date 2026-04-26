---
tags: [raw, llm]
id: "raw-llm-001"
title: "Attention Is All You Need"
author: "Vaswani et al."
year: 2017
source_type: "paper"
url: "https://arxiv.org/abs/1706.03762"
status: "processed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Attention Is All You Need

## What Is This?
The paper that introduced the Transformer architecture, replacing recurrence and convolutions with pure self-attention for sequence-to-sequence tasks.

## Why It Matters
Foundation of all modern LLMs. Every GPT, BERT, LLaMA, Claude, and Gemini model is a descendant of this architecture.

## Key Takeaways
1. Self-attention allows modeling dependencies regardless of distance in the sequence
2. Multi-head attention lets the model attend to information from different representation subspaces
3. Positional encoding is needed because attention is permutation-invariant
4. The encoder-decoder structure with residual connections and layer normalization became the template

## Chunk Candidates
- [ ] Scaled dot-product attention formula and intuition
- [ ] Multi-head attention mechanism
- [ ] Positional encoding design choices
- [ ] Why self-attention beats recurrence (parallelism, path length)
