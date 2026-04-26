---
tags: [llm, raw]
source_type: specification
source_title: "Model Context Protocol Specification"
authors: [Anthropic]
year: 2024
up: "[[Sources Index]]"
---

# Model Context Protocol (MCP)

## Summary

Anthropic announced the Model Context Protocol in November 2024 as an open standard for connecting LLMs to external tools and data sources. MCP uses a client-server architecture with JSON-RPC transport, exposing three primitives: tools (executable functions), resources (readable data), and prompt templates. The protocol solves the N×M integration problem — N AI applications connecting to M tools — by standardising the interface. Adoption spread rapidly across Claude Desktop, Cursor, VS Code, Zed, and other AI-integrated development environments.

## Key Claims

1. MCP replaces ad-hoc tool integrations with a universal open standard
2. Client-server architecture with JSON-RPC transport enables cross-platform compatibility
3. Three primitives (tools, resources, prompts) cover the full range of LLM-external-system interactions
4. The N×M integration problem is reduced to N+M implementations
5. Community-driven server ecosystem provides plug-and-play access to databases, APIs, and services

## Atomic Facts

1. Announced November 2024 by Anthropic as open-source specification
2. Transport: JSON-RPC over stdio or HTTP+SSE
3. Three primitives: tools, resources, prompt templates
4. Adopted by Claude Desktop, Cursor, VS Code, Zed, Windsurf
5. 100+ community-built MCP servers on GitHub
6. Analogous to USB-C: one standard connecting many devices

## Significance

MCP established the first widely-adopted open standard for LLM tool integration, creating network effects as the ecosystem of servers grows and reducing the barrier to extending AI agent capabilities.

## Chunks Extracted

*Pending*