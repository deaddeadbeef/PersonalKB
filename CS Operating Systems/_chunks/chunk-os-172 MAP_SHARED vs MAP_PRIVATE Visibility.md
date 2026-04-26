---
id: chunk-csos-172
type: chunk
source: "[[raw-os-031]]"
source_loc: "Memory-Mapped Files"
topic: "memory"
claim: "MAP_SHARED makes writes visible to other processes and propagates them to the file, while MAP_PRIVATE creates copy-on-write mappings where writes are process-local"
confidence: verified
supports:
  - "[[Memory-Mapped IO]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — MAP_SHARED vs MAP_PRIVATE control write visibility

## Context

MAP_SHARED creates a mapping where writes are visible to all processes mapping the same file and are eventually written to disk. MAP_PRIVATE uses copy-on-write: writes create private page copies never written back, useful for shared library data segments. MAP_ANONYMOUS (fd=-1) creates zero-filled mappings not backed by a file, commonly used by malloc() for allocations above the mmap_threshold (default 128 KB).

## Why It Matters

The SHARED/PRIVATE distinction is fundamental: shared mappings enable inter-process communication while private mappings enable safe per-process modifications of shared data. Understanding MAP_ANONYMOUS explains how malloc() works for large allocations.

## QnA Seeds

- Q: What happens when a process writes to a MAP_SHARED mapping?
- Q: How does MAP_PRIVATE use copy-on-write for process isolation?
- Q: What is MAP_ANONYMOUS used for and how does malloc() use it?
