---
tags: [cs-ds, chunk]
id: chunk-ds-124
source: "[[raw-ds-007]]"
supports: ["[[Hash Tables and Hash Functions]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Perfect hashing gives O1 worst-case lookup for static key sets

## Context
Dynamic hash tables only guarantee expected O(1).

## Claim
For a static set of n keys perfect hashing constructs a two-level scheme: first level hashes to buckets, second level uses per-bucket perfect hash functions. Total space O(n) and lookup is guaranteed O(1) worst-case.

## Why It Matters
Optimal for read-only dictionaries like compiler keyword tables and network protocol dispatch.

## QnA Seeds
- Q: Why two levels? -> A: First level may collide. Second level has no collisions by construction.
- Q: Construction time? -> A: Expected O(n) using randomized algorithm. May need to retry hash functions.
