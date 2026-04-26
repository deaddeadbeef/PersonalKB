---
tags: [raw, llm]
id: "raw-llm-023"
title: "Finetuned Language Models Are Zero-Shot Learners"
author: "Wei et al."
year: 2021
source_type: "paper"
url: "https://arxiv.org/abs/2109.01652"
status: "unprocessed"
chunk_count: 0
up: "[[LLM/Sources/Sources Index]]"
---

# Finetuned Language Models Are Zero-Shot Learners

## What Is This?
Introduces FLAN (Finetuned Language Net), which instruction-tunes a 137B language model on 60+ NLP datasets phrased as natural language instructions, dramatically improving zero-shot performance on unseen tasks.

## Why It Matters
FLAN demonstrated that instruction tuning on diverse tasks creates strong zero-shot generalization, establishing the paradigm that became standard practice (InstructGPT, ChatGPT, and all instruction-following models).

## Key Takeaways
1. Instruction tuning: fine-tune on many tasks described via natural language templates
2. Zero-shot performance on held-out tasks improves substantially (surpassing GPT-3 few-shot on many benchmarks)
3. Benefits increase with number and diversity of instruction-tuning tasks
4. Model scale matters: instruction tuning helps large models most; small models can degrade

## Chunk Candidates
- [ ] Instruction tuning methodology and template design for 60+ tasks
- [ ] Zero-shot generalization results on held-out task clusters
- [ ] Scaling behavior: interaction between model size and instruction tuning benefits
- [ ] Relationship to InstructGPT and the instruction-following paradigm shift
