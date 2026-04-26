---
id: chunk-csa-165
type: chunk
source: "[[Gusfield 1997 - Suffix Trees and Arrays]]"
source_loc: "Suffix Trees"
topic: "strings"
claim: "Suffix trees enable O(m) substring search in a text of length n after O(n) construction, making them theoretically optimal for exact pattern matching"
confidence: verified
supports:
  - "[[Suffix Tree]]"
  - "[[String Indexing]]"
tags:
  - csa
  - csa/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Strings — Suffix tree O(m) substring search after O(n) construction

## Context

A suffix tree for a string of length n is a compressed trie of all n suffixes, with exactly n leaves and at most n-1 internal nodes. Each edge is labeled with a substring represented as a (start, end) index pair. Any substring corresponds to a path prefix from the root, enabling O(m) substring search by walking down the tree matching characters. Suffix trees also solve the longest common substring problem in O(n + m) for two strings via a generalized suffix tree. The O(n) construction and O(m) query make suffix trees the theoretically optimal indexing structure.

## Why It Matters

Suffix trees are among the most powerful string processing tools in computer science, underpinning genome assembly, sequence alignment, and substring search across massive texts.

## QnA Seeds

- Q: How does a suffix tree enable O(m) substring search?
- Q: What are the size bounds on a suffix tree for a string of length n?
- Q: How does a generalized suffix tree solve longest common substring?
