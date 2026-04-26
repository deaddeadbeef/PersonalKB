---
tags: [chunk, llm]
id: "chunk-llm-007"
source: "[[LLM/_raw/raw-llm-002 GPT-3 Language Models are Few-Shot Learners]]"
source_loc: "Section 3"
topic: "few-shot prompting"
claim: "Few-shot prompting (providing examples in context) outperforms zero-shot across most tasks but the gap narrows with scale"
confidence: "verified"
supports: ["[[LLM/Prompting and In-Context Learning/Few-Shot Prompting]]"]
up: "[[LLM/LLM]]"
---

# Few-Shot Prompting Outperforms Zero-Shot

## Context

GPT-3 was evaluated in three prompting regimes: zero-shot (task description only), one-shot (one example), and few-shot (typically 10–100 examples, limited by context window). Across the majority of benchmarks, few-shot prompting significantly outperformed zero-shot, with one-shot falling in between. The examples in the prompt appeared to help the model disambiguate the task format and calibrate its output distribution.

Interestingly, the gap between zero-shot and few-shot performance narrowed as model size increased. The largest GPT-3 model (175B) in zero-shot mode often outperformed smaller models in the few-shot regime, suggesting that larger models internalize task structure more effectively during pre-training and require fewer in-context demonstrations to activate the right behavior.

## Why It Matters

This finding established the practical hierarchy of prompting strategies that practitioners still use today. It also revealed an important scaling dynamic: at sufficient scale, models may need fewer explicit examples, pointing toward the "instruction following" capability later exploited by InstructGPT and ChatGPT. The gap-narrowing effect also informed the development of zero-shot instruction-tuned models.

## QnA Seeds
- Q: Why does providing a few examples in the prompt improve performance over zero-shot?
  A: Examples serve multiple functions: they disambiguate the task format (e.g., showing the model that Q&A means short answers, not essays), provide implicit constraints on output style, and activate relevant knowledge patterns from pre-training. They essentially anchor the model's probability distribution toward the desired output space.
- Q: Why does the few-shot vs zero-shot gap narrow with larger models?
  A: Larger models internalize more task patterns during pre-training, so they can infer the intended task from a description alone. A small model may need examples to "understand" that a translation task expects target-language output, while a large model recognizes this from the instruction. In effect, larger models are better meta-learners.
