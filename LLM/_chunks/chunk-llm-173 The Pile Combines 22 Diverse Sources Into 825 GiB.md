---
tags: [chunk, llm]
id: "chunk-llm-173"
source: "[[LLM/_raw/raw-llm-044 The Pile An 800GB Dataset]]"
source_loc: "What Is This, Chunk Candidates"
topic: "Pile dataset composition"
claim: "The Pile is an 825 GiB open-source English pre-training dataset assembled from 22 diverse sources including academic papers, books, code, web crawls, and domain-specific corpora."
confidence: "verified"
supports:
  - "[[LLM/2020–2021 — The Scaling Era/2020–2021 — The Scaling Era]]"
qna_seeds:
  - "Q: What is The Pile? A: An 825 GiB open-source English dataset for LLM pre-training, combining 22 diverse sub-corpora including PubMed, ArXiv, GitHub, Stack Exchange, Books3, Wikipedia, and Common Crawl subsets."
  - "Q: Why was The Pile created? A: To provide a reproducible, high-quality, diverse pre-training dataset that improves on web-only corpora by covering academic, technical, literary, and conversational domains."
up: "[[LLM/LLM]]"
---

# The Pile Combines 22 Diverse Sources Into 825 GiB

The Pile is an 825 GiB English-language dataset created by EleutherAI specifically for large-scale language model pre-training. It aggregates 22 sub-corpora spanning academic papers (PubMed, ArXiv), code (GitHub), books (Books3, Gutenberg), knowledge bases (Wikipedia, Stack Exchange), web text (Common Crawl subsets like OpenWebText2), and specialized sources like USPTO patents and Ubuntu IRC logs. Each source is weighted to balance diversity against quality, with domain-specific corpora intentionally over-represented relative to their raw size. The dataset was released with full documentation of its composition and processing pipeline.
