---
id: chunk-csos-159
type: chunk
source: "[[raw-os-028]]"
source_loc: "Linux Kernel Architecture"
topic: "case-studies"
claim: "Linux is a monolithic kernel where all core services share one address space, but loadable kernel modules enable runtime extensibility without reboot via insmod/modprobe"
confidence: verified
supports:
  - "[[Linux Kernel]]"
tags:
  - csos
  - csos/case-studies
  - chunk
up: "[[CS Operating Systems]]"
---
# Case Studies — Linux monolithic kernel with loadable modules

## Context

All core OS services — scheduling, memory management, file systems, networking, drivers — run in a single kernel address space, eliminating IPC overhead. Loadable kernel modules (LKMs) use module_init()/module_exit() macros and can be inserted at runtime with full kernel privileges. Device drivers comprise over 60% of kernel source (30M+ lines in 6.x), making driver quality the dominant reliability factor.

## Why It Matters

Linux's monolithic-with-modules architecture is a pragmatic compromise: monolithic performance with modular extensibility. This design decision is why Linux scales from smartphones to supercomputers and why driver bugs are the most common source of kernel crashes.

## QnA Seeds

- Q: Why is Linux considered monolithic despite supporting loadable modules?
- Q: What percentage of the Linux kernel source is device drivers?
- Q: How do loadable modules achieve extensibility without microkernel IPC overhead?
