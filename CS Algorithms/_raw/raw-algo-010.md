---
tags: [cs-algorithms, raw]
source_type: textbook
source_title: "Binary Search Trees and Balanced Trees"
authors: "G.M. Adelson-Velsky, E.M. Landis"
year: 1962
---

# Binary Search Trees and AVL Trees

## Summary
Binary search trees (BSTs) support search, insert, and delete operations in O(h) time where h is the tree height, but unbalanced BSTs can degenerate to O(n) in the worst case (e.g., inserting sorted data creates a linked list). AVL trees, invented by Adelson-Velsky and Landis in 1962, were the first self-balancing BST, maintaining a balance invariant that limits height to O(log n) through single and double rotations after each modification. Red-black trees provide a less strict balance condition with at most two rotations per insertion, making them preferred in practice for standard library implementations.

## Key Claims
- An unbalanced BST built by inserting n random keys has expected height O(log n), specifically approximately 4.311 ln n, but worst-case height is n − 1 (a degenerate chain)
- AVL trees maintain the invariant that for every node, the heights of its left and right subtrees differ by at most 1, guaranteeing a maximum height of at most 1.4405 log₂(n + 2) − 0.3277
- Single rotations fix "outside" imbalances (left-left or right-right), while double rotations (rotate child then parent) fix "inside" imbalances (left-right or right-left), each requiring O(1) pointer changes
- Red-black trees guarantee height at most 2 log₂(n + 1), using a coloring invariant that requires at most O(log n) recolorings but only O(1) rotations per insertion or deletion
- Splay trees achieve O(log n) amortized time per operation without storing any balance information, using a "move to root" strategy that provides the working-set property

## Atomic Facts
1. The minimum number of nodes in an AVL tree of height h follows the recurrence N(h) = N(h−1) + N(h−2) + 1 with N(0) = 1, N(1) = 2, growing as approximately φʰ/√5 where φ = (1+√5)/2 ≈ 1.618 (Fibonacci-like growth)
2. AVL deletion may trigger up to O(log n) rotations propagating up to the root, compared to insertion which requires at most 2 rotations (one single or one double) to restore balance
3. Red-black trees store one extra bit per node (color), while AVL trees store a balance factor (−1, 0, +1) requiring 2 bits; in practice both use at least a full byte or embed the bit in a pointer
4. Java's TreeMap and C++ std::map use red-black trees; the Linux kernel's Completely Fair Scheduler also uses a red-black tree to index process virtual runtimes for O(log n) scheduling
5. A BST with n nodes has exactly C(n) = (2n choose n)/(n+1) distinct shapes, where C(n) is the nth Catalan number; for n = 10, there are 16,796 distinct BST shapes
6. B-trees generalize BSTs for disk-based storage, with branching factor up to thousands; a B-tree of order m = 1000 stores 10⁹ keys in a tree of height at most 3, requiring only 3 disk reads per search

## Significance
BSTs are the canonical data structure for maintaining dynamic sorted sets, enabling O(log n) search, predecessor/successor, range queries, and order-statistics operations. The invention of AVL trees in 1962 established that self-balancing was achievable with O(1) structural changes per operation, spawning decades of research into balanced tree variants. Red-black trees struck the practical balance between strict AVL balance and implementation simplicity, becoming the de facto standard in systems programming. Understanding BST balance is essential for database indexing (B-trees), computational geometry (augmented BSTs), and the design of persistent data structures.

## Chunks Extracted
*Pending*
