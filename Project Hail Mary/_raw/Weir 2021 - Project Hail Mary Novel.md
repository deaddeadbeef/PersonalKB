---
id: raw-novel-001
type: raw
title: "Project Hail Mary (Novel)"
author: "Weir, Andy"
year: 2021
url: ""
status: ingestion-complete
source_file: "D:\\Sources\\ProjectHailMary\\Weir 2021 - Project Hail Mary.epub"
format: epub
ocr_note: "OCR-scanned EPUB. Embedded chapter headings are unreliable (systematic off-by-one errors in chapter numbers; some headings garbled or absent). chapter_map.json is the authoritative navigation source."
chunk_count: 4
tags:
  - phm
  - raw
  - novel
up: "[[Sources Index]]"
---
# Weir 2021 — Project Hail Mary Novel

## What This Source Is

The primary novel: Andy Weir, *Project Hail Mary* (Ballantine Books, 2021). Science fiction novel combining hard-science problem-solving with first-contact xenobiology. This is the foundational source for the entire knowledge base — every wiki note ultimately derives from or comments on content in this book.

## Why It Matters to PHM

All other sources in `_raw/` provide external validation or context for claims in the novel. The novel itself is the only source for plot structure, character decisions, in-universe science descriptions, and the primary narrative. Chapter-level analysis enables:

- Tracking which science concepts appear where in the story
- Mapping the dual-timeline structure (present-day mission vs. flashback recruitment)
- Extracting chunk-worthy claims directly from Weir's descriptions
- Supporting the adaptation comparison with precise chapter references

## Current Status

**Primary-ingestion pass complete; defect-fix pass complete.** The source EPUB is staged externally and all 31 chapter notes have been upgraded to `source_mode: primary`. A post-Phase-8 defect-fix pass resolved: Ch20 duplicate content (replaced with verified pp. 372–394); Ch13 summary self-reference typo; Epilogue Beetle-launch chapter cross-reference; Ch16 and Ch27 overlong quote blocks.

> **Vault-side pointer — canonical external EPUB path:**
> `D:\Sources\ProjectHailMary\Weir 2021 - Project Hail Mary.epub`
>
> The EPUB file itself is **not inside this vault and must never be placed here.** Vault storage of full-length copyrighted source files violates fair-use scope and would bloat any sync target. This `_raw` note serves as the authoritative vault-side pointer to that external file. Any session needing to re-read the source navigates to `D:\Sources\ProjectHailMary\` on the local machine.

- **Source file (external):** `D:\Sources\ProjectHailMary\Weir 2021 - Project Hail Mary.epub` (1.8 MB, OCR scan)
- **Format:** EPUB — OCR scan; see OCR note in frontmatter
- **Navigation:** `D:\Sources\ProjectHailMary\chapter_map.json` (authoritative; EPUB nav.xhtml and toc.ncx are empty)
- **Helper scripts:** `discover_chapters.py`, `extract_chapter.py` in the same staging folder

> **Compliance note:** The full text of the novel must never be stored inside this vault. Only short fair-use quotes (1–2 sentences) and original summaries are permitted in chapter notes and chunks.

## Chapter Layer — Primary Ingestion Complete

The primary EPUB source has been fully processed. All 31 chapter notes (Ch 01–30 + Epilogue) have been upgraded from **secondary mode to primary mode**. Every note now has:
- Verified summary against the primary EPUB text
- Direct quotes (fair use: 1–2 sentences, max 3 per chapter, with page numbers)
- `source_mode: primary` and `quotes_pending: false`
- `status: processed`

**Remaining work:** Chunk extraction for candidates identified during the primary pass. Each chapter note's Chunk Candidates section lists specific claims ready for extraction into `_chunks/`. Secondary-mode notes that formed the bootstrap scaffold have been superseded; the [[PHM Chapter Summaries - Secondary Sources Registry]] documents those original sources for reference only.

## Chunk Candidates

Chunk extraction depends on chapter-level processing. Candidates are identified per chapter in each `PHM Novel - Chapter NN` note. Secondary-mode chapters may identify candidates for extraction, but chunk content must be paraphrase-only until primary-mode verification.

## Related Wiki Notes

- [[Chapter Index]] — MOC for chapter-level notes (bootstrap layer in progress)
- [[Novel Ingestion Guide]] — Processing workflow, secondary mode, and upgrade path
- [[PHM Chapter Summaries - Secondary Sources Registry]] — Public sources used for chapter bootstrap
- [[Novel vs Film Adaptation]] — Requires chapter references for comparison
- [[Project Hail Mary]] — Master MOC