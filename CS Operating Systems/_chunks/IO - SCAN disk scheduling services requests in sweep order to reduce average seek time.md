---
id: chunk-csos-031
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 5"
topic: "io"
claim: "SCAN disk scheduling sweeps the disk arm in one direction servicing all pending requests, then reverses — like an elevator — providing no-starvation guarantees and lower variance than SSTF"
confidence: verified
supports:
  - "[[Disk Scheduling Algorithms]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — SCAN disk scheduling services requests in sweep order to reduce average seek time

## Context

SSTF (shortest seek time first) minimises individual seeks but can starve requests at the disk extremes if requests keep arriving near the current head position. SCAN solves this by committing the arm to travel to the end of the disk in the current direction, servicing all requests on the way, then reversing. A request can wait at most two full sweeps to be serviced. C-SCAN improves uniformity by only servicing on one direction (reset at the end) — requests near the just-visited end don't get unfair advantage.

## Why It Matters

SCAN variants are the standard choice for HDD-intensive workloads (database servers, NAS). Understanding them is also necessary to understand why they become irrelevant for SSDs (no seek latency) and why NVMe multi-queue schedulers (which parallelise across queues) replace single-queue SCAN entirely on modern storage.

## QnA Seeds

- Q: How does SCAN prevent the starvation problem that affects SSTF?
- Q: Why is C-SCAN fairer than SCAN for requests at disk extremes?
- Q: Why do disk scheduling algorithms matter less for SSDs than HDDs?
