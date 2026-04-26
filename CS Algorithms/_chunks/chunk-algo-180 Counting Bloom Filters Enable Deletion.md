---
id: chunk-csa-180
type: chunk
source: "[[Bloom 1970 - Bloom Filters]]"
source_loc: "Counting Variants"
topic: "data-structures"
claim: "Counting Bloom filters replace bits with 3-4 bit counters to enable deletion at 3-4x space cost; cuckoo filters offer deletion with similar space and better lookup performance"
confidence: verified
supports:
  - "[[Bloom Filter]]"
  - "[[Cuckoo Filter]]"
tags:
  - csa
  - csa/data-structures
  - chunk
up: "[[CS Algorithms]]"
---
# Data Structures — Counting Bloom filters and cuckoo filters enable deletion

## Context

Standard Bloom filters cannot support deletion because clearing a bit may remove evidence for other elements. Counting Bloom filters replace each bit with a 3-4 bit counter; insertion increments and deletion decrements, enabling removal at the cost of 3-4x more space. Counter overflow is handled by not incrementing past the maximum, accepting a small additional error. Cuckoo filters (Fan et al., 2014) provide an alternative supporting deletion with similar space efficiency and better lookup performance for high load factors, using cuckoo hashing with fingerprints.

## Why It Matters

Many practical applications require deletion support—understanding the Bloom filter variants and their tradeoffs is essential for choosing the right probabilistic membership structure.

## QnA Seeds

- Q: Why do counting Bloom filters use 3-4 bit counters instead of 1-bit entries?
- Q: How do cuckoo filters improve on counting Bloom filters?
- Q: What error does counter overflow introduce in counting Bloom filters?
