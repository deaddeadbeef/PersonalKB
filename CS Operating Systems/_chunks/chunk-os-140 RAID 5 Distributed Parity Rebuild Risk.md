---
id: chunk-csos-140
type: chunk
source: "[[raw-os-023]]"
source_loc: "RAID Levels"
topic: "io"
claim: "RAID 5 uses distributed parity to avoid a parity-disk bottleneck but is vulnerable during rebuilds when a second failure causes total array loss"
confidence: verified
supports:
  - "[[RAID and Redundant Storage]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — RAID 5 distributed parity with rebuild vulnerability

## Context

RAID 5 stripes data across N disks with parity blocks rotated across all drives, so no single disk becomes a write bottleneck. Storage overhead is 1/N. The write penalty requires four I/O operations per small write (read old data, read old parity, write new data, write new parity). A 10 TB array at 200 MB/s rebuild throughput takes ~14 hours to reconstruct, during which a second failure means total data loss.

## Why It Matters

RAID 5 is historically the most common RAID level for general-purpose storage, but growing disk sizes make rebuild windows dangerously long. This vulnerability is driving the industry toward RAID 6 and explains why RAID 5 is increasingly considered insufficient for large-capacity drives.

## QnA Seeds

- Q: Why does RAID 5 rotate parity across all disks instead of using a dedicated parity disk?
- Q: What is the RAID 5 write penalty and how many I/Os does a small write require?
- Q: Why are long rebuild times dangerous for RAID 5 arrays?
