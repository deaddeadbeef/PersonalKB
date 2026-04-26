---
tags: [cs-ds, chunk]
id: chunk-ds-013
source: "[[raw-ds-010]]"
supports: ["[[Tries and Prefix Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Trie lookup is O(m) independent of number of stored keys

## Context
Hash tables and BSTs have lookup dependent on n.

## Claim
Trie lookup traverses exactly m edges (one per character) regardless of n, making tries uniquely efficient for prefix-based queries.

## Why It Matters
Independence from n makes tries ideal for autocomplete, IP routing, and dictionaries.

## QnA Seeds
- Q: Why O(m) not O(m log n)? -> A: Each character directly indexes into child array -- no key comparisons.
- Q: What can tries do that hash tables cannot? -> A: Prefix enumeration, longest prefix match, ordered iteration.
