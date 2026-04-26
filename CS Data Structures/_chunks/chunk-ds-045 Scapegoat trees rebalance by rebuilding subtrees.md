---
tags: [cs-ds, chunk]
id: chunk-ds-045
source: "[[raw-ds-033]]"
supports: ["[[Binary Search Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Scapegoat trees rebalance by rebuilding subtrees with zero metadata

## Context
AVL and Red-Black trees store per-node metadata for balance.

## Claim
Scapegoat trees store no balance metadata. On insert, if the tree becomes alpha-unbalanced, they walk up to find the shallowest unbalanced ancestor (scapegoat) and rebuild its entire subtree into a perfectly balanced BST in O(size).

## Why It Matters
Simplest self-balancing BST to implement — O(log n) amortized with zero per-node overhead.

## QnA Seeds
- Q: What triggers rebalancing? -> A: When depth exceeds log_{1/alpha}(n).
- Q: Why amortized not worst-case? -> A: Rebuilding is O(size) but charged across prior cheap inserts.
