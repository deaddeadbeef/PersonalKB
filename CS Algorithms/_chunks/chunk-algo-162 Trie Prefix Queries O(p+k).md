---
id: chunk-csa-162
type: chunk
source: "[[Sedgewick 2011 - Trie Data Structures]]"
source_loc: "Prefix Queries"
topic: "data-structures"
claim: "Prefix queries in tries are a natural O(p+k) operation (p = prefix length, k = matches) that hash tables cannot perform efficiently"
confidence: verified
supports:
  - "[[Trie]]"
  - "[[Autocomplete]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Trie prefix queries in O(p+k) impossible for hash tables

## Context

Finding all keys sharing a given prefix requires only traversing to the prefix node in O(p) time, then collecting all complete keys in the subtrie via DFS/BFS in O(k) time where k is the number of matches. Hash tables cannot perform prefix queries efficiently because hashing destroys the character-by-character structure of keys. This makes tries the essential data structure for autocomplete systems (search engines, IDEs), spell checkers, and IP routing tables that need longest prefix matching.

## Why It Matters

Prefix queries are the killer feature that differentiates tries from hash tables, and this capability drives their use in autocomplete, routing, and dictionary applications.

## QnA Seeds

- Q: Why can't hash tables support efficient prefix queries?
- Q: How does autocomplete use trie prefix queries?
- Q: What is the time complexity of finding all keys with a given prefix in a trie?
