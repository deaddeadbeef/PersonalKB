---
tags: [chunk, llm]
id: "chunk-llm-092"
source: "[[LLM/_raw/raw-llm-023 FLAN Instruction Tuning Zero-Shot]]"
source_loc: "Why It Matters, Key Takeaways 1"
topic: "Instruction tuning bridges pretraining to instruction following"
claim: "Instruction tuning bridges the gap between base model pretraining and the ability to follow natural language instructions."
confidence: "verified"
supports: ["[[LLM/Fine-Tuning and Adaptation/Supervised Fine-Tuning]]"]
up: "[[LLM/LLM]]"
---

# Instruction Tuning Bridges Pretraining to Instruction Following

## Context
Base language models trained with next-token prediction learn rich linguistic and world knowledge but lack the ability to reliably follow user instructions. They tend to continue text in the style of their training data rather than responding to requests. FLAN demonstrated that a relatively small amount of supervised instruction tuning — fine-tuning on tasks phrased as natural language instructions — fundamentally changes the model's behavior from "text continuation" to "instruction following."

This bridging role is distinct from both pretraining (which provides knowledge and capability) and RLHF (which refines style and safety). Instruction tuning specifically teaches the model the format and pragmatics of following instructions: understand what is being asked, produce the requested output type, and stop when the task is complete. The FLAN paradigm established this as a necessary intermediate step in the LLM training pipeline.

## Why It Matters
Instruction tuning created the practical foundation for all modern chat and assistant models. Without it, even the most powerful base models remain difficult to use interactively. It is the step that transforms a language model from a research artifact into a usable tool, and every production LLM pipeline now includes this stage.

## QnA Seeds
- Q: What gap does instruction tuning bridge in LLM development?
  A: It bridges the gap between base models (which do text continuation) and usable assistants (which follow natural language instructions), teaching the model the format and pragmatics of instruction following.
- Q: How does instruction tuning differ from RLHF in purpose?
  A: Instruction tuning teaches the model to follow instructions and produce requested output types, while RLHF refines style, helpfulness, and safety preferences on top of that instruction-following capability.
