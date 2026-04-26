---
tags: [cs-ds, chunk]
id: chunk-ds-079
source: "[[raw-ds-019]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# The potential method proves amortized bounds via virtual savings

## Context
Amortized analysis needs to show that expensive operations are rare enough.

## Claim
The potential method assigns a potential function to the data structure state. Amortized cost = actual cost + change in potential. If potential increases during cheap operations and decreases during expensive ones the amortized cost is smooth.

## Why It Matters
The standard proof technique for dynamic arrays, splay trees, Fibonacci heaps, and Union-Find.

## QnA Seeds
- Q: What is a good potential function for dynamic arrays? -> A: 2n - capacity where n is current size.
- Q: Why does potential decrease during expensive ops? -> A: Resize releases stored potential to pay for the O(n) copy.
