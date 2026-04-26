---
tags: [cs-ds, chunk]
id: chunk-ds-010
source: "[[raw-ds-007]]"
supports: ["[[Hash Tables and Hash Functions]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Hash tables achieve expected O(1) via load factor management

## Context
Hash tables map keys to array indices via hash functions.

## Claim
Hash tables achieve expected O(1) by keeping load factor alpha = n/m below threshold (typically 0.75) and resizing when exceeded.

## Why It Matters
This makes hash tables the fastest general-purpose structure for key-value lookup.

## QnA Seeds
- Q: What is load factor? -> A: alpha = n/m (items/slots); higher means more collisions.
- Q: What happens when threshold exceeded? -> A: Table doubles and all entries rehashed -- O(n) amortized to O(1).
