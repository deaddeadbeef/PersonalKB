---
id: chunk-csos-003
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 1"
topic: "foundations"
claim: "System calls are the controlled interface through which user programs request kernel services, implemented via a software interrupt or trap instruction that switches CPU privilege level"
confidence: verified
supports:
  - "[[System Calls]]"
  - "[[OS Fundamentals]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — System calls are the controlled interface from user space to the kernel

## Context

User programs cannot call kernel functions directly — those functions run in kernel mode at addresses the user has no right to jump to. Instead, the OS defines a set of numbered entry points (system calls). The user program places the system call number and arguments in designated registers, then executes a trap instruction (`syscall` on x86-64). The CPU switches to kernel mode, validates the request, performs the service, switches back to user mode, and returns the result.

## Why It Matters

System calls are the only channel through which user code can affect the OS's internal state. Everything that a program does — reading a file, creating a process, allocating memory beyond the current stack — goes through this bottleneck. The kernel can validate every request at this choke point, enforcing security, resource limits, and correct usage.

## QnA Seeds

- Q: What instruction does a program execute to invoke a system call on x86-64?
- Q: Why can't a user program directly call kernel functions?
- Q: Is `printf` a system call? Explain.
