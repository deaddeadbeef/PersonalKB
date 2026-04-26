---
tags: [cs-algorithms, chunk]
source: "[[raw-algo-007]]"
confidence: high
supports:
  - "[[Mergesort]]"
  - "[[Master Theorem]]"
  - "[[Recurrence Relations]]"
qna_seeds:
  - "Q: Which Master Theorem case applies to mergesort? A: Case 2, with T(n) = 2T(n/2) + Θ(n) resolving to Θ(n log n), where a = 2, b = 2, and f(n) = Θ(n^{log_b a})."
---

# Master Theorem Mergesort Recurrence

Mergesort's recurrence T(n) = 2T(n/2) + Θ(n) resolves to T(n) = Θ(n log n) by Case 2 of the Master Theorem, where a = 2, b = 2, and f(n) = Θ(n) = Θ(n^{log_b a}). Bottom-up mergesort performs exactly ⌈log₂ n⌉ passes over the data, each requiring O(n) work, confirming the same O(n log n) total as top-down mergesort.