---
id: chunk-csa-171
type: chunk
source: "[[Cormen 2022 - Red-Black Trees]]"
source_loc: "RB vs AVL"
topic: "data-structures"
claim: "Red-black trees trade slightly looser balance (height up to 2 log n vs AVL 1.44 log n) for fewer rotations per modification, favoring write-heavy workloads"
confidence: verified
supports:
  - "[[Red-Black Tree]]"
  - "[[AVL Tree]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Red-black vs AVL tradeoff in balance strictness and rotation cost

## Context

AVL trees enforce stricter balance (subtree heights differ by at most 1), yielding height at most 1.44*log2(n) versus red-black's 2*log2(n). This means AVL trees are slightly faster for lookups. However, AVL trees may require O(log n) rotations per insert or delete, while red-black trees need at most 2 and 3 respectively. For write-heavy workloads the fewer rotations make red-black trees faster overall, which is why they dominate in standard library implementations (Java TreeMap, C++ std::map, Linux kernel).

## Why It Matters

Choosing between red-black and AVL trees is a practical engineering decision—understanding this tradeoff helps select the right balanced BST for the workload characteristics.

## QnA Seeds

- Q: When would you prefer an AVL tree over a red-black tree?
- Q: Why do standard libraries overwhelmingly choose red-black trees over AVL trees?
- Q: What are the height bounds for AVL vs red-black trees?
