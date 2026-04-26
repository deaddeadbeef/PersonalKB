---
tags: [raw, llm]
id: "raw-llm-024"
title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
author: "Lewis et al."
year: 2020
source_type: "paper"
url: "https://arxiv.org/abs/2005.11401"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

## What Is This?
Proposes RAG, a model that combines a parametric seq2seq generator (BART) with a non-parametric retrieval component (DPR over Wikipedia) to ground generation in retrieved documents.

## Why It Matters
RAG formalized the retrieve-then-generate pattern that became the dominant strategy for reducing hallucination and enabling knowledge-grounded LLM applications in production systems.

## Key Takeaways
1. Architecture: DPR retriever fetches top-k documents → BART generator conditions on retrieved passages
2. Two variants: RAG-Sequence (same document for full sequence) and RAG-Token (different document per token)
3. Retriever and generator are jointly fine-tuned end-to-end via marginalization over retrieved documents
4. State-of-the-art on open-domain QA, fact verification, and knowledge-grounded generation at time of publication

## Chunk Candidates
- [ ] RAG architecture: retriever + generator pipeline with marginalization
- [ ] RAG-Sequence vs RAG-Token generation strategies
- [ ] End-to-end training of retriever and generator
- [ ] Impact on production RAG systems and modern adaptations
