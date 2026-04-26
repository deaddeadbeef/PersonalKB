---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-009]]"
confidence: high
supports:
  - "[[Hash Tables]]"
  - "[[Cuckoo Hashing]]"
qna_seeds:
  - "Q: What are cuckoo hashing's time guarantees? A: O(1) worst-case lookup and O(1) amortized expected insertion using two hash functions; insertion fails requiring rehash with probability O(1/n)."
---

# Cuckoo Hashing O(1) Lookup and Insert

Cuckoo hashing provides O(1) worst-case lookup and O(1) amortized expected insertion using two hash functions and two tables. When inserting a key that collides, the existing key is displaced to its alternate table position, potentially triggering a chain of displacements. Insertion fails (requiring a full rehash with new hash functions) with probability O(1/n), keeping the amortized cost constant.