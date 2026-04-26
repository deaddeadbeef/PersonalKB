---
tags: [cs-os, chunk]
source: "[[raw-os-005]]"
confidence: high
supports:
  - "[[Process Synchronization]]"
  - "[[Computer Architecture]]"
qna_seeds:
  - "Q: Why does Peterson's algorithm fail on modern hardware without memory barriers? A: Modern CPUs reorder instructions for performance. x86 has relatively strong total store order, but ARM and RISC-V have weaker memory models where stores and loads can be reordered, breaking the assumption that flag and turn writes are immediately visible to other cores."
---

# Memory Ordering Breaks Software Synchronization

Peterson's algorithm — the simplest correct two-process software-only critical section solution using a turn variable and flag array — fails on modern hardware without explicit memory barriers due to instruction reordering by the CPU. x86 processors provide relatively strong total store order, but ARM and RISC-V have weaker memory models requiring explicit fence instructions to prevent reordering. This gap between the sequential consistency assumed by theoretical algorithms and the relaxed ordering of real hardware is why all practical synchronization primitives rely on hardware atomic instructions rather than pure software protocols.
