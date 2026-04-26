---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Network Flow: Ford-Fulkerson Method and Max-Flow Min-Cut Theorem"
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
---

## Summary

The Ford-Fulkerson method computes maximum flow in a flow network—a directed graph with source s, sink t, and edge capacities. The algorithm repeatedly finds augmenting paths from s to t in the residual graph and pushes flow along them until no augmenting path exists. The max-flow min-cut theorem (Ford and Fulkerson, 1956) establishes that the maximum flow equals the minimum capacity of any s-t cut, providing both an optimality condition and a duality result. The basic Ford-Fulkerson method using DFS runs in O(E·|f*|) where |f*| is the maximum flow value, which can be exponential for irrational capacities. The Edmonds-Karp refinement uses BFS to find shortest augmenting paths, guaranteeing O(VE²) time regardless of capacity values. The residual graph tracks remaining capacity: for each edge (u,v) with capacity c and flow f, it contains a forward edge with capacity c−f and a backward edge with capacity f, enabling flow rerouting. Network flow has remarkably diverse applications: bipartite matching (model as unit-capacity network), project selection (minimum cut formulation), airline scheduling, baseball elimination, and image segmentation. Dinic's algorithm achieves O(V²E) using blocking flows and level graphs, while push-relabel algorithms achieve O(V²E) or O(V³) with specific implementations.

## Key Claims

1. The max-flow min-cut theorem states that the value of the maximum flow in a network equals the capacity of the minimum s-t cut, establishing a fundamental duality in combinatorial optimization.
2. Ford-Fulkerson with DFS has time complexity O(E·|f*|) which can be poor for large capacity values; Edmonds-Karp with BFS guarantees O(VE²) independent of capacities.
3. The residual graph with backward edges is essential for correctness: it allows the algorithm to implicitly "undo" previously pushed flow, preventing the algorithm from getting stuck at suboptimal solutions.
4. Maximum bipartite matching reduces directly to maximum flow in a unit-capacity network, demonstrating the power of flow as a modeling framework.
5. The integrality theorem guarantees that if all capacities are integers, the maximum flow has an integer value and there exists an integer-valued optimal flow.

## Atomic Facts

1. An augmenting path is any s-to-t path in the residual graph; the bottleneck capacity of the path determines how much flow is pushed.
2. Edmonds-Karp performs at most O(VE) augmentations because each BFS-found augmenting path has non-decreasing length, and the distance from s to any vertex increases monotonically.
3. A minimum cut (S, T) partitions vertices into sets containing s and t respectively; its capacity is the sum of capacities of edges crossing from S to T.
4. For bipartite matching, a super-source connects to all left vertices and all right vertices connect to a super-sink, with all edge capacities set to 1.
5. Dinic's algorithm improves to O(E√V) on unit-capacity graphs, making it efficient for bipartite matching with O(E√V) time.
6. The push-relabel algorithm maintains a preflow (excess at vertices) rather than augmenting paths, achieving O(V²E) time with FIFO selection and O(V³) with highest-label selection.

## Significance

Network flow is one of the most versatile algorithmic frameworks in combinatorial optimization, with the max-flow min-cut theorem serving as a cornerstone of duality theory. Ford-Fulkerson and its refinements underpin solutions to problems spanning logistics, telecommunications, computer vision, and scheduling. The reduction from bipartite matching to max-flow demonstrates how seemingly different problems share structural foundations. Modern flow algorithms (push-relabel, blocking flows) remain critical in practical applications including image segmentation, network reliability analysis, and transportation planning.

## Chunks Extracted

*Pending*
