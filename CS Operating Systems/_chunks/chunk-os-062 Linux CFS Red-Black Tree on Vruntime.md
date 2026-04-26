---
tags: [cs-os, chunk]
source: "[[raw-os-003]]"
confidence: high
supports:
  - "[[CPU Scheduling]]"
  - "[[Linux Internals]]"
qna_seeds:
  - "Q: How does Linux CFS achieve fair scheduling? A: CFS tracks each process's virtual runtime (vruntime), which advances proportionally to wall-clock time divided by the process's weight (from nice value). Processes are stored in a red-black tree keyed on vruntime; the leftmost node (smallest vruntime) is always selected next, achieving O(log n) decisions."
---

# Linux CFS Red-Black Tree on Vruntime

Linux's Completely Fair Scheduler (CFS), introduced in kernel 2.6.23 (2007), models fairness as equal CPU time allocation. Each runnable process has a virtual runtime (vruntime) that advances proportionally to wall-clock time divided by the process's weight (derived from its nice value). Processes are stored in a red-black tree keyed on vruntime; the scheduler always picks the process with the smallest vruntime (leftmost node), achieving O(log n) scheduling decisions. CFS replaced the O(1) scheduler, which had poor interactive responsiveness despite its superior algorithmic complexity.
