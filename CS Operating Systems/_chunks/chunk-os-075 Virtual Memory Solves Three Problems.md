---
tags: [cs-os, chunk]
source: "[[raw-os-007]]"
confidence: high
supports:
  - "[[Virtual Memory]]"
qna_seeds:
  - "Q: What three fundamental problems does virtual memory solve? A: Protection (each process gets an isolated address space), abstraction (decouples programmer's memory view from physical layout), and multiplexing (enables efficient use of limited physical RAM across many processes via demand paging)."
---

# Virtual Memory Solves Three Problems

Virtual memory solves three fundamental problems simultaneously by mapping virtual addresses to physical addresses through page tables managed by the OS and hardware MMU. It provides protection by giving each process an isolated address space. It provides abstraction by decoupling the programmer's view of memory from the physical layout. It provides multiplexing by enabling efficient use of limited physical RAM, allowing programs whose total memory exceeds physical RAM to run via demand paging from disk.
