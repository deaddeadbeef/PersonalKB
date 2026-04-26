---
tags: [cs-os, chunk]
source: "[[raw-os-007]]"
confidence: high
supports:
  - "[[Virtual Memory]]"
  - "[[Performance Tuning]]"
qna_seeds:
  - "Q: Why is the TLB the most performance-critical cache in the memory hierarchy? A: A TLB hit adds 0–1 cycles to memory access, while a TLB miss triggers a page table walk costing 10–100 cycles. TLBs typically hold 64–1024 entries with >99% hit rate. Huge pages (2 MB/1 GB) reduce TLB pressure by covering more address space per entry."
---

# TLB as Critical Translation Cache

The Translation Lookaside Buffer (TLB) is the most performance-critical cache in the memory hierarchy. A TLB hit adds zero to one cycle to memory access latency, while a miss triggers a multi-level page table walk costing 10–100 cycles. TLBs typically hold 64–1024 entries and achieve hit rates above 99% for most workloads. On x86, TLB misses are handled by a hardware page table walker; some RISC architectures (MIPS, older SPARC) handle them in software. Huge pages (2 MB or 1 GB on x86-64) reduce TLB pressure by covering more address space per entry.
