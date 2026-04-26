---
tags: [chunk, llm]
id: "chunk-llm-005"
source: "[[LLM/_raw/raw-llm-002 GPT-3 Language Models are Few-Shot Learners]]"
source_loc: "Abstract, Section 1"
topic: "in-context learning"
claim: "GPT-3 (175B params) demonstrated that in-context learning emerges at scale — the model performs tasks from examples in the prompt without weight updates"
confidence: "verified"
supports: ["[[LLM/Prompting and In-Context Learning/Few-Shot Prompting]]"]
up: "[[LLM/LLM]]"
---

# In-Context Learning Emerges at Scale

## Context

GPT-3, a 175-billion parameter autoregressive Transformer, demonstrated a remarkable capability: it could perform a wide range of NLP tasks simply by conditioning on a few examples provided in the prompt, without any gradient updates or fine-tuning. This "in-context learning" was qualitatively different from anything seen at smaller scales — the model appeared to learn the task specification from the prompt alone, leveraging patterns internalized during pre-training.

This capability was evaluated across dozens of tasks including translation, question answering, arithmetic, and commonsense reasoning. While smaller GPT-3 variants (125M–13B) showed limited in-context learning, the 175B model exhibited dramatic improvements, suggesting that in-context learning is an emergent property of sufficient scale rather than a deliberately trained skill.

## Why It Matters

In-context learning fundamentally changed how we interact with language models. Instead of the train-then-deploy paradigm requiring task-specific datasets and fine-tuning, users could specify tasks through natural language prompts. This launched the "prompt engineering" era and made LLMs accessible as general-purpose tools, eventually leading to products like ChatGPT.

## QnA Seeds
- Q: What is in-context learning and how does it differ from fine-tuning?
  A: In-context learning means the model adapts to a task based solely on examples or instructions provided in the prompt, with no changes to the model's weights. Fine-tuning involves gradient-based optimization on task-specific data, permanently updating the model. In-context learning is more flexible but generally less performant than fine-tuning for specialized tasks.
- Q: Why does in-context learning require large model scale?
  A: Smaller models lack the capacity to internalize enough general patterns during pre-training to recognize and adapt to task specifications at inference time. At scale, models develop richer internal representations that can be dynamically repurposed based on context, effectively implementing a form of meta-learning during pre-training.
