---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-008]]"
confidence: high
supports:
  - "[[Binary Search]]"
  - "[[Comparison-Based Lower Bounds]]"
qna_seeds:
  - "Q: How many comparisons does binary search need for n = 1,000,000? A: At most 20 comparisons (⌊log₂ 1,000,000⌋ + 1 = 20), which is optimal by a decision-tree lower bound of ⌈log₂(n+1)⌉."
---

# Binary Search Optimal Comparison Bound

Binary search requires exactly ⌊log₂ n⌋ + 1 comparisons in the worst case, which is optimal among comparison-based search algorithms on sorted arrays. For n = 1,000,000 elements, this means at most 20 comparisons. The lower bound proof uses a decision tree argument: any comparison-based algorithm must distinguish among n + 1 outcomes, requiring tree height at least ⌈log₂(n + 1)⌉.