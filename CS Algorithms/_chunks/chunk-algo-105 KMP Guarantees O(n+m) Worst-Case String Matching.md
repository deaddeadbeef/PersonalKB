---
id: chunk-algo-105
type: chunk
source: "[[raw-algo-017]]"
source_loc: "String Matching Algorithms - Key Claims"
topic: "strings"
claim: "KMP preprocesses a pattern of length m to build a failure function in O(m) time, then scans text of length n in O(n) with the text pointer never retreating, achieving O(n+m) worst-case guaranteed string matching."
confidence: verified
supports:
  - "[[String Matching - KMP]]"
tags:
  - cs-algorithms
  - cs-algorithms/strings
  - chunk
up: "[[CS Algorithms]]"
---
# KMP Guarantees O(n+m) Worst-Case String Matching

## Context

KMP's failure function pi[i] gives the length of the longest proper prefix of pattern[0..i] that is also a suffix. For pattern 'abcabd', pi = [0,0,0,1,2,0]. Upon mismatch at position j, KMP shifts the pattern to align position pi[j-1] with the current text position, avoiding re-scanning. The text pointer advances monotonically—never backward—enabling the O(n) scan guarantee. The failure function computation uses amortized analysis: total pointer advances during preprocessing are at most 2m.

## Why It Matters

KMP is the foundational linear-time exact string matching algorithm. Its failure function concept recurs in Aho-Corasick and suffix automata. The amortized text pointer analysis is a canonical example of proving linear-time bounds.

## QnA Seeds

- Q: What does KMP's failure function pi[i] represent?
- Q: Why does the KMP text pointer never retreat?
- Q: What input triggers O(nm) worst case for naive string matching?