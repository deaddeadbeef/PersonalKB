---
tags: [cs-ds, probabilistic]
up: "[[Hash-Based Structures Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# HyperLogLog

> **One-line summary**: A probabilistic cardinality estimator that counts the number of distinct elements in a multiset using only $O(\log \log n)$ bits per register, achieving ~1.04/$\sqrt{m}$ standard error with m registers.

## 🎯 Intuition
**The Core Idea:** Hash each element, observe patterns of leading zeros in the binary hash, and use the maximum run of leading zeros across many buckets to estimate how many distinct elements you've seen.
**Analogy:** Imagine estimating crowd size at a stadium by asking everyone to flip coins. If the longest streak anyone reports is 20 heads in a row, the crowd is probably around 2²⁰ ≈ 1 million — because it takes roughly that many people for someone to get that lucky. HyperLogLog partitions the crowd into sections and combines their longest-streak reports.
**Why It Matters:** Counting unique visitors, unique IP addresses, unique search queries, or distinct anything at web scale where exact sets would require gigabytes of memory.

---

## ⚙️ Core Mechanics
### How It Works
HyperLogLog maintains an array `M` of `m = 2^b` registers (typically 8-bit each), where `b` is the precision parameter.

**Add element `x`:**
1. Compute `h = hash(x)` — a uniformly distributed hash.
2. Use the first `b` bits of `h` to select register index `j` (0 to m−1).
3. Let `w` = remaining bits of `h`. Compute `ρ(w)` = position of the leftmost 1-bit (1-indexed).
4. Set `M[j] = max(M[j], ρ(w))`.

**Estimate cardinality:**
1. Compute the harmonic mean: `Z = (Σ 2^(−M[j]))^(−1)`.
2. Raw estimate: `E = α_m × m² × Z`, where `α_m` is a bias-correction constant.
3. Apply small-range and large-range corrections if needed.

### Key Operations

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Add element | $O(1)$ | — | One hash + register update |
| Estimate count | $O(m)$ | — | Scan all m registers |
| Merge two HLLs | $O(m)$ | — | Element-wise max of registers |
| Initialize | $O(m)$ | $O(m)$ bytes | m registers × 8 bits each |
| Memory (typical) | — | ~1.5 KB | m=2048 (b=11), 6-bit registers |

### Key Facts
- **Standard error**: approximately `1.04/√m` — with 2048 registers, ~2.3% error.
- **Mergeable**: union of two HLLs is the element-wise maximum of their registers, making it ideal for distributed counting.
- **Cannot delete elements**: insertions are irreversible (max operation is not invertible).
- **Space vs. accuracy tradeoff**: doubling registers halves the standard error but doubles memory.
- The algorithm only needs hash uniformity, not independence — practical hash functions like MurmurHash3 work well.

---

## 🔬 Deep Dive
### Formal Properties
**Bias correction constant:**
`α_m = (m × ∫₀^∞ (log₂((2+u)/(1+u)))^m du)^(−1)`

For practical values: α₁₆ = 0.673, α₃₂ = 0.697, α₆₄ = 0.709, α_m = 0.7213/(1 + 1.079/m) for m ≥ 128.

**Error analysis:**
- The raw estimator has relative bias < 5×10⁻⁵ for m ≥ 16.
- Standard error = `1.04/√m` (slightly better than the earlier LogLog's `1.30/√m`).
- With m = 16384 (14-bit precision): 0.81% standard error using only 12 KB.

**Small/large range corrections (original paper):**
- If `E ≤ 5m/2` and any registers are zero, use Linear Counting: `E* = m × ln(m / V)` where V = number of zero registers.
- If `E > 2³²/30`, apply large-range correction: `E* = −2³² × ln(1 − E/2³²)` (for 32-bit hashes).

**HyperLogLog++ (Google's improvement):** uses 64-bit hashes (eliminating large-range correction), empirical bias correction for small cardinalities, and sparse representation for initially empty registers.

### Edge Cases and Pitfalls
- **Hash collisions**: a poor hash function (non-uniform) destroys accuracy. Always use a high-quality hash (MurmurHash3, xxHash64).
- **Small cardinalities**: raw HLL overestimates for small sets. HLL++ adds bias correction tables derived from empirical simulation.
- **Sparse regime**: when most registers are still zero, memory can be saved with a sparse map (HLL++ sparse representation).
- **Cannot compute intersection directly**: `|A ∩ B|` requires inclusion-exclusion (`|A| + |B| − |A ∪ B|`), which amplifies error for nearly disjoint sets.
- **Register overflow**: with 8-bit registers, max representable leading-zero run is 255, supporting cardinalities up to ~2²⁵⁵. Not a practical concern.

### Real-World Usage
- **Redis**: `PFADD`, `PFCOUNT`, `PFMERGE` commands implement HyperLogLog with 12 KB per key (m=16384). Used for unique visitor counting.
- **Google BigQuery**: `APPROX_COUNT_DISTINCT()` uses HLL++ internally.
- **Apache Spark / Flink**: built-in approximate distinct count functions use HLL.
- **Presto/Trino**: `approx_distinct()` is HLL-based, widely used at Facebook/Meta for analytics.
- **Network security**: counting unique source IPs per destination for DDoS detection.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does HyperLogLog use the *harmonic mean* instead of the arithmetic mean of register values?
2. With m = 1024 registers, what is the approximate standard error of the cardinality estimate?
3. If two HyperLogLog sketches are merged, is the result equivalent to having processed the union of both input streams? Why?

### Core Problems
1. **Implement HLL from scratch**: Write a basic HyperLogLog with `add(item)` and `count()` methods. Use a 64-bit hash, b=14 precision. Test on known-cardinality datasets and measure actual vs. estimated error.
2. **Set intersection estimation**: Given two HyperLogLog sketches A and B, estimate |A ∩ B| using inclusion-exclusion. Derive the error bound and explain when this approach fails badly.

### Challenge
Design a **sliding-window HyperLogLog** that estimates the number of distinct elements in the last T seconds of a stream. You cannot simply expire old registers. Propose a scheme (e.g., using multiple time-bucketed HLLs, or LPCA) and analyze its space-accuracy-time tradeoffs.

---

*See also:* [[CS Data Structures/Hash-Based Structures/Bloom Filters and Probabilistic Structures|Bloom Filter]] · [[Count-Min Sketch]] · [[CS Data Structures/Hash-Based Structures/Cuckoo Filters|Cuckoo Filter]] | **CS Algorithms:** [[CS Algorithms/Techniques/Streaming Algorithms|Streaming Algorithms]] · [[CS Algorithms/Techniques/Randomized Algorithms|Randomized Algorithms]]

## References
-> [[CS Data Structures/Sources/Sources Index|Sources Index]]
