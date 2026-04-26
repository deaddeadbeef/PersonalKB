---
tags: [raw, llm]
id: "raw-llm-012"
title: "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"
author: "Raffel et al."
year: 2019
source_type: "paper"
url: "https://arxiv.org/abs/1910.10683"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer

## What Is This?
Proposes T5, which frames every NLP task as a text-to-text problem and conducts a systematic study of transfer learning strategies, model architectures, pre-training objectives, and dataset sizes.

## Why It Matters
T5 provided the most comprehensive empirical comparison of pre-training choices at the time, established the text-to-text paradigm, and introduced the C4 dataset that became a community standard.

## Key Takeaways
1. All tasks (classification, translation, summarization) cast as text-in → text-out with task-specific prefixes
2. Encoder-decoder architecture outperformed decoder-only and prefix-LM variants in their ablations
3. Span corruption pre-training objective (replace spans with sentinel tokens) was most effective
4. Scaling model size and data together yields consistent improvements across benchmarks

## Chunk Candidates
- [ ] Text-to-text framing and task prefix design
- [ ] Systematic comparison of pre-training objectives (LM, prefix-LM, span corruption)
- [ ] C4 dataset construction and filtering decisions
- [ ] Encoder-decoder vs decoder-only architecture trade-offs
