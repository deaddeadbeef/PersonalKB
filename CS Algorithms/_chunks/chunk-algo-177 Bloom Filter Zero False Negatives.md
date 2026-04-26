---
id: chunk-csa-177
type: chunk
source: "[[Bloom 1970 - Bloom Filters]]"
source_loc: "Core Properties"
topic: "data-structures"
claim: "Bloom filters guarantee zero false negatives with tunable false positive rate using approximately 1.44 n log2(1/e) bits for n elements and error rate e"
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
# Data Structures — Bloom filter zero false negatives with tunable false positive rate

## Context

A Bloom filter uses a bit array of m bits and k hash functions. To insert: set k bit positions to 1. To query: check if all k bits are 1—if any is 0, the element is definitely absent (zero false negatives); if all are 1, probably present (possible false positives). The false positive probability after n insertions is approximately (1 - e^(-kn/m))^k. Required space for desired rate e is m = -n*ln(e)/(ln 2)^2, roughly 1.44*n*log2(1/e) bits. Standard Bloom filters do not support deletion since clearing a bit may remove evidence for other elements.

## Why It Matters

Bloom filters are among the most widely deployed probabilistic data structures, appearing in web browsers, CDNs, databases, and network routers wherever approximate membership testing saves expensive operations.

## QnA Seeds

- Q: Why do Bloom filters guarantee zero false negatives?
- Q: What is the space formula for a Bloom filter with desired false positive rate e?
- Q: Why can't standard Bloom filters support deletion?
