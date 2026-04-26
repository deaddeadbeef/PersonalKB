---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Graph Representations"
authors: [Jeff Erickson]
year: 2019
up: "[[Sources Index]]"
---

# Graph Representations

## Summary

Graphs use adjacency lists (O(V+E) space, efficient for sparse), adjacency matrices (O(V^2) space, O(1) edge query), or edge lists. Most real-world graphs are sparse, making adjacency lists the default. CSR format optimizes for cache performance on static graphs.

## Key Claims

1. Adjacency lists are optimal for sparse graphs
2. Adjacency matrices provide O(1) edge queries
3. Sparse/dense threshold is approximately E = V^2/log V
4. Representation choice directly affects algorithm performance
5. CSR optimizes adjacency lists for cache performance

## Atomic Facts

1. Adj list: iterate neighbors O(deg(v)), edge query O(deg(v))
2. Adj matrix: edge query O(1), iterate neighbors O(V)
3. Edge list: O(E) space, useful for Kruskal's MST
4. CSR: two arrays (offsets + neighbors), cache-efficient
5. Most real-world graphs are sparse
6. Directed graphs: separate in-neighbor and out-neighbor lists

## Significance

The choice of graph representation is one of the most impactful design decisions in graph algorithm implementation.

## Chunks Extracted

*Pending*
