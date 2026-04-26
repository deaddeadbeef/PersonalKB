---
id: chunk-csos-168
type: chunk
source: "[[raw-os-030]]"
source_loc: "Network Stack in OS"
topic: "io"
claim: "NAPI combines interrupt-driven and polling-based packet processing: after the first packet interrupt, the driver switches to polling to batch-process packets, reducing interrupt overhead at high rates"
confidence: verified
supports:
  - "[[Network Stack]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — NAPI hybrid interrupt-polling reduces packet overhead

## Context

At low packet rates, interrupt-per-packet is efficient. At high rates, the interrupt overhead itself becomes a bottleneck. NAPI (New API) solves this by switching to polling mode after the first interrupt, batch-processing thousands of packets per cycle. GRO (Generic Receive Offload) further coalesces multiple small packets into fewer large ones before passing them up the stack.

## Why It Matters

NAPI is why Linux can handle millions of packets per second without being overwhelmed by interrupts. Understanding the interrupt-to-polling transition explains network performance under varying load and why high-throughput applications need NAPI-capable drivers.

## QnA Seeds

- Q: What problem does NAPI solve for high packet rate processing?
- Q: How does NAPI transition between interrupt and polling modes?
- Q: What does GRO do to complement NAPI?
