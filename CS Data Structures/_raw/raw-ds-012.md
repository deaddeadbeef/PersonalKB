---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Union-Find Disjoint Sets"
authors: [Jeff Erickson]
year: 2019
up: "[[Sources Index]]"
---

# Union-Find (Disjoint Sets)

## Summary

Union-Find maintains disjoint sets with MakeSet, Find, Union. Tree-based with union by rank and path compression achieving O(alpha(n)) amortized -- effectively constant. Inverse Ackermann alpha(n) <= 4 for all practical n. Optimal per Fredman-Saks lower bound.

## Key Claims

1. Union by rank + path compression gives O(alpha(n)) amortized
2. Inverse Ackermann alpha(n) <= 4 for any practical input
3. This bound is optimal (proven lower bound)
4. Path compression alone gives O(log n) amortized
5. Both optimizations together are necessary for near-constant time

## Atomic Facts

1. MakeSet: single-element tree, O(1)
2. Find: follow parent pointers to root, apply path compression
3. Union: link shorter tree under taller tree
4. alpha(n) <= 4 for n up to 2^(2^(2^65536))
5. Applications: Kruskal's MST, connected components
6. Tarjan, 1975: proved the amortized bound

## Significance

Union-Find is one of the most elegant data structures in computer science, achieving near-constant time for dynamic connectivity through two simple optimizations.

## Chunks Extracted

*Pending*
