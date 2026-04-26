---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-009]]"
confidence: high
supports:
  - "[[Hash Tables]]"
  - "[[Universal Hashing]]"
qna_seeds:
  - "Q: What guarantee do universal hash families provide? A: For any pair of distinct keys, collision probability is at most 1/m, eliminating adversarial worst cases without requiring randomness in the data."
---

# Universal Hashing Collision Bound

Universal hashing families guarantee that for any pair of distinct keys, the probability of collision is at most 1/m, eliminating adversarial worst-case inputs without requiring randomness in the data. The Carter-Wegman family h_{a,b}(k) = ((ak + b) mod p) mod m, where p is prime, a ∈ {1,...,p−1}, b ∈ {0,...,p−1}, achieves collision probability exactly ⌈p/m⌉/p ≤ 1/m + 1/p.