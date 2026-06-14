# 2026-06-15 - LLM retrieval evaluation and reranking lab

## Goal

Add a dedicated local RAG retrieval-evaluation lab so retrieval quality, reranking impact, hybrid-search decisions, context selection, and citation validity are measured before judging the local generator.

## Scope

- Add `LLM/Study/Local RAG Retrieval Evaluation and Reranking Lab.md`.
- Route the lab through the LLM MOC, study index, RAG assistant lab, minimal Python harness, quality harness, benchmark log, troubleshooting tree, RAG review drill, mastery roadmap, capstone workbook, self-assessment exam, and relevant academic RAG notes.
- Regenerate `index.md` and `_ops/reports/audit-summary.json`.

## Verification

- External docs checked: Ollama embeddings, Chroma query/get, Sentence Transformers retrieve-and-rerank, and Qdrant hybrid queries.
- Regenerated `index.md` with `python _ops\personal_kb.py index`.
- Regenerated `_ops/reports/audit-summary.json` with `python _ops\personal_kb.py audit`.
- Audit result: 4,856 files, 2,985 markdown files, 847 candidate articles, 938 broken-link occurrences.
