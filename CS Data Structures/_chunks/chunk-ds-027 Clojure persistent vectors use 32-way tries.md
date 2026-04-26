---
tags: [cs-ds, chunk]
id: chunk-ds-027
source: "[[raw-ds-024]]"
supports: ["[[Advanced Structures Overview]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Clojure persistent vectors use 32-way tries for near O1 operations

## Context
Immutable arrays normally require O(n) copy on modification.

## Claim
Clojure's persistent vector uses a 32-way trie with structural sharing, achieving O(log32 n) = effectively O(1) for get, set, and append — at most 7 levels for 34 billion elements.

## Why It Matters
Proves that immutability and performance are not mutually exclusive for practical programming.

## QnA Seeds
- Q: Why 32-way? -> A: Matches cache line size and gives very shallow trees (log32 n).
- Q: How does append work? -> A: Path copy from root to rightmost leaf, add new element, share rest.
