---
tags: [cs-ds, raw]
id: raw-ds-027
source: "Various (string algorithms literature)"
up: "[[CS Data Structures]]"
---

# Suffix Trees

## Key Ideas
- Suffix tree: compressed trie of all suffixes of string S
- Contains n leaves (one per suffix) and at most n-1 internal nodes
- Ukkonen's algorithm: build in O(n) time online (left to right)
- Space: O(n) with edge labels stored as (start, end) index pairs
- Exact pattern matching: O(m) time by traversing from root
- Longest repeated substring: deepest internal node — O(n)
- Longest common substring of two strings: generalized suffix tree — O(n+m)
- Suffix links: pointer from internal node for 'aX' to node for 'X' — enables online construction
- Practical issue: constant factor ~20 bytes/character vs 4-8 for suffix arrays
- Suffix automaton: equivalent power, sometimes more space-efficient

## Suffix Tree vs Suffix Array
- Suffix tree: O(n) construction, O(m) search, ~20n bytes
- Suffix array + LCP: O(n) construction, O(m log n) search (O(m) with LCP), ~8n bytes
- Modern preference: suffix arrays due to space and cache performance
