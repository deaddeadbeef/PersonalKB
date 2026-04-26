---
tags: [cs-os, chunk]
source: "[[raw-os-008]]"
confidence: high
supports:
  - "[[Page Replacement]]"
qna_seeds:
  - "Q: What is Belady's optimal algorithm and why can't it be implemented? A: OPT replaces the page that will not be used for the longest time in the future, providing a theoretical lower bound on page faults. It requires future knowledge of the reference string, making it unrealizable — but it serves as the benchmark for evaluating practical algorithms like LRU and Clock."
---

# Beladys Optimal Algorithm as Benchmark

Belady's optimal algorithm (OPT) replaces the page that will not be used for the longest time in the future, providing a theoretical lower bound on the number of page faults for any reference string. It requires complete future knowledge, making it unrealizable in practice. OPT's importance is as a benchmark: by comparing a practical algorithm's fault rate against OPT, system designers can measure how close their approximation comes to theoretical optimality. Stack algorithms including LRU and OPT are immune to Belady's anomaly because their in-memory page sets are monotonically inclusive as frames increase.
