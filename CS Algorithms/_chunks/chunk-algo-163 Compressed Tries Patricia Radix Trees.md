---
id: chunk-csa-163
type: chunk
source: "[[Sedgewick 2011 - Trie Data Structures]]"
source_loc: "Compressed Tries"
topic: "data-structures"
claim: "Compressed tries (Patricia/radix trees) collapse single-child chains into multi-character edges, reducing space from O(nRm) to O(nm) for n keys of average length m"
confidence: verified
supports:
  - "[[Patricia Tree]]"
  - "[[Trie]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Compressed tries collapse single-child chains for space efficiency

## Context

Standard R-way tries allocate R pointers per node regardless of actual children, leading to O(n*R*m) space for n keys of average length m with alphabet size R. Compressed tries (Patricia trees, radix trees) address this by collapsing chains of single-child nodes into single edges labeled with substrings, reducing node count dramatically for sparse key sets. Patricia trees were invented by Morrison in 1968 for IP address lookup. Ternary search tries (TSTs) use three pointers per node (less, equal, greater), achieving O(m + log n) search with much less memory than R-way tries.

## Why It Matters

Space optimization is critical for large-scale string indexing—compressed tries make trie-based approaches practical for applications like IP routing and text indexing where memory is constrained.

## QnA Seeds

- Q: What is the space reduction from standard tries to compressed tries?
- Q: How do ternary search tries balance memory and time efficiency?
- Q: What problem do Patricia trees solve compared to standard R-way tries?
