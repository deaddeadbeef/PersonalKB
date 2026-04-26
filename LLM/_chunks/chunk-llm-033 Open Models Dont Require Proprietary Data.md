---
tags: [chunk, llm]
id: "chunk-llm-033"
source: "[[LLM/_raw/raw-llm-009 LLaMA Open Foundation Language Models]]"
source_loc: "Section 2"
topic: "open-weight models"
claim: "LLaMA trained only on publicly available data (1.4T tokens), proving competitive open models don't require proprietary data"
confidence: "verified"
supports: ["[[LLM/History and Landscape/Open-Weight Model Ecosystem]]"]
up: "[[LLM/LLM]]"
---

# Open Models Don't Require Proprietary Data

## Context

LLaMA was trained exclusively on publicly available data sources: English CommonCrawl (67%), C4 (15%), GitHub (4.5%), Wikipedia (4.5%), Books (4.5%), ArXiv (2.5%), and StackExchange (2%). Totaling approximately 1.4 trillion tokens, this dataset was assembled entirely from sources that any research group could access. No proprietary data from user interactions, internal company documents, or commercially licensed datasets was used.

This was a deliberate strategic choice by Meta. Prior state-of-the-art models like GPT-3 used curated web data (WebText from Reddit links), Chinchilla used MassiveText (internal to DeepMind), and PaLM used a proprietary data mixture. The prevailing assumption was that proprietary data advantages were necessary for frontier performance. LLaMA disproved this: its models were competitive with or exceeded proprietary-data models at equivalent sizes, demonstrating that careful curation and sufficient quantity of public data is enough.

## Why It Matters

By proving that publicly available data suffices for competitive models, LLaMA removed the most significant barrier to open LLM development. Previously, the combination of compute costs and proprietary data gave only a handful of companies the ability to train competitive models. LLaMA showed that with enough care in data curation and the right training recipe, any well-resourced research group could build frontier models from publicly accessible data.

## QnA Seeds
- Q: How did LLaMA achieve competitive results without proprietary data?
  A: Three factors: (1) sufficient data quantity — 1.4T tokens is enough to Chinchilla-optimally train models up to 70B parameters; (2) careful data curation — aggressive quality filtering, deduplication, and source balancing ensured high data quality; (3) more training compute per parameter than competitors — by training smaller models longer than Kaplan-optimal (following Chinchilla recommendations), LLaMA extracted maximum value from each parameter.
- Q: What are the limitations of training exclusively on public data?
  A: Public data has known biases and quality issues: it over-represents English and certain internet communities, contains factual errors and outdated information, and may lack coverage of specialized or proprietary domains. Some tasks (medical, legal, code from private repos) may benefit from proprietary data that public sources can't match. Additionally, public data is increasingly contaminated with LLM-generated content, creating concerns about model collapse in future training runs.
