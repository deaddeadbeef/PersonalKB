---
tags: [llm, chunk]
source: "[[raw-llm-032]]"
confidence: high
supports:
  - "[[LLM/2018–2019 — Pretrained Language Models/Data Curation and Deduplication]]"
qna_seeds:
  - "Q: What was the WebText dataset and how was it curated? A: WebText was a 40 GB dataset of web pages linked from Reddit posts with at least 3 karma, used to train GPT-2. This social-signal filtering produced higher-quality training data than undifferentiated web scrapes."
---

# WebText Dataset Quality Filtering via Social Signals

GPT-2 was trained on WebText, a ~40 GB dataset of web pages sourced by scraping all outbound links from Reddit posts that received at least 3 karma (upvotes). This social-signal-based filtering strategy produced a substantially higher-quality corpus than undifferentiated Common Crawl scrapes, without manual curation. The WebText approach demonstrated that data quality — not just quantity — is a critical training variable, influencing later curation strategies like those used for The Pile and RedPajama.