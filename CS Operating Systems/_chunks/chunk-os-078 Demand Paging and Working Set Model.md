---
tags: [cs-os, chunk]
source: "[[raw-os-007]]"
confidence: high
supports:
  - "[[Virtual Memory]]"
  - "[[Page Replacement]]"
qna_seeds:
  - "Q: What is demand paging and how does the working set model prevent thrashing? A: Demand paging defers loading a page until the first access triggers a page fault. The working set W(t,Δ) is the set of pages referenced in interval (t−Δ, t). Keeping each process's working set in memory is the key to preventing thrashing."
---

# Demand Paging and Working Set Model

Demand paging loads pages from disk only on first access: when a process references an unmapped page, a page fault occurs, the handler loads the page from disk, updates the page table, and restarts the faulting instruction transparently. The working set of a process at time t with window Δ is the set of pages referenced during the interval (t−Δ, t). Maintaining each process's working set in physical memory is the key to avoiding thrashing — the condition where the system spends more time paging than executing useful instructions.
