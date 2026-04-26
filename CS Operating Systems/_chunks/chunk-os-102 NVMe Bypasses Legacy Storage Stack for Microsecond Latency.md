---
id: chunk-csos-102
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 5 — I/O Systems Architecture"
topic: "io"
claim: "NVMe (Non-Volatile Memory Express) bypasses the traditional SCSI/AHCI storage stack, communicating directly via PCIe with up to 65,535 I/O queues of 65,536 entries each, achieving microsecond-level latency and millions of IOPS"
confidence: verified
supports:
  - "[[IO Hardware Fundamentals]]"
  - "[[IO Overview]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — NVMe bypasses legacy storage stacks for microsecond-latency I/O

## Context

Traditional storage interfaces (SCSI, AHCI/SATA) were designed around the assumption of slow, mechanical disks and use a single command queue with limited depth. NVMe was designed from scratch for flash storage connected via PCIe, supporting up to 65,535 I/O queues with 65,536 entries each. This massive parallelism matches the internal parallelism of NAND flash arrays. NVMe eliminates the overhead of the SCSI translation layer, achieving microsecond-level latency and millions of IOPS — orders of magnitude better than AHCI on the same underlying flash.

## Why It Matters

NVMe demonstrates that interface design can be as important as the underlying hardware. The same flash chips behind an AHCI SATA SSD deliver dramatically better performance when accessed through NVMe, because the interface no longer bottlenecks the device's inherent parallelism. Memory-mapped I/O through device registers mapped into the processor's address space further reduces per-operation overhead.

## QnA Seeds

- Q: Why was a new storage interface needed for flash-based SSDs?
- Q: How does NVMe's queue architecture differ from AHCI's?
- Q: What throughput and latency improvements does NVMe achieve over SATA?
