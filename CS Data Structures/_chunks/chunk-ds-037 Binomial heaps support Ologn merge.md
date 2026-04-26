---
tags: [cs-ds, chunk]
id: chunk-ds-037
source: "[[raw-ds-029]]"
supports: ["[[Heaps and Priority Queues Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Binomial heaps support Ologn merge by linking same-degree trees

## Context
Binary heap merge requires O(n) — rebuild from scratch.

## Claim
Binomial heaps merge in O(log n) by linking binomial trees of equal degree, analogous to binary addition — each tree represents a power of 2 in the node count.

## Why It Matters
First heap to achieve efficient merge — key building block for Fibonacci heaps and priority queue theory.

## QnA Seeds
- Q: Why O(log n) merge? -> A: At most O(log n) trees per heap; linking same-degree trees is O(1).
- Q: How does it relate to binary numbers? -> A: n nodes decompose into binomial trees for each 1-bit in binary representation of n.
