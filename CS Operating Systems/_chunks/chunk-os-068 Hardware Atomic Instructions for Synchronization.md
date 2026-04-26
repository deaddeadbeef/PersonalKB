---
tags: [cs-os, chunk]
source: "[[raw-os-005]]"
confidence: high
supports:
  - "[[Process Synchronization]]"
  - "[[Concurrency Primitives]]"
qna_seeds:
  - "Q: How do test-and-set and compare-and-swap work? A: Test-and-set atomically reads a memory location, returns the old value, and sets it to true — a spinlock loops on this until the old value is false. CAS atomically compares a location to an expected value and replaces it only if they match; CAS is the basis for lock-free data structures (x86 cmpxchg)."
---

# Hardware Atomic Instructions for Synchronization

Hardware atomic instructions provide the foundation for all practical synchronization primitives by executing indivisibly. Test-and-set atomically reads a memory location, returns its old value, and sets it to true — a spinlock loops on test-and-set until the returned value is false (lock was free). Compare-and-swap (CAS) atomically compares a memory location to an expected value and replaces it with a new value only if they match. CAS, exposed as `cmpxchg` on x86, is the basis for lock-free data structures and wait-free algorithms.
