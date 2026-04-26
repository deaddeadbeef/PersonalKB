---
id: chunk-csos-133
type: chunk
source: "Silberschatz, Galvin, Gagne; Tanenbaum, Bos (2018/2015)"
source_loc: "Memory Allocation: Buddy System"
topic: "memory"
claim: "Linux's physical page allocator uses a buddy system with orders 0–10 (1 to 1024 contiguous pages, 4 KB to 4 MB on x86), maintaining per-zone free lists (DMA, DMA32, Normal, HighMem) to respect hardware addressing constraints"
confidence: verified
supports:
  - "[[Memory Management Overview]]"
  - "[[Virtual Memory and Paging]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — Linux buddy allocator manages per-zone free lists of orders 0 through 10

## Context

The Linux kernel's physical page frame allocator is a buddy system managing contiguous runs of 1 to 1024 pages (orders 0–10, corresponding to 4 KB to 4 MB on x86). Free lists are maintained independently per memory zone — DMA (legacy 16-bit addressable), DMA32 (32-bit addressable), Normal (kernel-addressable), and HighMem (beyond kernel's direct mapping on 32-bit systems) — because different hardware devices have different addressing constraints. The current state of these free lists is exposed via `/proc/buddyinfo`. On top of this allocator, kmalloc() provides general-purpose kernel allocation from slab caches in sizes 8 to 8192 bytes.

## Why It Matters

Understanding the zone-based buddy allocator explains allocation failures that seem puzzling — the system may have free memory overall but lack contiguous pages in a specific zone needed for a DMA transfer. It also explains why /proc/buddyinfo is a key diagnostic tool for memory fragmentation issues on Linux servers.

## QnA Seeds

- Q: What are the buddy allocator orders in Linux and what sizes do they represent?
- Q: Why does Linux maintain separate free lists per memory zone?
- Q: What does /proc/buddyinfo show and when is it useful for diagnosis?
