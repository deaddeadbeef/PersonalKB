---
tags: [raw, llm]
id: "raw-llm-017"
title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
author: "Gu & Dao"
year: 2023
source_type: "paper"
url: "https://arxiv.org/abs/2312.00752"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Mamba: Linear-Time Sequence Modeling with Selective State Spaces

## What Is This?
A selective state space model (SSM) that makes SSM parameters input-dependent, enabling content-based reasoning with linear-time complexity and no attention mechanism.

## Why It Matters
Mamba challenged the dominance of transformers by matching or exceeding their quality at language modeling while scaling linearly in sequence length, reigniting research into attention-free architectures.

## Key Takeaways
1. Makes SSM discretization parameters (Δ, B, C) input-dependent ("selective"), allowing content-based filtering
2. Hardware-aware parallel scan implementation avoids materializing expanded state for GPU efficiency
3. Linear-time and constant-memory inference (no KV cache), enabling very long sequences
4. Matches Transformer quality at 1-3B scale on language modeling with 5× higher throughput at long lengths

## Chunk Candidates
- [ ] Selective state space mechanism (input-dependent Δ, B, C)
- [ ] Hardware-aware parallel scan algorithm
- [ ] Comparison with Transformers on language modeling benchmarks
- [ ] Implications for KV-cache-free inference and long-context scaling
