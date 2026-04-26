---
id: chunk-csos-004
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 1"
topic: "foundations"
claim: "Monolithic kernels run all OS services in a single kernel address space; this maximises performance through direct function calls but means any driver bug can crash the whole system"
confidence: verified
supports:
  - "[[OS Structure]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — Monolithic kernels colocate all OS services for performance

## Context

In a monolithic kernel (Linux, traditional BSD), the scheduler, memory manager, file systems, device drivers, and network stack all compile into one binary running in a single privileged address space. Calls between subsystems are direct function calls — no IPC overhead, no context switches. This is why Linux device drivers can call memory allocation functions directly.

## Why It Matters

The monolithic design delivers the best achievable throughput — essential for high-performance I/O, database servers, and real-time workloads. The trade-off is fault isolation: a null-pointer dereference in a third-party GPU driver panics the entire kernel. This is the primary argument Tanenbaum used in his famous 1992 debate with Torvalds about whether Linux's design was defensible.

## QnA Seeds

- Q: What is a monolithic kernel and what are its performance implications?
- Q: Why can a device driver bug crash the entire OS in a monolithic kernel?
- Q: How do Linux kernel modules reconcile extensibility with the monolithic model?
