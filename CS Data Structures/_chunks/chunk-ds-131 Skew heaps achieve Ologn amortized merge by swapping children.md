---
tags: [cs-ds, chunk]
id: chunk-ds-131
source: "[[raw-ds-029]]"
supports: ["[[Heaps and Priority Queues Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Skew heaps achieve Ologn amortized merge by unconditionally swapping children

## Context
Leftist heaps track s-values to maintain right-spine bias.

## Claim
Skew heaps simplify leftist heaps by unconditionally swapping left and right children after every merge step along the right spine. This achieves O(log n) amortized without storing any balance metadata.

## Why It Matters
Simplest mergeable heap implementation. Shows that self-adjusting behavior can replace explicit balance tracking.

## QnA Seeds
- Q: How does skew heap differ from leftist? -> A: No s-value tracking. Just swap children after every merge step.
- Q: Why does this work? -> A: Swapping prevents one-sided growth amortizing over the sequence of operations.
