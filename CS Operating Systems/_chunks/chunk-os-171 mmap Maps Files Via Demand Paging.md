---
id: chunk-csos-171
type: chunk
source: "[[raw-os-031]]"
source_loc: "Memory-Mapped Files"
topic: "memory"
claim: "mmap() maps file contents into virtual address space so file I/O becomes pointer operations backed by demand paging, with the kernel loading pages on first access via page faults"
confidence: verified
supports:
  - "[[Memory-Mapped IO]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — mmap maps files into address space via demand paging

## Context

mmap(addr, length, prot, flags, fd, offset) maps a file into the process's virtual address space. Reads become pointer dereferences; the kernel loads pages from disk on first access (page fault) and writes back dirty pages via the writeback daemon or explicit msync(). On 64-bit systems (128 TB user space on x86-64), files far larger than physical RAM can be mapped.

## Why It Matters

mmap bridges the gap between file I/O and memory operations. It underpins shared library loading, database engines, and shared memory. Understanding how demand paging backs mmap explains both its power and its limitations (SIGBUS on truncated files, kernel-controlled writeback timing).

## QnA Seeds

- Q: How does mmap convert file I/O into memory operations?
- Q: What triggers the kernel to load a mapped file page into memory?
- Q: Can mmap handle files larger than physical RAM and how?
