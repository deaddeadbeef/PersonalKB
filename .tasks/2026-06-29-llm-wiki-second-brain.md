---
status: complete
created: 2026-06-29
scope: llm-wiki-second-brain-orientation
---
# LLM Wiki and Second Brain Orientation

## Goal

Explain what Karpathy means by an LLM Wiki, relate it to Second Brain practice, inspect how the current PersonalKB vault already maps to the pattern, and record the recommended next operating steps.

## Constraints

- Preserve raw sources and chunks.
- Do not rewrite existing LLM articles during this orientation pass.
- Use current web verification for Karpathy and Second Brain references.
- Leave an audit trail in `log.md`.

## Planned Output

- `_ops/reports/llm-wiki-second-brain-strategy.md`
- `log.md` maintenance entry

## Verification

- `python _ops\personal_kb.py audit` exited 0.
- Audit counts: 963 candidate reader-facing articles, 374 reader-facing broken links, 58 reader-facing placeholder hits, 249 missing references, 247 missing confidence fields.
- `git diff --check` exited 0.
- Protected raw, chunk, template, media, `.obsidian`, and `.git` paths were not edited.
