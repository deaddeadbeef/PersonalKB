---
tags: [chunk, llm]
id: "chunk-llm-104"
source: "[[LLM/_raw/raw-llm-026 HELM Holistic Evaluation]]"
source_loc: "Key Takeaways 3, Why It Matters"
topic: "Accuracy vs fairness/robustness trade-offs"
claim: "HELM demonstrated that models can score well on accuracy while performing poorly on fairness or robustness, highlighting the need for multi-dimensional evaluation."
confidence: "verified"
supports: ["[[LLM/Evaluation and Benchmarks/Human Evaluation and Preference Studies]]"]
up: "[[LLM/LLM]]"
---

# Accuracy Can Mask Poor Fairness and Robustness

## Context
HELM's multi-dimensional analysis revealed a troubling pattern: models could achieve high accuracy scores while simultaneously showing significant weaknesses in fairness (varying performance across demographic groups), robustness (degraded performance under input perturbations), or toxicity (generating harmful content in certain contexts). These failures were invisible in traditional accuracy-only evaluations.

For example, a model might correctly answer 85% of questions overall but show a 20-point accuracy gap between questions about different demographic groups. Or a model might perform well on clean inputs but fail catastrophically on slightly rephrased questions. Without HELM's multi-dimensional measurement, these patterns would go undetected until encountered by real users in production.

## Why It Matters
This finding is a direct warning against deploying models based solely on accuracy benchmarks. For any application that affects real people, fairness and robustness must be measured explicitly. HELM's evidence strengthened the case for responsible AI evaluation practices and influenced subsequent benchmark designs to include safety-relevant metrics alongside accuracy.

## QnA Seeds
- Q: What dangerous pattern did HELM reveal about accuracy-focused evaluation?
  A: Models can score well on accuracy while performing poorly on fairness, robustness, or toxicity — failures that are invisible in traditional single-score evaluations.
- Q: Give an example of hidden failure that HELM-style evaluation can catch.
  A: A model with 85% overall accuracy might show a 20-point accuracy gap between demographic groups, or fail catastrophically on slightly rephrased inputs — patterns invisible without multi-dimensional measurement.
