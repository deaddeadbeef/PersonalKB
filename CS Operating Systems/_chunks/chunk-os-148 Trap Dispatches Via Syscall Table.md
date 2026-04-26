---
id: chunk-csos-148
type: chunk
source: "[[raw-os-025]]"
source_loc: "System Calls and API"
topic: "foundations"
claim: "The trap instruction atomically switches from user mode to kernel mode and dispatches through a system call table — an array of function pointers indexed by call number"
confidence: verified
supports:
  - "[[System Calls]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — Trap instruction dispatches via system call table

## Context

The process places the system call number in a register (e.g., eax) and arguments in additional registers. The trap instruction switches to kernel mode and transfers control to the system call handler, which indexes into a system call table (defined in `arch/x86/entry/syscall_64.c` on Linux) to dispatch the appropriate kernel function. After execution, the return value is placed in a register and control returns to user mode.

## Why It Matters

The system call table is the kernel's dispatch mechanism — every kernel entry point is routed through it. Understanding this explains how strace works, how seccomp can filter calls by number, and why adding a new system call requires modifying the table.

## QnA Seeds

- Q: What is the system call table and how is it used for dispatch?
- Q: Where are system call arguments placed on x86-64?
- Q: How does the kernel return a result to user space after a system call?
