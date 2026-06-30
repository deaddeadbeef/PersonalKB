---
tags: [cs-ds, compression]
up: "[[Foundational Concepts Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Succinct and Compressed Data Structures

> **One-line summary**: Data structures that use space close to the information-theoretic minimum while still supporting efficient queries directly on the compressed representation — no decompression needed.

## 🎯 Intuition
**The Core Idea:** Store data using (almost) the minimum possible bits dictated by information theory, while still answering queries in $O(1)$ or $O(\log n)$ time without decompressing.
**Analogy:** Imagine a dictionary printed in tiny font on rice paper — it takes almost the minimum amount of paper physically possible, yet you can still look up any word instantly because the structure (alphabetical order, page headers) is preserved in the compressed form. You never need to "uncompress" the dictionary to use it.
**Why It Matters:** Genomic databases, web search indexes, mobile devices with limited RAM, and any system where data is orders of magnitude larger than available memory benefit from succinct structures that fit data in near-optimal space while remaining queryable.

---

## ⚙️ Core Mechanics
### How It Works

**Information-theoretic minimum:**
For a set S from a universe of size U, the minimum bits needed is `Z = ⌈log₂ C(U, |S|)⌉` (the number of bits to distinguish all possible sets of that size).

**Succinctness spectrum:**
- **Implicit**: uses exactly Z bits (e.g., a sorted array for a static set).
- **Succinct**: uses `Z + o(Z)` bits — the leading term is optimal, with a lower-order-term overhead.
- **Compact**: uses `O(Z)` bits — within a constant factor.
- **Compressed**: uses space proportional to the entropy of the specific input (e.g., compressed suffix arrays use space proportional to the empirical entropy of the text).

**Fundamental building blocks:**

**Bitvector with Rank and Select:**
- Store a bitvector B[0..n-1] using n bits.
- `rank₁(i)` = number of 1-bits in B[0..i]. Supported in $O(1)$ time with o(n) extra bits using a two-level lookup table.
- `select₁(j)` = position of the j-th 1-bit. Also $O(1)$ with o(n) extra bits.
- These are the building blocks for virtually all succinct structures.

**Rank structure (Jacobson, 1989):**
- Divide bitvector into superblocks of size `(log n)²` and blocks of size `(log n)/2`.
- Store cumulative rank at each superblock boundary ($O(n / \log n)$ bits).
- Store relative rank within each block ($O(n × \log \log n / \log n)$ bits).
- Within a block, use a precomputed lookup table indexed by the block's bit pattern ($O(√n)$ bits).
- Total extra space: o(n) bits. Query time: $O(1)$.

### Key Operations

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Rank(i) | $O(1)$ | n + o(n) bits | Two-level table |
| Select(j) | $O(1)$ | n + o(n) bits | Three-level with binary search |
| Access B[i] | $O(1)$ | n bits | Direct bit access |
| Succinct tree navigation | $O(1)$ | 2n + o(n) bits | BP or LOUDS encoding |
| Wavelet tree query | $O(\log σ)$ | n log σ + o(n log σ) bits | σ = alphabet size |

### Key Facts
- A bitvector of n bits with rank/select support uses `n + o(n)` total bits — the overhead vanishes relative to the data.
- **Succinct trees**: an n-node ordinal tree can be represented in `2n + o(n)` bits (balanced parentheses encoding or LOUDS) supporting parent, child, subtree-size queries in $O(1)$.
- **Wavelet trees**: represent a sequence of n symbols from an alphabet of size σ using `n log₂ σ + o(n log σ)` bits, supporting rank, select, and range queries.
- **Compressed Suffix Arrays (CSA)** and **FM-indexes** store a text's suffix array in space proportional to the text's k-th order empirical entropy while supporting pattern matching in $O(m \log σ)$ time for a pattern of length m.
- Succinct structures trade a small amount of query speed (higher constants) for dramatic space savings — often 10-100× compression vs. pointer-based structures.

---

## 🔬 Deep Dive
### Formal Properties
**Lower bound for rank/select:**
Miltersen (1998) proved that any structure supporting $O(1)$ rank on a bitvector of n bits requires n + $\Omega(n / (\log n)$^$O(1)$) bits — Jacobson's structure essentially matches this.

**Balanced Parentheses (BP) encoding for trees:**
- Traverse the tree in DFS. Write '(' when entering a node, ')' when leaving.
- The resulting 2n-bit string uniquely encodes the tree.
- With $O(n / \log n)$ auxiliary bits, supports: parent, first-child, next-sibling, subtree-size, depth, LCA — all in $O(1)$.

**Entropy-compressed structures:**
For a text T of length n over alphabet σ, the k-th order empirical entropy is:
`H_k(T) = Σ_{w∈σ^k} (|T_w|/n) × H_0(T_w)`
where T_w is the subsequence of characters following context w.

The FM-index (Ferragina & Manzini, 2000) achieves `nH_k(T) + o(n log σ)` bits and supports:
- `count(P)`: number of occurrences of pattern P in $O(|P| \log σ)$ time.
- `locate(P)`: positions of occurrences in $O(\log^(1+ε)$ n) time per occurrence.

### Edge Cases and Pitfalls
- **Construction cost**: building succinct structures often requires $O(n)$ time and $O(n)$ words of working space — the compression ratio is only realized after construction.
- **Update difficulty**: most succinct structures are static. Dynamic succinct bitvectors exist but have $O(\log n / \log \log n)$ per operation — significantly slower than $O(1)$ for static.
- **Practical constants**: the o(n) terms in space and the lookup tables can be non-trivial for small n. Succinct structures pay off primarily for large datasets (millions+ elements).
- **Cache behavior**: bit-level packing can cause poor cache utilization compared to word-aligned structures. Modern implementations use word-parallel operations (popcount, BMI2) to mitigate this.
- **Implementation complexity**: correct implementation of rank/select with o(n) overhead is subtle. Use tested libraries (SDSL, Succinct, rank9) rather than rolling your own.

### Real-World Usage
- **Bioinformatics**: FM-indexes are the backbone of read aligners like BWA, Bowtie, and HISAT2, indexing human genomes (~3 billion characters) in ~1.5 GB.
- **Web search**: Google's original index used succinct structures for inverted index compression. Lucene/Elasticsearch use succinct bitvector techniques.
- **Databases**: Roaring Bitmaps (a practical compressed bitvector) are used in Apache Druid, Apache Spark, and Pilosa for set operations on large column stores.
- **Succinct trees**: the LOUDS representation is used in Google's Protobuf FieldMask and in succinct trie implementations for IP routing tables.
- **SDSL-lite**: a C++ library providing production-quality implementations of compressed suffix arrays, wavelet trees, and rank/select structures. Widely used in research and industry.
- **Mobile/embedded**: succinct structures enable deploying large dictionaries and indexes on memory-constrained devices (e.g., spell-check dictionaries on smartphones).

---

## 🏋️ Practice
### Warm-Up (5 min)
1. What does it mean for a data structure to be "succinct" vs. "compact" vs. "compressed"?
2. How many bits are needed to represent an arbitrary binary tree with n nodes, and how does the balanced parentheses encoding achieve this?
3. Why is `rank` on a bitvector the fundamental building block of most succinct structures?

### Core Problems
1. **Rank/Select Bitvector**: Implement a bitvector supporting $O(1)$ rank using superblocks and blocks as described by Jacobson. Verify correctness against a naive $O(n)$ rank. Measure space overhead for bitvectors of size 10⁶, 10⁷, 10⁸.
2. **Succinct Tree (BP encoding)**: Encode a given tree as a balanced parentheses bitvector. Implement `parent(v)`, `first_child(v)`, `next_sibling(v)`, and `subtree_size(v)` using `rank`/`select` on '(' and ')'. Test on a tree with 100,000 nodes.

### Challenge
Implement a simplified **FM-index** for a DNA sequence (alphabet {A, C, G, T}):
1. Construct the BWT (Burrows-Wheeler Transform) of the input text.
2. Build a wavelet tree over the BWT to support rank queries.
3. Implement `count(pattern)` using backward search.
4. Test on a 1 MB genome fragment and compare space usage vs. a suffix array.

---

*See also:* [[Bloom Filters and Probabilistic Structures|Bloom Filter]] · [[Tries and Prefix Trees|Tries]] · Suffix Trees and Arrays | **CS Algorithms:** Information Theory · Compression Algorithms

## References
-> [[Sources Index]]
