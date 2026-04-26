---
tags: [chunk, llm]
id: "chunk-llm-115"
source: "[[LLM/_raw/raw-llm-029 Survey of Large Language Models]]"
source_loc: "Key Takeaways, Chunk Candidates"
topic: "Three open challenges in LLM research"
claim: "The survey identifies data quality, alignment stability, and evaluation methodology as the three main open challenges in LLM research."
confidence: "verified"
supports: ["[[LLM/Evaluation and Benchmarks/Contamination and Data Leakage]]"]
up: "[[LLM/LLM]]"
---

# Three Open Challenges: Data Quality, Alignment, Evaluation

## Context
Zhao et al.'s survey synthesizes the open challenges facing LLM research into three primary areas. First, data quality: as models consume ever-larger training corpora, ensuring data diversity, deduplication, decontamination, and appropriate mixing remains a major unsolved problem. Low-quality or contaminated data directly degrades model performance and can compromise evaluation validity. Second, alignment stability: RLHF and related methods can be brittle — reward hacking, mode collapse, and catastrophic forgetting during alignment training are recurring issues without robust solutions. Third, evaluation methodology: existing benchmarks suffer from contamination (training data overlap), saturation (models approach ceiling scores), and narrow coverage, making it increasingly difficult to meaningfully measure progress.

These three challenges are interconnected: poor data quality contaminates evaluation benchmarks, unstable alignment makes evaluation results inconsistent, and inadequate evaluation makes it hard to assess whether data and alignment improvements are working.

## Why It Matters
Understanding these open challenges provides a roadmap for LLM research priorities. For practitioners, awareness of data contamination and evaluation limitations is critical for making sound model selection decisions. For researchers, these challenges represent the highest-impact areas where progress would benefit the entire field.

## QnA Seeds
- Q: What three open challenges does the LLM survey identify?
  A: Data quality (diversity, deduplication, decontamination at scale), alignment stability (reward hacking, mode collapse, catastrophic forgetting), and evaluation methodology (contamination, saturation, narrow coverage).
- Q: How are the three challenges interconnected?
  A: Poor data contaminates benchmarks, unstable alignment produces inconsistent evaluation results, and inadequate evaluation makes it hard to assess whether data and alignment improvements are actually working.
