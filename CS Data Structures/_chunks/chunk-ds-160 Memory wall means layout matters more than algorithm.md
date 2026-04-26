---
tags: [cs-ds, chunk]
id: chunk-ds-160
source: "[[raw-ds-022]]"
supports: ["[[Foundational Concepts Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# The memory wall means data structure layout matters more than algorithm choice

## Context
CPU speed has grown 1000x faster than memory latency since 1980.

## Claim
The memory wall (CPU-memory speed gap growing annually) means cache-friendly data layouts often matter more than algorithmic complexity. O(n) with good cache can beat O(log n) with poor cache for practical n.

## Why It Matters
Explains why arrays often beat trees in practice and why cache-aware/cache-oblivious design is critical.

## QnA Seeds
- Q: What is the memory wall? -> A: CPU speed grows faster than memory speed creating an ever-widening gap.
- Q: Example? -> A: Linear search in sorted array can beat BST lookup for n up to millions due to cache effects.
