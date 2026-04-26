---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-010]]"
confidence: high
supports:
  - "[[B-Trees]]"
  - "[[Database Indexing]]"
qna_seeds:
  - "Q: Why do B-trees use high branching factors for disk storage? A: A B-tree of order m = 1000 stores 10⁹ keys in height ≤ 3, requiring only 3 disk reads per search, making it optimal for I/O-bound operations."
---

# B-Tree Disk-Optimized Branching

B-trees generalize BSTs for disk-based storage with branching factors up to thousands, minimizing disk I/O. A B-tree of order m = 1000 stores 10⁹ keys in a tree of height at most 3, requiring only 3 disk reads per search. Each node fills one disk page, and the high fanout ensures that the tree height grows as O(log_m n), making B-trees the standard index structure for databases and file systems.