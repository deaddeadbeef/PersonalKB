---
tags: [cs-ds, raw]
id: raw-ds-037
source: "Various (van Emde Boas 1975)"
up: "[[CS Data Structures]]"
---

# Van Emde Boas Trees

## Key Ideas
- Universe size u, stores integers in {0, ..., u-1}
- All operations: O(log log u) — doubly logarithmic!
- Structure: recursive — divide universe into sqrt(u) clusters of size sqrt(u)
- Each cluster is a smaller vEB tree, plus a summary vEB tree over non-empty clusters
- Insert, delete, successor, predecessor, min, max: all O(log log u)
- Space: O(u) naive — problematic for large universes
- X-fast trie: O(log log u) with O(n) space using hashing
- Y-fast trie: O(log log u) expected with O(n) space
- Practical issue: u must be known upfront, and O(u) space is wasteful for sparse sets
- For 32-bit integers: O(log log 2^32) = O(log 32) = O(5) — effectively constant
- For 64-bit: O(log 64) = O(6) — still essentially constant

## When to Use
- Integer keys from bounded universe where O(log n) is too slow
- Predecessor queries on integers (routers, IP lookup)
- Theoretical importance: breaks the comparison-based O(log n) barrier
