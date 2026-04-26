---
id: chunk-csos-101
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 5 — I/O Systems Architecture"
topic: "io"
claim: "I/O scheduling for rotating disks optimizes mechanical seek time using elevator algorithms (SCAN/C-SCAN), while SSDs reduce scheduling importance but still benefit from queue depth management and write amplification reduction"
confidence: verified
supports:
  - "[[Disk Scheduling Algorithms]]"
  - "[[IO Overview]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — I/O scheduling optimizes mechanical seek time with elevator algorithms

## Context

For HDDs, I/O scheduling is essentially a seek-time optimization problem. The elevator algorithm (SCAN) and its variants (C-SCAN, LOOK) service requests in a sweep pattern across the disk, reducing total head movement compared to FCFS ordering. Linux's deadline scheduler maintains separate read/write queues sorted by sector plus FIFO deadline queues (500ms for reads, 5000ms for writes) to prevent starvation. The CFQ scheduler provided per-process fairness until being replaced by mq-deadline and BFQ in newer kernels. With SSDs eliminating seek time, scheduling focus has shifted to managing NVMe queue depth and reducing write amplification.

## Why It Matters

The transition from HDD to SSD scheduling illustrates how hardware changes invalidate software optimizations. Algorithms designed around mechanical constraints become irrelevant when the constraint disappears, but new constraints (flash wear, write amplification, parallelism) create new scheduling needs.

## QnA Seeds

- Q: Why does the deadline I/O scheduler give reads a shorter deadline than writes?
- Q: How did the shift from HDDs to SSDs change I/O scheduling priorities?
- Q: What replaced CFQ as the default Linux I/O scheduler?
