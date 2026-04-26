---
id: chunk-csos-028
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 5"
topic: "io"
claim: "DMA (Direct Memory Access) offloads bulk data transfer from the CPU to a dedicated controller that moves data between device and memory autonomously, interrupting the CPU only once per block"
confidence: verified
supports:
  - "[[IO Hardware Fundamentals]]"
  - "[[Interrupts and DMA]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — DMA offloads bulk data transfers from the CPU to a dedicated controller

## Context

For large transfers (reading a disk sector, receiving a network packet), interrupt-driven I/O still requires the CPU to copy each byte from the device data register to memory. DMA eliminates this: the CPU programs the DMA controller with source (device register/memory address), destination (memory address), transfer count, and direction. The DMA controller takes the memory bus and moves the data autonomously. The CPU is interrupted once when the entire block is done, not once per byte.

## Why It Matters

DMA is what makes high-throughput I/O possible. A 10 Gbps NIC receiving packets cannot interrupt the CPU once per 64-byte packet — it would consume the entire CPU just servicing interrupts. DMA (or its modern successor, scatter-gather DMA with descriptor rings) decouples data movement from CPU execution. Modern NVMe SSDs use DMA queues with up to 65535 outstanding commands per queue.

## QnA Seeds

- Q: What information must the CPU program into the DMA controller to initiate a transfer?
- Q: Why is DMA important for high-throughput devices like Gigabit Ethernet?
- Q: What is bus arbitration in the context of DMA?
