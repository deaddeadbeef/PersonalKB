---
id: chunk-csos-137
type: chunk
source: "[[raw-os-022]]"
source_loc: "Disk Scheduling Algorithms"
topic: "io"
claim: "LOOK and C-LOOK optimize SCAN and C-SCAN by reversing at the last actual pending request instead of traveling to the physical disk boundary"
confidence: verified
supports:
  - "[[Disk Scheduling Algorithms]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — LOOK C-LOOK reverse at last request not disk edge

## Context

SCAN travels to the physical end of the disk before reversing, even if no requests exist beyond the last pending one. LOOK reverses as soon as the last request in the current direction is serviced, eliminating wasted empty sweeps. C-LOOK applies the same optimization to C-SCAN, jumping back without servicing on the return.

## Why It Matters

LOOK/C-LOOK are the algorithms actually deployed in real disk schedulers, not the textbook SCAN. Understanding the optimization explains why practical implementations diverge from the theoretical description and how unnecessary seeks are eliminated.

## QnA Seeds

- Q: How does LOOK differ from SCAN in head reversal behavior?
- Q: What inefficiency does C-LOOK eliminate compared to C-SCAN?
- Q: Why are LOOK variants preferred over pure SCAN in real disk schedulers?
