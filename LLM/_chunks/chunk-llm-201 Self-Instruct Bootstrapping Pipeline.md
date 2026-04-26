---
tags: [chunk, llm]
id: "chunk-llm-201"
source: "[[LLM/_raw/raw-llm-051 Self-Instruct Aligning LMs with Self-Generated Instructions]]"
source_loc: "What Is This, Chunk Candidates"
topic: "self-instruct iterative pipeline"
claim: "Self-Instruct bootstraps instruction-tuning data by iteratively generating tasks, input-output pairs, and filtering from a small seed set."
confidence: "verified"
supports: ["[[LLM/2022 — Alignment and Chat/Instruction Tuning]]"]
qna_seeds:
  - q: "How does the Self-Instruct pipeline generate training data?"
    a: "Starting from a small seed set of human-written tasks, the LLM iteratively generates new task instructions, classifies them, produces input-output instances, and filters low-quality examples before adding them to the training pool."
  - q: "Why is iterative generation important in Self-Instruct?"
    a: "Each round expands the diversity and coverage of instruction types, allowing the model to bootstrap a large, varied instruction-following dataset from only 175 seed tasks."
up: "[[LLM/LLM]]"
---
# Self-Instruct Bootstraps Instruction Data from a Seed Set

Self-Instruct is a framework where a language model iteratively generates its own instruction-following training data. Starting from 175 human-written seed tasks, the model produces new task descriptions, determines whether each task requires input, generates input-output instances, and then filters out low-quality or duplicate examples. This iterative bootstrapping loop creates a large and diverse instruction-tuning dataset without requiring expensive human annotation at scale.

The pipeline's filtering heuristics — including ROUGE-based deduplication against existing tasks and format validation — are critical for maintaining data quality across iterations. The resulting dataset can then be used to fine-tune the same or a different language model for improved instruction following.
