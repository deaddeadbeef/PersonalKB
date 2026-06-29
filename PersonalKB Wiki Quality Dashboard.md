---
type: generated-quality-dashboard
tags: [vault-index, quality, audit, navigation]
up: "[[PersonalKB Book Reading Guide]]"
confidence: verified
tier-coverage: [core, practice]
---
# PersonalKB Wiki Quality Dashboard

## Verdict

Readable with the new book spines, but not yet good enough as a polished wiki.

The wiki is now navigable as a reading shelf because every committed top-level topic has a book-style spine. It is not yet clean as a finished reference set because reader-facing pages still have unresolved links, placeholder lines, and incomplete provenance metadata.

## Reader-Facing Wiki Health

| Check | Count | Meaning |
| --- | ---: | --- |
| Candidate reader-facing articles | 963 | Wiki pages outside raw, chunk, query, template, audio, task, and ops layers |
| Broken links in reader-facing articles | 374 | Navigation defects that affect normal reading |
| Placeholder lines in reader-facing articles | 58 | Draft markers visible to readers |
| Missing references sections | 249 | Pages that still need a source/provenance footer |
| Missing confidence frontmatter | 247 | Pages without confidence classification |
| Missing up frontmatter | 28 | Pages without explicit parent navigation |
| Stubs under 1500 bytes | 20 | Thin pages that may not carry their topic yet |
| Empty notes | 1 | Notes with no body text |
| Orphan articles | 0 | Reader-facing pages with no inbound wikilinks |

## Maintenance-Layer Noise

These counts are still useful, but they include chunks, templates, queries, schema examples, and operational notes. Do not use them alone to judge reading quality.

| Check | Count |
| --- | ---: |
| All broken wikilink occurrences | 925 |
| All placeholder hits | 79 |
| Heavy audio embed pages | 0 |

## Next Housekeeping Order

1. Fix reader-facing broken links first; they interrupt reading and graph traversal.
2. Remove visible placeholder lines from reader-facing LLM and SpaceX pages.
3. Add references sections and confidence frontmatter to high-traffic book-spine targets.
4. Only then spend time on chunk/query/template noise.

## Top Reader-Facing Broken Links

- `CS Algorithms/Backtracking/Backtracking Overview.md` -> `CS Algorithms Index`
- `CS Algorithms/Backtracking/Backtracking Overview.md` -> `Dynamic Programming Overview`
- `CS Algorithms/Backtracking/Backtracking Overview.md` -> `Recursion and Call Stack`
- `CS Algorithms/Backtracking/N-Queens Problem.md` -> `Dynamic Programming Overview`
- `CS Algorithms/Backtracking/N-Queens Problem.md` -> `Arrays`
- `CS Algorithms/Backtracking/N-Queens Problem.md` -> `Hash Sets`
- `CS Algorithms/Complexity/Halting Problem.md` -> `Complexity - The Halting Problem is undecidable via Turing’s diagonalisation argument`
- `CS Algorithms/Complexity/Halting Problem.md` -> `Complexity - Rice’s Theorem shows all non-trivial semantic program properties are undecidable`
- `CS Algorithms/Complexity/NP Completeness.md` -> `Dijkstra’s Algorithm`
- `CS Algorithms/Complexity/NP Completeness.md` -> `Complexity - The Halting Problem is undecidable via Turing’s diagonalisation argument`
- `CS Algorithms/Complexity/P vs NP.md` -> `Dijkstra’s Algorithm`
- `CS Algorithms/Complexity/P vs NP.md` -> `Complexity - The Halting Problem is undecidable via Turing’s diagonalisation argument`
- `CS Algorithms/Compression/Huffman Coding.md` -> `Priority Queue`
- `CS Algorithms/Compression/Huffman Coding.md` -> `Binary Tree`
- `CS Algorithms/Compression/LZW Compression.md` -> `Hash Table`
- `CS Algorithms/Compression/Run-Length Encoding.md` -> `Array`
- `CS Algorithms/Divide and Conquer/Divide and Conquer Overview.md` -> `CS Algorithms Index`
- `CS Algorithms/Divide and Conquer/Divide and Conquer Overview.md` -> `Quick Sort`
- `CS Algorithms/Divide and Conquer/Divide and Conquer Overview.md` -> `Dynamic Programming Overview`
- `CS Algorithms/Divide and Conquer/Divide and Conquer Overview.md` -> `Arrays`
- `CS Algorithms/Divide and Conquer/Divide and Conquer Overview.md` -> `Recursion and Call Stack`
- `CS Algorithms/Divide and Conquer/Master Theorem Applications.md` -> `Quick Sort`
- `CS Algorithms/Divide and Conquer/Master Theorem Applications.md` -> `Recursion and Call Stack`
- `CS Algorithms/Graphs/BFS and DFS.md` -> `Topological Sort`
- `CS Algorithms/Graphs/BFS and DFS.md` -> `Queues`

## Top Reader-Facing Placeholder Hits

- `LLM/2017 — The Transformer/Attention Mechanism.md:93` -> *(To be populated as chunks are created)*
- `LLM/2017 — The Transformer/Encoder-Decoder Models.md:78` -> *(To be populated as chunks are created)*
- `LLM/2017 — The Transformer/Positional Encoding.md:94` -> *(To be populated as chunks are created)*
- `LLM/2017 — The Transformer/Transformer Architecture.md:104` -> *(To be populated as chunks are created)*
- `LLM/2017 — The Transformer/Transformer Breakthrough and Scaling Era.md:102` -> *(To be populated as chunks are created)*
- `LLM/2018–2019 — Pretrained Language Models/BERT and Encoder Lineage.md:92` -> *(To be populated as chunks are created)*
- `LLM/2018–2019 — Pretrained Language Models/Data Curation and Deduplication.md:98` -> *(To be populated as chunks are created)*
- `LLM/2018–2019 — Pretrained Language Models/Decoder-Only Models.md:85` -> *(To be populated as chunks are created)*
- `LLM/2018–2019 — Pretrained Language Models/Encoder-Only Models.md:91` -> *(To be populated as chunks are created)*
- `LLM/2018–2019 — Pretrained Language Models/GPT and Decoder-Only Lineage.md:98` -> *(To be populated as chunks are created)*
- `LLM/2018–2019 — Pretrained Language Models/Knowledge and Reasoning Benchmarks.md:98` -> *(To be populated as chunks are created)*
- `LLM/2020–2021 — The Scaling Era/Contamination and Data Leakage.md:105` -> *(To be populated as chunks are created)*
- `LLM/2020–2021 — The Scaling Era/Mixture-of-Experts Models.md:89` -> *(To be populated as chunks are created)*
- `LLM/2020–2021 — The Scaling Era/Retrieval Pipelines and Context Assembly.md:107` -> *(To be populated as chunks are created)*
- `LLM/2020–2021 — The Scaling Era/Scaling Laws.md:90` -> *(To be populated as chunks are created)*
- `LLM/2020–2021 — The Scaling Era/Training Infrastructure and Parallelism.md:96` -> *(To be populated as chunks are created)*
- `LLM/2020–2021 — The Scaling Era/Vision-Language Models.md:92` -> *(To be populated as chunks are created)*
- `LLM/2022 — Alignment and Chat/Alignment Objectives and Failure Modes.md:88` -> *(To be populated as chunks are created)*
- `LLM/2022 — Alignment and Chat/Compute Data and Parameter Trade-offs.md:94` -> *(To be populated as chunks are created)*
- `LLM/2022 — Alignment and Chat/Constitutional AI.md:91` -> *(To be populated as chunks are created)*
- `LLM/2022 — Alignment and Chat/Direct Preference Optimization.md:104` -> *(To be populated as chunks are created)*
- `LLM/2022 — Alignment and Chat/Human Evaluation and Preference Studies.md:91` -> *(To be populated as chunks are created)*
- `LLM/2022 — Alignment and Chat/Mechanistic Interpretability.md:121` -> *(To be populated as chunks are created)*
- `LLM/2022 — Alignment and Chat/Red-Teaming and Safety Evaluations.md:123` -> *(To be populated as chunks are created)*
- `LLM/2022 — Alignment and Chat/Reinforcement Learning from Human Feedback.md:129` -> *(To be populated as chunks are created)*

## Report Files

- [Reader-facing quality summary JSON](<_ops/reports/wiki-quality-summary.json>)
- [Reader-facing broken links](<_ops/reports/wiki-broken-links.md>)
- [Reader-facing placeholder hits](<_ops/reports/wiki-placeholder-hits.md>)
- [Full audit summary JSON](<_ops/reports/audit-summary.json>)
- [Full broken-link report](<_ops/reports/audit-broken-links.md>)
- [Full placeholder report](<_ops/reports/audit-placeholder-hits.md>)

## References

- [[PersonalKB Book Reading Guide]]
- [[index|PersonalKB Index]]
- [[log|PersonalKB Maintenance Log]]
- [Generated wiki quality summary](<_ops/reports/wiki-quality-summary.json>)
- [Generated full audit summary](<_ops/reports/audit-summary.json>)

Generated: 2026-06-29T21:54:21
