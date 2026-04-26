---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-010]]"
confidence: high
supports:
  - "[[AVL Trees]]"
  - "[[Balanced BSTs]]"
qna_seeds:
  - "Q: What is the maximum height of an AVL tree with n nodes? A: At most 1.4405 log₂(n + 2) − 0.3277, maintained by requiring left and right subtree heights to differ by at most 1."
---

# AVL Tree Height Guarantee

AVL trees maintain the invariant that for every node, the heights of its left and right subtrees differ by at most 1, guaranteeing maximum height at most 1.4405 log₂(n + 2) − 0.3277. The minimum number of nodes in an AVL tree of height h follows N(h) = N(h−1) + N(h−2) + 1, growing as approximately φʰ/√5 where φ ≈ 1.618 (Fibonacci-like growth). AVL insertion requires at most 2 rotations, but deletion may trigger up to O(log n) rotations.