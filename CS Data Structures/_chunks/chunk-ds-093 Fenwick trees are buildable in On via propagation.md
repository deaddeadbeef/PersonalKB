---
tags: [cs-ds, chunk]
id: chunk-ds-093
source: "[[raw-ds-014]]"
supports: ["[[Fenwick Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Fenwick trees are buildable in On via prefix-sum propagation

## Context
Naive Fenwick construction does n update operations each O(log n) for O(n log n).

## Claim
Optimal O(n) construction propagates each elements value to its parent using the lowest-set-bit relationship: after setting tree[i] = a[i] add tree[i] to tree[i + lowbit(i)].

## Why It Matters
Reduces initialization cost and demonstrates deep understanding of the implicit tree structure.

## QnA Seeds
- Q: How does parent propagation work? -> A: tree[i + (i AND -i)] += tree[i] for each i from 1 to n.
- Q: Why not just call update n times? -> A: That gives O(n log n). Direct propagation is O(n).
