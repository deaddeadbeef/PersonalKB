---
tags: [llm, chunk]
id: chunk-llm-252
source: "[[raw-llm-067]]"
supports: ["[[Agentic Coding Systems]]"]
confidence: verified
up: "[[LLM]]"
---

# Claude Code Reads Entire Files and Traces Dependencies for Deep Context

## Context

Many coding assistants use embedding-based retrieval to gather context snippets. Claude Code takes a different approach, reading entire files and tracing dependency chains directly.

## Claim

Claude Code emphasises deep context understanding by reading entire files and tracing dependencies directly rather than relying on embedding-based retrieval, producing more accurate multi-file changes.

## Why It Matters

Direct file reading avoids the information loss inherent in retrieval-augmented approaches, enabling the agent to understand full module interfaces and side effects.

## QnA Seeds

- Q: Why does Claude Code read entire files instead of using RAG? → A: Full file reading captures complete interfaces, type signatures, and side effects that snippet-based retrieval may miss.
- Q: What is the trade-off of this approach? → A: Higher per-call token usage, but more accurate changes that require fewer iterations.
