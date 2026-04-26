---
id: chunk-csos-138
type: chunk
source: "[[raw-os-022]]"
source_loc: "Disk Scheduling Algorithms"
topic: "io"
claim: "SSDs have uniform access latency regardless of address, making traditional seek-optimizing schedulers irrelevant; SSD scheduling focuses on queue depth and parallelism instead"
confidence: verified
supports:
  - "[[Disk Scheduling Algorithms]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — SSD scheduling optimizes queue depth not seek order

## Context

Solid-state drives have no mechanical head or platter, so access times are uniform at 25-100 microseconds regardless of address. Linux uses the `none` (noop) scheduler for NVMe SSDs, passing requests directly to the device without reordering. NVMe drives support up to 65,535 hardware queues with 65,535 entries each, making software-level reordering unnecessary.

## Why It Matters

This shows how hardware evolution can obsolete entire algorithm classes. Understanding why SCAN is irrelevant for SSDs prevents engineers from applying HDD-era thinking to modern storage and directs attention to parallelism and queue management as the actual bottlenecks.

## QnA Seeds

- Q: Why are disk scheduling algorithms like SCAN irrelevant for SSDs?
- Q: What I/O scheduler does Linux use by default for NVMe SSDs and why?
- Q: How many hardware queues can NVMe drives support?
