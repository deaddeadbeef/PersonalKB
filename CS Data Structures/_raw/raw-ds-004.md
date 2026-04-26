---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Binary Search Trees"
authors: [Pat Morin]
year: 2013
up: "[[Sources Index]]"
---

# Binary Search Trees

## Summary

BSTs maintain left < root < right invariant enabling O(log n) average search/insert/delete. Worst case O(n) when skewed. In-order traversal yields sorted output. Deletion with two children requires in-order successor replacement.

## Key Claims

1. BST operations are O(h) where h is tree height
2. Average height of random BST is O(log n) but worst case is O(n)
3. In-order traversal produces sorted output in O(n)
4. BST insertion mirrors quicksort partition sequence
5. Self-balancing variants are needed for O(log n) guarantees

## Atomic Facts

1. Deletion: leaf (remove), one child (bypass), two children (swap with successor)
2. Successor: leftmost node in right subtree
3. Random BST expected height: 4.311 ln(n)
4. Supports ordered ops: min, max, predecessor, successor, range query
5. Degenerate BST from sorted insertion becomes a linked list
6. Equivalent to binary search on a dynamic sorted collection

## Significance

BSTs are the foundation for all balanced tree structures and demonstrate why self-balancing is necessary.

## Chunks Extracted

*Pending*
