---
tags: [raw, llm]
id: "raw-llm-003"
title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
author: "Devlin et al."
year: 2018
source_type: "paper"
url: "https://arxiv.org/abs/1810.04805"
status: "processed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# BERT: Pre-training of Deep Bidirectional Transformers

## What Is This?
Introduced masked language modeling for bidirectional pre-training, establishing the pre-train then fine-tune paradigm.

## Why It Matters
Dominated NLP benchmarks for years. Established that bidirectional context dramatically improves language understanding. The encoder-only architecture branch.

## Key Takeaways
1. Masked Language Modeling (MLM): randomly mask 15% of tokens, predict them
2. Next Sentence Prediction (NSP) as auxiliary task (later shown unnecessary by RoBERTa)
3. [CLS] token for classification tasks
4. BERT-base (110M) and BERT-large (340M) variants

## Chunk Candidates
- [ ] Masked language modeling design and masking strategy
- [ ] Pre-train then fine-tune paradigm
- [ ] Bidirectional vs unidirectional context comparison
- [ ] Impact on NLP benchmarks
