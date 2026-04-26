---
tags: [cs-ds, chunk]
id: chunk-ds-100
source: "[[raw-ds-037]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# X-fast and Y-fast tries reduce vEB space to O(n) with hashing

## Context
Van Emde Boas trees use O(u) space which is wasteful for sparse sets.

## Claim
X-fast tries store only occupied paths using hash tables at each level achieving O(log log u) with O(n log u) space. Y-fast tries add indirection through balanced BSTs of O(log u) elements achieving O(n) space with O(log log u) expected time.

## Why It Matters
Makes predecessor search on integer keys practical for sparse sets where vEB space is prohibitive.

## QnA Seeds
- Q: How does X-fast reduce space? -> A: Store only prefix paths of existing keys using per-level hash tables.
- Q: How does Y-fast improve further? -> A: Groups consecutive keys into balanced BSTs of size O(log u).
