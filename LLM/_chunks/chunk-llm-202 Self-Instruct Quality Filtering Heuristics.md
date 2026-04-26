---
tags: [chunk, llm]
id: "chunk-llm-202"
source: "[[LLM/_raw/raw-llm-051 Self-Instruct Aligning LMs with Self-Generated Instructions]]"
source_loc: "Chunk Candidates"
topic: "self-instruct filtering heuristics"
claim: "Self-Instruct applies ROUGE-based deduplication, length filtering, and keyword heuristics to maintain quality of self-generated instruction data."
confidence: "verified"
supports: ["[[LLM/2022 — Alignment and Chat/Instruction Tuning]]"]
qna_seeds:
  - q: "What quality filters does Self-Instruct use on generated data?"
    a: "ROUGE-L similarity against existing tasks for deduplication, length constraints on instructions and outputs, and keyword heuristics to reject degenerate or overly simple generations."
  - q: "Why is filtering essential in Self-Instruct?"
    a: "Without filtering, the iterative generation loop would accumulate duplicates, trivial tasks, and malformed outputs that degrade the fine-tuned model's quality."
up: "[[LLM/LLM]]"
---
# Self-Instruct Relies on Quality Filtering Heuristics

The Self-Instruct pipeline applies multiple filtering stages to ensure generated instruction-output pairs maintain sufficient quality. ROUGE-L similarity is computed against the existing task pool to reject near-duplicates, ensuring diversity across the growing dataset. Length-based filters remove instructions that are too short (likely trivial) or too long (likely degenerate), and keyword heuristics catch common failure patterns such as self-referential instructions.

These heuristics are essential because LLM-generated data naturally contains repetition and low-quality samples. The filtering step is what makes the bootstrapping loop viable — without it, noise would compound across iterations and the resulting fine-tuned model would inherit systematic biases from degenerate training examples.
