---
tags: [raw, llm]
id: "raw-llm-043"
title: "SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing"
author: "Kudo et al."
year: 2018
source_type: "paper"
url: "https://arxiv.org/abs/1808.06226"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# SentencePiece

## What Is This?
A language-independent subword tokenizer/detokenizer that treats the input as a raw Unicode stream (no pre-tokenization), implementing both BPE and Unigram language model algorithms in a single library.

## Why It Matters
Became the de facto tokenizer for multilingual and open-source LLMs (LLaMA, T5, mBART). Its language-agnostic design and lossless reversibility make it essential for any model that needs to handle arbitrary scripts without language-specific preprocessing.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Raw Unicode stream processing without pre-tokenization assumptions
- [ ] BPE vs. Unigram LM subword algorithms within the SentencePiece framework
- [ ] Lossless detokenization and multilingual vocabulary construction
