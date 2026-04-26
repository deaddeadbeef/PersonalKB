---
tags: [cs-ds, chunk]
id: chunk-ds-032
source: "[[raw-ds-027]]"
supports: ["[[Tries and Prefix Trees]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Ukkonens algorithm builds suffix trees in On time online

## Context
Naive suffix tree construction takes O(n^2) time.

## Claim
Ukkonen's algorithm builds the suffix tree incrementally left-to-right in O(n) time using suffix links, active point tracking, and the key insight that leaf edges extend implicitly.

## Why It Matters
Made suffix trees practical for large-scale string processing in bioinformatics and text search.

## QnA Seeds
- Q: What makes Ukkonen's O(n)? -> A: Suffix links plus implicit extensions avoid redundant work.
- Q: What is an implicit extension? -> A: Leaf edges automatically extend when a new character is added.
