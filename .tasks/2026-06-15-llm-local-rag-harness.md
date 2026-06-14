# LLM Local RAG Harness

## Goal

Add a practical local RAG implementation harness that turns the existing RAG assistant lab into reproducible artifacts: corpus manifest, chunks, embedding/index config, retrieval evidence, cited answer, unsupported-question refusal, diagnosed failure row, benchmark row, and quality row.

## Scope

- Work in the isolated `llm-local-rag-harness` worktree.
- Touch only the LLM study layer, generated index/audit reports, this task note, and `log.md`.
- Do not touch unrelated active-vault Japanese, CS, recipe, or older LLM learning-path edits.

## Verification Evidence

- Baseline `python _ops\personal_kb.py audit`: 4832 files, 2961 Markdown files, 835 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- Source check: Ollama embeddings and OpenAI compatibility docs, Chroma getting-started/client/query docs, and Sentence Transformers semantic search docs.
- Final: `python _ops\personal_kb.py index`
- Final: `python _ops\personal_kb.py audit`
- Final: `git diff --check`
