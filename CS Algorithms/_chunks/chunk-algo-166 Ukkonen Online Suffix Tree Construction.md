---
id: chunk-csa-166
type: chunk
source: "[[Gusfield 1997 - Suffix Trees and Arrays]]"
source_loc: "Ukkonen Algorithm"
topic: "strings"
claim: "Ukkonen's algorithm constructs suffix trees online in O(n) time using suffix links, implicit extensions, and the once-a-leaf-always-a-leaf observation"
confidence: verified
supports:
  - "[[Suffix Tree]]"
  - "[[Ukkonen Algorithm]]"
tags:
  - csa
  - csa/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Strings — Ukkonen's online O(n) suffix tree construction

## Context

Ukkonen's algorithm (1995) builds a suffix tree left to right, extending the tree one character at a time. Three key optimizations achieve O(n) time: (1) implicit extensions avoid explicitly extending suffixes that end at leaves (once a leaf, always a leaf), (2) suffix links connect internal nodes to enable O(1) amortized transitions between extension points, and (3) the active point tracks the current position in the tree to avoid redundant traversals. Each phase processes one character and performs at most O(1) amortized explicit work.

## Why It Matters

Ukkonen's algorithm is the standard O(n) suffix tree construction method, and understanding its three optimizations is essential for implementing practical suffix-based string indexing.

## QnA Seeds

- Q: What are the three key optimizations in Ukkonen's algorithm?
- Q: What does 'once a leaf, always a leaf' mean in Ukkonen's algorithm?
- Q: How do suffix links contribute to O(n) construction time?
