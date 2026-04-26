---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Union-Find: Disjoint Set Data Structures"
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
---

## Summary

The Union-Find (disjoint set) data structure maintains a collection of non-overlapping sets and supports three operations: Make-Set(x) creates a singleton set, Find(x) returns the representative element of x's set, and Union(x, y) merges two sets. The naive implementation using linked lists or simple trees can degrade to O(n) per operation. Two key optimizations transform Union-Find into a near-constant-time structure: union by rank (attach the shorter tree under the taller one) keeps tree height logarithmic, and path compression (during Find, make every node on the path point directly to the root) flattens the structure over time. Together, these optimizations yield an amortized cost of O(α(n)) per operation, where α is the inverse Ackermann function—a function so slowly growing that α(n) ≤ 4 for any practical input size (n < 2^65536). This was proven by Tarjan in 1975 and is essentially the tightest possible bound, as Fredman and Saks showed Ω(α(n)) is a lower bound for any pointer-based implementation. Union-Find is indispensable in Kruskal's minimum spanning tree algorithm, where it efficiently tracks which vertices are in the same connected component as edges are processed in weight order. Other applications include dynamic connectivity in networks, equivalence class maintenance, and percolation theory simulations.

## Key Claims

1. Path compression combined with union by rank achieves O(α(n)) amortized time per operation, where α(n) is the inverse Ackermann function—effectively constant for all practical purposes.
2. Without optimizations, Union-Find degrades to O(n) per Find on a linked-list or unbalanced tree representation; union by rank alone achieves O(log n).
3. The inverse Ackermann function α(n) grows so slowly that it does not exceed 4 for any input size conceivable in practice, making the amortized bound virtually O(1).
4. Union-Find is the enabling data structure for Kruskal's MST algorithm, allowing each edge consideration to run in near-constant time rather than the O(V) needed by naive component tracking.
5. The Ω(α(n)) lower bound by Fredman and Saks (1989) proves that no pointer-based disjoint set structure can beat this amortized complexity.

## Atomic Facts

1. Make-Set initializes each element as its own parent with rank 0; Find follows parent pointers to the root; Union links roots based on rank.
2. Path compression modifies Find to set the parent of every visited node directly to the root, flattening the tree for subsequent operations.
3. Union by rank maintains a rank field (upper bound on height) and attaches the lower-rank tree under the higher-rank root; ranks only increase when merging equal-rank trees.
4. In Kruskal's algorithm, Union-Find performs O(E) Find and Union operations on V elements, yielding O(E·α(V)) total time for the connectivity checks.
5. Path splitting and path halving are simpler alternatives to full path compression that achieve the same asymptotic bound with single-pass traversal.
6. Weighted Union-Find variants store additional information (like set size) at the root, enabling O(α(n)) queries on aggregate set properties.

## Significance

Union-Find is one of the most elegant data structures in computer science, achieving near-constant amortized time through two simple heuristics. Its analysis by Tarjan introduced the inverse Ackermann function to algorithm analysis, connecting discrete mathematics to practical data structure design. Beyond Kruskal's algorithm, Union-Find appears in image processing (connected component labeling), network connectivity (dynamic graph problems), and compiler optimization (alias analysis). The structure exemplifies how simple optimizations can yield dramatic asymptotic improvements—from O(n) to effectively O(1)—and remains a staple of algorithm courses and competitive programming.

## Chunks Extracted

*Pending*
