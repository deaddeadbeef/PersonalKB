---
tags: [cs-os, chunk]
source: "[[raw-os-008]]"
confidence: high
supports:
  - "[[Page Replacement]]"
  - "[[Virtual Memory]]"
qna_seeds:
  - "Q: What causes thrashing and how is it resolved? A: Thrashing occurs when the combined working sets of all active processes exceed physical memory, causing the system to spend more time paging than executing. The solution is reducing the degree of multiprogramming — suspending processes until working sets fit in available RAM."
---

# Thrashing from Working Set Overflow

Thrashing occurs when the total working set of all active processes exceeds physical memory, causing the system to spend more time servicing page faults (disk I/O) than executing useful instructions. The page fault rate spikes, CPU utilization drops, and the OS may respond by admitting more processes (worsening the problem). The solution is to reduce the degree of multiprogramming by suspending processes until the remaining processes' working sets fit in physical memory. The dirty bit affects eviction cost: clean pages can be discarded immediately, while dirty pages require an expensive disk write before eviction.
