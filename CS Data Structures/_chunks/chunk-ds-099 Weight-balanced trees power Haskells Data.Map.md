---
tags: [cs-ds, chunk]
id: chunk-ds-099
source: "[[raw-ds-033]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Weight-balanced trees power Haskells Data.Map with size invariant

## Context
Haskell needs persistent balanced trees with efficient split and join.

## Claim
Weight-balanced trees maintain the invariant that each subtree is at most a constant factor larger than its sibling using size fields. Adams variant supports O(log n) split and join making it ideal for functional set operations.

## Why It Matters
Default map and set implementation in Haskell. Also used in MIT Scheme and some ML implementations.

## QnA Seeds
- Q: What is the balance invariant? -> A: size(left) <= delta * size(right) and vice versa for a tuning parameter delta.
- Q: Why preferred for functional languages? -> A: Efficient split, join and persistent operations via structural sharing.
