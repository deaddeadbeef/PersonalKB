---
tags: [cs-ds, chunk]
id: chunk-ds-118
source: "[[raw-ds-032]]"
supports: ["[[Graphs Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Boruvkas algorithm is naturally parallelizable for MST

## Context
Kruskal and Prim are inherently sequential.

## Claim
Boruvka finds the cheapest edge leaving each component simultaneously then contracts components. Each round halves the number of components giving O(log V) rounds each costing O(E). Total O(E log V).

## Why It Matters
Natural fit for parallel and distributed MST computation. Used in parallel graph processing frameworks.

## QnA Seeds
- Q: Why parallelizable? -> A: Finding cheapest edge per component is independent across components.
- Q: How many rounds? -> A: O(log V) since each round at least halves the component count.
