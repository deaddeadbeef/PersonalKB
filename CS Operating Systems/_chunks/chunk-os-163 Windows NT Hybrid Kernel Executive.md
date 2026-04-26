---
id: chunk-csos-163
type: chunk
source: "[[raw-os-029]]"
source_loc: "Windows NT Kernel Architecture"
topic: "case-studies"
claim: "Windows NT uses a hybrid architecture: a microkernel handles scheduling and interrupts while the executive runs higher-level services in kernel mode for performance"
confidence: verified
supports:
  - "[[Windows NT Architecture]]"
tags:
  - csos
  - csos/case-studies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — Windows NT hybrid kernel with executive layer

## Context

Designed by Dave Cutler (first released 1993), NT's microkernel handles thread scheduling (32 priority levels: 0-15 dynamic, 16-31 real-time), interrupt dispatching via IRQL, and synchronization. The executive layer provides Object Manager, I/O Manager, Memory Manager, Process Manager, Security Reference Monitor, and Configuration Manager (registry) — all running in kernel mode rather than as user-space servers.

## Why It Matters

NT's hybrid design is the architectural foundation of all Windows versions from 2000 through 11. Understanding the kernel/executive split explains why Windows has different performance and security characteristics than pure microkernels or monolithic kernels.

## QnA Seeds

- Q: Why is Windows NT called a hybrid kernel rather than a true microkernel?
- Q: What components make up the NT executive layer?
- Q: How many priority levels does the Windows scheduler support?
