---
tags:
  - csos
  - query
up: "[[CS Operating Systems/_queries/QnA System Roadmap|QnA System Roadmap]]"
---
# QnA — Chapter Coverage

## Purpose

Track which chapters of *Modern Operating Systems* (Tanenbaum, 4th ed.) have been seeded with summary notes and chunks. Use this to identify where to focus next extraction effort.

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual table below.

```dataview
TABLE chapter, status, chunk_count
FROM "CS Operating Systems/Books/Modern Operating Systems/Chapters"
WHERE type = "book-chapter"
SORT chapter ASC
```

## Manual Search Fallback

```
path:"CS Operating Systems/Books" tag:#book-chapter
```

## Current Coverage

| # | Chapter | Status | Chunks | Note |
|---|---------|--------|--------|------|
| 1 | Introduction | seeded | 5 | [[MOS - Chapter 01]] |
| 2 | Processes and Threads | seeded | 10 | [[MOS - Chapter 02]] |
| 3 | Memory Management | seeded | 6 | [[MOS - Chapter 03]] |
| 4 | File Systems | seeded | 5 | [[MOS - Chapter 04]] |
| 5 | Input/Output | seeded | 5 | [[MOS - Chapter 05]] |
| 6 | Deadlocks | seeded | 4 | [[MOS - Chapter 06]] |
| 7 | Virtualization and the Cloud | seeded | 3 | [[MOS - Chapter 07]] |
| 8 | Multiple Processor Systems | seeded | 4 | [[MOS - Chapter 08]] |
| 9 | Security | seeded | 5 | [[MOS - Chapter 09]] |
| 10 | Case Study 1: UNIX, Linux, Android | seeded | 3 | [[MOS - Chapter 10]] |
| 11 | Case Study 2: Windows 8 | seeded | 2 | [[MOS - Chapter 11]] |
| 12 | Operating System Design | seeded | 2 | [[MOS - Chapter 12]] |

**All 12 chapters have at least one chapter note. Total chunks: 54.**

## Next Steps

Chapters with the fewest chunks (11 and 12 at 2 each) are candidates for next extraction round. Chapter 2 (Processes and Threads) is the densest chapter and warrants further deepening (readers-writers, POSIX threads, more scheduling detail).
