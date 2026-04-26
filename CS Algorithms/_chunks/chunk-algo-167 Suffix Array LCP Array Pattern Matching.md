---
id: chunk-csa-167
type: chunk
source: "[[Gusfield 1997 - Suffix Trees and Arrays]]"
source_loc: "Suffix Arrays"
topic: "strings"
claim: "Suffix arrays with LCP arrays enable O(m + log n) pattern matching using 4-8 bytes per character versus 20+ for suffix trees"
confidence: verified
supports:
  - "[[Suffix Array]]"
  - "[[String Indexing]]"
tags:
  - csa
  - csa/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Strings — Suffix array plus LCP array achieves O(m + log n) matching in less space

## Context

A suffix array stores starting positions of all suffixes sorted lexicographically, requiring only O(n) space (4-8 bytes per character versus 20+ for suffix trees). Construction takes O(n) with the DC3 algorithm or O(n log n) with prefix doubling. The LCP array, built in O(n) using Kasai's algorithm, stores the longest common prefix between consecutive sorted suffixes. Together, they enable O(m + log n) pattern matching via LCP-enhanced binary search, approaching suffix tree performance with dramatically less memory.

## Why It Matters

Suffix arrays are the practical choice for large-scale string indexing where suffix trees' memory overhead is prohibitive, making them essential in bioinformatics and text processing.

## QnA Seeds

- Q: What space advantage do suffix arrays have over suffix trees?
- Q: How does Kasai's algorithm compute the LCP array in O(n)?
- Q: How does the LCP array improve binary search from O(m log n) to O(m + log n)?
