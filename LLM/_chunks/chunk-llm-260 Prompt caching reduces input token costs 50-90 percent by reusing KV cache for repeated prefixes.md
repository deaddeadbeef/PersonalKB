---
tags: [llm, chunk]
id: chunk-llm-260
source: "[[raw-llm-061]]"
supports: ["[[Prompt Caching and Inference Infrastructure]]"]
confidence: verified
up: "[[LLM]]"
---

# Prompt Caching Reduces Input Token Costs 50-90% by Reusing KV Cache

## Context

Every LLM inference call processes the full prompt to build a KV cache. For agentic workloads with repeated system prompts, this reprocessing is wasteful and expensive.

## Claim

Prompt caching stores the KV cache for common prompt prefixes and reuses it across requests, reducing input token costs by 50-90% and time-to-first-token by 80%+ for agentic and conversational workloads.

## Why It Matters

Prompt caching makes agentic AI economically viable — without it, a coding agent making 50 tool calls with 100K context would process 5M input tokens; with caching, the prefix is processed once.

## QnA Seeds

- Q: What is being cached in prompt caching? → A: The key-value (KV) cache — the internal state produced when the model processes the prompt tokens through its layers.
- Q: Why is prompt caching especially important for agents? → A: Agents make many sequential calls with the same system prompt and context, so caching avoids reprocessing 10K-100K static tokens each time.
