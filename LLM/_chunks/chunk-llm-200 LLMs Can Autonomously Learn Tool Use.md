---
tags: [chunk, llm]
id: "chunk-llm-200"
source: "[[LLM/_raw/raw-llm-050 Toolformer Language Models Can Teach Themselves to Use Tools]]"
source_loc: "Why It Matters"
topic: "Autonomous tool-use learning"
claim: "Toolformer demonstrated that LLMs can autonomously learn when and how to use external tools without human-annotated tool-use examples, a key capability for agentic AI systems."
confidence: "verified"
supports:
  - "[[LLM/2023 — Open Models and Agents/2023 — Open Models and Agents]]"
qna_seeds:
  - "Q: Why is Toolformer's self-supervised approach significant? A: It showed that tool use can be learned from the language modeling objective alone, without the expensive process of having humans annotate when and how to use tools in training data."
  - "Q: How does Toolformer relate to modern agentic AI? A: It was a key early step toward agentic systems — demonstrating that models can learn to augment themselves with external capabilities (search, calculation, translation) by recognizing their own limitations."
up: "[[LLM/LLM]]"
---

# LLMs Can Autonomously Learn Tool Use

Toolformer's demonstration that LLMs can teach themselves to use tools was a foundational result for the development of agentic AI systems. Prior approaches to tool-augmented LLMs required either hand-crafted prompting strategies or expensive human annotation of tool-use examples. Toolformer showed this could be automated through self-supervision, with the model learning both the mechanics of API calls and the judgment of when tools are needed. This influenced subsequent work on function-calling capabilities (OpenAI function calling, Anthropic tool use), ReAct-style agents, and autonomous AI systems that combine language models with external tools and APIs to accomplish complex tasks.
