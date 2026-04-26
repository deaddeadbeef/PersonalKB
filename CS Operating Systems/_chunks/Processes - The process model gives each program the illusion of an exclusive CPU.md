---
id: chunk-csos-006
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 2"
topic: "processes"
claim: "The process model gives each program the illusion of a dedicated CPU and private address space, while the OS multiplexes the real hardware transparently"
confidence: verified
supports:
  - "[[Process Model]]"
tags:
  - csos
  - csos/processes
  - chunk
up: "[[CS Operating Systems]]"
---
# Processes — The process model gives each program the illusion of an exclusive CPU

## Context

Before multiprogramming, a program ran alone on the machine. The process model preserves this illusion in a shared system: each process has its own virtual CPU (the OS saves and restores register state on context switch) and its own virtual address space (MMU enforces isolation). The process cannot tell whether 3 or 300 other processes are running — the OS's scheduler and MMU hide that fact.

## Why It Matters

The process abstraction is foundational to all modern OS design. It decouples program logic from scheduling decisions, enables isolation between applications, and allows the OS to enforce resource limits independently for each program. Everything from shell pipelines to web server worker pools rests on this abstraction.

## QnA Seeds

- Q: What two illusions does the process model provide to each program?
- Q: What OS data structure tracks the state needed to resume a process?
- Q: What happens to CPU registers when a context switch occurs?
