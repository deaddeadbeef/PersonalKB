---
tags: [cs-algorithms, query]
up: "[[CS Algorithms/_queries/QnA System Roadmap|QnA System Roadmap]]"
---
# QnA — Chunk Coverage Map

## Purpose

See which canonical wiki notes have supporting chunks and which still have gaps. Use this to identify where the evidence base needs strengthening.

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual approach below.

**Chunks grouped by the wiki notes they support:**

```dataview
TABLE rows.claim AS "Supporting Claims", rows.confidence AS "Confidence"
FROM "CS Algorithms/_chunks"
FLATTEN supports AS supported_note
GROUP BY supported_note
```

**All chunks by topic:**

```dataview
TABLE claim, confidence, source
FROM "CS Algorithms/_chunks"
WHERE type = "chunk"
SORT topic ASC, claim ASC
```

## Manual Search Fallback

**Find all chunks supporting a specific wiki note:**
1. Open the wiki note (e.g., [[Dijkstra's Algorithm]]).
2. Open the backlinks pane — all chunk notes linking to it appear there.

**Find all chunks by topic:**
```
path:"CS Algorithms/_chunks" topic: graphs
```

## Current Coverage (Wave 1–2)

Existing chunks (001–060) from original build and initial expansion:

| Wiki Note | Chunk Count |
|-----------|-------------|
| [[Algorithm Definition]] | 3 |
| [[Asymptotic Notation]] | 3 |
| [[Loop Invariant]] | 2 |
| [[Comparison Sort Lower Bound]] | 3 |
| [[Dynamic Programming]] | 3 |
| [[Recurrence Relations]] | 2 |
| [[Master Theorem]] | 2 |
| [[Sorting Overview]] | 8 |
| [[Inversions]] | 2 |
| [[Selection Sort]] | 3 |
| [[Insertion Sort]] | 3 |
| [[Merge Sort]] | 2 |
| [[Quicksort]] | 2 |
| [[Counting Sort]] | 2 |
| [[Radix Sort]] | 3 |
| [[Binary Search]] | 3 |
| [[DAG and Topological Sort]] | 3 |
| [[Graph Fundamentals]] | 2 |
| [[Dijkstra's Algorithm]] | 2 |
| [[Bellman-Ford Algorithm]] | 2 |
| [[Floyd-Warshall Algorithm]] | 2 |
| [[Shortest Path Overview]] | 6 |
| [[LCS - Longest Common Subsequence]] | 2 |
| [[Edit Distance]] | 3 |
| [[String Matching - KMP]] | 2 |
| [[Cryptography Foundations]] | 5 |
| [[RSA Algorithm]] | 2 |
| [[Random Number Generation]] | 2 |
| [[Data Compression Overview]] | 3 |
| [[Huffman Coding]] | 2 |
| [[Run-Length Encoding]] | 2 |
| [[LZW Compression]] | 2 |
| [[P vs NP]] | 3 |
| [[NP Completeness]] | 4 |
| [[Halting Problem]] | 2 |
| [[Approximation Algorithms]] | 3 |

**Total existing chunks: 60** across 36 canonical wiki pages. All pages meet the 2-chunk minimum target.

## Wave 3 — Expected Chunks (061–200)

140 new chunks to be extracted from raw notes 006–040. Expected allocation by raw note:

| Raw Note | Topic | Expected Chunks |
|----------|-------|-----------------|
| [[raw-algo-006]] | Quicksort Analysis | 4 |
| [[raw-algo-007]] | Mergesort and Divide-and-Conquer | 4 |
| [[raw-algo-008]] | Binary Search and Variants | 4 |
| [[raw-algo-009]] | Hash Tables | 4 |
| [[raw-algo-010]] | BSTs and AVL Trees | 4 |
| [[raw-algo-011]] | Heap and Priority Queue | 4 |
| [[raw-algo-012]] | Dijkstra's Shortest Path | 4 |
| [[raw-algo-013]] | Bellman-Ford and Negative Weights | 4 |
| [[raw-algo-014]] | BFS and DFS Graph Traversal | 4 |
| [[raw-algo-015]] | Minimum Spanning Trees | 4 |
| [[raw-algo-016]] | Dynamic Programming Principles | 4 |
| [[raw-algo-017]] | String Matching Algorithms | 4 |
| [[raw-algo-018]] | NP-Completeness Theory | 4 |
| [[raw-algo-019]] | Amortized Analysis | 4 |
| [[raw-algo-020]] | Randomized Algorithms | 4 |
| [[raw-algo-021]] | Floyd-Warshall | 4 |
| [[raw-algo-022]] | Network Flow: Ford-Fulkerson | 4 |
| [[raw-algo-023]] | Union-Find / Disjoint Sets | 4 |
| [[raw-algo-024]] | Counting Sort and Radix Sort | 4 |
| [[raw-algo-025]] | B-Trees and External Memory | 4 |
| [[raw-algo-026]] | Greedy Algorithms | 4 |
| [[raw-algo-027]] | Backtracking and Branch-and-Bound | 4 |
| [[raw-algo-028]] | Approximation Algorithms | 4 |
| [[raw-algo-029]] | Computational Geometry | 4 |
| [[raw-algo-030]] | Segment Trees and Range Queries | 4 |
| [[raw-algo-031]] | Trie Data Structure | 4 |
| [[raw-algo-032]] | Suffix Arrays and Trees | 4 |
| [[raw-algo-033]] | Red-Black Trees | 4 |
| [[raw-algo-034]] | Skip Lists | 4 |
| [[raw-algo-035]] | Bloom Filters | 4 |
| [[raw-algo-036]] | Kadane's Algorithm | 4 |
| [[raw-algo-037]] | Topological Sort | 4 |
| [[raw-algo-038]] | Strongly Connected Components | 4 |
| [[raw-algo-039]] | FFT and Polynomial Multiplication | 4 |
| [[raw-algo-040]] | Linear Programming | 4 |

**Expected total after Wave 3: 200 chunks** (60 existing + 140 new).

## Notes

- This coverage map should be updated as new chunks are added.
- With Dataview installed, the table auto-updates; without it, maintain manually.
- Wave 3 allocates 4 chunks per raw note as a baseline; actual counts may vary by topic depth.
- Target: every wiki page has at least 2 supporting chunks before considering the topic mature.
