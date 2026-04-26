---
tags: [cs-ds, chunk]
id: chunk-ds-114
source: "[[raw-ds-009]]"
supports: ["[[Bloom Filters and Probabilistic Structures]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Counting Bloom filters allow deletion at 4x space cost

## Context
Standard Bloom filters cannot delete because clearing a bit may affect other elements.

## Claim
Counting Bloom filters replace each bit with a 4-bit counter. Insert increments delete decrements. This supports deletion at 4x the space of a standard Bloom filter.

## Why It Matters
Useful when set membership changes over time but the higher space cost limits applicability.

## QnA Seeds
- Q: Why 4 bits per counter? -> A: Probability of counter exceeding 15 is negligible for practical load factors.
- Q: Can counters overflow? -> A: Theoretically yes but extremely rare with 4-bit counters.
