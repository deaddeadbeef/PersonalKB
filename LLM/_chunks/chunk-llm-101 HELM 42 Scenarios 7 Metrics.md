---
tags: [chunk, llm]
id: "chunk-llm-101"
source: "[[LLM/_raw/raw-llm-026 HELM Holistic Evaluation]]"
source_loc: "What Is This, Key Takeaways 1-2"
topic: "HELM 42 scenarios and 7 metrics"
claim: "HELM evaluates language models across 42 scenarios and 7 metrics (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency)."
confidence: "verified"
supports: ["[[LLM/Evaluation and Benchmarks/Knowledge and Reasoning Benchmarks]]"]
up: "[[LLM/LLM]]"
---

# HELM Evaluates Across 42 Scenarios and 7 Metrics

## Context
HELM (Holistic Evaluation of Language Models) introduced a comprehensive benchmarking framework with 42 evaluation scenarios spanning question answering, summarization, information retrieval, sentiment analysis, toxicity detection, and more. Each scenario is measured along seven metric categories: accuracy, calibration (confidence alignment with correctness), robustness (performance under perturbation), fairness (performance across demographic groups), bias (stereotypical associations), toxicity (harmful content generation), and efficiency (computational cost).

This multi-dimensional approach was a deliberate response to the prevailing leaderboard culture that ranked models on single accuracy scores. HELM's taxonomy ensures that a model's weaknesses in safety-relevant dimensions cannot be hidden behind strong accuracy numbers, providing a more complete picture of model quality for deployment decisions.

## Why It Matters
HELM transformed LLM evaluation from a single-score competition into a multi-dimensional assessment. For practitioners choosing models for production, HELM's framework provides the structured information needed to make informed trade-off decisions — a model that excels in accuracy but performs poorly on fairness may be unsuitable for certain applications.

## QnA Seeds
- Q: What are the seven metric categories in HELM?
  A: Accuracy, calibration, robustness, fairness, bias, toxicity, and efficiency.
- Q: Why did HELM use 42 scenarios instead of a single benchmark?
  A: To prevent models from being ranked on narrow accuracy alone, ensuring that safety-relevant dimensions (fairness, toxicity, robustness) are systematically measured and cannot be hidden behind strong accuracy scores.
