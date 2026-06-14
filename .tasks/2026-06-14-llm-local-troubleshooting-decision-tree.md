# Local LLM troubleshooting decision tree

- [x] Review current local hosting, serving, benchmark, RAG, client, and request-lifecycle troubleshooting coverage.
- [x] Add local LLM troubleshooting decision tree.
- [x] Link it from the study index, LLM MOC, mastery roadmap, hosting lab, serving runbook, benchmark log, and capstone workbook.
- [x] Regenerate index.
- [x] Run audit.
- [x] Commit and merge.

## Verification

- `git diff --check` passed.
- `python _ops\personal_kb.py index` wrote `index.md`.
- `python _ops\personal_kb.py audit` completed:
  - files_total: 4810
  - markdown_files: 2939
  - candidate_articles: 824
  - missing_references: 250
  - broken_link_occurrences: 938
  - placeholder_hits: 79
