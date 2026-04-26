---
id: chunk-csos-005
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 1"
topic: "foundations"
claim: "Microkernels move all non-essential OS services (file systems, drivers) to user-space server processes, improving reliability and security at the cost of IPC overhead"
confidence: verified
supports:
  - "[[OS Structure]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — Microkernels move services to user space for reliability at a performance cost

## Context

A microkernel retains only the bare minimum in kernel mode: IPC, basic scheduling, and address-space management. Everything else — file systems, device drivers, network stacks — runs as ordinary user processes. They communicate with each other and with user apps via message passing through the microkernel. If a driver crashes, it can be restarted without rebooting. Examples: MINIX 3, QNX, seL4, early Mach.

## Why It Matters

Microkernel design directly addresses the reliability flaw in monolithic kernels. The argument is particularly compelling for safety-critical systems: seL4 is formally verified. However, crossing the user-kernel boundary on every IPC message adds significant latency, which is why most high-performance OSes are monolithic or hybrid. Tanenbaum's advocacy for microkernels is a central thread through the book.

## QnA Seeds

- Q: What is the minimal set of services that must remain in a microkernel?
- Q: What is the main performance penalty of a microkernel compared to a monolithic kernel?
- Q: Name two production systems that use a microkernel or microkernel-inspired architecture.
