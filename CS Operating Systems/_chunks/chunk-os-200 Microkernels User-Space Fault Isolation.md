---
id: chunk-csos-200
type: chunk
source: "[[raw-os-038]]"
source_loc: "Microkernels vs Monolithic Kernels"
topic: "design"
claim: "Microkernels minimize kernel-mode code to address spaces, scheduling, and IPC, running file systems and drivers as restartable user-space servers for strong fault isolation"
confidence: verified
supports:
  - "[[Kernel Architecture]]"
tags:
  - csos
  - csos/design
  - chunk
up: "[[CS Operating Systems]]"
---
# Design — Microkernels isolate services as user-space servers

## Context

Microkernels keep only essential primitives (address space management, thread scheduling, IPC) in kernel mode. File systems, drivers, and network protocols run as user-space server processes communicating via message passing. A crashing driver can be restarted without taking down the kernel. QNX achieves driver restart in ~100 ms, suitable for automotive ASIL-D and medical IEC 62304 certifications.

## Why It Matters

Microkernel fault isolation is critical for safety-critical systems where a driver crash cannot be allowed to bring down the entire system. QNX commercial success in automotive and medical demonstrates that this architecture has real-world value beyond academic interest.

## QnA Seeds

- Q: What code runs in kernel mode in a microkernel?
- Q: How does a microkernel handle a crashing device driver?
- Q: Why is QNX used in safety-critical systems like automotive and medical?
