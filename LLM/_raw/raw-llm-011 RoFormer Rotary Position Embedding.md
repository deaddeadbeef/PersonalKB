---
tags: [raw, llm]
id: "raw-llm-011"
title: "RoFormer: Enhanced Transformer with Rotary Position Embedding"
author: "Su et al."
year: 2021
source_type: "paper"
url: "https://arxiv.org/abs/2104.09864"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# RoFormer: Enhanced Transformer with Rotary Position Embedding

## What Is This?
Introduces Rotary Position Embedding (RoPE), which encodes absolute position with a rotation matrix and naturally incorporates relative position information into self-attention.

## Why It Matters
RoPE became the dominant positional encoding in modern LLMs (LLaMA, PaLM, etc.) because it decays with relative distance, supports length extrapolation, and is simple to implement.

## Key Takeaways
1. Positions are encoded by rotating query/key vectors by angle θ proportional to position index
2. Inner product of rotated vectors depends only on relative distance, giving built-in relative encoding
3. Decaying inter-token dependency with increasing distance emerges naturally
4. Compatible with linear attention kernels and easily extended via NTK-aware scaling for longer contexts

## Chunk Candidates
- [ ] RoPE mathematical formulation (rotation matrices on query/key pairs)
- [ ] Comparison with absolute, relative, and ALiBi positional encodings
- [ ] Length extrapolation properties and NTK-aware scaling
- [ ] Adoption in modern architectures (LLaMA, PaLM, Mistral)
