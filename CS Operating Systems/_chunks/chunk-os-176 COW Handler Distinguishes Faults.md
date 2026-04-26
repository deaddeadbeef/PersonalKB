---
id: chunk-csos-176
type: chunk
source: "[[raw-os-032]]"
source_loc: "Copy-on-Write Mechanism"
topic: "memory"
claim: "The COW fault handler distinguishes COW faults from genuine protection violations by checking page reference counts or COW bits in page table entries"
confidence: verified
supports:
  - "[[Copy-on-Write]]"
tags:
  - csos
  - csos/memory
  - chunk
up: "[[CS Operating Systems]]"
---
# Memory — COW handler distinguishes shared faults from violations

## Context

When a page fault occurs on a read-only page, the handler must determine if it's a COW page (originally writable, shared between processes) or a true protection fault (SIGSEGV). On x86, bit 1 (R/W) in the PTE controls write permission; the kernel uses software-defined bits or struct page flags to distinguish COW. Linux's copy_page_range() copies PTEs and increments reference counts on physical frames during fork.

## Why It Matters

This distinction is critical: misidentifying a COW fault as a segfault would crash the process; misidentifying a real protection fault as COW would create a security vulnerability. Understanding the mechanism reveals how the kernel maintains memory safety during process creation.

## QnA Seeds

- Q: How does the page fault handler distinguish COW faults from real protection faults?
- Q: What x86 PTE bits are used for COW implementation?
- Q: What does copy_page_range() do during fork on Linux?
