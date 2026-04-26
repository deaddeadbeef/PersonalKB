---
tags: [cs-os, chunk]
source: "[[raw-os-003]]"
confidence: high
supports:
  - "[[CPU Scheduling]]"
qna_seeds:
  - "Q: How does time quantum size affect Round Robin scheduling? A: Too large degrades to FCFS (no fairness); too small causes excessive context-switch overhead. A typical quantum is 10–100 ms, sized so 80% of CPU bursts complete within one quantum."
---

# Round Robin Quantum Tradeoff

Round Robin scheduling assigns each process a fixed time quantum and cycles through the ready queue. When the quantum is too large, Round Robin degrades to FCFS behavior; when too small, context-switch overhead dominates useful work. A typical quantum is 10–100 milliseconds. The practical rule of thumb is that the quantum should be large enough that 80% of CPU bursts complete within a single quantum, balancing responsiveness for interactive processes against switching overhead.
