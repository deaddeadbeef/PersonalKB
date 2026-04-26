---
tags: [cs-ds, raw]
id: raw-ds-035
source: "Various (spatial data structure literature)"
up: "[[CS Data Structures]]"
---

# Range Trees and Multi-Dimensional Search

## Key Ideas
- 1D range query: BST gives O(log n + k) for k results
- Range tree (2D): primary tree on x-coordinate, each node stores secondary tree on y-coordinate
- 2D range query: O(log^2 n + k) time, O(n log n) space
- Fractional cascading: reduces query to O(log n + k) by sharing sorted arrays between levels
- d-dimensional range tree: O(log^d n + k) query, O(n log^{d-1} n) space
- Priority search tree: combines BST on x with heap on y — O(n) space for 3-sided queries
- Layered range tree: alternative to fractional cascading, simpler implementation
- Range tree vs k-d tree: range trees have better worst-case but more space
- k-d tree: O(sqrt(n) + k) query in 2D, O(n) space — better for low dimensions with tight space
- Applications: database range queries, computational geometry, GIS systems

## Construction
- Build primary tree on x-sorted points: O(n log n)
- Build secondary structures during construction
- Cannot be efficiently updated — mostly static structure
