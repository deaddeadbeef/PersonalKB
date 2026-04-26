---
tags: [cs-ds, chunk]
id: chunk-ds-083
source: "[[raw-ds-003]]"
supports: ["[[Stacks and Queues]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Monotonic stacks solve next-greater-element in On

## Context
Finding the next greater element for each position naively takes O(n^2).

## Claim
A monotonic stack maintains elements in decreasing order. When a larger element arrives pop all smaller elements assigning their next-greater. Each element pushed and popped at most once giving O(n) total.

## Why It Matters
Key technique for stock span, histogram area, and temperature problems in competitive programming.

## QnA Seeds
- Q: Why O(n) total? -> A: Each of n elements pushed once and popped at most once.
- Q: What variant for next-smaller? -> A: Maintain increasing order instead of decreasing.
