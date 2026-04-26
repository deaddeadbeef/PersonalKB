---
id: chunk-csa-178
type: chunk
source: "[[Bloom 1970 - Bloom Filters]]"
source_loc: "Optimal Parameters"
topic: "data-structures"
claim: "The optimal number of Bloom filter hash functions is k = (m/n) ln 2, balancing collision rate against bit saturation"
confidence: verified
supports:
  - "[[Bloom Filter]]"
  - "[[Probabilistic Data Structures]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Optimal Bloom filter hash count k = (m/n) ln 2

## Context

The false positive rate is minimized when k = (m/n)*ln(2). Too few hash functions means high collision rate (many elements share bit positions). Too many means too many bits set to 1 (the array saturates). In practice, k is computed from the desired error rate and n. Double hashing generates k values from just two independent hashes: h_i(x) = h1(x) + i*h2(x) mod m, requiring only 2 hash computations regardless of k. Practical implementations use MurmurHash or xxHash.

## Why It Matters

Understanding the optimal k formula is essential for correctly sizing Bloom filters—misconfigured parameters can dramatically degrade performance or waste space.

## QnA Seeds

- Q: What happens if too many hash functions are used in a Bloom filter?
- Q: How does double hashing reduce the number of required hash computations?
- Q: What is the formula for optimal k in a Bloom filter?
