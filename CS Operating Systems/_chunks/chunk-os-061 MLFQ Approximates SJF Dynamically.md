---
tags: [cs-os, chunk]
source: "[[raw-os-003]]"
confidence: high
supports:
  - "[[CPU Scheduling]]"
qna_seeds:
  - "Q: How does MLFQ approximate SJF without advance knowledge? A: MLFQ uses 3–8 priority levels with shorter quanta at higher levels. Processes that exhaust their quantum are demoted (likely CPU-bound); those that block early are promoted (likely I/O-bound), dynamically sorting by burst length."
---

# MLFQ Approximates SJF Dynamically

Multilevel Feedback Queue (MLFQ) scheduling adapts to process behavior without requiring advance knowledge of burst lengths, effectively approximating SJF. It typically uses 3–8 priority levels, with higher-priority queues assigned shorter time quanta. Processes that exhaust their full quantum are demoted to a lower-priority queue (indicating CPU-bound behavior), while processes that block before their quantum expires are promoted (indicating I/O-bound behavior). This feedback mechanism dynamically classifies processes by their CPU burst characteristics.
