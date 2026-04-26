---
id: chunk-algo-115
type: chunk
source: "[[raw-algo-019]]"
source_loc: "Amortized Analysis - Atomic Facts"
topic: "amortized-analysis"
claim: "Fibonacci heaps use potential Phi = t + 2m (t=trees, m=marked nodes) to achieve O(1) amortized insert, O(1) amortized decrease-key, and O(log n) amortized extract-min, with cascading cuts ensuring O(log n) trees after consolidation."
confidence: verified
supports:
  - "[[Amortized Analysis]]"
  - "[[Fibonacci Heaps]]"
tags:
  - cs-algorithms
  - cs-algorithms/amortized-analysis
  - chunk
up: "[[CS Algorithms]]"
---
# Fibonacci Heap O(1) Amortized Insert and Decrease-Key

## Context

Insert adds a new root tree (O(1), potential +1). Decrease-key cuts the node to a new root; cascading cuts propagate when a node loses its second child. Each cascading cut reduces m by 1, paying for its O(1) work. Extract-min consolidates trees by linking equal-degree trees, reducing t to O(log n) at actual cost O(t) offset by potential drop. This makes Fibonacci heaps optimal for Dijkstra: O(V log V + E) vs O(E log V) with binary heaps.

## Why It Matters

Fibonacci heaps provide the theoretically optimal priority queue for Dijkstra and Prim, reducing their complexity. The cascading cut analysis is one of the most elegant potential method applications.

## QnA Seeds

- Q: What potential function is used for Fibonacci heap analysis?
- Q: Why does decrease-key achieve O(1) amortized in Fibonacci heaps?
- Q: How does consolidation reduce trees to O(log n)?