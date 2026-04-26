---
tags: [raw, llm]
id: "raw-llm-041"
title: "Layer Normalization"
author: "Ba et al."
year: 2016
source_type: "paper"
url: "https://arxiv.org/abs/1607.06450"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Layer Normalization

## What Is This?
Proposes normalizing across the feature dimension within each training example (rather than across the batch as in BatchNorm), making it naturally suited to recurrent and sequence models where batch statistics are unstable.

## Why It Matters
LayerNorm became a core building block of virtually every Transformer architecture. Its batch-size independence makes it essential for variable-length sequences, and the Pre-LN vs. Post-LN placement debate shaped modern LLM training stability.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] LayerNorm vs. BatchNorm: normalizing across features vs. across batch
- [ ] Invariance properties and why LayerNorm suits variable-length sequences
- [ ] Pre-LN vs. Post-LN placement in Transformers (later work implications)
