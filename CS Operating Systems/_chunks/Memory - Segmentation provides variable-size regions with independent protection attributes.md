---
id: chunk-csos-021
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 3"
topic: "memory"
claim: "Segmentation divides a program's address space into variable-size logical regions (code, stack, data) each with independent base, limit, and protection, matching the compiler's view of a program"
confidence: verified
supports:
  - "[[Segmentation]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — Segmentation provides variable-size regions with independent protection attributes

## Context

Where paging imposes a uniform fixed-size grid, segmentation reflects the logical structure of a program. The code segment is read+execute only; the data segment is read+write; a shared library segment is shared with other processes but individually mapped. Each segment has its own base and limit in physical memory, and can grow or shrink independently. The x86 real-mode (and early protected-mode) design used segmentation heavily; modern x86-64 retains the segment registers but effectively sets them all to base 0, relying on paging for isolation.

## Why It Matters

Segmentation illustrates the power of matching the protection model to the logical structure of programs. It explains why MULTICS combined segmentation and paging — one for logical structure, one for physical allocation. Understanding segmentation is necessary to understand the evolution toward pure paging (simpler, less fragmentation) and to understand legacy x86 platform code.

## QnA Seeds

- Q: What is the difference between segmentation and paging?
- Q: What is external fragmentation and why does segmentation suffer from it?
- Q: How does combining segmentation with paging address the weaknesses of each?
