---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-009]]"
confidence: high
supports:
  - "[[Hash Tables]]"
  - "[[Perfect Hashing]]"
qna_seeds:
  - "Q: How does perfect hashing achieve O(1) worst-case lookup? A: A two-level scheme with O(n) total space uses m_j = n_j² slots at the second level for n_j keys mapping to slot j, guaranteeing zero collisions."
---

# Perfect Hashing O(1) Worst-Case Lookup

Perfect hashing achieves O(1) worst-case lookup for static key sets using a two-level scheme with O(n) total space. The first level hashes n keys into m = n buckets, then each bucket j with n_j keys uses a second-level table of m_j = n_j² slots, guaranteeing zero collisions at the second level. The quadratic sizing ensures that the total space across all second-level tables is O(n) in expectation.