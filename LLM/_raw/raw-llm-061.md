---
tags: [llm, raw]
source_type: technical_report
source_title: "Learning to Reason with LLMs"
authors: [OpenAI]
year: 2024
up: "[[Sources Index]]"
---

# OpenAI o1 — Learning to Reason

## Summary

OpenAI released o1-preview and o1-mini in September 2024, introducing reasoning models that allocate additional compute at inference time via extended hidden chain-of-thought. The models generate internal reasoning tokens before producing a final answer, enabling step-by-step problem decomposition and self-verification. On AIME 2024, o1 scored 83.3% compared to GPT-4o's 13.4%. On GPQA Diamond (graduate-level science), o1 reached 78.0%. Its Codeforces rating of 1807 placed it in the 93rd percentile. The o3 and o3-mini models (early 2025) extended the approach with configurable thinking budgets.

## Key Claims

1. Test-time compute scaling is a new axis of capability improvement orthogonal to parameter count
2. Hidden chain-of-thought enables self-correction and multi-step reasoning within a single generation
3. Performance on competition mathematics improved from 13.4% to 83.3% with reasoning
4. Safety can be improved by monitoring the chain-of-thought for harmful reasoning patterns
5. Inference scaling laws predict performance improvement as a function of thinking time

## Atomic Facts

1. o1-preview released September 12, 2024 alongside o1-mini
2. AIME 2024: o1 scored 83.3% vs GPT-4o at 13.4%
3. GPQA Diamond: o1 scored 78.0%
4. Codeforces rating: 1807 (93rd percentile)
5. o3-mini offers low/medium/high reasoning effort settings
6. Reasoning tokens are generated but hidden from the user

## Significance

o1 demonstrated that making models "think harder" at inference time can yield improvements comparable to orders-of-magnitude increases in training compute, opening a new dimension for AI capability improvement.

## Chunks Extracted

*Pending*