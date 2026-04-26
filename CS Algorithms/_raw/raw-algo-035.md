---
tags: [cs-algorithms, raw]
source_type: research-paper
source_title: "Bloom Filters: Space-Efficient Probabilistic Set Membership"
authors: [Burton H. Bloom]
year: 1970
---

## Summary

A Bloom filter is a space-efficient probabilistic data structure for approximate set membership queries. It answers "is element x in the set?" with two possible outcomes: "definitely not" (no false negatives) or "probably yes" (possible false positives). The structure consists of a bit array of m bits, initially all zeros, and k independent hash functions mapping elements uniformly to positions in [0, m). To insert an element, compute all k hash values and set those bit positions to 1. To query, compute all k hash values and check if all corresponding bits are 1—if any bit is 0, the element is definitely absent; if all are 1, the element is probably present (the bits may have been set by other elements). The false positive probability after inserting n elements is approximately (1 − e^(−kn/m))^k, minimized when k = (m/n)·ln 2. For a desired false positive rate ε, the required space is m = −n·ln(ε)/(ln 2)² ≈ 1.44·n·log₂(1/ε) bits—roughly 10 bits per element for a 1% false positive rate. This is dramatically less than storing the actual elements. Bloom filters do not support deletion (clearing a bit may remove other elements' evidence). Counting Bloom filters replace each bit with a counter, enabling deletion at the cost of 3–4× more space. Applications are pervasive: web browsers use them to check URLs against malware databases, CDNs use them to avoid caching one-hit wonders, databases use them to skip unnecessary disk reads for absent keys, and network routers use them for packet classification. Distributed systems use Bloom filters to summarize set contents for efficient set reconciliation between nodes.

## Key Claims

1. Bloom filters provide O(k) insert and query time with zero false negatives and a tunable false positive rate, using only ~1.44·n·log₂(1/ε) bits for n elements and error rate ε.
2. The optimal number of hash functions is k = (m/n)·ln 2, balancing between too few hash functions (high collision rate) and too many (too many bits set to 1).
3. Standard Bloom filters do not support deletion; counting Bloom filters address this by replacing bits with counters at the cost of increased space.
4. At 10 bits per element (~1.2 bytes), a Bloom filter achieves approximately 1% false positive rate—orders of magnitude less space than storing actual elements or hashes.
5. The false positive rate degrades gracefully as more elements are inserted: it increases smoothly rather than failing catastrophically, allowing capacity monitoring.

## Atomic Facts

1. The false positive probability formula (1 − e^(−kn/m))^k assumes ideal hash functions with uniform, independent output; practical implementations use MurmurHash or xxHash with double hashing.
2. Double hashing generates k hash values from two independent hashes h₁ and h₂: hᵢ(x) = h₁(x) + i·h₂(x) mod m, requiring only 2 hash computations regardless of k.
3. Counting Bloom filters use 3–4 bit counters per position; counter overflow is handled by not incrementing past the maximum, accepting a small additional error.
4. Cuckoo filters (Fan et al., 2014) support deletion with similar space and better lookup performance for high load factors, using cuckoo hashing with fingerprints.
5. In Google Chrome, a Bloom filter stored locally checks URLs against a compact representation of known malicious sites, avoiding network round-trips for safe URLs.
6. In LSM-tree databases (LevelDB, RocksDB, Cassandra), per-SSTable Bloom filters prevent unnecessary disk reads by quickly ruling out absent keys during point lookups.

## Significance

Bloom filters are one of the most widely deployed probabilistic data structures, appearing in systems across every scale of computing. Their elegance lies in the fundamental tradeoff: accept a small probability of false positives to achieve dramatic space savings and eliminate expensive operations (disk reads, network requests, database lookups). The mathematical framework for analyzing false positive rates connects information theory to practical system design. Variants including counting Bloom filters, cuckoo filters, quotient filters, and ribbon filters continue to evolve, each optimizing for specific use cases. Bloom filters exemplify how relaxing exactness requirements enables data structures with properties impossible under strict correctness guarantees.

## Chunks Extracted

chunk-algo-177 through chunk-algo-180
