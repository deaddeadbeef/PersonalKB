---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "AVL Trees and Red-Black Trees"
authors: [Pat Morin]
year: 2013
up: "[[Sources Index]]"
---

# AVL Trees and Red-Black Trees

## Summary

AVL trees (1962) maintain balance factor in {-1,0,1} via rotations, guaranteeing height at most 1.44 log2(n). Red-Black trees use node coloring with five invariants, guaranteeing height at most 2 log2(n+1). RB trees need at most 2 rotations on insert, 3 on delete. AVL is better for reads, RB for writes.

## Key Claims

1. AVL trees are more strictly balanced than Red-Black trees
2. Red-Black trees need fewer rotations per mutation (max 3 vs O(log n))
3. Both guarantee O(log n) worst-case operations
4. Red-Black trees are isomorphic to 2-3-4 trees
5. AVL trees have faster lookups due to stricter balancing

## Atomic Facts

1. AVL: Adelson-Velsky and Landis, 1962 -- first self-balancing BST
2. AVL height: h < 1.44 log2(n+2) - 0.328
3. RB height: h <= 2 log2(n+1)
4. RB used in Java TreeMap, C++ std::map, Linux CFS scheduler
5. Left-leaning RB: Sedgewick simplification
6. Fibonacci trees: worst-case AVL structure

## Significance

These two structures represent the primary approaches to BST balancing and are the most widely deployed tree structures in standard libraries.

## Chunks Extracted

*Pending*
