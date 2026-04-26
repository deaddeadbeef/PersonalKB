---
id: chunk-csos-173
type: chunk
source: "[[raw-os-031]]"
source_loc: "Memory-Mapped Files"
topic: "memory"
claim: "mmap eliminates one data copy compared to read() by allowing direct access to the kernel page cache, and simplifies random access to pointer arithmetic"
confidence: verified
supports:
  - "[[Memory-Mapped IO]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — mmap eliminates copy and simplifies random access

## Context

With read(), data is copied from the page cache to a user-space buffer — a copy mmap avoids by letting the process access page cache pages directly. Random access becomes pointer addition instead of lseek+read. Two processes mapping the same file with MAP_SHARED share the same physical page frames, providing efficient inter-process shared memory.

## Why It Matters

The copy elimination is why mmap outperforms read/write for random-access workloads. The shared physical pages explain how inter-process shared memory works without explicit IPC mechanisms, which is widely used in database and multimedia applications.

## QnA Seeds

- Q: What data copy does mmap eliminate compared to read()?
- Q: How does mmap simplify random file access patterns?
- Q: How does MAP_SHARED enable efficient shared memory between processes?
