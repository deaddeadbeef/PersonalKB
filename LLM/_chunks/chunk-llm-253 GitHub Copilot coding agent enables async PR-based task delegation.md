---
tags: [llm, chunk]
id: chunk-llm-253
source: "[[raw-llm-067]]"
supports: ["[[Agentic Coding Systems]]"]
confidence: verified
up: "[[LLM]]"
---

# GitHub Copilot Coding Agent Enables Async PR-Based Task Delegation

## Context

GitHub Copilot evolved from inline autocomplete to a full coding agent that can be assigned issues and autonomously produce pull requests.

## Claim

GitHub Copilot coding agent shifts the interaction model from real-time pair programming to asynchronous task delegation: users assign issues, the agent creates branches, implements changes, runs CI, and opens PRs.

## Why It Matters

Asynchronous task delegation allows developers to assign work and context-switch, reviewing completed PRs rather than supervising real-time coding — a fundamentally different workflow.

## QnA Seeds

- Q: How does Copilot coding agent differ from Copilot autocomplete? → A: Autocomplete suggests code inline in real-time; the coding agent independently implements entire tasks and opens pull requests.
- Q: What triggers the Copilot coding agent? → A: Assigning a GitHub issue to the agent, which then works asynchronously.
