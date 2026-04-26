---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-015]]"
confidence: high
supports:
  - "[[Minimum Spanning Trees]]"
  - "[[Greedy Algorithms]]"
qna_seeds:
  - "Q: What property guarantees correctness of MST algorithms? A: The cut property: for any cut (S, V−S) respecting current MST edges, the minimum-weight crossing edge is safe to add to the MST."
---

# MST Cut Property Correctness

The cut property guarantees correctness of both Kruskal's and Prim's algorithms: for any cut (S, V−S) that respects the current MST edges, the minimum-weight edge crossing the cut is safe to add to the MST. An MST of a connected graph with V vertices contains exactly V − 1 edges. If the graph has multiple components, the result is a minimum spanning forest with V − C edges, where C is the number of components.