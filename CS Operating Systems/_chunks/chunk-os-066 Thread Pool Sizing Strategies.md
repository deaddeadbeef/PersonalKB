---
tags: [cs-os, chunk]
source: "[[raw-os-004]]"
confidence: high
supports:
  - "[[Threads and Concurrency]]"
  - "[[Performance Tuning]]"
qna_seeds:
  - "Q: How should thread pools be sized for compute-bound vs I/O-bound workloads? A: For compute-bound work, size to the number of CPU cores. For I/O-bound work, use a larger multiple (2×–10× cores) since threads spend most time blocked. Default thread stack size (1–8 MB on Linux) limits practical thread count per process."
---

# Thread Pool Sizing Strategies

Thread pools amortize thread creation cost by pre-allocating worker threads that process tasks from a shared queue, avoiding both per-request creation overhead and resource exhaustion from unbounded spawning. For compute-bound work, the optimal pool size matches the number of CPU cores. For I/O-bound work where threads spend most time blocked, a larger multiple (2×–10× cores) is appropriate. The typical thread stack size of 1–8 MB (default 8 MB on Linux) limits practical thread count, motivating event-driven architectures and coroutines for high-concurrency scenarios.
