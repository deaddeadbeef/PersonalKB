---
tags:
  - csa
  - query
up: "[[CS Algorithms/_queries/QnA System Roadmap|QnA System Roadmap]]"
---
# QnA — Canonical Coverage

## Purpose

Track which canonical algorithm topics have wiki pages, which are stubs, and which are missing entirely. Identifies gaps in the wiki layer versus the book's scope.

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual approach below.

**All wiki pages by domain folder:**

```dataview
TABLE file.folder AS "Domain", up, tags
FROM "CS Algorithms"
WHERE type != "chunk" AND type != "raw" AND type != "book-chapter" AND type != "template"
SORT file.folder ASC, file.name ASC
```

## Manual Search Fallback

**All wiki pages in the Analysis domain:**
```
path:"CS Algorithms/Analysis"
```

**All wiki pages in the Graphs domain:**
```
path:"CS Algorithms/Graphs"
```

## Current Canonical Coverage

### Analysis

| Page | Status |
|------|--------|
| [[Algorithm Definition]] | ✅ Complete |
| [[Asymptotic Notation]] | ✅ Complete |
| [[Loop Invariant]] | ✅ Complete |
| [[Comparison Sort Lower Bound]] | ✅ Complete |
| [[Dynamic Programming]] | ✅ Complete |
| [[Recurrence Relations]] | ✅ Complete |
| [[Master Theorem]] | ✅ Complete |

### Sorting

| Page | Status |
|------|--------|
| [[Sorting Overview]] | ✅ Complete |
| [[Merge Sort]] | ✅ Complete |
| [[Quicksort]] | ✅ Complete |
| [[Counting Sort]] | ✅ Complete |
| [[Radix Sort]] | ✅ Complete |
| [[Selection Sort]] | ✅ Complete |
| [[Insertion Sort]] | ✅ Complete |
| [[Inversions]] | ✅ Complete |

### Searching

| Page | Status |
|------|--------|
| [[Binary Search]] | ✅ Complete |

### Graphs

| Page | Status |
|------|--------|
| [[Graph Fundamentals]] | ✅ Complete |
| [[DAG and Topological Sort]] | ✅ Complete |
| [[Dijkstra's Algorithm]] | ✅ Complete |
| [[Bellman-Ford Algorithm]] | ✅ Complete |
| [[Floyd-Warshall Algorithm]] | ✅ Complete |
| [[Shortest Path Overview]] | ✅ Complete |

### Strings

| Page | Status |
|------|--------|
| [[LCS - Longest Common Subsequence]] | ✅ Complete |
| [[Edit Distance]] | ✅ Complete |
| [[String Matching - KMP]] | ✅ Complete |

### Cryptography

| Page | Status |
|------|--------|
| [[Cryptography Foundations]] | ✅ Complete |
| [[RSA Algorithm]] | ✅ Complete |
| [[Random Number Generation]] | ✅ Complete |

### Compression

| Page | Status |
|------|--------|
| [[Data Compression Overview]] | ✅ Complete |
| [[Huffman Coding]] | ✅ Complete |
| [[Run-Length Encoding]] | ✅ Complete |
| [[LZW Compression]] | ✅ Complete |

### Complexity

| Page | Status |
|------|--------|
| [[P vs NP]] | ✅ Complete |
| [[NP Completeness]] | ✅ Complete |
| [[Halting Problem]] | ✅ Complete |
| [[Approximation Algorithms]] | ✅ Complete |

## Topics Not Yet Covered (Future Expansion)

| Topic | Suggested Domain | Notes |
|-------|-----------------|-------|
| Heap Sort | Sorting | Referenced in Sorting Overview table but not a dedicated topic in *Algorithms Unlocked* (Ch 3 in CLRS). Future expansion outside this book's direct coverage. |

## Notes

- **36 canonical wiki pages** now created and linked (was 35; +1 from Princeton deepening wave: Inversions).
- Batch-2 additions: Dynamic Programming, Selection Sort, Insertion Sort, Run-Length Encoding, Halting Problem, Approximation Algorithms.
- Wave-2 additions: Master Theorem (Analysis), Shortest Path Overview (Graphs).
- Closure pass additions: Recurrence Relations (Analysis), LZW Compression (Compression), Random Number Generation (Cryptography).
- Princeton deepening wave: Inversions (Sorting) added; Approximation Algorithms, Comparison Sort Lower Bound, Selection Sort, Insertion Sort deepened to 3 chunks each using Princeton Algorithms 4e source.
- Raw sources: 5 total — Cormen 2013 (primary), Erickson 2019, MIT OCW 6.006, CP Algorithms, Princeton Algorithms 4e.
- Heap Sort: not a dedicated topic in *Algorithms Unlocked*; marked as future expansion outside this book's scope.
