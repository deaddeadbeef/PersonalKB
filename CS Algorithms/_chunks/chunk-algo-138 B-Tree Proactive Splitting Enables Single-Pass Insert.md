---
id: chunk-algo-138
type: chunk
source: "[[raw-algo-025]]"
source_loc: "B-Trees - Key Claims"
topic: "data-structures"
claim: "B-tree insertion splits full nodes (2t-1 keys) proactively during descent by promoting the median to the parent and creating two t-1 key children, guaranteeing leaf space without backtracking in a single root-to-leaf pass."
confidence: verified
supports:
  - "[[B-Trees]]"
tags:
  - cs-algorithms
  - cs-algorithms/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# B-Tree Proactive Splitting Enables Single-Pass Insert

## Context

As the search descends toward the insertion leaf, any full node encountered is immediately split: median key promoted to parent, node split into two children with t-1 keys each. The parent is guaranteed non-full because it was checked on the previous level. This top-down approach requires one pass with at most O(log_t n) splits. Bottom-up insertion would require backtracking up the tree, complicating implementation and potentially doubling I/O operations.

## Why It Matters

Proactive splitting is the standard B-tree insertion strategy, avoiding backtracking and minimizing disk I/O. Understanding this technique is essential for implementing B-trees in databases and file systems.

## QnA Seeds

- Q: How does proactive splitting work during B-tree insert?
- Q: Why does proactive splitting avoid backtracking?
- Q: How are keys distributed when a full node splits?