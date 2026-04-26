---
tags: [chunk, llm]
id: "chunk-llm-080"
source: "[[LLM/_raw/raw-llm-020 Llama 3 Herd of Models]]"
source_loc: "Key Takeaways 1, 4"
topic: "LLaMA 3 training data mixture"
claim: "LLaMA 3's training data included code, multilingual text, and math data mixed at carefully tuned proportions."
confidence: "verified"
supports: ["[[LLM/Pretraining/Data Curation and Deduplication]]"]
up: "[[LLM/LLM]]"
---

# LLaMA 3 Training Data Composition

## Context
LLaMA 3's 15T+ token training dataset was a carefully curated mixture of multiple data sources: web crawl text (the majority), code from public repositories, multilingual text across dozens of languages, mathematical text and problem sets, and scientific papers. The proportions of each data type were not fixed but tuned through ablation experiments — Meta adjusted the data mix based on downstream evaluation performance, treating data composition as a hyperparameter to optimize.

The data curation pipeline involved extensive filtering: quality classifiers trained on high-quality reference text, deduplication at both the document and near-duplicate level, safety filtering to remove harmful content, and domain-specific processing (e.g., preserving code formatting and mathematical notation). The multilingual component was deliberately expanded compared to LLaMA 2, which was predominantly English, reflecting the goal of building a globally useful model.

## Why It Matters
LLaMA 3's data engineering demonstrates that at frontier scale, data curation is as important as model architecture or training algorithms. The careful tuning of data mix proportions — treating them as hyperparameters rather than fixed ratios — represents a maturation of the field's understanding that what you train on matters as much as how you train. This data-centric approach has become the standard for all competitive LLM training efforts.

## QnA Seeds
- Q: What types of data were included in LLaMA 3's training mixture?
  A: Web crawl text (majority), code from public repositories, multilingual text across dozens of languages, mathematical text and problems, and scientific papers. The proportions were tuned through ablation experiments optimizing downstream performance.
- Q: How did LLaMA 3's data curation pipeline ensure quality?
  A: Multiple stages: quality classifiers trained on reference text, document-level and near-duplicate deduplication, safety filtering, and domain-specific processing (preserving code formatting, math notation). Data mix proportions were treated as hyperparameters and optimized through evaluation-driven ablations.
