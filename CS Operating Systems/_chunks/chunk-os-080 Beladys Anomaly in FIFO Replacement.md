---
tags: [cs-os, chunk]
source: "[[raw-os-008]]"
confidence: high
supports:
  - "[[Page Replacement]]"
qna_seeds:
  - "Q: What is Belady's anomaly and which algorithms are affected? A: Belady's anomaly is where increasing physical frames increases page faults. Demonstrated with FIFO on string 1,2,3,4,1,2,5,1,2,3,4,5: 3 frames → 9 faults, 4 frames → 10 faults. Stack algorithms (LRU, OPT) are provably immune because pages in n frames are always a subset of those in n+1 frames."
---

# Beladys Anomaly in FIFO Replacement

Belady's anomaly is the counterintuitive phenomenon where increasing the number of physical frames can increase the page fault rate. It was demonstrated with FIFO replacement on reference string 1,2,3,4,1,2,5,1,2,3,4,5: with 3 frames there are 9 page faults, but with 4 frames there are 10. Stack algorithms — including LRU and OPT — are provably immune to this anomaly because the set of pages in memory with n frames is always a subset of the set with n+1 frames. This property is why LRU-based approaches are strongly preferred over FIFO in practice.
