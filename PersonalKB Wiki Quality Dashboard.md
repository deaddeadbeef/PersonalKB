---
type: generated-quality-dashboard
tags: [vault-index, quality, audit, navigation]
up: "[[PersonalKB Book Reading Guide]]"
confidence: verified
tier-coverage: [core, practice]
---
# PersonalKB Wiki Quality Dashboard

## Verdict

Ready as a clean reference wiki.

The wiki is now navigable as a reading shelf because every committed top-level topic has a book-style spine. It is not yet clean as a finished reference set because reader-facing pages still have unresolved links, placeholder lines, and incomplete provenance metadata.

## Reader-Facing Wiki Health

| Check | Count | Meaning |
| --- | ---: | --- |
| Candidate reader-facing articles | 976 | Wiki pages outside raw, chunk, query, template, audio, task, and ops layers |
| Broken links in reader-facing articles | 0 | Navigation defects that affect normal reading |
| Placeholder lines in reader-facing articles | 0 | Draft markers visible to readers |
| Missing references sections | 0 | Pages that still need a source/provenance footer |
| Missing confidence frontmatter | 0 | Pages without confidence classification |
| Missing up frontmatter | 0 | Pages without explicit parent navigation |
| Stubs under 1500 bytes | 21 | Thin pages that may not carry their topic yet |
| Empty notes | 0 | Notes with no body text |
| Orphan articles | 0 | Reader-facing pages with no inbound wikilinks |

## Maintenance-Layer Noise

These counts are still useful, but they include chunks, templates, queries, schema examples, and operational notes. Do not use them alone to judge reading quality.

| Check | Count |
| --- | ---: |
| All broken wikilink occurrences | 551 |
| All placeholder hits | 21 |
| Heavy audio embed pages | 0 |

## Next Housekeeping Order

1. Fix reader-facing broken links first; they interrupt reading and graph traversal.
2. Remove visible placeholder lines from reader-facing LLM and SpaceX pages.
3. Add references sections and confidence frontmatter to high-traffic book-spine targets.
4. Only then spend time on chunk/query/template noise.

## Top Reader-Facing Broken Links

- None.

## Top Reader-Facing Placeholder Hits

- None.

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

Generated: 2026-07-01T19:21:16
