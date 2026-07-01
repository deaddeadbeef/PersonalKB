---
type: generated-quality-dashboard
tags: [vault-index, quality, audit, navigation]
up: "[[PersonalKB Book Reading Guide]]"
confidence: verified
tier-coverage: [core, practice]
---
# PersonalKB Wiki Quality Dashboard

## Verdict

Good enough for guided reading, but not yet clean enough to call finished.

The wiki is navigable for normal reading: reader-facing broken links and visible draft placeholders are cleared. The remaining work is metadata and depth cleanup: missing freshness classifications.

## Reader-Facing Wiki Health

| Check | Count | Meaning |
| --- | ---: | --- |
| Candidate reader-facing articles | 987 | Wiki pages outside raw, chunk, query, template, audio, task, and ops layers |
| Broken links in reader-facing articles | 0 | Navigation defects that affect normal reading |
| Broken section links in reader-facing articles | 0 | Wikilinks whose target note exists but requested heading does not |
| Ambiguous wikilinks in reader-facing articles | 0 | Unqualified links whose note name exists in multiple reader-facing topics |
| Placeholder lines in reader-facing articles | 0 | Draft markers visible to readers |
| Missing references sections | 0 | Pages that still need a source/provenance footer |
| Empty references sections | 0 | Pages with a references heading but no provenance links or notes |
| Missing confidence frontmatter | 0 | Pages without confidence classification |
| Missing freshness frontmatter | 16 | Pages without stable/current-sensitive currency classification |
| Missing up frontmatter | 0 | Pages without explicit parent navigation |
| Stubs under 1500 bytes | 0 | Thin pages that may not carry their topic yet |
| Empty notes | 0 | Notes with no body text |
| Orphan articles | 0 | Reader-facing pages with no inbound wikilinks |

## Freshness And Currency

Freshness classification is metadata, not a claim that every current fact has just been rechecked. Current-sensitive pages should gain a `last-verified`, `as-of`, or `source-date` marker when a human or agent refreshes their live claims against sources.

| Check | Count | Meaning |
| --- | ---: | --- |
| Current-sensitive reader-facing articles | 253 | Pages about live models, local-inference tooling, SpaceX operations, or other facts likely to age |
| Current-sensitive pages missing dated review marker | 120 | Refresh queue for pages that need explicit source-date evidence before relying on live claims |

## Editorial Readiness

These checks are reader-facing structure checks rather than raw lint counts. They record whether the wiki has the surfaces needed to read, study, verify, and maintain the vault without falling back to a flat inventory.

| Gate | Status | Evidence |
| --- | --- | --- |
| Human front door | Ready | [[Welcome]] routes readers to book, study, quality, catalog, and source paths |
| Book-mode reading | Ready | [[PersonalKB Book Reading Guide]] provides shelf order, cross-topic routes, operating modes, and proof targets |
| Topic root routers | Ready | Major topic roots expose book mode, study or practice, provenance, and catalog browsing before domain lists |
| Study and proof routing | Ready | Learning paths and study indexes explain when to use book spines, pass-based curricula, drills, labs, and proof artifacts |
| Provenance routing | Ready | Source indexes explain how to verify claims, classify source type, and handle freshness-sensitive facts |
| Generated summary prose | Ready | Generated index and book-spine summaries use reader prose instead of Mermaid directives, summary labels, generic template claims, or example-only snippets |
| Exhaustive catalog boundary | Ready | [[index]] labels itself as the generated catalog for search and agent queries, not the first reading path |

## Maintenance-Layer Noise

These counts are still useful, but they include chunks, templates, queries, schema examples, and operational notes. Do not use them alone to judge reading quality. Protected-layer counts come from `_raw`, `_chunks`, and `_templates`, which are evidence or scaffolding layers rather than normal reading pages.

| Check | Count |
| --- | ---: |
| Operational broken wikilinks outside protected layers | 0 |
| Operational placeholder hits outside templates | 0 |
| Protected raw/chunk/template broken wikilinks | 516 |
| Template placeholder hits | 10 |
| All broken wikilink occurrences | 516 |
| All placeholder hits | 10 |
| Heavy audio embed pages | 0 |

## Next Housekeeping Order

1. Add freshness frontmatter so stable, historical, and current-sensitive pages are not mixed together.
2. Refresh current-sensitive pages with dated source checks, starting from LLM frontier/local-inference and SpaceX live-company pages.
3. Only then spend time on chunk/query/template noise.

## Top Reader-Facing Broken Links

- None.

## Top Reader-Facing Broken Section Links

- None.

## Top Reader-Facing Ambiguous Wikilinks

- None.

## Top Reader-Facing Placeholder Hits

- None.

## Top Current-Sensitive Pages Missing Dated Review

- `LLM/2024–2025 — Frontier and Efficiency/2024–2025 — Frontier and Efficiency Overview.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/Batching and Continuous Batching.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/Code and Agentic Benchmarks.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/Code Generation Agents.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/Efficient Attention and Long-Context Variants.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/KV Cache and Context Reuse.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/Memory and State Management.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/Multi-Agent Systems.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/Multimodal Evaluation and Safety.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/OCR Documents and UI Understanding.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/Serving Architectures and Throughput-Latency Trade-offs.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/Speculative Decoding.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/Speech-Language Models.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/State Space Models and Mamba.md` -> missing last-verified/as-of/source-date marker
- `LLM/2024–2025 — Frontier and Efficiency/Video Understanding Models.md` -> missing last-verified/as-of/source-date marker
- `LLM/2026 — Reasoning and Agents/Agentic Coding Systems.md` -> missing last-verified/as-of/source-date marker
- `LLM/2026 — Reasoning and Agents/Computer Use and GUI Agents.md` -> missing last-verified/as-of/source-date marker
- `LLM/2026 — Reasoning and Agents/DeepSeek R1 and Open Reasoning.md` -> missing last-verified/as-of/source-date marker
- `LLM/2026 — Reasoning and Agents/Model Context Protocol.md` -> missing last-verified/as-of/source-date marker
- `LLM/2026 — Reasoning and Agents/Prompt Caching and Inference Infrastructure.md` -> missing last-verified/as-of/source-date marker
- `LLM/2026 — Reasoning and Agents/Reasoning Distillation.md` -> missing last-verified/as-of/source-date marker
- `LLM/2026 — Reasoning and Agents/Reasoning Models and Test-Time Compute.md` -> missing last-verified/as-of/source-date marker
- `LLM/Study/Inference and Efficiency - Review Drill.md` -> missing last-verified/as-of/source-date marker
- `LLM/Study/LLM Inference Request Lifecycle Lab.md` -> missing last-verified/as-of/source-date marker
- `LLM/Study/Local LLM Client Harness Lab.md` -> missing last-verified/as-of/source-date marker

## Report Files

- [Reader-facing quality summary JSON](<_ops/reports/wiki-quality-summary.json>)
- [Reader-facing broken links](<_ops/reports/wiki-broken-links.md>)
- [Reader-facing broken section links](<_ops/reports/wiki-broken-anchor-links.md>)
- [Reader-facing ambiguous wikilinks](<_ops/reports/wiki-ambiguous-wikilinks.md>)
- [Reader-facing placeholder hits](<_ops/reports/wiki-placeholder-hits.md>)
- [Current-sensitive dated-review queue](<_ops/reports/wiki-current-sensitive-review.md>)
- [Full audit summary JSON](<_ops/reports/audit-summary.json>)
- [Missing freshness frontmatter](<_ops/reports/audit-missing-freshness.md>)
- [Empty references sections](<_ops/reports/audit-empty-references.md>)
- [Operational broken links](<_ops/reports/audit-operational-broken-links.md>)
- [Operational placeholder hits](<_ops/reports/audit-operational-placeholder-hits.md>)
- [Protected-layer broken links](<_ops/reports/audit-protected-broken-links.md>)
- [Template placeholder hits](<_ops/reports/audit-template-placeholder-hits.md>)
- [Full broken-link report](<_ops/reports/audit-broken-links.md>)
- [Full placeholder report](<_ops/reports/audit-placeholder-hits.md>)

## References

- [[PersonalKB Book Reading Guide]]
- [[index|PersonalKB Index]]
- [[log|PersonalKB Maintenance Log]]
- [Generated wiki quality summary](<_ops/reports/wiki-quality-summary.json>)
- [Generated full audit summary](<_ops/reports/audit-summary.json>)

Generated: 2026-07-01T20:45:04
