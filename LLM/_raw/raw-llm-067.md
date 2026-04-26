---
tags: [llm, raw]
source_type: product_analysis
source_title: "Claude Code and the Rise of Agentic Coding"
authors: [Anthropic]
year: 2025
up: "[[Sources Index]]"
---

# Claude Code and Agentic Coding

## Summary

Claude Code is a terminal-based coding agent from Anthropic that can autonomously navigate codebases, read and write files, execute commands, run tests, and manage git operations. It represents the maturation of code generation from single-completion assistance to multi-step autonomous software engineering. Alongside GitHub Copilot coding agent (async PR-based), Cursor (AI-native IDE), and Devin (persistent web environment), Claude Code exemplifies the shift from pair programming to task delegation in software development.

## Key Claims

1. Agentic coding systems can autonomously plan, implement, test, and iterate on code changes
2. Deep context reading (entire files, dependency tracing) produces better results than embedding-based retrieval
3. The agentic loop (plan→implement→test→iterate) enables self-correcting development
4. Different interaction models serve different workflows: terminal, PR-based, IDE-integrated, web-based
5. SWE-bench provides standardised evaluation of autonomous coding capabilities

## Atomic Facts

1. Claude Code operates as a terminal agent with filesystem and shell access
2. GitHub Copilot coding agent creates branches, implements changes, runs CI, opens PRs
3. Cursor is an AI-native IDE with codebase-wide context
4. Devin (Cognition, 2024) was introduced as the first AI software engineer
5. SWE-bench evaluates ability to resolve real GitHub issues
6. Context management is the critical technical challenge for large codebases

## Significance

Agentic coding systems shift the developer role from writing code to reviewing and directing code, with implications for productivity, team size, and the economics of software development.

## Chunks Extracted

*Pending*