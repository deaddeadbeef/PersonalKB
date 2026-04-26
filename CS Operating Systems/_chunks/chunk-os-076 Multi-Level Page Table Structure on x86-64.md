---
tags: [cs-os, chunk]
source: "[[raw-os-007]]"
confidence: high
supports:
  - "[[Virtual Memory]]"
  - "[[Computer Architecture]]"
qna_seeds:
  - "Q: Why do 64-bit systems use multi-level page tables? A: A single-level page table for a 64-bit address space would be impractically large. x86-64 uses four levels (PML4→PDPT→PD→PT) with 9 bits per level plus a 12-bit offset, mapping 48-bit virtual addresses. Linux 5.x added optional five-level paging (PML5) extending to 57-bit virtual addresses."
---

# Multi-Level Page Table Structure on x86-64

A single-level page table for a 64-bit address space would require an impractically large contiguous structure, so modern architectures use multi-level page tables. x86-64 uses a four-level hierarchy — PML4→PDPT→PD→PT — with 9 bits indexing each level and a 12-bit page offset, mapping 48-bit virtual addresses to physical frames. Each page table entry (PTE) stores the physical frame number plus control bits: present/absent, read/write, user/supervisor, dirty, accessed, and no-execute (NX). Linux 5.x added optional five-level paging (PML5) extending support to 57-bit virtual addresses.
