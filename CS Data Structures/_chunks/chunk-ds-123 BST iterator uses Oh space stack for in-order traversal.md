---
tags: [cs-ds, chunk]
id: chunk-ds-123
source: "[[raw-ds-004]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# BST iterator uses O(h) space stack for in-order traversal without recursion

## Context
Recursive in-order traversal uses O(h) stack space implicitly.

## Claim
An explicit stack-based BST iterator pushes left children then pops and processes nodes yielding in-order elements one at a time in O(1) amortized per next() call with O(h) space.

## Why It Matters
Required for iterator interfaces in Java TreeMap and C++ std::map where full recursive traversal is impractical.

## QnA Seeds
- Q: What does the stack hold? -> A: Ancestors along the leftmost path from current position.
- Q: Why O(1) amortized? -> A: Each node pushed and popped exactly once over full traversal.
