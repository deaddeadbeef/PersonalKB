---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Bloom Filters and Probabilistic Membership"
authors: [Pat Morin]
year: 2013
up: "[[Sources Index]]"
---

# Bloom Filters and Probabilistic Membership

## Summary

Bloom filters use a bit array of m bits and k hash functions for set membership testing. No false negatives, tunable false positives. Optimal k = (m/n) ln(2). At 1% FP rate, only 9.6 bits per element needed. Cannot support deletion without counting variant.

## Key Claims

1. Bloom filters guarantee zero false negatives
2. Optimal hash count is k = (m/n) * ln(2)
3. Space is constant per element for a given error rate
4. Standard Bloom filters do not support deletion
5. Count-Min Sketch and HyperLogLog use similar probabilistic trade-offs

## Atomic Facts

1. FP rate: approximately (1 - e^(-kn/m))^k
2. At 1% FP: ~9.6 bits per element
3. Used in Chrome safe browsing, Bitcoin SPV, database optimization
4. Counting Bloom filter: counters instead of bits, supports delete
5. Cuckoo filter: supports deletion, often more space-efficient
6. HyperLogLog: cardinality estimation using ~1.5 KB

## Significance

Bloom filters demonstrate the power of probabilistic trade-offs: accepting small error probability for dramatic space savings.

## Chunks Extracted

*Pending*
