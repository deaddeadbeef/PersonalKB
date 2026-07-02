---
tags: [llm, chunk]
id: chunk-llm-267
source: "[[LLM/_raw/raw-llm-071|raw-llm-071]]"
source_loc: "p. 343"
supports: ["[[LLM/Study/LLM Progressive Systems Route]]", "[[LLM/2026 — Reasoning and Agents/Agentic Coding Systems]]", "[[LLM/2026 — Reasoning and Agents/Computer Use and GUI Agents]]"]
confidence: verified
up: "[[LLM/LLM]]"
---

# Agent Harness Design Separates Reasoning Execution Memory Communication And Observability

## Context

The harness chapter defines an agent harness as runtime infrastructure that wraps a stateless language model into a stateful, goal-directed system capable of multi-step reasoning, tool use, memory retrieval, and interaction with external systems.

## Claim

Agent harnesses should keep reasoning, execution, memory, communication, and observability as separate concerns. Mixing them into one prompt makes the system harder to debug, secure, and improve.

## Why It Matters

This is the systems layer behind the user's LLM wiki and second-brain work: the wiki should teach not just what an agent says, but which runtime layer owns state, tools, memory, logs, and human handoff.

## QnA Seeds

- Q: What does the LLM own in a harness? -> A: Reasoning and decision-making over the visible context.
- Q: What should the harness own? -> A: Tool dispatch, I/O, memory stores, message routing, sandboxing, logs, traces, and safety checks.
