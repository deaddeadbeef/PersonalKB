# LLM Local Tool Calling Lab

## Goal

Add a practical local tool-calling and structured-output lab that connects function-calling theory, JSON Schema, constrained decoding, local OpenAI-compatible runtime support, security policy, and evaluation evidence.

## Scope

- Work in the isolated `llm-local-tool-calling-lab` worktree.
- Touch only the LLM study layer, generated index/audit reports, this task note, and `log.md`.
- Do not touch unrelated active-vault Japanese, CS, recipe, or learning-path edits.

## Verification Evidence

- Baseline `python _ops\personal_kb.py audit`: 4830 files, 2959 Markdown files, 834 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- Source check: OpenAI function calling and structured outputs docs, Ollama tool calling docs, vLLM tool calling docs, llama.cpp server README, and llama-cpp-python structured output/function calling docs.
- Final: `python _ops\personal_kb.py index`
- Final: `python _ops\personal_kb.py audit`
- Final: `git diff --check`
