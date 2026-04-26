---
tags: [chunk, llm]
id: "chunk-llm-032"
source: "[[LLM/_raw/raw-llm-008 Chain-of-Thought Prompting]]"
source_loc: "Section 4, cf. Kojima et al."
topic: "zero-shot CoT"
claim: "Zero-shot CoT ('let's think step by step') works without any examples, though less effectively than few-shot CoT"
confidence: "verified"
supports: ["[[LLM/Prompting and In-Context Learning/Chain-of-Thought Prompting]]"]
up: "[[LLM/LLM]]"
---

# Zero-Shot Chain-of-Thought Prompting

## Context

While the original CoT paper focused on few-shot prompting (providing examples with reasoning traces), Kojima et al. (2022) discovered that simply appending "Let's think step by step" to a prompt — without any examples — triggers chain-of-thought reasoning in large language models. This zero-shot CoT approach is remarkably effective: it improved accuracy on MultiArith from 17.7% to 78.7% with PaLM 540B, without any task-specific examples.

Zero-shot CoT works because large language models have internalized the pattern of step-by-step reasoning from their pre-training data (which contains math solutions, logical arguments, and explanatory texts). The trigger phrase activates this latent pattern, causing the model to decompose the problem into steps. The approach is less effective than few-shot CoT (which provides task-specific reasoning demonstrations) but vastly more practical because it requires no example crafting or prompt engineering for each new task.

## Why It Matters

Zero-shot CoT demonstrated that reasoning capabilities are not just elicited by in-context examples but are genuinely internalized by the model during pre-training. The simplicity of the technique — a single phrase added to any prompt — made it immediately practical and widely adopted. It became the default reasoning elicitation strategy in many applications and influenced the design of instruction-tuned models that are trained to produce reasoning traces by default.

## QnA Seeds
- Q: Why does "let's think step by step" trigger better reasoning?
  A: The phrase matches patterns in the pre-training data where step-by-step solutions follow such introductions (math textbooks, StackExchange answers, tutorials). When the model generates text following this prefix, it enters a "reasoning mode" conditioned on the statistical patterns associated with structured problem-solving text. Essentially, it's a prompt that biases the model's generation toward the distribution of careful, decomposed reasoning.
- Q: When should you use zero-shot CoT vs few-shot CoT?
  A: Use zero-shot CoT when: you need a quick, generalizable approach across many different task types, you don't have good examples to draw from, or you want minimal prompt engineering. Use few-shot CoT when: maximum accuracy matters, you have high-quality reasoning demonstrations for the specific task, or the task has unusual formatting requirements that the model wouldn't infer from a generic prompt. Few-shot CoT typically adds 5–15% accuracy over zero-shot CoT.
