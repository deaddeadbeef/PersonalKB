---
id: raw-2013-001
type: raw
title: "Algorithms Unlocked"
author: "Thomas H. Cormen"
year: 2013
publisher: "MIT Press"
url: ""
status: processed
chunk_count: 37
tags:
  - csa
  - raw
up: "[[CS Algorithms]]"
---
# Cormen 2013 — Algorithms Unlocked

## What This Source Is

A book (printed and EPUB) — a concise, reader-friendly introduction to algorithms for non-specialists. 10 chapters, roughly 240 pages. Aimed at practitioners and curious general readers rather than CS graduate students. Companion to the comprehensive *Introduction to Algorithms* (CLRS) by the same lead author.

Local copy: `C:\Users\fpan1\Downloads\Algorithms Unlocked - Thomas H. Cormen.epub`

## Why It Matters to CS Algorithms

This book is the **primary source** for this knowledge base. It covers every major topic area: correctness and asymptotic analysis, comparison and non-comparison sorting, graph algorithms (DAG, Dijkstra, Bellman-Ford, Floyd-Warshall), string algorithms (LCS, edit distance, KMP), cryptography (substitution ciphers, RSA), data compression (Huffman, LZW), and complexity theory (P vs NP, NP-completeness, undecidability). The accessible style makes it ideal for building intuition before consulting CLRS for deeper proofs.

## Key Takeaways

- Algorithm choice matters as much as hardware — an O(n lg n) sort on a slow machine beats O(n²) on a 1000× faster machine once n = 10 million.
- Asymptotic notation abstracts away constants; only the dominant term of the growth function determines scalability.
- Many important algorithms (Dijkstra, Huffman, topological sort) are greedy — locally optimal choices yield globally optimal results under the right conditions.
- The P vs NP question is the deepest open problem in computer science; no polynomial algorithm is known for any NP-complete problem.
- Cryptographic security can rely on mathematical hardness (integer factorisation for RSA) rather than algorithm secrecy.

## Chunk Candidates

- [x] Algorithm definition and correctness spectrum
- [x] Algorithm choice matters as much as hardware (order of growth)
- [x] Asymptotic notation — Θ, O, Ω — and why constants are dropped
- [x] Loop invariants as a correctness proof technique
- [x] RAM model of computation
- [x] Divide-and-conquer recurrence relation
- [x] Dynamic programming — overlapping subproblems, bottom-up tabulation
- [x] Binary search — O(lg n) on sorted arrays
- [x] Selection sort — always Θ(n²), n−1 swaps
- [x] Insertion sort — Θ(n) best case; adaptive
- [x] Ω(n lg n) lower bound for comparison sorts (decision-tree proof)
- [x] Counting sort — linear time via bounded integer keys
- [x] Radix sort — LSD-first multi-pass with stable subroutine
- [x] Merge sort — guaranteed Θ(n lg n), O(n) auxiliary space
- [x] Quicksort — partition-based; fast in practice, Θ(n²) worst case
- [x] Topological sort — Kahn's algorithm, Θ(n+m)
- [x] PERT critical path — longest path in task-duration DAG
- [x] DAG shortest paths — topological-order relaxation
- [x] Dijkstra's algorithm — greedy, non-negative weights
- [x] Bellman-Ford — handles negatives, detects negative cycles
- [x] Floyd-Warshall — all-pairs DP, Θ(n³)
- [x] LCS dynamic programming recurrence
- [x] Edit distance recurrence — DP over string prefixes
- [x] Edit distance DP table — Θ(mn) time and space
- [x] KMP failure function and matching time
- [x] Substitution ciphers — frequency analysis vulnerability; motivation for stronger cryptography
- [x] One-time pad — perfect secrecy, impractical key size
- [x] RSA — key generation, encrypt/decrypt, factoring hardness
- [x] Hybrid encryption — public-key exchange + symmetric bulk
- [x] Pseudorandom bit generation — PRBG from short seed; why poor randomness undermines security
- [x] Huffman coding — greedy optimal prefix-free code
- [x] Run-length encoding — count-symbol pairs; linear time
- [x] Graph representation — adjacency lists vs adjacency matrices, in-degree (Chapter 5)
- [x] NP-completeness — Cook-Levin theorem, reduction chains
- [x] Approximation algorithms — α-approximation for NP-complete problems
- [x] Halting Problem undecidability via diagonalisation

## Related Wiki Notes

- [[Algorithm Definition]] — Chapter 1 core concept
- [[Asymptotic Notation]] — Chapters 1–2 core concept
- [[Loop Invariant]] — Chapter 2 proof technique
- [[Dynamic Programming]] — Chapters 2, 5, 6, 7 design paradigm
- [[Sorting Overview]] — Chapters 3–4
- [[Selection Sort]] — Chapter 3
- [[Insertion Sort]] — Chapter 3
- [[Merge Sort]] — Chapter 3
- [[Quicksort]] — Chapter 3
- [[Binary Search]] — Chapter 3
- [[Counting Sort]] — Chapter 4
- [[Radix Sort]] — Chapter 4
- [[Comparison Sort Lower Bound]] — Chapter 4
- [[Recurrence Relations]] — Chapter 2
- [[Graph Fundamentals]] — Chapter 5 prerequisites
- [[DAG and Topological Sort]] — Chapter 5
- [[Dijkstra's Algorithm]] — Chapter 6
- [[Bellman-Ford Algorithm]] — Chapter 6
- [[Floyd-Warshall Algorithm]] — Chapter 6
- [[LCS - Longest Common Subsequence]] — Chapter 7
- [[Edit Distance]] — Chapter 7
- [[String Matching - KMP]] — Chapter 7
- [[Cryptography Foundations]] — Chapter 8
- [[RSA Algorithm]] — Chapter 8
- [[Random Number Generation]] — Chapter 8
- [[Data Compression Overview]] — Chapter 9
- [[Huffman Coding]] — Chapter 9
- [[Run-Length Encoding]] — Chapter 9
- [[LZW Compression]] — Chapter 9
- [[P vs NP]] — Chapter 10
- [[NP Completeness]] — Chapter 10
- [[Approximation Algorithms]] — Chapter 10
- [[Halting Problem]] — Chapter 10

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Sources Index]].
