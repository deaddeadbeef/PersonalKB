---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-010]]"
confidence: high
supports:
  - "[[Red-Black Trees]]"
  - "[[Balanced BSTs]]"
qna_seeds:
  - "Q: How does a red-black tree's height compare to an AVL tree's? A: Red-black trees guarantee height ≤ 2 log₂(n + 1), less strict than AVL, but require only O(1) rotations per insertion or deletion."
---

# Red-Black Tree Height and Rotation Bounds

Red-black trees guarantee height at most 2 log₂(n + 1) using a coloring invariant that requires at most O(log n) recolorings but only O(1) rotations per insertion or deletion. This less strict balance (vs AVL's 1.4405 log₂ n) enables simpler updates. Java's TreeMap, C++ std::map, and the Linux kernel's Completely Fair Scheduler all use red-black trees for O(log n) operations.