---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Greedy Algorithms: Framework, Analysis, and Applications"
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
---

## Summary

Greedy algorithms construct solutions incrementally by making the locally optimal choice at each step, never reconsidering past decisions. Two properties must hold for a greedy approach to yield a globally optimal solution: the greedy choice property (a locally optimal choice leads to a globally optimal solution) and optimal substructure (an optimal solution contains optimal solutions to subproblems). The activity selection problem is the canonical example: given activities with start and finish times, selecting the activity that finishes earliest and recursing on compatible activities yields the maximum-size subset. Huffman coding constructs optimal prefix-free binary codes by repeatedly merging the two lowest-frequency symbols into a subtree—a greedy strategy that minimizes expected code length. The fractional knapsack problem (items can be split) admits a greedy solution: take items in decreasing order of value-per-weight ratio. However, the 0-1 knapsack (items are indivisible) does not satisfy the greedy choice property, demonstrating that small problem changes can invalidate greedy approaches. Matroid theory provides a unifying mathematical framework: a greedy algorithm produces an optimal solution for any optimization problem whose feasible sets form a matroid. This theory explains why greedy works for minimum spanning trees (graphic matroid) and scheduling (uniform matroid) but fails for other problems. Proving a greedy algorithm correct typically involves an exchange argument showing that any optimal solution can be transformed into the greedy solution without loss.

## Key Claims

1. A greedy algorithm requires both the greedy choice property and optimal substructure; the absence of either property means greedy may fail to produce optimal solutions.
2. Activity selection with earliest-finish-time ordering is the prototypical greedy algorithm, achieving an optimal solution in O(n log n) time.
3. Huffman coding builds optimal prefix codes in O(n log n) time using a min-priority queue, with the greedy strategy of always merging the two least-frequent nodes.
4. The 0-1 knapsack problem demonstrates greedy's limitations: the value-per-weight strategy that works for fractional knapsack fails when items cannot be divided.
5. Matroid theory provides a sufficient condition for greedy optimality: if the feasible sets form a matroid, the greedy algorithm on a weighted matroid produces a maximum-weight independent set.

## Atomic Facts

1. The greedy choice property states that a globally optimal solution can be assembled by making locally optimal (greedy) choices without backtracking.
2. In activity selection, sorting by finish time and greedily selecting compatible activities produces a maximum-cardinality set; this is provable by an exchange argument.
3. Huffman coding produces a full binary tree (every internal node has exactly two children) with leaves representing symbols, achieving the minimum weighted external path length.
4. Fractional knapsack has a greedy O(n log n) solution; 0-1 knapsack requires dynamic programming in O(nW) pseudo-polynomial time.
5. A matroid (S, I) is a finite set S with a collection I of independent subsets satisfying the hereditary property and the exchange property.
6. The exchange argument proof technique shows that any element in an optimal solution not in the greedy solution can be swapped without increasing cost.

## Significance

Greedy algorithms are among the most intuitive algorithmic paradigms, yet proving their correctness requires rigorous analysis. The greedy framework encompasses critical algorithms including Dijkstra's shortest path, Prim's and Kruskal's MST, Huffman coding, and various scheduling algorithms. Understanding when greedy works—and when it doesn't—is a core skill in algorithm design. Matroid theory elevates this understanding from case-by-case analysis to a unified theoretical framework, connecting combinatorial optimization to abstract algebra. In practice, greedy heuristics are widely used even when optimality is not guaranteed, often serving as fast approximations or components of more complex algorithms.

## Chunks Extracted

chunk-algo-141 through chunk-algo-144
