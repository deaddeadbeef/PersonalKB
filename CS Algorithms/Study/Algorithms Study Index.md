---
tags:
  - csa
  - csa/study
up: "[[CS Algorithms]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---
# Algorithms Study Index

Central index for all CS Algorithms active-recall drill notes. Each drill note covers one domain of the wiki, distilled into questions, contrasts, and common-mistake warnings. Use this index to plan review sessions and track which areas need more repetitions.

## Start Here By Goal

Do not start with drills unless you are already reviewing. Use this page to choose the next kind of work.

| Goal | Start with | Then use | Proof you should leave behind |
|---|---|---|---|
| Read algorithms as a book | [[CS Algorithms/CS Algorithms Book Reading Spine|CS Algorithms Book Reading Spine]] | [[CS Algorithms/Analysis/Foundations and Analysis Overview|Foundations and Analysis Overview]], [[CS Algorithms/Techniques/Techniques Overview|Techniques Overview]] | A one-page map from problem shape to algorithm family |
| Choose an algorithm for implementation | [[CS Algorithms/Study/Algorithm Complexity Cheatsheet|Algorithm Complexity Cheatsheet]] | [[CS Algorithms/Graphs/Graphs Overview|Graphs Overview]], [[CS Algorithms/Strings/Strings Overview|Strings Overview]], [[CS Algorithms/Compression/Data Compression Overview|Data Compression Overview]] | A constraint table: input size, graph/string/data shape, cost target, and failure mode |
| Prove or explain a cost bound | [[CS Algorithms/Analysis/Foundations and Analysis Overview|Foundations and Analysis Overview]] | [[CS Algorithms/Complexity/Complexity Theory Overview|Complexity Theory Overview]], [[CS Algorithms/Divide and Conquer/Divide and Conquer Overview|Divide and Conquer Overview]] | A recurrence, invariant, reduction, or lower-bound explanation in your own words |
| Prepare for recall | [[CS Algorithms/Study/Foundations and Analysis - Review Drill|Foundations and Analysis - Review Drill]] | The matching drill note in the table below | A list of missed questions and the canonical pages reopened to fix them |

---

## How to Use

1. **First pass** — read through a drill note once to surface gaps. If you cannot answer a question without looking, mark it (e.g., highlight or add a `?` comment).
2. **Spaced repetition** — revisit marked questions on subsequent days. The questions are written for retrieval practice, not re-reading.
3. **Check against the wiki** — each note links back to the canonical page. After struggling with a question, open the canonical page for the full explanation, then close it and try again.
4. **Cross-domain sessions** — for a broad review, pick one question from each drill note in a single sitting.

---

## Drill Notes by Domain

| Drill Note | Canon pages covered | Difficulty focus |
|-----------|---------------------|-----------------|
| [[Foundations and Analysis - Review Drill]] | Algorithm Definition, Asymptotic Notation, Loop Invariant, Comparison Sort Lower Bound, Dynamic Programming, Recurrence Relations, Master Theorem | Notation precision; proof structure |
| [[Sorting and Searching - Review Drill]] | Sorting Overview, Merge Sort, Quicksort, Counting Sort, Radix Sort, Selection Sort, Insertion Sort, Inversions, Binary Search | Complexity trade-offs; inversion analysis |
| [[Graphs and Shortest Paths - Review Drill]] | Graph Fundamentals, DAG and Topological Sort, Shortest Path Overview, Dijkstra's Algorithm, Bellman-Ford Algorithm, Floyd-Warshall Algorithm | Algorithm selection; negative-weight handling |
| [[Strings - Review Drill]] | LCS - Longest Common Subsequence, Edit Distance, String Matching - KMP | DP table construction; failure function |
| [[Cryptography - Review Drill]] | Cryptography Foundations, RSA Algorithm, Random Number Generation | Security definitions; RSA mechanics |
| [[Data Compression - Review Drill]] | Data Compression Overview, Huffman Coding, Run-Length Encoding, LZW Compression | Greedy optimality; adaptive coding |
| [[Complexity Theory - Review Drill]] | P vs NP, NP Completeness, Halting Problem, Approximation Algorithms | Reductions; approximation ratio proofs |

---

## Mapping to the Canonical Wiki

The drill notes shadow the domain structure of the root [[CS Algorithms]] MOC:

```
CS Algorithms (root)
├── Foundations and Analysis  →  Foundations and Analysis - Review Drill
├── Sorting and Searching     →  Sorting and Searching - Review Drill
├── Graphs and Shortest Paths →  Graphs and Shortest Paths - Review Drill
├── Strings                   →  Strings - Review Drill
├── Cryptography              →  Cryptography - Review Drill
├── Data Compression          →  Data Compression - Review Drill
└── Complexity Theory         →  Complexity Theory - Review Drill
```

Each drill note uses `up: [[Algorithms Study Index]]` and provides `## Links Back` to the specific canonical pages it covers.

---

## Session Patterns

| Goal | Pattern |
|------|---------|
| Full domain review | Open one drill note; answer all Core Recall questions cold |
| Quick refresh | Open index; pick 3 questions from two different drill notes |
| Pre-exam sweep | Work through all Compare and Contrast sections across all notes |
| Gap-finding | Focus on any question where you cannot state the answer in one sentence |

---

## Notes

- Content is distilled from the `_chunks/` layer and canonical wiki pages; go there for proofs and derivations.
- These notes are intentionally concise — the goal is retrieval, not re-explanation.
- Update drill notes when canonical pages are substantially deepened.

## References

- [[CS Algorithms/CS Algorithms]]
- [[CS Algorithms/Sources/Sources Index]]
