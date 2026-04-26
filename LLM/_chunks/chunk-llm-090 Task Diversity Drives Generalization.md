---
tags: [chunk, llm]
id: "chunk-llm-090"
source: "[[LLM/_raw/raw-llm-023 FLAN Instruction Tuning Zero-Shot]]"
source_loc: "Key Takeaways 3"
topic: "Task diversity improves generalization"
claim: "Instruction tuning benefits from task diversity — more different tasks in training leads to better generalization."
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/Instruction Tuning]]"]
up: "[[LLM/LLM]]"
---

# Task Diversity Drives Instruction Tuning Generalization

## Context
FLAN's ablation studies systematically varied the number and diversity of instruction-tuning tasks to measure their impact on zero-shot generalization. The results showed a clear positive relationship: as more task clusters were added to the instruction-tuning mixture, zero-shot performance on held-out tasks improved monotonically. This held across different held-out task types and model sizes.

The diversity dimension was particularly important — adding tasks from new categories (e.g., adding NLI tasks to a mixture that already includes QA and summarization) produced larger gains than adding more tasks from already-represented categories. This suggests that instruction tuning benefits from breadth of task coverage more than depth within any single task type.

## Why It Matters
This finding directly shaped how the community constructs instruction-tuning datasets. Modern datasets like FLAN v2, Super-NaturalInstructions, and the Open Assistant corpus deliberately maximize task diversity, knowing that breadth of coverage is the key driver of generalizable instruction-following ability.

## QnA Seeds
- Q: How does task diversity affect instruction tuning quality?
  A: More diverse tasks in the instruction-tuning mixture lead to better zero-shot generalization on unseen tasks, with diversity across task categories mattering more than depth within any single category.
- Q: What evidence supports the task diversity finding?
  A: FLAN's ablation studies showed monotonic improvement in held-out task performance as more task clusters were added to training, across different held-out types and model sizes.
