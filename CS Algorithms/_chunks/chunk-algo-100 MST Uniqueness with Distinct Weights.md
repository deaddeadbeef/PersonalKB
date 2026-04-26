---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-015]]"
confidence: high
supports:
  - "[[Minimum Spanning Trees]]"
  - "[[Matroid Theory]]"
qna_seeds:
  - "Q: When is the MST unique? A: If all edge weights are distinct, the MST is unique. With ties, multiple MSTs may exist but all share the same total weight and identical multiset of edge weights."
---

# MST Uniqueness with Distinct Weights

If all edge weights are distinct, the minimum spanning tree is unique. With ties, multiple MSTs may exist but all have the same total weight, and the multiset of edge weights in any MST is identical (the MST matroid property). The optimal deterministic MST algorithm by Chazelle (2000) runs in O(E · α(E, V)) time, while Karger-Klein-Tarjan's randomized algorithm achieves O(V + E) expected time.