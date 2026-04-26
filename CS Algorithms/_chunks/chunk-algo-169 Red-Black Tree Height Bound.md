---
id: chunk-csa-169
type: chunk
source: "[[Cormen 2022 - Red-Black Trees]]"
source_loc: "Properties and Height Bound"
topic: "data-structures"
claim: "The five red-black tree properties guarantee height at most 2 log2(n+1), ensuring O(log n) worst-case search, insert, and delete"
confidence: verified
supports:
  - "[[Red-Black Tree]]"
  - "[[Balanced BST]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Red-black tree height bound 2 log2(n+1) from five properties

## Context

Red-black trees enforce five properties: (1) every node is red or black, (2) root is black, (3) every NIL leaf is black, (4) red nodes have only black children, (5) all root-to-leaf paths have equal black-height. These ensure the longest path is at most twice the shortest: if black-height is bh, the shortest path has bh nodes (all black) and the longest has 2*bh (alternating red and black). A tree with n internal nodes has black-height at most log2(n+1), giving height at most 2*log2(n+1).

## Why It Matters

Red-black trees are the most widely deployed balanced BST in production (Java TreeMap, C++ std::map, Linux CFS scheduler), and understanding the five properties explains why they guarantee logarithmic performance.

## QnA Seeds

- Q: Which red-black property prevents the tree from becoming too unbalanced?
- Q: How does the black-height property bound the tree's total height?
- Q: Why is the longest root-to-leaf path at most twice the shortest?
