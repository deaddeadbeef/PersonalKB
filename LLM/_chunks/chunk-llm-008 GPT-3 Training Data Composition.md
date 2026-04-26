---
tags: [chunk, llm]
id: "chunk-llm-008"
source: "[[LLM/_raw/raw-llm-002 GPT-3 Language Models are Few-Shot Learners]]"
source_loc: "Section 2.2"
topic: "data curation"
claim: "GPT-3 was trained on 300B tokens from a filtered Common Crawl mixture plus books, Wikipedia, and WebText2"
confidence: "verified"
supports: ["[[LLM/Pretraining/Data Curation and Deduplication]]"]
up: "[[LLM/LLM]]"
---

# GPT-3 Training Data Composition

## Context

GPT-3's training corpus comprised approximately 300 billion tokens drawn from five sources with different sampling weights: filtered Common Crawl (410B tokens, sampled at 60%), WebText2 (19B tokens, sampled at 22%), two books corpora (Books1 and Books2, totaling ~67B tokens, sampled at ~16%), and English Wikipedia (3B tokens, sampled at ~3%). The sampling weights intentionally over-sampled higher-quality sources relative to their size — Wikipedia and books were seen multiple times during training while most of Common Crawl was seen less than once.

The Common Crawl data underwent significant filtering: a binary classifier trained on WebText (the curated data from GPT-2) was used to select high-quality pages, and fuzzy deduplication was applied to remove near-duplicate documents. This quality filtering reduced the usable Common Crawl data from petabytes of raw crawl to hundreds of billions of curated tokens.

## Why It Matters

GPT-3's data composition established key principles still followed today: diverse sources, quality filtering of web crawl data, strategic oversampling of high-quality corpora, and deduplication. The decision to mix broad web data with curated sources (books, Wikipedia) set the template for subsequent training data recipes in PaLM, LLaMA, and other large-scale models.

## QnA Seeds
- Q: Why did GPT-3 oversample smaller, high-quality datasets like Wikipedia?
  A: Oversampling high-quality sources increases the model's exposure to well-structured, factual, and diverse language during training. Even though Wikipedia is only 3B tokens (tiny compared to Common Crawl), its high information density and consistent quality make multiple passes worthwhile. This improves the model's factual knowledge and writing quality.
- Q: How was Common Crawl filtered for GPT-3 training?
  A: A logistic regression classifier was trained to distinguish WebText (curated, high-quality web pages) from raw Common Crawl. This classifier scored each Common Crawl document, and only high-scoring pages were retained. Additionally, fuzzy deduplication using MinHash was applied to remove near-duplicate content, reducing data redundancy.
