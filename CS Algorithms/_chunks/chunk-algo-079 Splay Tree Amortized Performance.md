---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-010]]"
confidence: high
supports:
  - "[[Splay Trees]]"
  - "[[Amortized Analysis]]"
qna_seeds:
  - "Q: What is special about splay trees' performance? A: They achieve O(log n) amortized time per operation without storing any balance information, using a move-to-root strategy that provides the working-set property."
---

# Splay Tree Amortized Performance

Splay trees achieve O(log n) amortized time per operation without storing any balance information, using a "move to root" zig-zig/zig-zag splaying strategy. They provide the working-set property: recently or frequently accessed elements are found faster. Unlike AVL and red-black trees, splay trees require no per-node metadata (color bits or balance factors), making them simpler to implement at the cost of non-guaranteed single-operation performance.