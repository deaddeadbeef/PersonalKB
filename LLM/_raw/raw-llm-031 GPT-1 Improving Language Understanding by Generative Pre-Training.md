---
tags: [raw, llm]
id: "raw-llm-031"
title: "Improving Language Understanding by Generative Pre-Training"
author: "Radford et al."
year: 2018
source_type: "paper"
url: "https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# GPT-1: Improving Language Understanding by Generative Pre-Training

## What Is This?
The original GPT paper introducing generative pre-training on unlabeled text followed by discriminative fine-tuning on downstream tasks. Demonstrated that a single unsupervised language model could be adapted to a wide range of NLP benchmarks.

## Why It Matters
Established the pre-train → fine-tune paradigm that became the default recipe for NLP. Showed that generative (left-to-right) objectives transfer effectively, setting the stage for GPT-2, GPT-3, and the entire decoder-only lineage.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Pre-train → fine-tune paradigm and task-specific input transformations
- [ ] 12-layer Transformer decoder architecture and BPE tokenization
- [ ] Benchmark gains on 9 of 12 NLP tasks over discriminative baselines
