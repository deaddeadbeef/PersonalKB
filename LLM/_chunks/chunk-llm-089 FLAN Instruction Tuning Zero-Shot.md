---
tags: [chunk, llm]
id: "chunk-llm-089"
source: "[[LLM/_raw/raw-llm-023 FLAN Instruction Tuning Zero-Shot]]"
source_loc: "What Is This, Key Takeaways 1-2"
topic: "FLAN instruction tuning for zero-shot"
claim: "FLAN showed that instruction tuning on diverse tasks enables strong zero-shot performance on unseen tasks."
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/Instruction Tuning]]"]
up: "[[LLM/LLM]]"
---

# FLAN Instruction Tuning Enables Zero-Shot Generalization

## Context
FLAN (Finetuned Language Net) instruction-tuned a 137B parameter language model on over 60 NLP datasets, each reformulated as natural language instructions with templates. Tasks spanned sentiment analysis, translation, question answering, summarization, and more. The key experiment held out entire task clusters during training and measured zero-shot performance on those unseen task types.

The results were striking: FLAN substantially outperformed the untuned base model on held-out tasks and even surpassed GPT-3's few-shot performance on many benchmarks — despite using zero examples at inference time. This demonstrated that instruction tuning doesn't just improve performance on trained tasks but creates a general capacity to follow novel instructions.

## Why It Matters
FLAN established instruction tuning as the standard paradigm for making language models useful. Every major instruction-following model since — InstructGPT, ChatGPT, Claude, Llama-Chat — builds on this finding that diverse instruction tuning creates generalizable instruction-following ability, not just task-specific improvement.

## QnA Seeds
- Q: What did FLAN demonstrate about instruction tuning and zero-shot performance?
  A: That instruction-tuning a model on 60+ diverse tasks with natural language templates substantially improves zero-shot performance on entirely unseen task types, even surpassing GPT-3's few-shot results.
- Q: How was zero-shot generalization measured in FLAN?
  A: By holding out entire task clusters during instruction tuning and evaluating the model's performance on those unseen task types with zero examples.
