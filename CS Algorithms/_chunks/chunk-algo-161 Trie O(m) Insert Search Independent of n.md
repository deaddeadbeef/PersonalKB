---
id: chunk-csa-161
type: chunk
source: "[[Sedgewick 2011 - Trie Data Structures]]"
source_loc: "Trie Basics"
topic: "data-structures"
claim: "Tries provide O(m) insert and search where m is key length, independent of the number of stored keys, unlike balanced BSTs which need O(m log n)"
confidence: verified
supports:
  - "[[Trie]]"
  - "[[String Data Structures]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Trie O(m) insert and search independent of key count

## Context

A trie stores strings in a tree where each node represents a single character and paths from root spell out prefixes. For alphabet size R, each node contains up to R children. Insert and search both follow child pointers character by character in O(m) time where m is the key length—completely independent of n, the number of keys stored. By contrast, balanced BSTs require O(m log n) for string keys because each comparison takes O(m) time across O(log n) levels. Search reaches a null pointer for absent keys or checks for a stored value at the end of the key.

## Why It Matters

Tries are the optimal data structure for string-keyed lookups, and understanding their O(m) bound versus the O(m log n) of tree-based alternatives is essential for choosing the right data structure.

## QnA Seeds

- Q: Why is trie search O(m) independent of the number of stored keys?
- Q: How does trie search complexity compare to balanced BST search for string keys?
- Q: What does each node in an R-way trie store?
