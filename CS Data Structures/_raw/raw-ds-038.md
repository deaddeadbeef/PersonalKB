---
tags: [cs-ds, raw]
id: raw-ds-038
source: "Various (Tarjan 1983, Sleator & Tarjan 1985)"
up: "[[CS Data Structures]]"
---

# Leftist, Skew, and Pairing Heaps

## Key Ideas
- Leftist heap: binary heap where left path is always >= right path (s-value)
- Merge is fundamental op: O(log n) by merging along right spines
- Insert = merge with singleton: O(log n)
- Delete-min = merge left and right children of root: O(log n)
- Skew heap: self-adjusting version of leftist heap — swap children after every merge
- Skew heap: O(log n) amortized, simpler than leftist (no s-values needed)
- Pairing heap: multi-way tree, extremely simple implementation
- Pairing heap insert: O(1) — link new node as child of root
- Pairing heap delete-min: O(log n) amortized — pair children then merge
- Pairing heap decrease-key: O(1) amortized (conjectured, proven O(log log n))
- Pairing heap vs Fibonacci: simpler, comparable empirical performance, weaker theoretical bounds
- Brodal queue: worst-case O(1) insert, O(1) decrease-key, O(log n) delete-min — theoretical breakthrough

## Practical Recommendation
- Binary heap: default choice for simplicity and cache performance
- Pairing heap: when decrease-key frequency is high and code simplicity matters
- Fibonacci heap: rarely worth the implementation complexity
