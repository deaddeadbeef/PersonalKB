---
tags: [raw, llm]
id: "raw-llm-034"
title: "DeBERTa: Decoding-enhanced BERT with Disentangled Attention"
author: "He et al."
year: 2020
source_type: "paper"
url: "https://arxiv.org/abs/2006.03654"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# DeBERTa: Decoding-enhanced BERT with Disentangled Attention

## What Is This?
Introduces disentangled attention that separates content and position representations into two vectors and computes attention using disentangled matrices, plus an enhanced mask decoder for pre-training.

## Why It Matters
First model to surpass human performance on the SuperGLUE benchmark. The disentangled attention mechanism improves how position information interacts with content, yielding better representations especially for tasks requiring fine-grained positional reasoning.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Disentangled attention: content-to-content, content-to-position, position-to-content matrices
- [ ] Enhanced mask decoder with absolute position in decoding layer
- [ ] SuperGLUE human-parity results and downstream fine-tuning recipe
