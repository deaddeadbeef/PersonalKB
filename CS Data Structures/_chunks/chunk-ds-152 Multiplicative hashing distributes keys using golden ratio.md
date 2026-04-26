---
tags: [cs-ds, chunk]
id: chunk-ds-152
source: "[[raw-ds-007]]"
supports: ["[[Hash Tables and Hash Functions]]"]
confidence: verified
up: "[[CS Data Structures]]"
---

# Multiplicative hashing distributes keys using golden ratio constant

## Context
A good hash function must distribute keys uniformly across buckets.

## Claim
Multiplicative hashing computes h(k) = floor(m * frac(k * A)) where A is an irrational constant. Using the golden ratio reciprocal A = 0.6180339... achieves particularly good distribution across any table size m.

## Why It Matters
Knuth recommended the golden ratio constant. It produces near-uniform distribution with a single multiply.

## QnA Seeds
- Q: Why golden ratio? -> A: Its continued fraction convergents are maximally slow giving optimal spacing.
- Q: Is it better than modular hashing? -> A: Works well for any m. Modular needs m to be prime for good distribution.
