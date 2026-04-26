---
id: chunk-csos-136
type: chunk
source: "[[raw-os-022]]"
source_loc: "Disk Scheduling Algorithms"
topic: "io"
claim: "SSTF selects the nearest pending request to minimize average seek distance but can starve distant requests when nearby requests continuously arrive"
confidence: verified
supports:
  - "[[Disk Scheduling Algorithms]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — SSTF minimizes seek distance but risks starvation

## Context

Shortest Seek Time First always services the request closest to the current head position, producing the smallest average seek distance. However, if new requests keep arriving near the head, requests at extreme inner or outer tracks may wait indefinitely. This unbounded wait time makes SSTF unsuitable where fairness is required.

## Why It Matters

SSTF illustrates the classic throughput-vs-fairness tradeoff in scheduling. It motivates SCAN/C-SCAN variants that provide bounded waiting times by guaranteeing the head sweeps the entire disk range.

## QnA Seeds

- Q: How does SSTF select which I/O request to service next?
- Q: Under what conditions does SSTF starve requests?
- Q: Why is SSTF optimal for average seek but not for worst-case latency?
