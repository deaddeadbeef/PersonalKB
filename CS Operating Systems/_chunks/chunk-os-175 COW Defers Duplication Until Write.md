---
id: chunk-csos-175
type: chunk
source: "[[raw-os-032]]"
source_loc: "Copy-on-Write Mechanism"
topic: "memory"
claim: "Copy-on-Write defers physical page duplication until a write occurs by marking shared pages read-only and handling the copy in the page fault handler"
confidence: verified
supports:
  - "[[Copy-on-Write]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — COW defers page duplication until write faults

## Context

After fork(), both parent and child page table entries point to the same physical frames marked read-only. When either process writes, a page fault fires. The handler checks for a COW condition (via COW bit or reference count), allocates a new frame, copies the content, updates the faulting process's PTE with write permission, and resumes. If the reference count is 1, the kernel simply re-enables write permission without copying.

## Why It Matters

COW exemplifies the lazy evaluation principle — deferring expensive work until absolutely necessary. This fundamental optimization makes fork() viable for large processes and is the template for copy-on-write in filesystems, VM deduplication, and private mmap.

## QnA Seeds

- Q: How does the kernel set up COW during fork()?
- Q: What happens in the page fault handler when a COW fault occurs?
- Q: When can the kernel avoid copying by just re-enabling write permission?
