---
tags: [cs-ds, chunk]
id: chunk-ds-116
source: "[[raw-ds-026]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Augmentation theorem: rotations preserve derivable metadata

## Context
Self-balancing BSTs rely on rotations which change tree structure.

## Claim
If metadata at each node is derivable from the node itself and its childrens metadata in O(1) then rotations can maintain it in O(1). This is the augmentation theorem enabling order-statistics interval trees and range aggregates.

## Why It Matters
General principle for extending BSTs with custom capabilities without changing asymptotic complexity.

## QnA Seeds
- Q: What must be true for augmentation to work? -> A: Metadata computable from node plus children metadata in O(1).
- Q: Give three examples. -> A: Subtree size, max endpoint, subtree sum.
