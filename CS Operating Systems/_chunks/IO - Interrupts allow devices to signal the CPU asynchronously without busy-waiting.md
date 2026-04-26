---
id: chunk-csos-027
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 5"
topic: "io"
claim: "Interrupts allow a device to signal the CPU asynchronously when I/O is complete, freeing the CPU from busy-waiting and enabling it to do other work between I/O initiation and completion"
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
# IO — Interrupts allow devices to signal the CPU asynchronously without busy-waiting

## Context

In programmed I/O, the CPU repeatedly reads the device status register until the device reports "done" — wasting CPU cycles. Interrupt-driven I/O lets the CPU start the operation and then run something else; when the device finishes, it asserts an interrupt line, the CPU saves its state, and executes the interrupt handler. The handler services the device, then returns to the interrupted work. For slow devices (keyboard, network at low load), this is a massive efficiency improvement.

## Why It Matters

Interrupt-driven I/O is the foundation of modern OS concurrency. Without it, every blocked I/O call would stall the CPU. The interrupt mechanism allows the OS to overlap CPU computation with I/O on all devices simultaneously — the basis for multiprogramming. Understanding interrupt latency, masking, and priority is essential for real-time and embedded OS design where interrupt response time is a hard requirement.

## QnA Seeds

- Q: What are the three I/O paradigms and how do they differ in CPU involvement?
- Q: What does "interrupt latency" mean and why does it matter?
- Q: What is an interrupt vector and how is it used?
