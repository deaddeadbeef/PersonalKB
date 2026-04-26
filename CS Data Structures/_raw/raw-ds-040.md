---
tags: [cs-ds, raw]
id: raw-ds-040
source: "Various (succinct data structure literature)"
up: "[[CS Data Structures]]"
---

# Succinct Data Structures

## Key Ideas
- Information-theoretic minimum: bits needed = ceil(log2(number of possible instances))
- Implicit: exactly the minimum bits (e.g., binary heap in array)
- Succinct: minimum + o(minimum) lower-order bits
- Compact: O(minimum) bits (constant factor overhead)
- Succinct bit vector: n bits + o(n) bits supporting O(1) rank and select
- Rank(i): count of 1s in positions 0..i — uses two-level lookup table
- Select(j): position of j-th 1 — uses similar technique
- Wavelet tree: succinct structure for sequences — O(log sigma) rank/select on any symbol
- Succinct trees: 2n + o(n) bits for n-node tree with O(1) navigation
- LOUDS (Level-Order Unary Degree Sequence): encode tree in ~2n bits
- FM-index: compressed full-text index using BWT — search in O(m) time, O(n log sigma) bits
- Practical implementations: sdsl-lite library (C++), Succinct library (Rust)

## Why It Matters
- Process datasets larger than RAM by reducing memory footprint 10-100x
- Genomics: human genome (3 billion bases) indexed in ~1 GB
- Web search: compressed inverted indices with fast query
