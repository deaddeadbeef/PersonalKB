---
id: chunk-csos-135
type: chunk
source: "[[raw-os-022]]"
source_loc: "Disk Scheduling Algorithms"
topic: "io"
claim: "Seek time dominates HDD access latency, making request ordering far more important than raw transfer speed for spinning disk performance"
confidence: verified
supports:
  - "[[Disk Scheduling Algorithms]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — Seek time dominates HDD access latency over transfer speed

## Context

Total disk access time comprises seek time (3-15 ms to move the head), rotational latency (averaging half a rotation, ~4.17 ms at 7200 RPM), and transfer time (under 1 ms). Because seek time dwarfs the other components, algorithms that reorder requests to minimize head movement yield the largest throughput gains.

## Why It Matters

This asymmetry is why disk scheduling algorithms exist at all. Any I/O-bound workload on spinning disks benefits from intelligent reordering. It also explains why SSDs, with uniform access latency, render these algorithms irrelevant.

## QnA Seeds

- Q: What are the three components of HDD access time and which dominates?
- Q: Why does request ordering matter more than transfer speed for HDDs?
- Q: What typical seek time range makes reordering worthwhile?
