# LLM First Inference Evidence Pack

## Goal

Add a first-run evidence pack for local LLM hosting so the vault has one concrete binder for machine preflight, model choice, runtime, endpoint, response, timing, quality, safety boundary, and next decision.

## Scope

- Work in the isolated `llm-first-inference-evidence-pack` worktree.
- Touch only the LLM study layer, generated index/audit reports, this task note, and `log.md`.
- Do not touch unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

## Verification Evidence

- Baseline `python _ops\personal_kb.py audit`: 4836 files, 2965 Markdown files, 837 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- Source check: current Ollama, LM Studio, llama.cpp, llama-cpp-python, and vLLM docs for first-run endpoints and OpenAI-compatible serving.
- Final: `python _ops\personal_kb.py index`
- Final: `python _ops\personal_kb.py audit`
- Final: `git diff --check`
