---
tags: [cs-os, chunk]
source: "[[raw-os-003]]"
confidence: high
supports:
  - "[[CPU Scheduling]]"
qna_seeds:
  - "Q: Why is Shortest Job First optimal yet impractical? A: SJF is mathematically optimal for minimizing average waiting time, but it requires knowing future CPU burst lengths, which are unknown. The preemptive variant (SRTF) is optimal among all preemptive algorithms."
---

# SJF Optimality and Impracticality

Shortest Job First (SJF) is mathematically proven optimal for minimizing average waiting time among non-preemptive algorithms. Its preemptive variant, Shortest Remaining Time First (SRTF), is optimal among all preemptive algorithms for the same metric. However, SJF is impractical in production because future CPU burst lengths are unknown and must be estimated — typically via exponential averaging of past burst durations. This gap between theoretical optimality and practical realizability motivates the design of adaptive heuristic schedulers.
