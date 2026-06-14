# LLM Context Token Budgeting

## Goal

Add a practical context-window and token-budgeting lab that connects tokenizer theory, chat templates, RAG packing, KV-cache pressure, and local inference benchmarking.

## Scope

- Work in the isolated `llm-context-token-budgeting` worktree.
- Touch only the LLM study layer, generated index/audit reports, this task note, and `log.md`.
- Do not touch unrelated active-vault Japanese, CS, recipe, or learning-path edits.

## Verification Evidence

- Baseline: worktree created from `829f004 Add local LLM model provenance checklist`.
- Source check: Hugging Face Transformers chat templates/tokenizer docs, Ollama context/Modelfile docs, vLLM engine/OpenAI-compatible docs, and llama.cpp server README.
- Final: `python _ops/personal_kb.py index`
- Final: `python _ops/personal_kb.py audit`
- Final: `git diff --check`
