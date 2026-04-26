---
tags: [cs-ds, chunk]
id: chunk-ds-044
source: "[[raw-ds-032]]"
supports: ["[[Heaps and Priority Queues Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# The MST cut property proves lightest crossing edge must be in MST

## Context
MST algorithms need correctness proof for their greedy choices.

## Claim
For any cut of the graph, the lightest edge crossing the cut must be in every MST (assuming unique weights). This cut property is the foundation for both Kruskal's and Prim's correctness.

## Why It Matters
Unifies the correctness argument for all MST algorithms — greedy is provably optimal.

## QnA Seeds
- Q: What is a cut? -> A: Partition of vertices into two non-empty sets.
- Q: Does the cut property hold with duplicate weights? -> A: It guarantees at least one MST contains the lightest edge.
