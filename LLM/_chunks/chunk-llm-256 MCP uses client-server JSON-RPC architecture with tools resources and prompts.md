---
tags: [llm, chunk]
id: chunk-llm-256
source: "[[raw-llm-066]]"
supports: ["[[Model Context Protocol]]"]
confidence: verified
up: "[[LLM]]"
---

# MCP Uses Client-Server JSON-RPC Architecture with Three Primitives

## Context

Before MCP, every AI application needed custom connectors for each tool it wanted to integrate, creating an N times M integration problem.

## Claim

MCP uses a client-server architecture over JSON-RPC transport, exposing three primitives — tools (executable functions), resources (readable data), and prompt templates — through a standardised discoverable interface.

## Why It Matters

The three-primitive design covers the full range of LLM-external-system interactions while keeping the protocol simple enough for widespread adoption.

## QnA Seeds

- Q: What are MCP's three primitives? → A: Tools (callable functions), resources (readable data like files or DB rows), and prompt templates (reusable prompt structures).
- Q: What transport protocol does MCP use? → A: JSON-RPC over stdio (for local servers) or HTTP+SSE (for remote servers).
