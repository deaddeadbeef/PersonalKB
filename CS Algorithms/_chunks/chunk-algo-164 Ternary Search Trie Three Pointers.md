---
id: chunk-csa-164
type: chunk
source: "[[Sedgewick 2011 - Trie Data Structures]]"
source_loc: "Ternary Search Tries"
topic: "data-structures"
claim: "Ternary search tries use three pointers per node (less, equal, greater) achieving O(m + log n) search, balancing BST memory efficiency with trie time efficiency"
confidence: verified
supports:
  - "[[Ternary Search Trie]]"
  - "[[Trie]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Ternary search trie O(m + log n) with three pointers per node

## Context

A ternary search trie (TST) replaces the R-pointer array at each node with just three pointers: less (character is smaller), equal (character matches, advance to next), and greater (character is larger). Search compares the current character with the node's character and follows the appropriate pointer. This provides O(m + log n) search time—O(m) for matching characters plus O(log n) for BST-like comparisons at each position. TSTs use far less memory than R-way tries while supporting all trie operations including prefix queries.

## Why It Matters

TSTs represent a practical middle ground in the data structure design space, offering trie functionality with BST-like memory usage—important for applications where both features matter.

## QnA Seeds

- Q: How does a ternary search trie navigate its three pointers during search?
- Q: Why is TST search O(m + log n) rather than O(m)?
- Q: What advantage do TSTs have over R-way tries in terms of space?
