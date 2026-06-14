# LLM Mastery Roadmap Pass

## Goal

Make the LLM study area easier to consume as a complete mastery path by connecting academic knowledge, active recall, implementation practice, and local inference proof.

## Scope

- Work in the isolated `llm-mastery-roadmap` worktree.
- Add a learner-facing mastery roadmap under `LLM/Study`.
- Link the roadmap from the LLM MOC, learning path, study index, and local inference lab.
- Keep the pass limited to study/navigation notes plus generated audit/index reports, task state, and `log.md`.

## Verification Evidence

- Baseline: `python _ops/personal_kb.py audit`
- Baseline counts: 4780 files, 2909 Markdown files, 809 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- Final: `python _ops/personal_kb.py index`
- Final: `python _ops/personal_kb.py audit`
- Final counts: 4782 files, 2911 Markdown files, 810 candidate articles, 20 stubs, 250 missing references, 79 placeholder hits, 938 broken-link occurrences.
- Final: `git diff --check`
