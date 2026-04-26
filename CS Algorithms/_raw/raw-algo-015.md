---
tags: [cs-algorithms, raw]
source_type: journal_paper
source_title: "Minimum Spanning Trees: Kruskal's and Prim's Algorithms"
authors: "Joseph Kruskal, Robert C. Prim"
year: 1956
---

# Minimum Spanning Trees

## Summary
A minimum spanning tree (MST) of a connected, weighted, undirected graph is a subset of edges that connects all vertices with the minimum total weight and no cycles. The two classic algorithms—Kruskal's and Prim's—both exploit the cut property (the lightest edge crossing any cut must be in some MST) but use different strategies. Kruskal's algorithm sorts edges by weight and greedily adds edges that don't create cycles (using union-find), while Prim's algorithm grows a single tree by repeatedly adding the cheapest edge connecting the tree to a non-tree vertex (using a priority queue).

## Key Claims
- The cut property guarantees correctness of both algorithms: for any cut (S, V−S) that respects the current MST edges, the minimum-weight edge crossing the cut is safe to add to the MST
- Kruskal's algorithm runs in O(E log E) time, dominated by sorting edges; the union-find operations contribute O(E · α(V)) ≈ O(E) using union by rank and path compression
- Prim's algorithm with a binary heap runs in O((V + E) log V) = O(E log V) for connected graphs; with a Fibonacci heap, this improves to O(E + V log V)
- For dense graphs (E = Θ(V²)), Prim's with an array-based priority queue runs in O(V²), which is optimal and outperforms both Kruskal's O(V² log V) and heap-based Prim's O(V² log V)
- Borůvka's algorithm (1926, the earliest MST algorithm) runs in O(E log V) by finding the cheapest edge from each component in parallel rounds, halving the number of components each round in at most ⌈log₂ V⌉ phases

## Atomic Facts
1. Kruskal's algorithm performs at most E union-find operations; with union by rank and path compression, each operation takes O(α(V)) amortized time, where α is the inverse Ackermann function—effectively O(1) for all practical input sizes (α(V) ≤ 4 for V < 10^{80})
2. An MST of a connected graph with V vertices contains exactly V − 1 edges; if the graph has multiple components, the result is a minimum spanning forest with V − C edges, where C is the number of components
3. If all edge weights are distinct, the MST is unique; with ties, there may be multiple MSTs but all have the same total weight, and the multiset of edge weights in any MST is identical (the MST matroid property)
4. Prim's algorithm starting from any vertex visits each vertex exactly once and performs at most E decrease-key operations; with a Fibonacci heap, each costs O(1) amortized, giving O(E + V log V) total
5. The optimal deterministic MST algorithm by Chazelle (2000) runs in O(E · α(E, V)) time, nearly linear, using soft heaps; whether a linear-time deterministic algorithm exists remains open
6. Karger, Klein, and Tarjan's randomized MST algorithm (1995) runs in O(V + E) expected time by combining Borůvka steps with random sampling and verification, proving that linear expected time is achievable

## Significance
MST algorithms are foundational in network design—constructing minimum-cost communication networks, power grids, and pipeline systems. Kruskal's algorithm is a primary example of the greedy paradigm with a matroid-theoretic justification: the graphic matroid guarantees that the greedy approach yields an optimal solution. The MST problem also connects to clustering (single-linkage clustering is equivalent to computing the MST and removing the k − 1 heaviest edges), approximation algorithms (the MST provides a 2-approximation for metric TSP), and the study of matroids in combinatorial optimization.

## Chunks Extracted
*Pending*
