---
tags: [cs-ds, chunk]
id: chunk-ds-091
source: "[[raw-ds-012]]"
supports: ["[[Disjoint Sets and Union-Find]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Path splitting and path halving are practical alternatives to full compression

## Context
Full path compression flattens the entire find path to the root in one pass.

## Claim
Path splitting makes every node on the find path point to its grandparent. Path halving makes every other node point to its grandparent. Both achieve O(alpha(n)) amortized while being simpler to implement than full compression.

## Why It Matters
Path halving is often preferred in practice for its single-pass simplicity. Used in many library implementations.

## QnA Seeds
- Q: How does path splitting differ from full compression? -> A: Each node points to grandparent not root. Still flattens over time.
- Q: Do they achieve same bound? -> A: Yes all three give O(alpha(n)) amortized with union by rank.
