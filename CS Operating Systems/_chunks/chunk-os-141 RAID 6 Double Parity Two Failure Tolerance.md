---
id: chunk-csos-141
type: chunk
source: "[[raw-os-023]]"
source_loc: "RAID Levels"
topic: "io"
claim: "RAID 6 uses double distributed parity (P+Q) to tolerate two simultaneous disk failures, becoming essential as large-disk rebuild times exceed 24 hours"
confidence: verified
supports:
  - "[[RAID and Redundant Storage]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — RAID 6 double parity tolerates two failures

## Context

RAID 6 extends RAID 5 with two independent parity calculations, typically using Reed-Solomon coding or combined XOR (P) and Galois-field (Q) parity. It tolerates two simultaneous disk failures with a storage overhead of 2/N. As disk capacities grow into multi-TB ranges, rebuild times can exceed 24 hours, during which a second failure would destroy a RAID 5 array.

## Why It Matters

RAID 6 addresses the growing gap between disk capacity and rebuild speed. Understanding why double parity is now the minimum acceptable redundancy for large arrays is essential for modern storage system design and data durability planning.

## QnA Seeds

- Q: What parity schemes does RAID 6 typically use for dual redundancy?
- Q: Why is RAID 6 increasingly preferred over RAID 5 for large-capacity drives?
- Q: How does RAID 6 storage overhead compare to RAID 5?
