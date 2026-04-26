---
tags: [raw, llm]
id: "raw-llm-035"
title: "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension"
author: "Lewis et al."
year: 2019
source_type: "paper"
url: "https://arxiv.org/abs/1910.13461"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# BART: Denoising Sequence-to-Sequence Pre-training

## What Is This?
A pre-training approach combining a bidirectional encoder (like BERT) with an autoregressive decoder (like GPT), trained by corrupting text with arbitrary noising functions and learning to reconstruct the original.

## Why It Matters
Unified the strengths of encoder-only and decoder-only models in a single encoder-decoder framework, excelling at both generation (summarization, translation) and comprehension tasks — becoming a foundational architecture for seq2seq NLP.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Noising schemes: token masking, deletion, infilling, sentence permutation, document rotation
- [ ] Encoder-decoder architecture combining bidirectional and autoregressive strengths
- [ ] State-of-the-art summarization on CNN/DailyMail and XSum benchmarks
