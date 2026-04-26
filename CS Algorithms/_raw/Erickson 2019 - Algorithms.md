---
id: raw-csa-002
type: raw
title: "Algorithms"
author: "Jeff Erickson"
year: 2019
publisher: "Self-published (open access)"
url: "https://jeffe.cs.illinois.edu/teaching/algorithms/"
status: processed
chunk_count: 6
tags:
  - csa
  - raw
  - open-access
up: "[[CS Algorithms]]"
---
# Erickson 2019 — Algorithms

## Bibliographic Reference

Erickson, Jeff. *Algorithms*. Self-published, 2019. Available free at https://jeffe.cs.illinois.edu/teaching/algorithms/

## Description

Erickson's *Algorithms* is a freely available, full-length textbook used at UIUC (University of Illinois Urbana-Champaign) for their advanced algorithms course. The book covers recursion and induction, backtracking, dynamic programming, greedy algorithms, graphs (BFS, DFS, shortest paths, spanning trees), and NP-hardness. It is particularly strong on correctness proofs — loop invariants, cut invariants, and exchange arguments are treated with greater rigour than Cormen's *Algorithms Unlocked*.

## Why It Matters

- **Open access**: freely downloadable PDF; no paywalls; perpetually available.
- **Proof depth**: provides deeper correctness arguments (e.g., Dijkstra cut invariant, loop-invariant technique with quantified loop variables) that complement Cormen's more intuitive treatment.
- **NP-hardness**: thorough reduction-based NP-hardness proofs and Rice's Theorem generalisation are in scope.
- **Course-tested**: widely assigned at top universities; worked examples are vetted through years of problem-set feedback.

## Chunk Candidates

| Chunk Topic | Target Wiki Notes |
|---|---|
| Strong loop invariants coupling loop variable to measurable quantity | [[Loop Invariant]] |
| NP-hardness via polynomial reduction from known NP-hard problem | [[NP Completeness]], [[P vs NP]] |
| Dijkstra cut invariant correctness proof | [[Dijkstra's Algorithm]] |
| Rice's Theorem — all non-trivial semantic properties of programs are undecidable | [[Halting Problem]] |
| Floyd-Warshall negative-cycle diagonal test | [[Floyd-Warshall Algorithm]], [[Shortest Path Overview]] |
| LZW patent history and PNG/DEFLATE context | [[LZW Compression]] |

## Related Wiki Notes

- [[Loop Invariant]] — proof technique treated at greater depth here than in Cormen
- [[Dijkstra's Algorithm]] — cut invariant formalises the greedy correctness argument
- [[NP Completeness]] — reduction-based NP-hardness proof strategy
- [[Halting Problem]] — Rice's Theorem as a generalisation of undecidability
- [[Floyd-Warshall Algorithm]] — negative-cycle diagonal detection
- [[Recurrence Relations]], [[Master Theorem]] — three-case Master Theorem

## Chunks Created This Wave

- [[Analysis - Strong loop invariants couple the loop variable to a measurable quantity]] (chunk-csa-038)
- [[Complexity - Rice's Theorem shows all non-trivial semantic program properties are undecidable]] (chunk-csa-040)
- [[Complexity - NP-hardness is established by polynomial reduction from a known NP-hard problem]] (chunk-csa-041)
- [[Graphs - Dijkstra's algorithm maintains a cut invariant that guarantees correctness on non-negative graphs]] (chunk-csa-043)
- [[Graphs - Floyd-Warshall negative-cycle detection uses the diagonal of the distance matrix]] (chunk-csa-048)
- [[Compression - LZW patent history and PNG DEFLATE choice illustrate how IP affects algorithm adoption]] (chunk-csa-050)
