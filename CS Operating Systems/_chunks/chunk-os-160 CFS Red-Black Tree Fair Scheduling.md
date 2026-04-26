---
id: chunk-csos-160
type: chunk
source: "[[raw-os-028]]"
source_loc: "Linux Kernel Architecture"
topic: "case-studies"
claim: "CFS tracks per-task virtual runtime in a red-black tree and always schedules the task with the smallest vruntime, achieving proportional fair CPU allocation"
confidence: verified
supports:
  - "[[Linux Kernel]]"
tags:
  - csos
  - csos/case-studies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — CFS uses red-black tree for fair scheduling

## Context

The Completely Fair Scheduler (CFS) assigns each task a virtual runtime (vruntime) that advances inversely proportional to its weight (derived from nice value). The task with the smallest vruntime is always selected next from a red-black tree. Real-time tasks use SCHED_FIFO or SCHED_RR with static priorities above the CFS range. CFS replaced the earlier O(1) scheduler with a more mathematically fair approach.

## Why It Matters

CFS is the default scheduler for all non-realtime Linux processes. Understanding vruntime and the red-black tree structure explains scheduling behavior, why nice values affect CPU allocation proportionally, and how to reason about fairness in multi-process workloads.

## QnA Seeds

- Q: How does CFS determine which task to schedule next?
- Q: What is vruntime and how does it relate to nice values?
- Q: Why did CFS replace the O(1) scheduler?
