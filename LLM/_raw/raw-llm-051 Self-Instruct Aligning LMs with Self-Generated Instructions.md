---
tags: [raw, llm]
id: "raw-llm-051"
title: "Self-Instruct: Aligning Language Models with Self-Generated Instructions"
author: "Wang et al."
year: 2022
source_type: "paper"
url: "https://arxiv.org/abs/2212.10560"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Self-Instruct: Aligning LMs with Self-Generated Instructions

## What Is This?
A framework where a language model generates its own instruction-following training data by iteratively producing tasks, input-output pairs, and filtering for quality — bootstrapping instruction tuning from a small seed set.

## Why It Matters
Enabled cheap instruction tuning without expensive human annotation, directly inspiring Alpaca and the wave of open-source instruction-tuned models. Showed that LLMs can bootstrap their own alignment data, fundamentally changing the cost equation for fine-tuning.

## Key Takeaways
1. 
2. 
3. 

## Chunk Candidates
- [ ] Iterative self-instruction pipeline: seed tasks → generation → filtering → fine-tuning
- [ ] Quality filtering heuristics for self-generated instruction-output pairs
- [ ] GPT-3 Self-Instruct vs. InstructGPT comparison and downstream Alpaca lineage
