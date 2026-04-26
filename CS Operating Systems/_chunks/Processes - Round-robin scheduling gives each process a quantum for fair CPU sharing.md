---
id: chunk-csos-010
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2"
topic: "processes"
claim: "Round-robin scheduling assigns each process a fixed time quantum and preempts it at expiry, placing it at the back of the ready queue — giving all runnable processes equal CPU shares"
confidence: verified
supports:
  - "[[CPU Scheduling]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — Round-robin scheduling gives each process a quantum for fair CPU sharing

## Context

Round-robin (RR) is the simplest fair scheduling algorithm. The ready queue is a FIFO; the running process gets a quantum (typically 10–100 ms). At quantum expiry it is preempted and appended to the queue. The next process at the head of the queue gets the CPU. Response time is bounded: with n runnable processes and quantum q, the worst-case response time is (n−1)×q.

## Why It Matters

RR is the baseline for interactive system fairness. The quantum length is a key design parameter: too short (1 ms) and context-switching overhead dominates; too long (1 s) and the system feels unresponsive. Linux CFS replaces fixed quanta with virtual runtime tracking but achieves the same fairness goal. Understanding RR is essential for understanding why MLFQ and CFS are improvements over it.

## QnA Seeds

- Q: In round-robin scheduling with 4 processes and a 20 ms quantum, what is the worst-case response time?
- Q: What is the trade-off in choosing a shorter vs longer time quantum?
- Q: How does round-robin differ from FCFS?
