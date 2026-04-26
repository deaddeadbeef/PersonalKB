---
tags: [chunk, llm]
id: "chunk-llm-100"
source: "[[LLM/_raw/raw-llm-025 ReAct Reasoning and Acting]]"
source_loc: "Why It Matters, Chunk Candidates"
topic: "ReAct as foundation for agent frameworks"
claim: "ReAct became the foundational pattern for LLM agent frameworks (LangChain, LlamaIndex agents, AutoGPT)."
confidence: "verified"
supports: ["[[LLM/Agents and Tool Use/Planning and Task Decomposition]]"]
up: "[[LLM/LLM]]"
---

# ReAct Is the Foundation for LLM Agent Frameworks

## Context
The ReAct paper's Thought-Action-Observation loop became the standard architecture for virtually all LLM agent frameworks that followed. LangChain's original agent implementation directly mirrors ReAct's structure, with the model generating reasoning traces, selecting tools, and processing results in a loop. LlamaIndex agents, AutoGPT, BabyAGI, and Microsoft's Semantic Kernel all adopted variations of this pattern.

The pattern's success comes from its simplicity and generality: any task that requires a model to interact with external systems — search engines, databases, APIs, code interpreters, or physical environments — can be structured as a ReAct loop. The framework is agnostic to the specific tools available, making it composable and extensible. New tools can be added by simply describing them in the prompt without changing the agent architecture.

## Why It Matters
ReAct's influence extends far beyond academic benchmarks — it defined how the entire industry builds AI agents. Understanding ReAct is essential for working with any modern agent framework, and its design principles (explicit reasoning, grounded actions, observable state) continue to guide the development of more sophisticated multi-agent and planning systems.

## QnA Seeds
- Q: Which major agent frameworks are based on the ReAct pattern?
  A: LangChain, LlamaIndex agents, AutoGPT, BabyAGI, and Microsoft Semantic Kernel all implement variations of ReAct's Thought-Action-Observation loop.
- Q: Why did ReAct become so widely adopted as an agent pattern?
  A: Its simplicity and generality — any task involving external tool interaction can be structured as a ReAct loop, and new tools can be added via prompt descriptions without architectural changes.
