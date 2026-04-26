---
tags: [cs-ds, chunk]
id: chunk-ds-153
source: "[[raw-ds-012]]"
supports: ["[[Disjoint Sets and Union-Find]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Union-Find solves dynamic connectivity in near O1 per query

## Context
Dynamic connectivity asks whether two elements are in the same set as unions occur.

## Claim
Union-Find with path compression and union by rank answers connectivity queries in O(alpha(n)) amortized which is practically O(1). No other data structure matches this for the union-find problem.

## Why It Matters
The definitive solution for online connectivity: Kruskal MST, percolation simulation, image segmentation.

## QnA Seeds
- Q: Is O(alpha(n)) proven optimal? -> A: Yes. Fredman and Saks proved omega(alpha(n)) lower bound for union-find.
- Q: Can it handle disconnects? -> A: No. Standard UF only supports union not split. Link-cut trees handle dynamic connectivity.
