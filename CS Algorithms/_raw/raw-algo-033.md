---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Red-Black Trees: Self-Balancing Binary Search Trees"
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
---

## Summary

Red-black trees are self-balancing binary search trees that guarantee O(log n) time for search, insertion, and deletion by enforcing five structural properties via node coloring (red or black) and local rotations. The five properties are: (1) every node is red or black, (2) the root is black, (3) every leaf (NIL sentinel) is black, (4) a red node's children are both black (no two consecutive reds on any path), and (5) all paths from any node to its descendant leaves contain the same number of black nodes (the black-height). These properties ensure the longest root-to-leaf path is at most twice the shortest: if the black-height is bh, the shortest path has bh nodes (all black) and the longest has 2·bh (alternating red and black). This guarantees a height bound of 2·log₂(n+1), keeping all operations logarithmic. Insertion adds a red node and may violate property 4 (red parent with red child). The fix involves at most O(log n) recolorings and at most 2 rotations, propagating the violation upward until resolved. Deletion is more complex, potentially violating property 5 (black-height imbalance), requiring up to O(log n) recolorings and at most 3 rotations. Compared to AVL trees, which enforce a stricter balance (heights of subtrees differ by at most 1), red-black trees perform fewer rotations per operation—at most 2 for insert and 3 for delete versus O(log n) for AVL—making them preferable when modifications are frequent. Red-black trees are used in the Linux kernel (CFS scheduler, memory management), Java's TreeMap and TreeSet, and C++ STL's std::map and std::set.

## Key Claims

1. The five red-black properties guarantee a height of at most 2·log₂(n+1), ensuring O(log n) worst-case time for search, insert, and delete operations.
2. Insertion requires at most 2 rotations and O(log n) recolorings; deletion requires at most 3 rotations and O(log n) recolorings—a constant number of structural changes per operation.
3. The black-height property (equal black nodes on all root-to-leaf paths) is the key invariant: it constrains the tree's shape more flexibly than AVL's strict height-balance condition.
4. Red-black trees trade slightly looser balance (height up to 2·log n vs AVL's 1.44·log n) for fewer rotations on modifications, making them faster for write-heavy workloads.
5. Left-leaning red-black trees (LLRB, Sedgewick 2008) simplify implementation by requiring red links to lean left, reducing the number of cases to handle during insertion and deletion.

## Atomic Facts

1. Every NIL leaf is considered black; implementations use a single sentinel node T.nil shared by all leaves to save space.
2. A tree with n internal nodes has black-height at most log₂(n+1), since a subtree rooted at any node contains at least 2^bh − 1 internal nodes.
3. Insertion fixup has three cases (uncle is red: recolor; uncle is black with triangle: rotate to line; uncle is black with line: rotate and recolor), applied iteratively up the tree.
4. Deletion fixup has four cases based on the sibling's color and its children's colors, involving rotations and recolorings to restore the black-height invariant.
5. Left rotation at node x makes x's right child y the new subtree root, with x becoming y's left child and y's former left child becoming x's right child.
6. The correspondence between red-black trees and 2-3-4 trees maps each red-black tree to a unique 2-3-4 tree: red edges connect nodes within the same 2-3-4 node.

## Significance

Red-black trees are the most widely deployed balanced BST variant in production systems. Their guaranteed O(log n) performance and bounded rotation count make them ideal for kernel-level data structures where predictable worst-case behavior is critical. The Linux CFS scheduler uses red-black trees to manage process scheduling, and virtually all major standard libraries (Java, C++, .NET) use them for ordered collections. Understanding red-black trees provides insight into the design space of balanced search trees and the tradeoffs between balance strictness, rotation cost, and implementation complexity. The connection to 2-3-4 trees provides an intuitive understanding of why the coloring rules work.

## Chunks Extracted

chunk-algo-169 through chunk-algo-172
