---
tags: [cs-os, chunk]
source: "[[raw-os-009]]"
confidence: high
supports:
  - "[[Memory Management]]"
  - "[[Computer Architecture]]"
qna_seeds:
  - "Q: What happened to segmentation in x86-64? A: In long mode, CS, DS, ES, and SS segment bases are forced to zero and limits ignored, effectively flattening the address space. Only FS and GS retain functional base addresses, used by OSes to point to per-CPU or per-thread data structures (thread-local storage)."
---

# x86-64 Vestigial Segment Registers

Intel x86 processors from the 8086 through the Pentium used segmentation extensively, but x86-64 (AMD64) long mode effectively flattened the segment model. The CS, DS, ES, and SS segment base addresses are forced to zero and limits are ignored, making segmentation vestigial for memory management. Only the FS and GS registers retain functional base addresses, used by operating systems to point to per-CPU data structures (kernel) or per-thread data (user space thread-local storage via TLS). This evolution explains why the term "segmentation fault" persists despite modern systems using paging exclusively.
