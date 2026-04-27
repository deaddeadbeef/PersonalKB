---
tags: [cs-ds, hash]
up: "[[Hash-Based Structures Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Universal and Perfect Hashing

> **One-line summary**: Universal hashing provides probabilistic collision guarantees independent of input distribution, while perfect hashing eliminates collisions entirely for static key sets.

## 🎯 Intuition
**The Core Idea:** Universal hashing randomises the hash function so no adversary can craft worst-case inputs; perfect hashing goes further and guarantees zero collisions for a known, fixed set of keys.
**Analogy:** Universal hashing is like shuffling a deck of cards before dealing — no matter how the opponent arranged the deck, the shuffle makes the outcome fair. Perfect hashing is like custom-printing name badges for a guest list — every name maps to a unique badge number with no duplicates.
**Why It Matters:** Universal hashing is the theoretical backbone that lets hash-table analyses hold without input assumptions (critical for security against HashDoS attacks). Perfect hashing converts any static lookup into guaranteed $O(1)$ — essential for routing tables, keyword recognisers, and constant databases.

---

## ⚙️ Core Mechanics
### How It Works
**Universal Hashing**: a family ℋ of hash functions is **universal** if, for any two distinct keys x ≠ y, Pr[h(x) = h(y)] ≤ 1/m when h is chosen uniformly from ℋ. Because the function is chosen *after* the adversary commits to a key set, no fixed input can consistently cause worst-case behaviour.

**Carter-Wegman family** (canonical construction):
h_{a,b}(k) = ((a·k + b) mod p) mod m
where *p* is a prime larger than the key universe, and *a*, *b* are chosen uniformly at random with a ≠ 0. This is universal and efficient — one multiply, one add, two modular reductions.

**Perfect Hashing (FKS scheme)** for static dictionaries:
1. **First level**: a universal hash distributes *n* keys into m = n buckets.
2. **Second level**: for each bucket of size s_i, build a table of size s_i² with its own universal hash function, chosen so no collisions remain.
3. The birthday-paradox argument ensures a collision-free second-level function exists with constant probability when the table size is quadratic in bucket size.
4. Total space: $O(n)$. Every lookup: exactly two hash evaluations → **$O(1)$ worst-case**.

**Minimal perfect hashing** maps *n* keys to exactly {0, …, n−1} with no gaps — useful for compact static dictionaries (≈ 2–3 bits/key).

### Key Operations

| Scheme | Build Time | Query Time | Space |
|---|---|---|---|
| Universal (Carter-Wegman) | $O(1)$ to select h | $O(1)$ expected per query | $O(m)$ table |
| FKS Perfect Hashing | $O(n)$ expected | $O(1)$ worst case | $O(n)$ |
| Minimal Perfect Hashing | $O(n)$ expected | $O(1)$ worst case | $O(n)$ (≈ 2–3 bits/key) |

### Key Facts
- A universal family guarantees Pr[h(x) = h(y)] ≤ 1/m for any distinct x, y, independent of the key distribution.
- Carter-Wegman (1979) was the first explicit universal family; it requires a prime p > |U|.
- k-independence (or k-wise independence) is a stronger property: any k distinct keys hash to uniformly random independent values.
- 2-independent hashing suffices for expected $O(1)$ chained hash-table lookups.
- FKS perfect hashing achieves $O(1)$ worst-case lookups with $O(n)$ space for n static keys.
- The construction is Las Vegas randomised: building the table may need a few random trials but always produces a correct result.
- Minimal perfect hashing maps n keys to exactly {0, …, n−1} with no gaps — useful for compact static dictionaries.
- Practical libraries (CMPH, BBHash) build minimal perfect hash functions for millions of keys in seconds.

---

## 🔬 Deep Dive
### Formal Properties / Proofs
- **Universality proof (Carter-Wegman)**: for distinct keys x, y and random a, b with a ≠ 0, the linear function a·x + b mod p is a bijection on Z_p. The number of (a, b) pairs such that (a·x + b) mod p ≡ (a·y + b) mod p (mod m) is at most p(p−1)/m, giving collision probability ≤ 1/m.
- **FKS space analysis**: let s_i be the number of keys in bucket *i*. The total second-level space is Σ s_i² . By the universality of the first-level hash, E[Σ s_i²] = n + n(n−1)/m. Setting m = n gives E[Σ s_i²] ≤ 2n, so total space is $O(n)$ in expectation.
- **k-wise independence**: a family is k-independent if for any k distinct keys, the joint distribution of their hash values is uniform over $m^{k}$. Higher independence gives stronger concentration bounds (e.g., tabulation hashing is 3-independent and suffices for linear probing).

### Edge Cases and Pitfalls
- **Dynamic key sets**: FKS perfect hashing is static — if keys change, the entire structure must be rebuilt. For dynamic workloads, use universal hashing with chaining.
- **Prime selection**: the Carter-Wegman family requires a prime p > max key value. For large key universes, Mersenne primes (e.g., $2^{61}$ − 1) enable fast modular arithmetic.
- **Overkill for small tables**: the constant factors in FKS and minimal perfect hashing make them slower than simple chaining for tables with fewer than ~1,000 keys.
- **Hash function reuse**: using the same universal hash function across multiple data structures can create correlated failures. Choose independently for each.

### Real-World Usage
- **Language runtimes**: Python (since 3.3), Ruby, and Perl randomise hash seeds at startup using universal-hashing principles to defeat HashDoS attacks.
- **Compiler keyword recognition**: minimal perfect hashing maps language keywords (e.g., "if", "while", "return") to unique indices for $O(1)$ token classification (GNU gperf).
- **Network routing tables**: static forwarding tables use perfect hashing for guaranteed $O(1)$ next-hop lookup.
- **Databases**: static dictionaries (e.g., country codes, HTTP status codes) benefit from perfect hashing in tight loops.
- **Bioinformatics**: minimal perfect hash functions compress k-mer indexes for DNA sequence databases (BBHash).

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why is a deterministic hash function vulnerable to adversarial inputs, but a universal hash function is not?
2. If you have a universal family with m = 100 and two distinct keys x, y, what is the maximum collision probability?
3. True or false: FKS perfect hashing can handle insertions and deletions efficiently.

### Core Problems
1. **Implement Carter-Wegman Hashing**: choose a prime p, implement h_{a,b}(k) = ((a·k + b) mod p) mod m, and empirically verify the collision rate over 10,000 random key pairs matches the 1/m bound.
2. **Two-Level FKS Construction**: given a static set of 1,000 keys, implement the two-level FKS scheme. Measure the total space used (sum of second-level table sizes) and verify it is $O(n)$. Count the number of random trials needed to find collision-free second-level functions.

### Challenge
1. **Minimal Perfect Hashing**: implement a minimal perfect hash function using the CHD algorithm (Belazzougui et al., 2009). Given a static set of 100,000 keys, build the function and measure: (a) build time, (b) bits per key, (c) query time compared to a standard hash table. Discuss when minimal perfect hashing is worth the build cost.

---

*See also:* [[Hash Tables and Hash Functions]] | [[Collision Resolution Strategies]] | [[Cuckoo Hashing]] | [[Randomized Algorithms]] | [[Birthday Paradox]] | **CS Algorithms:** [[Dijkstra's Algorithm]], [[Huffman Coding]]

## Supporting Chunks

- [[CS Data Structures/_chunks/chunk-ds-066 Universal hashing eliminates adversarial worst-case|Universal hashing eliminates adversarial worst-case input]]
- [[CS Data Structures/_chunks/chunk-ds-124 Perfect hashing gives O1 worst-case for static sets|Perfect hashing gives O(1) worst-case lookup for static key sets]]

## References

→ [[CS Data Structures/Sources/Sources Index|Sources Index]]
