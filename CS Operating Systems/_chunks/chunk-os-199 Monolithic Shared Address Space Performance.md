---
id: chunk-csos-199
type: chunk
source: "[[raw-os-038]]"
source_loc: "Microkernels vs Monolithic Kernels"
topic: "design"
claim: "Monolithic kernels run all OS services in a single shared address space, achieving maximum inter-subsystem performance via direct function calls at the cost of fault isolation"
confidence: verified
supports:
  - "[[Kernel Architecture]]"
tags:
  - csos
  - csos/design
  - chunk
up: "[[CS Operating Systems]]"
---
# Design — Monolithic kernels maximize performance via shared space

## Context

A monolithic kernel (Linux is the canonical example) runs scheduler, memory manager, file systems, drivers, and networking in one kernel address space. All subsystems call each other directly via function calls with zero IPC overhead. However, a bug in any component (especially the 60%+ of code that is drivers) can crash the entire system. Linux 6.x exceeds 30 million lines of code in kernel mode.

## Why It Matters

The monolithic architecture explains Linux's performance advantage for kernel-intensive workloads and why driver bugs are the number one source of kernel crashes. Understanding this tradeoff is essential for evaluating when fault isolation (microkernel) matters more than raw performance.

## QnA Seeds

- Q: What performance advantage do monolithic kernels have over microkernels?
- Q: Why are driver bugs the most common source of monolithic kernel crashes?
- Q: How large is the Linux kernel codebase running in kernel mode?
