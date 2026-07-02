---
tags: [llm, chunk]
id: chunk-llm-265
source: "[[LLM/_raw/raw-llm-071|raw-llm-071]]"
source_loc: "p. 274"
supports: ["[[LLM/Study/LLM Metrics and Evaluation Interpretation Guide]]", "[[LLM/2023 — Open Models and Agents/LLM-as-Judge]]", "[[LLM/Study/LLM Progressive Systems Route]]"]
confidence: verified
up: "[[LLM/LLM]]"
---

# LLM Evaluation Must Handle Open-Ended Multidimensional Language Outputs

## Context

The evaluation chapter emphasizes that LLM evaluation is harder than classical held-out-label evaluation because model outputs are open-ended, quality has several axes, and judging language output is itself a language-understanding task.

## Claim

Evaluation must be introduced before accepting model, RAG, tool, or agent performance claims. Convenience metrics are not enough when helpfulness, factuality, safety, coherence, latency, and workload fit can diverge.

## Why It Matters

This supports the vault rule that local model and agent claims need proof artifacts: prompt suites, calibration, benchmark rows, human review, and explicit pass/hold/fail decisions.

## QnA Seeds

- Q: Why is one exact-answer metric often insufficient for LLMs? -> A: Many LLM tasks have multiple plausible outputs and several quality axes that may trade off.
- Q: Why can LLM-as-judge be risky? -> A: The judge is also a language model and can share biases, misunderstandings, or failure modes with the model being judged.
