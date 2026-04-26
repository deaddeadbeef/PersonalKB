---
tags: [cs-ds, raw]
id: raw-ds-026
source: "Introduction to Algorithms (CLRS, Ch. 14)"
up: "[[CS Data Structures]]"
---

# Interval Trees and Augmented Structures

## Key Ideas
- Augmented BST: store extra information at each node derived from subtree
- Order-statistic tree: augment with subtree size → O(log n) rank/select
- Interval tree: store intervals [lo, hi], augment with max endpoint in subtree
- Interval search: find any interval overlapping query — O(log n)
- All overlapping intervals: O(k log n) where k is number of results
- Augmentation theorem: if extra info is computable from node + children, rotations maintain it
- Range tree: multi-dimensional point queries via nested trees
- 2D range tree: O(log^2 n) query, O(n log n) space
- Fractional cascading: reduces query by log factor via shared sorted lists
- Priority search tree: combines heap and BST for 3-sided range queries

## Applications
- Calendar scheduling: find conflicting meetings
- Computational geometry: line segment intersection
- Database query optimization: range predicates on indexed columns
