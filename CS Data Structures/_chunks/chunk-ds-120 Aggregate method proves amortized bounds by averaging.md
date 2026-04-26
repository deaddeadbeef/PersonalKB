---
tags: [cs-ds, chunk]
id: chunk-ds-120
source: "[[raw-ds-019]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Aggregate method proves amortized bounds by averaging over sequences

## Context
Amortized analysis has three main techniques.

## Claim
The aggregate method computes total cost of n operations then divides by n. Simplest technique: if n operations cost T(n) total then amortized cost per operation is T(n)/n. Used for dynamic arrays and multi-pop stacks.

## Why It Matters
Most intuitive amortized technique. Starting point before potential or accounting when applicable.

## QnA Seeds
- Q: When is aggregate sufficient? -> A: When all operations have the same amortized cost.
- Q: When do you need potential method instead? -> A: When different operations have different amortized costs.
