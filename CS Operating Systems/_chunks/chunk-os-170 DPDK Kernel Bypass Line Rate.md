---
id: chunk-csos-170
type: chunk
source: "[[raw-os-030]]"
source_loc: "Network Stack in OS"
topic: "io"
claim: "Kernel bypass frameworks like DPDK map NIC queues directly into user-space memory for line-rate processing at 10-100 Gbps, but sacrifice kernel security and multi-tenant isolation"
confidence: verified
supports:
  - "[[Network Stack]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — DPDK kernel bypass for line-rate packet processing

## Context

DPDK (Data Plane Development Kit) maps NIC hardware queues directly into user-space memory, bypassing the entire kernel network stack. It uses hugepages (2 MB or 1 GB) to reduce TLB misses and binds NIC queues to dedicated CPU cores via UIO or VFIO drivers. This achieves line-rate processing at 10-100 Gbps but requires dedicated cores and sacrifices the kernel protocol stack, security model, and multi-tenant isolation.

## Why It Matters

DPDK represents the extreme end of the performance-vs-abstraction tradeoff. Understanding when kernel bypass is justified (telecom, NFV, high-frequency trading) vs. when the kernel stack is sufficient helps architects make informed design decisions.

## QnA Seeds

- Q: How does DPDK achieve line-rate packet processing?
- Q: What does DPDK sacrifice by bypassing the kernel network stack?
- Q: Why does DPDK use hugepages and CPU core pinning?
