---
id: chunk-csos-116
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 7 — Virtualization Fundamentals"
topic: "virtualization"
claim: "Trap-and-emulate virtualization runs the guest OS in user mode so that privileged instructions trap to the hypervisor, which emulates the instruction's effect on the virtual machine's state and returns control to the guest"
confidence: verified
supports:
  - "[[Virtualization Fundamentals]]"
  - "[[Hypervisors]]"
tags:
  - csos
  - csos/virtualization
  - chunk
up: "[[CS Operating Systems]]"
---
# Virtualization — Trap-and-emulate runs guest in user mode intercepting privileged ops

## Context

The trap-and-emulate technique is the foundational virtualization mechanism. The guest OS, believing it runs in kernel mode, is actually running in user mode. When it executes a privileged instruction (e.g., modifying page tables, accessing I/O ports), the CPU traps to the hypervisor. The hypervisor inspects the faulting instruction, emulates its intended effect on the virtual machine's state (virtual page tables, virtual device registers), and returns control to the guest. Most guest instructions (arithmetic, memory access, branches) execute at full native speed because they don't require hypervisor intervention.

## Why It Matters

Trap-and-emulate is why virtualization can achieve near-native performance — only the small fraction of instructions that are privileged incur overhead. This also explains the performance spectrum: workloads with heavy system call rates (I/O-intensive) show more virtualization overhead than compute-bound workloads.

## QnA Seeds

- Q: Why do most guest instructions run at native speed under trap-and-emulate?
- Q: What happens when the guest executes a privileged instruction?
- Q: Which types of workloads show the most virtualization overhead and why?
