---
tags: [chunk, llm]
id: "chunk-llm-097"
source: "[[LLM/_raw/raw-llm-025 ReAct Reasoning and Acting]]"
source_loc: "What Is This, Key Takeaways 1"
topic: "ReAct Thought-Action-Observation loop"
claim: "ReAct interleaves reasoning traces (Thought) with tool calls (Action) and results (Observation), producing more grounded and interpretable agent behavior."
confidence: "verified"
supports: ["[[LLM/Agents and Tool Use/Planning and Task Decomposition]]"]
up: "[[LLM/LLM]]"
---

# ReAct Interleaves Reasoning with Grounded Actions

## Context
ReAct introduced a prompting framework where the language model alternates between three types of outputs in a structured loop: Thought (a free-form reasoning trace where the model plans or interprets information), Action (a tool call such as a search query or environment command), and Observation (the result returned by the tool or environment). This Thought-Action-Observation cycle repeats until the task is complete.

The key insight is that reasoning and acting are synergistic. The Thought step allows the model to plan what action to take and interpret previous observations, while the Action step grounds the model's reasoning in real-world information rather than relying on potentially hallucinated internal knowledge. This produces agents that are both more accurate (grounded in external data) and more interpretable (reasoning traces explain the agent's decisions).

## Why It Matters
ReAct established the fundamental pattern for LLM-powered agents. The Thought-Action-Observation loop provides a natural interface for humans to understand, debug, and audit agent behavior — each step in the chain shows why the agent did what it did. This interpretability is essential for deploying agents in production settings where accountability matters.

## QnA Seeds
- Q: What are the three components of the ReAct loop?
  A: Thought (reasoning trace for planning and interpretation), Action (tool call or environment command), and Observation (result returned from the external tool or environment).
- Q: Why is interleaving reasoning with actions beneficial?
  A: Reasoning without actions risks hallucination; actions without reasoning lack planning. Combining them grounds reasoning in external data while maintaining explicit planning, producing more accurate and interpretable agents.
