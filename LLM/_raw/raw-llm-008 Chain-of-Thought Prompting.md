---
tags: [raw, llm]
id: "raw-llm-008"
title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
author: "Wei et al."
year: 2022
source_type: "paper"
url: "https://arxiv.org/abs/2201.11903"
status: "processed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

## What Is This?
Showed that including step-by-step reasoning traces in few-shot examples dramatically improves LLM performance on reasoning tasks.

## Why It Matters
Unlocked math, logic, and multi-step reasoning in LLMs without fine-tuning. One of the most impactful prompting techniques.

## Key Takeaways
1. Add "let's think step by step" or show worked examples with reasoning chains
2. Only effective at sufficient scale (>~100B parameters at the time)
3. Decomposes complex reasoning into manageable steps
4. Self-consistency: sample multiple chains, vote on answer

## Chunk Candidates
- [ ] CoT prompting technique and examples
- [ ] Scale dependence of CoT effectiveness
- [ ] Self-consistency improvement
- [ ] Faithfulness of reasoning traces
