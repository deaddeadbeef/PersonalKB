---
tags: [cs-os, chunk]
source: "[[raw-os-009]]"
confidence: high
supports:
  - "[[Memory Management]]"
  - "[[Segmentation]]"
qna_seeds:
  - "Q: How does segmentation differ from paging in address structure? A: Segmentation uses a two-dimensional (segment number, offset) address, matching the programmer's logical view (code, data, stack, heap as separate segments). Each segment table entry holds a base address and limit; the hardware checks the offset against the limit on every access, triggering SIGSEGV on violation."
---

# Segmentation Two-Dimensional Address Space

Segmentation divides a process's address space into variable-sized logical units corresponding to meaningful program structures — code, data, stack, heap — each identified by a (segment number, offset) pair. Each segment table entry stores the segment's base physical address and its limit (length). On every memory reference, hardware adds the offset to the base and verifies the offset is less than the limit; a violation triggers a segmentation fault (SIGSEGV on Unix). This two-dimensional addressing matches the programmer's logical view more naturally than a flat paged address space.
