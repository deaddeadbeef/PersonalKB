---
id: chunk-csos-139
type: chunk
source: "[[raw-os-023]]"
source_loc: "RAID Levels"
topic: "io"
claim: "RAID 0 stripes data across multiple disks for maximum throughput but provides zero fault tolerance — any single disk failure destroys the entire array"
confidence: verified
supports:
  - "[[RAID and Redundant Storage]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — RAID 0 stripes for throughput with zero redundancy

## Context

RAID 0 distributes data in fixed-size strips across all disks, parallelizing reads and writes. Throughput scales linearly with the number of disks. However, the array has no redundancy whatsoever — the failure probability increases with each added disk since any single failure causes total data loss.

## Why It Matters

RAID 0 establishes the baseline: pure performance with zero reliability. Understanding it is essential for grasping why RAID 1, 5, 6, and 10 exist and what tradeoffs each makes to add redundancy atop striping.

## QnA Seeds

- Q: What does RAID 0 optimize for and what does it sacrifice?
- Q: How does RAID 0 distribute data across disks?
- Q: Why does adding more disks to RAID 0 increase failure risk?
