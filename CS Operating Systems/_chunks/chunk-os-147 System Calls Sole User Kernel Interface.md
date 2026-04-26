---
id: chunk-csos-147
type: chunk
source: "[[raw-os-025]]"
source_loc: "System Calls and API"
topic: "foundations"
claim: "System calls are the only legal mechanism for user-space processes to request kernel services, enforced by hardware privilege levels that prevent direct access to privileged operations"
confidence: verified
supports:
  - "[[System Calls]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — System calls are the sole user-to-kernel interface

## Context

In user mode, a process cannot access hardware, modify page tables, or execute privileged instructions. When privileged operations are needed (file I/O, process creation, network access), the process issues a system call that triggers a mode switch. On x86-64, the `syscall` instruction is used (faster than the legacy `int 0x80`), with the call number in eax and arguments in registers.

## Why It Matters

System calls are the fundamental abstraction boundary in every OS. Every library, framework, and application ultimately reduces to system calls. Understanding this boundary is essential for performance optimization (minimizing mode switches), security (seccomp filtering), and debugging (strace).

## QnA Seeds

- Q: Why can't user-space processes access hardware directly?
- Q: How does a process invoke a system call on x86-64?
- Q: Why is the syscall instruction faster than int 0x80?
