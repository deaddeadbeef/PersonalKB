---
tags: [llm, chunk]
id: chunk-llm-266
source: "[[LLM/_raw/raw-llm-071|raw-llm-071]]"
source_loc: "p. 292"
supports: ["[[LLM/2026 — Reasoning and Agents/Agentic Coding Systems]]", "[[LLM/2024–2025 — Frontier and Efficiency/Memory and State Management]]", "[[LLM/Study/LLM Progressive Systems Route]]"]
confidence: verified
up: "[[LLM/LLM]]"
---

# Agentic AI Is An Observation Reason Action Loop With Memory Grounding Action And Safety

## Context

The agentic AI chapter defines an agentic system as an LLM loop: it receives observations, reasons about the next step, takes actions through tools or external systems, and iterates until a goal is met or human input is needed.

## Claim

The core agent object is a loop, not a chat response. Its new engineering problems are persistence, grounding, action interfaces, coordination, and safety.

## Why It Matters

This gives the wiki a clear boundary between prompting, tool use, RAG, memory, harness design, multi-agent coordination, and operational guardrails.

## QnA Seeds

- Q: What is the minimum shape of an agent loop? -> A: Observation -> reasoning -> action -> new observation, repeated until completion or handoff.
- Q: What new problems appear when a model becomes an agent? -> A: Remembering state, grounding in external data, acting through tools, coordinating across tasks or agents, and staying safe under autonomy.
