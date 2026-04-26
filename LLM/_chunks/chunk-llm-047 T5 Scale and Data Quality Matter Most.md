---
tags: [chunk, llm]
id: "chunk-llm-047"
source: "[[LLM/_raw/raw-llm-012 T5 Unified Text-to-Text Transformer]]"
source_loc: "Key Takeaways 2, 4"
topic: "T5 systematic comparison findings"
claim: "T5's systematic comparison of pretraining objectives, architectures, and data showed that scale and data quality matter most."
confidence: "verified"
supports: ["[[LLM/Pretraining/Scaling Laws]]"]
up: "[[LLM/LLM]]"
---

# T5 Scale and Data Quality Matter Most

## Context
The T5 paper is as much an empirical study as a model contribution. The authors systematically varied pretraining objectives (language modeling, BERT-style, span corruption, prefix LM), model architectures (encoder-decoder, decoder-only, prefix LM), unsupervised data sources (C4 variants with different filtering), fine-tuning strategies (multi-task, gradual unfreezing), and model sizes (from 60M to 11B parameters).

The headline finding was that while all these choices matter at the margin, the two factors with the largest impact were model scale (bigger models consistently outperform smaller ones given sufficient data) and data quality (careful filtering of the pretraining corpus yielded better results than using more but noisier data). This motivated the creation of the Colossal Clean Crawled Corpus (C4), which applied heuristic filtering to Common Crawl.

## Why It Matters
T5's empirical methodology set a standard for rigorous comparison in the field and validated the emerging intuition that scale and data quality dominate architectural tweaks. These findings foreshadowed the scaling laws work and the later emphasis on data curation (e.g., LLaMA, Llama 3), cementing the principle that getting scale and data right is more impactful than clever architectural modifications.

## QnA Seeds
- Q: What was the main finding from T5's systematic comparison of pretraining configurations?
  A: Scale (larger models) and data quality (careful filtering of pretraining data) had the largest impact on downstream performance. While the choice of pretraining objective and architecture mattered, the gains from scaling and cleaner data consistently dominated those from architectural or objective changes.
- Q: What is C4 and why was it created for T5?
  A: C4 (Colossal Clean Crawled Corpus) is a cleaned version of Common Crawl created for T5 pretraining. It applies heuristic filters (removing duplicates, short pages, offensive content, and code) to improve data quality, reflecting T5's finding that cleaner data yields better downstream performance.
