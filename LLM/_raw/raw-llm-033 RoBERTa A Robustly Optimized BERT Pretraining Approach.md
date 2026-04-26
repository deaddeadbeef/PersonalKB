---
tags: [raw, llm]
id: "raw-llm-033"
title: "RoBERTa: A Robustly Optimized BERT Pretraining Approach"
author: "Liu et al."
year: 2019
source_type: "paper"
url: "https://arxiv.org/abs/1907.11692"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# RoBERTa: A Robustly Optimized BERT Pretraining Approach

## What Is This?
A replication study showing that BERT was significantly under-trained, and that careful tuning of hyperparameters, training duration, batch size, and data volume yields substantial gains — matching or exceeding XLNet without architectural changes.

## Why It Matters
Demonstrated that training methodology matters as much as model architecture — removing Next Sentence Prediction, training longer on more data, and using dynamic masking all improved performance, becoming the new default for encoder pre-training.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Ablation of BERT's NSP objective and dynamic vs. static masking
- [ ] Impact of batch size, training steps, and data volume on final performance
- [ ] State-of-the-art results on GLUE, SQuAD, and RACE with no architectural changes
