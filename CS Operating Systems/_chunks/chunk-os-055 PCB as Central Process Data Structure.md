---
tags: [cs-os, chunk]
source: "[[raw-os-002]]"
confidence: high
supports:
  - "[[Process Management]]"
qna_seeds:
  - "Q: What information does a process control block (PCB) contain? A: The PCB stores the process ID, process state, program counter, CPU registers, memory management info (page tables, segment tables), I/O status, and accounting information — everything needed to restart a suspended process."
---

# PCB as Central Process Data Structure

The process control block (PCB) is the single most important data structure in an operating system. It contains all state needed to suspend and later restart a process: process ID, current state, program counter, saved CPU registers, memory management information (page tables, segment tables), I/O status, and accounting data. Every context switch reads from and writes to the PCB, making it the nexus of process management.
