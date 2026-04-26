---
tags: [raw, llm]
id: "raw-llm-042"
title: "Train Short, Test Long: Attention with Linear Biases Enables Input Length Generalization"
author: "Press et al."
year: 2021
source_type: "paper"
url: "https://arxiv.org/abs/2108.12409"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# ALiBi: Train Short, Test Long

## What Is This?
Replaces learned or sinusoidal position embeddings with a simple linear bias added to attention scores, penalizing attention proportionally to key-query distance. Enables extrapolation to sequence lengths far beyond those seen during training.

## Why It Matters
Solved a key limitation of absolute position embeddings — poor generalization to longer sequences at inference. ALiBi's simplicity (no extra parameters, trivial to implement) made it a practical alternative to RoPE for length extrapolation.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Linear bias mechanism: slope-based distance penalty per attention head
- [ ] Length extrapolation: training on 1K tokens, testing on 2K+ without degradation
- [ ] Comparison with sinusoidal, learned, rotary, and relative position encodings
