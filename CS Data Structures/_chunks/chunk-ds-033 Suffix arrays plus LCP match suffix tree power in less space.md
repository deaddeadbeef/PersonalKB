---
tags: [cs-ds, chunk]
id: chunk-ds-033
source: "[[raw-ds-027]]"
supports: ["[[Suffix Arrays]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Suffix arrays plus LCP arrays match suffix tree power in less space

## Context
Suffix trees use approximately 20 bytes per character.

## Claim
A suffix array with LCP array provides equivalent functionality to suffix trees for most queries while using only 8-12 bytes per character and offering better cache performance on modern hardware.

## Why It Matters
Modern bioinformatics tools like BWA and Bowtie use suffix arrays instead of suffix trees for genome indexing.

## QnA Seeds
- Q: What does the LCP array add? -> A: Longest Common Prefix between adjacent suffixes — enables O(m) pattern search.
- Q: How is it built? -> A: Kasai's algorithm computes LCP in O(n) from the suffix array.
