---
tags: [raw, llm]
id: "raw-llm-057"
title: "Dense Passage Retrieval for Open-Domain Question Answering"
author: "Karpukhin et al."
year: 2020
source_type: "paper"
url: "https://arxiv.org/abs/2004.04906"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Dense Passage Retrieval (DPR)

## What Is This?
Trains dual BERT encoders (question encoder + passage encoder) to produce dense vector representations for retrieval, replacing traditional sparse methods (BM25/TF-IDF) for open-domain question answering.

## Why It Matters
Demonstrated that learned dense retrieval significantly outperforms BM25 for knowledge-intensive QA, becoming the retrieval backbone for RAG systems. DPR's dual-encoder architecture became the standard pattern for semantic search and retrieval-augmented generation.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Dual-encoder architecture: question and passage encoders with dot-product similarity
- [ ] In-batch negatives and hard negative mining for contrastive training
- [ ] DPR vs. BM25 retrieval accuracy on Natural Questions, TriviaQA, and WebQuestions
