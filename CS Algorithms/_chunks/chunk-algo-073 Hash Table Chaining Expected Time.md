---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-009]]"
confidence: high
supports:
  - "[[Hash Tables]]"
  - "[[Collision Resolution]]"
qna_seeds:
  - "Q: What is the expected search time in a chained hash table? A: Under simple uniform hashing, successful search is Θ(1 + α/2) and unsuccessful search is Θ(1 + α), where α = n/m is the load factor."
---

# Hash Table Chaining Expected Time

Under the simple uniform hashing assumption with chaining, the expected time for a successful search is Θ(1 + α/2) and for an unsuccessful search is Θ(1 + α), where α = n/m is the load factor (items divided by slots). When the load factor exceeds a threshold (typically 0.75), resizing doubles the table to 2m slots and rehashes all elements in O(n) time; amortized over n insertions, this adds only O(1) per operation.