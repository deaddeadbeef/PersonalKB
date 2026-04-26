---
id: raw-novel-002
type: raw
title: "PHM Chapter Summaries — Secondary Sources Registry"
status: active
source_mode: secondary
tags:
  - phm
  - raw
  - novel
  - secondary-sources
up: "[[Sources Index]]"
---
# PHM Chapter Summaries — Secondary Sources Registry

Registry of the public, legal secondary sources used to bootstrap chapter notes for *Project Hail Mary* while a legally owned digital copy of the primary text remains unavailable. This note governs the source hygiene rules and tracks which secondary sources have been consulted.

---

## Legal and Copyright Status

All sources listed below are publicly accessible web content. Their use here is governed by the following constraints:

1. **No verbatim copying.** All chapter summaries derived from these sources must be original paraphrases. Do not reproduce the wording of any secondary source in a chapter note.
2. **These are not primary sources.** Chapter boundaries, event sequencing, and quoted material cannot be verified against the novel itself until a legally owned copy is available. All chapter content is approximate until that upgrade occurs.
3. **No quotes from the novel via secondary sources.** Secondary summary sites may quote the novel; do not relay those quotes into chapter notes. The Key Quotes section of every chapter note must remain as a placeholder until `source_mode: primary` is established.
4. **Secondary summaries have varying accuracy.** Different sites may disagree on chapter boundaries, minor plot details, or character phrasing. Where sources conflict, note the discrepancy in the relevant chapter note rather than choosing arbitrarily.

---

## Registered Sources

### PHM-SEC-001 — The Bibliofile: Chapter-by-Chapter Recap

| Field | Value |
|---|---|
| URL | `https://the-bibliofile.com/project-hail-mary-recap-chapter-summary/` |
| Type | Book-summary blog, chapter-by-chapter |
| Coverage | Full novel, Ch 1–30 + Epilogue |
| Reliability notes | Generally detailed; chapter boundaries appear consistent with the novel's structure. Summaries are plot-level, minimal science annotation. |
| Last verified accessible | 2025 |

### PHM-SEC-002 — BookNookCook: Full Summary

| Field | Value |
|---|---|
| URL | `https://booknookcook.com/project-hail-mary-summary/` |
| Type | Book-summary site, condensed |
| Coverage | Full novel overview; section-level rather than strict chapter-by-chapter |
| Reliability notes | Higher-level narrative arc; useful for confirming major plot beats. Chapter boundary mapping requires cross-reference with PHM-SEC-001. |
| Last verified accessible | 2025 |

### PHM-SEC-003 — UrSummary: Chapter-by-Chapter

| Field | Value |
|---|---|
| URL | `https://ursummary.com/project-hail-mary-summary-chapter-by-chapter-andy-weir/` |
| Type | Book-summary site, chapter-by-chapter |
| Coverage | Full novel, Ch 1–30 + Epilogue |
| Reliability notes | Independent chapter-level summaries; useful as a second source to cross-check PHM-SEC-001. Depth varies by chapter. |
| Last verified accessible | 2025 |

### PHM-SEC-004 — Wikipedia: Project Hail Mary

| Field | Value |
|---|---|
| URL | `https://en.wikipedia.org/wiki/Project_Hail_Mary` |
| Type | Encyclopaedia article |
| Coverage | Plot summary (condensed), publication info, reception, adaptation |
| Reliability notes | Highest editorial scrutiny of the four sources; most reliable for high-level plot structure and chapter count confirmation. Does not provide chapter-by-chapter breakdown. Use for structural cross-checks only. |
| Last verified accessible | 2025 |

---

## Chapter Boundary Approximation Note

The novel has 30 numbered chapters plus an Epilogue (31 notes total). Chapter boundaries in secondary sources are approximate: web summaries may mislabel chapter numbers or split chapters differently. Chapter notes created from these sources should include a frontmatter comment if a chapter boundary is uncertain:

```yaml
# boundary_confidence: approximate  (add this comment if uncertain)
```

Chapter boundaries will be confirmed during primary-mode upgrade when a legal digital copy is available.

---

## Source Conflict Resolution

If PHM-SEC-001, PHM-SEC-002, and PHM-SEC-003 disagree on a plot point:

1. Check PHM-SEC-004 (Wikipedia) for a higher-level corroboration.
2. If unresolvable, note the discrepancy inline in the chapter note with `> [!note] Source conflict: ...`.
3. Do not invent a resolution — mark it as pending primary-source verification.

---

## Related

- [[Weir 2021 - Project Hail Mary Novel]] — Primary source registration; legal-copy blocker documented
- [[Chapter Index]] — MOC for all 31 chapter notes
- [[Novel Ingestion Guide]] — Secondary mode workflow and primary upgrade path
- [[Sources Index]] — Full bibliography