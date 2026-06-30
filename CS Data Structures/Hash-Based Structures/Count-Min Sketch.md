---
tags: [cs-ds, probabilistic]
up: "[[Hash-Based Structures Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Count-Min Sketch

> **One-line summary**: A sub-linear space probabilistic data structure that estimates the frequency of events in a data stream, allowing controlled over-counting but never under-counting.

## 🎯 Intuition
**The Core Idea:** Use multiple independent hash functions to map events into a compact 2D array of counters, then take the minimum across rows to estimate frequency.
**Analogy:** Imagine an imperfect attendance counter at a music festival — several volunteers each track attendance on their own tally sheet with limited slots, occasionally lumping different people into the same slot. When you ask "how many times did Alice visit?", you check all volunteers and trust the lowest count, since higher counts are inflated by collisions.
**Why It Matters:** Streaming analytics, network traffic monitoring, NLP word frequency estimation, and database query optimization all need approximate frequency counts over massive data volumes where exact counting is infeasible.

---

## ⚙️ Core Mechanics
### How It Works
A Count-Min Sketch consists of a 2D array of counters with **d rows** and **w columns**, paired with **d** pairwise-independent hash functions (one per row). Each hash function maps items to columns in its corresponding row.

**Update (Add):** When item `x` arrives with count `c` (typically 1):
- For each row `i` in `[0, d)`, compute `h_i(x) mod w` and increment `table[i][h_i(x) mod w]` by `c`.

**Query (Estimate):** To estimate the frequency of item `x`:
- For each row `i`, read `table[i][h_i(x) mod w]`.
- Return the **minimum** value across all `d` rows.

The minimum is chosen because collisions can only increase counts, never decrease them — so the minimum is closest to the true count.

### Key Operations

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Update (add) | $O(d)$ | — | d hash computations + increments |
| Point query | $O(d)$ | — | d lookups + min |
| Initialize | $O(d × w)$ | $O(d × w)$ | d = ln(1/δ), w = e/ε |
| Merge two sketches | $O(d × w)$ | $O(d × w)$ | Element-wise addition |
| Inner product query | $O(d × w)$ | — | Dot product of two sketches per row |

### Key Facts
- **Never underestimates**: the true count ≤ estimated count, always.
- **Space-independent of stream length**: size depends only on desired accuracy (ε) and confidence (δ).
- **Mergeable**: two sketches with identical parameters can be combined by summing corresponding cells — critical for distributed systems.
- **Supports deletions** via Count-Min Sketch with negative updates (though this loses the non-negative guarantee).
- Each row is essentially an independent frequency estimator; taking the min reduces error.

---

## 🔬 Deep Dive
### Formal Properties
Given parameters:
- **Width** `w = ⌈e/ε⌉` (where e ≈ 2.718)
- **Depth** `d = ⌈ln(1/δ)⌉`
- Total space: `O((1/ε) × ln(1/δ))` counters

**Error guarantee (point query):** For any item `x` with true frequency `f_x` and total stream count `N`:
- `f_x ≤ f̂_x ≤ f_x + εN` with probability at least `1 − δ`.

This is an **(ε, δ)-approximation**: the over-estimate is bounded by εN with failure probability at most δ.

**Conservative Update** optimization: when incrementing, only increase cells whose current value equals the current minimum estimate. This strictly reduces over-counting and tightens error in practice.

### Edge Cases and Pitfalls
- **Heavy hitters dominate collisions**: if a few items have very high frequency, they inflate estimates for low-frequency items disproportionately. Use heavy-hitter detection (e.g., Space-Saving) alongside CMS.
- **Deletions break guarantees**: allowing decrements means estimates can drop below zero; use Count-Min-Log or similar variants for deletion support with probabilistic guarantees.
- **Hash function quality matters**: poor hash families introduce correlated collisions. Use universal or 2-independent hash families (e.g., Carter-Wegman).
- **Not suitable for low-frequency exact counts**: if you need exact counts for rare items, consider a hybrid approach with a small exact-count hash map for items exceeding a threshold.
- **Parameter tuning**: setting ε too large wastes accuracy; too small wastes space. Typical values: ε = 0.001, δ = 0.01 gives ~7 rows and ~2,718 columns.

### Real-World Usage
- **Network monitoring**: AT&T and Cisco use CMS variants for per-flow traffic estimation on backbone routers processing millions of packets/second.
- **Database systems**: Apache Spark and PostgreSQL use CMS for approximate query processing and join-size estimation.
- **NLP/ML pipelines**: estimating n-gram frequencies in large corpora; Google's Sawzall system used CMS for log analysis.
- **Redis**: the `CMS.*` commands in RedisBloom provide a production Count-Min Sketch implementation.
- **Advertising**: click and impression frequency capping at scale.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why does Count-Min Sketch take the *minimum* across rows rather than the average?
2. If you double the width `w`, how does the error bound ε change?
3. Can a Count-Min Sketch ever report a frequency of zero for an item that was actually inserted?

### Core Problems
1. **Heavy Hitters Detection**: Given a stream of N elements, design a system using a Count-Min Sketch that identifies all items with frequency > N/k (the "heavy hitters"). Analyze space and time.
2. **Range Query Support**: Extend a Count-Min Sketch to support range frequency queries `freq(a..b)` using dyadic intervals. What is the error amplification factor?

### Challenge
Design a **distributed Count-Min Sketch** system for a cluster of 100 nodes, each seeing a partition of a click stream. Nodes periodically merge sketches at a coordinator. Analyze: (a) communication cost per merge round, (b) accuracy degradation versus a single-node sketch, (c) how to handle clock skew and late-arriving data.

### Bonus Exploration
- Compare Count-Min Sketch vs. Count Sketch (which allows negative counters and uses median instead of min). When does each win?
- Investigate Count-Min-Log: a variant that stores logarithmic counters to reduce space at the cost of probabilistic increment.

---

*See also:* [[Bloom Filters and Probabilistic Structures|Bloom Filter]] · [[HyperLogLog]] · Cuckoo Filter | **CS Algorithms:** Streaming Algorithms · Randomized Algorithms

## References
-> [[Sources Index]]
