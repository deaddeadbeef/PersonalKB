---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "CPU Scheduling Algorithms"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# CPU Scheduling Algorithms

## Summary
CPU scheduling determines which process in the ready queue receives the processor next, directly impacting system throughput, response time, and fairness. Classical algorithms like FCFS and SJF establish theoretical baselines—SJF is provably optimal for minimizing average waiting time but requires future knowledge. Modern production schedulers like Linux's Completely Fair Scheduler (CFS) use sophisticated approaches that balance fairness, responsiveness, and throughput without requiring burst-time predictions.

## Key Claims
- Shortest Job First (SJF) is mathematically optimal for minimizing average waiting time, but it is impractical because future CPU burst lengths are unknown and must be estimated
- Round Robin scheduling degrades to FCFS when the time quantum is too large, and causes excessive context-switch overhead when the quantum is too small—a quantum of 10–100ms is typical
- Priority scheduling without aging leads to indefinite starvation of low-priority processes; aging (gradually increasing priority over time) is the standard remedy
- Multilevel Feedback Queue (MLFQ) adapts to process behavior dynamically, approximating SJF without requiring advance knowledge of burst lengths
- Linux CFS models fairness as equal CPU time allocation using a red-black tree keyed on virtual runtime (vruntime), achieving O(log n) scheduling decisions

## Atomic Facts
1. FCFS (First-Come, First-Served) is non-preemptive and suffers from the convoy effect, where short processes queue behind a single long-running process, dramatically inflating average wait times
2. SJF can be either non-preemptive or preemptive (Shortest Remaining Time First / SRTF); the preemptive variant is optimal among all preemptive algorithms for average waiting time
3. In Round Robin, the time quantum must be significantly larger than the context-switch time; a rule of thumb is that 80% of CPU bursts should complete within one quantum
4. MLFQ typically uses 3–8 priority levels, with higher-priority queues using shorter time quanta; processes that exhaust their quantum are demoted, while processes that block before their quantum expires are promoted
5. Linux CFS assigns each runnable process a vruntime that advances proportionally to wall-clock time divided by the process's weight (derived from its nice value); the process with the smallest vruntime is always selected next
6. CFS replaced the O(1) scheduler in Linux 2.6.23 (2007); the O(1) scheduler had excellent algorithmic complexity but exhibited poor interactive responsiveness and unfair behavior under certain workloads

## Significance
Scheduling algorithms represent one of the purest examples of systems tradeoffs in computer science—no single algorithm optimizes all metrics simultaneously. Understanding these tradeoffs explains why general-purpose OSes use adaptive heuristic schedulers rather than theoretically optimal ones, and why specialized domains (real-time, HPC, embedded) require entirely different scheduling philosophies.

## Chunks Extracted
*Pending*
