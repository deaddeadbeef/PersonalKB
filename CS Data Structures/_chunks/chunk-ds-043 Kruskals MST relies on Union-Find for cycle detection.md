---
tags: [cs-ds, chunk]
id: chunk-ds-043
source: "[[raw-ds-032]]"
supports: ["[[Disjoint Sets and Union-Find]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Kruskals MST relies on Union-Find for cycle detection

## Context
Kruskal's algorithm adds edges in weight order, skipping those creating cycles.

## Claim
Union-Find provides O(alpha(n)) amortized cycle detection: if Find(u) == Find(v), the edge u-v would create a cycle; otherwise Union(u,v) merges their components. Total: O(E log E + E alpha(V)).

## Why It Matters
The standard MST implementation — Union-Find makes the greedy edge selection practical.

## QnA Seeds
- Q: How does Union-Find detect cycles? -> A: If both endpoints are in the same set, adding the edge creates a cycle.
- Q: Why sort edges first? -> A: Greedy: consider cheapest edges first to build minimum spanning tree.
