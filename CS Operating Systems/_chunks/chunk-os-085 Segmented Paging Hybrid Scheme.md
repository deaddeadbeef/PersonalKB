---
tags: [cs-os, chunk]
source: "[[raw-os-009]]"
confidence: high
supports:
  - "[[Memory Management]]"
  - "[[Segmentation]]"
qna_seeds:
  - "Q: How does segmented paging combine both schemes? A: Used in Intel 386–Pentium, a logical address is first translated through a segment table to a linear address, then through a page table to a physical address. This provides segmentation's logical protection/sharing with paging's fragmentation-free allocation. Multics pioneered this approach in the 1960s."
---

# Segmented Paging Hybrid Scheme

Segmented paging, used in Intel 386 through Pentium processors, combines both memory management schemes: a logical address is first translated through a segment table to a linear address, which is then translated through a page table to a physical address. This hybrid provides segmentation's advantages (logical protection boundaries, fine-grained sharing of code segments) while using paging to eliminate external fragmentation. The Multics operating system (1960s) pioneered this approach, supporting up to 2^18 segments of up to 2^18 words each, with per-segment access control lists.
