---
tags: [chunk, llm]
id: "chunk-llm-029"
source: "[[LLM/_raw/raw-llm-008 Chain-of-Thought Prompting]]"
source_loc: "Section 2, Section 3"
topic: "chain-of-thought prompting"
claim: "Including step-by-step reasoning traces in few-shot examples dramatically improves performance on math and reasoning tasks"
confidence: "verified"
supports: ["[[LLM/Prompting and In-Context Learning/Chain-of-Thought Prompting]]"]
up: "[[LLM/LLM]]"
---

# Chain-of-Thought Improves Reasoning Performance

## Context

Wei et al. (2022) demonstrated that simply including step-by-step reasoning in few-shot examples — "chain-of-thought" (CoT) prompting — dramatically improves LLM performance on tasks requiring multi-step reasoning. Instead of providing just input-output pairs as examples, CoT examples include the intermediate reasoning steps. For example, rather than "Q: Roger has 5 balls. He buys 2 cans of 3. A: 11", the example includes "Q: Roger has 5 balls. He buys 2 cans of 3. A: Roger started with 5 balls. 2 cans of 3 balls each is 6 balls. 5 + 6 = 11. The answer is 11."

The gains were most pronounced on math word problems (GSM8K: +20% accuracy), multi-step arithmetic, symbolic reasoning, and commonsense reasoning tasks. The improvement scales with problem complexity — simple single-step problems see little benefit, while multi-step problems that require decomposition see dramatic gains. The key mechanism is that CoT decomposes complex reasoning into manageable intermediate steps that the model can execute more reliably.

## Why It Matters

Chain-of-thought prompting unlocked reasoning capabilities in LLMs without any training or fine-tuning — it's a pure prompting technique. It showed that LLMs have latent reasoning ability that standard prompting fails to elicit. This insight led to a explosion of reasoning-focused techniques (tree-of-thought, self-consistency, reflection) and directly influenced the design of reasoning-focused models like o1 and DeepSeek-R1 that generate CoT traces during inference.

## QnA Seeds
- Q: Why does showing reasoning steps in examples improve the model's reasoning?
  A: Two mechanisms are at play: (1) the examples teach the model the format — that it should show intermediate work rather than jumping to the answer, and (2) generating intermediate steps reduces the effective difficulty of each step. Instead of computing a complex multi-step answer in one forward pass (which the model may lack the capacity to do), it generates one step at a time, with each step conditioned on the previous results.
- Q: Does chain-of-thought always improve performance?
  A: No. CoT provides minimal or no benefit for simple tasks that don't require multi-step reasoning (e.g., sentiment classification, simple fact recall). It also requires sufficient model scale to be effective — at small model sizes, CoT can actually hurt performance because the model generates incoherent intermediate steps that derail the final answer. The benefit is concentrated on complex reasoning tasks with sufficiently large models.
