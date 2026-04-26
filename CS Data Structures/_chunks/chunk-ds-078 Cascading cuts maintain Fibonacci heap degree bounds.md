---
tags: [cs-ds, chunk]
id: chunk-ds-078
source: "[[raw-ds-017]]"
supports: ["[[Fibonacci Heaps]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Cascading cuts maintain Fibonacci heap tree degree bounds

## Context
Fibonacci heaps delay consolidation allowing nodes to lose children.

## Claim
Cascading cuts mark a node when it loses a child. If a marked node loses another child it is cut to the root list. This ensures each tree of degree k has at least F(k+2) nodes where F is Fibonacci numbers.

## Why It Matters
The Fibonacci number bound is why these heaps are named Fibonacci and why extract-min is O(log n).

## QnA Seeds
- Q: What triggers a cascading cut? -> A: A marked node losing a second child.
- Q: Why Fibonacci numbers? -> A: Minimum tree size for degree k follows the Fibonacci sequence.
