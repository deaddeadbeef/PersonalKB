# LLM 20-Paper Synthesis Map

## Goal

Add an academic synthesis map for the 20-paper fast path so the LLM study path connects architecture, pretraining, scaling, systems, alignment, adaptation, RAG, agents, evaluation, and local deployment in one causal story.

## Scope

- Work in the isolated `llm-20-paper-synthesis-map` worktree.
- Touch only the LLM study layer, generated index/audit reports, this task note, and `log.md`.
- Do not touch unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

## Verification Evidence

- Baseline `python _ops\personal_kb.py audit`: 4834 files, 2963 Markdown files, 836 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- Source check: existing vault raw notes for the 20 fast-path papers and `LLM/Sources/Sources Index.md`.
- Final: `python _ops\personal_kb.py index`
- Final: `python _ops\personal_kb.py audit`
- Final: `git diff --check`
