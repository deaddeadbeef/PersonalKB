---
tags: [cs-os, chunk]
source: "[[raw-os-009]]"
confidence: high
supports:
  - "[[Memory Management]]"
  - "[[Segmentation]]"
qna_seeds:
  - "Q: Why did paging replace segmentation as the dominant memory management scheme? A: Segmentation causes external fragmentation — variably-sized freed segments leave unusable gaps. Compaction (relocating segments) is O(n) memory copies, making it infeasible routinely. Paging's fixed-size pages eliminate external fragmentation entirely, which is why modern architectures favor paging."
---

# External Fragmentation in Segmentation

External fragmentation is the primary weakness of pure segmentation. As segments of varying sizes are allocated and freed, physical memory becomes riddled with small unusable gaps between allocated regions. Allocation algorithms — first-fit, best-fit, worst-fit — attempt to minimize fragmentation but none eliminate it. Compaction (relocating all segments to consolidate free space) requires updating all base addresses and involves O(n) memory copies, making it infeasible as a routine operation. This fundamental problem is why paging — with its fixed-size pages that eliminate external fragmentation entirely — ultimately replaced segmentation as the dominant memory management scheme.
