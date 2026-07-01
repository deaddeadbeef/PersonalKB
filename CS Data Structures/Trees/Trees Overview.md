---
tags:
  - cs-ds
  - hub
up: "[[CS Data Structures]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core]
---
# Trees Overview

Trees introduce hierarchy: each node may have multiple children, creating branching paths from a single root. This deceptively simple idea underpins file systems, databases, compilers, and countless search algorithms. The structures in this hub progress from unbalanced binary trees through self-balancing variants to disk-optimised multi-way trees, each trading implementation complexity for stronger performance guarantees.

## Binary Trees and Traversals

A **binary tree** limits every node to at most two children, yielding clean recursive definitions and four classic traversal orders — pre-order, in-order, post-order, and level-order. In-order traversal of a **binary search tree** (BST) produces sorted output, and average-case $O(\log n)$ search makes BSTs a natural first step beyond linear structures. However, skewed input can degrade a plain BST to $O(n)$, motivating the balanced variants below.

## Self-Balancing Trees

**AVL trees** enforce a strict height-balance invariant (subtree heights differ by at most one), guaranteeing $O(\log n)$ worst-case operations at the cost of frequent rotations. **Red-black trees** relax the invariant, colouring nodes red or black to maintain approximate balance with fewer rotations — making them the default backing structure for ordered maps in many standard libraries. **Splay trees** take an amortised approach, rotating recently accessed nodes to the root so that frequently queried elements become cheap to reach. **Treaps** combine BST ordering with random heap priorities to achieve expected $O(\log n)$ depth with minimal bookkeeping.

## Disk-Optimised Multi-Way Trees

When data lives on disk, minimising I/O reads matters more than CPU comparisons. **B-trees** widen each node to hold many keys, dramatically reducing tree height and disk seeks. **B+ trees** push all records to the leaves and link them for efficient range scans — the dominant index structure in relational databases and file systems worldwide.

## Pages in This Hub

- [[Binary Trees and Traversals]]
- [[Binary Search Trees]]
- [[AVL Trees]]
- [[Red-Black Trees]]
- [[B-Trees and B-Plus Trees]]
- [[Splay Trees and Treaps]]

## Related Hubs

- [[Foundational Concepts Overview]] — complexity analysis and amortised bounds used throughout
- [[Heaps and Priority Queues Overview]] — tree-shaped structures with a different ordering invariant
- [[Tries and String Structures Overview]] — tree variants specialised for string keys
- [[Advanced Structures Overview]] — segment trees, interval trees, and k-d trees

## References

- [[CS Data Structures/Sources/Sources Index]]
- [[CS Data Structures/CS Data Structures Book Reading Spine]]
