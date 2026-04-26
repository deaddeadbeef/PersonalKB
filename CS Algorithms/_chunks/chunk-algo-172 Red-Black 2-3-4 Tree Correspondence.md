---
id: chunk-csa-172
type: chunk
source: "[[Cormen 2022 - Red-Black Trees]]"
source_loc: "2-3-4 Correspondence"
topic: "data-structures"
claim: "Every red-black tree corresponds to a unique 2-3-4 tree where red edges connect nodes within the same 2-3-4 node, providing intuition for the coloring rules"
confidence: verified
supports:
  - "[[Red-Black Tree]]"
  - "[[2-3-4 Tree]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Red-black to 2-3-4 tree correspondence explains coloring rules

## Context

Each red-black tree maps to a unique 2-3-4 tree: a black node with no red children is a 2-node, a black node with one red child is a 3-node, and a black node with two red children is a 4-node. Red edges connect keys within the same multi-key node. This correspondence explains why the coloring rules work: the equal black-height property ensures all leaves are at the same depth in the 2-3-4 tree, and the no-consecutive-reds rule prevents nodes with more than 3 keys. Left-leaning red-black trees (LLRB, Sedgewick 2008) simplify by restricting to 2-3 trees only.

## Why It Matters

The 2-3-4 correspondence provides intuitive understanding of why red-black tree rules maintain balance, transforming seemingly arbitrary coloring constraints into natural multi-way tree properties.

## QnA Seeds

- Q: How does a black node with two red children map to a 2-3-4 tree node?
- Q: Why does the no-consecutive-reds rule correspond to the 2-3-4 node size limit?
- Q: How do left-leaning red-black trees simplify the 2-3-4 correspondence?
