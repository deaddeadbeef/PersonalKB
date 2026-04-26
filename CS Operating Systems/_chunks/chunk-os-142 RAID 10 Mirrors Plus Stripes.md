---
id: chunk-csos-142
type: chunk
source: "[[raw-os-023]]"
source_loc: "RAID Levels"
topic: "io"
claim: "RAID 10 stripes across mirrored pairs, combining RAID 1 redundancy with RAID 0 performance at 50% storage overhead for write-intensive workloads"
confidence: verified
supports:
  - "[[RAID and Redundant Storage]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — RAID 10 mirrors plus stripes for write performance

## Context

RAID 10 (1+0) creates mirrored pairs and then stripes across them. It tolerates multiple simultaneous failures as long as both disks in a mirror pair do not fail together. With 50% storage overhead, it offers the best combination of write performance and reliability because writes only need to update two disks (the mirror pair) with no parity computation.

## Why It Matters

RAID 10 is the standard choice for write-intensive workloads like database transaction logs. Understanding why it outperforms RAID 5/6 for writes (no parity penalty) while providing strong redundancy explains real-world storage architecture decisions.

## QnA Seeds

- Q: How does RAID 10 combine striping and mirroring?
- Q: Under what failure pattern does RAID 10 lose data?
- Q: Why is RAID 10 preferred over RAID 5 for write-intensive workloads?
