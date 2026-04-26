---
id: chunk-csos-048
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 10"
topic: "casestudies"
claim: "Linux is a monolithic kernel with loadable modules — a pragmatic compromise that achieves near-microkernel extensibility (load/unload drivers at runtime) while retaining monolithic performance"
confidence: verified
supports:
  - "[[Linux Architecture Overview]]"
  - "[[OS Structure]]"
tags:
  - csos
  - csos/casestudies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — Linux uses a monolithic kernel with loadable modules as a performance-reliability compromise

## Context

Linux is definitively monolithic: all kernel subsystems compile into one binary, share one address space, and call each other directly. But unlike early monolithic kernels, Linux supports loadable kernel modules (`.ko`) — drivers and file systems compiled separately that can be inserted and removed at runtime without rebooting. This gives operators the extensibility of a microkernel (swap out drivers on a running system) without the IPC overhead (the loaded module runs at kernel privilege with direct function calls).

## Why It Matters

The module system is why Linux can support thousands of device drivers across wildly different hardware without requiring users to compile a new kernel for each configuration. It also explains the central reliability risk: a badly written third-party kernel module (e.g., a proprietary printer driver) can crash a production server. This was the backdrop to the famous Torvalds-Tanenbaum debate and the argument for kernel hardening features like lockdown mode.

## QnA Seeds

- Q: What is a Linux kernel module and how does it differ from a user-space plugin?
- Q: Why is the module system not equivalent to a microkernel in terms of fault isolation?
- Q: How do you list currently loaded kernel modules?
