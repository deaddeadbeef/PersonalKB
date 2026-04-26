---
id: chunk-csos-016
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 3"
topic: "memory"
claim: "Address spaces decouple the logical addresses a program uses from the physical RAM addresses, enabling process isolation and relocation without program modification"
confidence: verified
supports:
  - "[[Address Spaces]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — Address spaces decouple logical and physical memory for protection and flexibility

## Context

Without address spaces, programs use absolute physical addresses and can overwrite each other. With an MMU, every process has its own logical address space starting at 0. The hardware maps each logical access to a physical address, and traps on out-of-bounds accesses. The simplest form is base+limit registers: physical address = logical address + base, validated against limit. Modern systems use paging for finer-grained control.

## Why It Matters

Address space isolation is the foundation of OS security and stability. It is why a buggy web browser cannot corrupt the kernel or another process's memory. It enables features like fork (copy the address space mapping), memory-mapped files (map file pages into the address space on demand), and ASLR (randomise the base addresses of stack, heap, and shared libraries to defeat memory-corruption exploits).

## QnA Seeds

- Q: What is the difference between a logical address and a physical address?
- Q: How does base-and-limit register protection work?
- Q: What happens when a process accesses a logical address outside its valid range?
