# Engineer Daemon Mission: PersonalKB Wiki Curation

## Objective

Keep `D:\Vaults\PersonalKB` trustworthy, navigable, source-backed, and progressively cleaner across small reviewable maintenance cycles. Improve article quality, metadata consistency, references, internal links, generated indexes, and audit health while preserving the vault's evidence trail.

Success means the vault becomes easier to browse and trust without losing provenance from `_raw/`, `_chunks/`, source indexes, or maintenance logs.

## Hard Guardrails

- Follow `AGENTS.md` before every pass.
- Treat these paths as protected unless explicitly assigned: `.git/`, `.obsidian/`, `*/_raw/`, `*/_chunks/`, `*/_templates/`, media files, and any unrelated dirty files.
- Start and end every cycle with `git status --short`.
- Do not touch user-modified files unless the task explicitly includes them.
- Prefer targeted edits over whole-note rewrites.
- Preserve frontmatter fields such as `tags`, `up`, `confidence`, and `tier-coverage` when present.
- Add or repair `## References` sections for substantive wiki notes using existing source indexes, chunks, raw notes, or checked current sources.
- Use Obsidian links for internal navigation. Prefer path-qualified links when short links are ambiguous.
- Do not paste long copyrighted text. Summarize and cite provenance.
- Do not update time-sensitive claims from memory. Use web verification for current domains such as `LLM` and `SpaceX`.
- Append each substantive maintenance pass to `log.md`.
- Commit coherent checkpoints only after verification passes.

## Cadence

One cycle should be a bounded maintenance unit, not an open-ended cleanup.

- Pilot phase: edit no more than 10 wiki notes total before human review.
- Normal phase: edit no more than 10-20 wiki notes, one domain query/report cleanup, or one broken-link cluster.
- Run audit before and after every cycle.
- Keep diffs path-scoped and easy to review.

## Scope Rotation

Default rotation:

1. `CS Data Structures` pilot
2. `CS Algorithms`
3. `CS Operating Systems`
4. `Programming Languages`
5. `NES Emulation`
6. `Japanese`
7. `Project Hail Mary`
8. `LLM`
9. `SpaceX`
10. `Recipes`
11. `Body Recomp`

Risk notes:

- `LLM` and `SpaceX` require live web verification for current claims.
- `Project Hail Mary` is copyright-sensitive; summarize and avoid long quotes.
- `Recipes` and `Body Recomp` may contain personal voice or personal data; avoid unnecessary stylistic rewrites.

## Per-Cycle Workflow

1. Baseline:
   - `cd D:\Vaults\PersonalKB`
   - `git status --short`
   - `python _ops/personal_kb.py audit`
2. Select one domain or one issue cluster.
3. Exclude protected paths and unrelated dirty files.
4. Inspect the relevant MOC, wiki notes, chunks, raw notes, and source index.
5. Edit minimally:
   - repair frontmatter
   - add `up` links
   - add `confidence`
   - add references
   - replace ambiguous links with canonical links
   - fill empty or stub notes only when evidence is present
6. Regenerate operational outputs:
   - `python _ops/personal_kb.py index`
   - `python _ops/personal_kb.py audit`
7. Review:
   - `git diff --check`
   - inspect path-scoped diffs
   - confirm no protected files changed
   - confirm unrelated dirty files were not touched
8. Append `log.md`.
9. Commit if verification passes and the checkpoint is coherent.

## Prioritization

Primary backlog:

1. Empty notes:
   - `LLM/Architecture Variants/Efficient Attention and Long-Context Variants.md`
   - `Priority Queues and Heaps.md`
2. Missing or weak provenance:
   - missing `## References`
   - placeholder text such as `To be populated as chunks are created`
   - query coverage `TBD`
3. Navigation quality:
   - missing `up`
   - ambiguous broken links such as `Array`, `Priority Queue`, or `Dynamic Programming Overview`
4. Metadata consistency:
   - missing `confidence`
   - inconsistent frontmatter
5. Domain polish:
   - source-backed stub expansion
   - query notes and coverage maps

Do not chase all broken links globally. Work by cluster and fix only the notes touched in the current cycle.

## Verification Commands

Run these every cycle:

```powershell
cd D:\Vaults\PersonalKB
git status --short
python _ops/personal_kb.py audit
python _ops/personal_kb.py index
python _ops/personal_kb.py audit
git diff --check
git diff --stat
git status --short
```

Optional focused checks:

```powershell
rg "To be populated as chunks are created|TBD|TODO" .
rg "\[\[Array\]\]|\[\[Priority Queue\]\]|\[\[Dynamic Programming Overview\]\]" .
```

## Stop and Escalate

Stop and ask for review if:

- The cycle would exceed the pilot or normal edit cap.
- A needed file has unrelated user modifications.
- Evidence conflicts between `_raw/`, `_chunks/`, and existing wiki text.
- A time-sensitive claim cannot be verified.
- A note appears to require a whole rewrite.
- The daemon would need to edit a protected path.
- Audit/index tooling fails unexpectedly.
- Broken-link fixes require a naming convention decision.
- Copyright-sensitive content would require substantial quoted material.

## First Five Cycles

1. CS Data Structures pilot baseline:
   - Audit current state.
   - Pick up to 3 safe notes.
   - Fix frontmatter, `up`, references, and obvious source-backed link issues.
   - Log and commit if clean.
2. Priority Queue / Heap link cluster:
   - Investigate root `Priority Queues and Heaps.md`.
   - Decide whether it should become a canonical note or redirect-style index note.
   - Repair only nearby links and references backed by existing chunks.
   - Stay within the 10-note pilot cap.
3. CS Data Structures pilot finish:
   - Use remaining pilot budget, up to 10 total notes across cycles 1-3.
   - Target missing confidence/references and ambiguous links.
   - Produce a short pilot report in `_ops/reports/`.
4. Human review gate:
   - No broad edits.
   - Run audit/index.
   - Summarize before/after counts.
   - Await approval to expand beyond the pilot.
5. Next approved domain:
   - Start `CS Algorithms` or `CS Operating Systems`.
   - Use the same bounded workflow.
   - Focus on one broken-link cluster or one metadata/reference cluster, not both.

## Operating Principle

Optimize for accumulated trust, not throughput. Make small, source-backed, reviewable improvements and leave a clear audit trail after every pass.
