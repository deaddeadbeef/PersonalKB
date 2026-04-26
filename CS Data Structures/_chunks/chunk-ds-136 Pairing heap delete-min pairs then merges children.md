---
tags: [cs-ds, chunk]
id: chunk-ds-136
source: "[[raw-ds-038]]"
supports: ["[[Heaps and Priority Queues Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Pairing heap delete-min pairs children left-to-right then merges right-to-left

## Context
After removing the root the children must be combined into a single heap.

## Claim
Pairing heap delete-min first pairs adjacent children left-to-right creating ceiling(k/2) trees then merges them right-to-left into a single tree. This two-pass approach achieves O(log n) amortized.

## Why It Matters
The two-pass pairing is what gives pairing heaps their name and their good amortized performance.

## QnA Seeds
- Q: Why two passes? -> A: Single left-to-right merge gives O(n) worst case. Two-pass gives O(log n) amortized.
- Q: Why right-to-left in second pass? -> A: Accumulated smaller trees are merged into progressively larger ones reducing total comparisons.
