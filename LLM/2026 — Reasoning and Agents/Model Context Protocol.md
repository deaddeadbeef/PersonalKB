---
tags: [llm, reasoning-agents]
up: "[[2026 — Reasoning and Agents Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Model Context Protocol

> **One-line summary** MCP is an open standard for connecting LLMs to external tools, data sources, and services through a uniform client-server interface, replacing ad-hoc tool integration approaches.

## 🎯 Intuition

### Core Idea

MCP standardises how AI applications talk to tools. Instead of every app building one-off integrations for every database, API, file system, or service, both sides can agree on one shared protocol.

### Analogy

MCP is like USB-C for AI tools — one standard plug for any device. Once both sides support the standard, they can connect without custom adapters every time.

### Why It Matters

That turns tool integration from a messy many-to-many problem into a composable ecosystem where new servers can be plugged into many AI clients.

---

## ⚙️ Core Mechanics

### How It Works

The Model Context Protocol (MCP), introduced by Anthropic in November 2024, uses a client-server architecture with **JSON-RPC** transport.

- An MCP **server** exposes capabilities:
  - **tools** (executable functions)
  - **resources** (readable data)
  - **prompts** (templates)
- An MCP **client** in an AI application or IDE discovers server capabilities, presents them to the model, and routes tool calls appropriately.

The key abstraction is separation of concerns: tool providers implement servers once, and AI applications implement clients once. Any compliant client can then talk to any compliant server without bespoke integration code.

### Key Specs

- Announced: **November 2024**
- Transport: **JSON-RPC over stdio or HTTP+SSE**
- Core primitives: **tools, resources, prompts**
- Architecture: **client-server**

### Key Facts

- **Announced**: November 2024 by Anthropic, open-source specification
- **Transport**: JSON-RPC over stdio or HTTP+SSE
- **Three primitives**: tools (functions), resources (data), prompts (templates)
- **Client-server**: MCP clients in AI apps connect to MCP servers
- **Adopted by**: Claude Desktop, Cursor, VS Code, Zed, Windsurf, and more
- **Community servers**: 100+ open-source MCP servers on GitHub
- **Comparison**: like USB-C for AI tool integration — one standard, many devices

| Feature | MCP | OpenAI Function Calling | LangChain Tools |
|---------|-----|----------------------|-----------------|
| Standard | Open specification | Proprietary API | Framework-specific |
| Transport | JSON-RPC (stdio/HTTP) | HTTP API | In-process |
| Discovery | Dynamic server capability query | Static schema definition | Code registration |
| Ecosystem | Cross-application | OpenAI-only | LangChain-only |

---

## 🔬 Deep Dive

### Technical Details

MCP solves the **N×M integration problem**. Without a standard, **N** AI applications connecting to **M** tools require **N×M** custom integrations. With MCP, the work becomes **N clients + M servers**, which scales much better and encourages ecosystem reuse.

Adoption has been rapid: Claude Desktop, Cursor, VS Code (GitHub Copilot), Zed, Windsurf, and many others support MCP. Community-built servers expose databases such as PostgreSQL and SQLite, cloud platforms like AWS and GCP, developer tools such as GitHub and Jira, and many web services.

### Limitations

- A standard protocol does not guarantee identical quality across servers
- Security, permissions, and trust boundaries still need careful handling
- Competing proprietary tool APIs still exist

### Impact

MCP lowers the cost of extending AI systems with tools and creates strong network effects as both clients and servers proliferate.

### Related Notes

- [[Function Calling]] — the capability MCP standardises
- [[Tool-Augmented Prompting]] — using tools to enhance LLM output
- [[Agentic Coding Systems]] — primary consumers of MCP
- [[Frontier Models 2025-2026]] — models that support MCP natively

---

## 🏋️ Practice

### Warm-Up

1. What three primitives does MCP expose?
2. Why is MCP compared with USB-C?

### Core Problems

1. Explain how MCP reduces the N×M integration problem.
2. Compare MCP with OpenAI function calling and LangChain tools.
3. Describe the roles of an MCP client and an MCP server.

### Challenge

Design a small AI workflow using one MCP client and three MCP servers, and explain why the standard makes that setup easier to maintain.

---

## Supporting Chunks

- [[LLM/_chunks/chunk-llm-256 MCP uses client-server JSON-RPC architecture with tools resources and prompts|chunk-llm-256 MCP standardises LLM tool integration via JSON-RPC client-server architecture with tools resources and prompts]]
- [[LLM/_chunks/chunk-llm-257 MCP solves the N times M integration problem reducing it to N plus M|chunk-llm-257 MCP solves N-times-M integration problem adopted by Claude Desktop Cursor VS Code and 100 plus servers]]

## References

→ [[Sources Index]]
