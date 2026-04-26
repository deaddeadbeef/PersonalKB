---
id: chunk-csos-030
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 5"
topic: "io"
claim: "I/O software is organised in four layers — interrupt handler, device driver, device-independent OS layer, user-space library — each hiding complexity from the layer above"
confidence: verified
supports:
  - "[[IO Software Layers]]"
tags:
  - csos
  - csos/io
  - chunk
up: "[[CS Operating Systems]]"
---
# IO — IO software uses four layers from interrupt handler to user-space library

## Context

Tanenbaum defines a clean four-layer model. Layer 1 (interrupt handler): catches hardware interrupts, services device registers, wakes the driver thread. Layer 2 (device driver): translates OS-level requests into device commands; blocks waiting for the interrupt to signal completion. Layer 3 (device-independent OS layer): provides naming, buffering, error handling, and a uniform block/character interface regardless of device type. Layer 4 (user-space): C library buffering (`stdio`), spooling daemons (print queue).

## Why It Matters

This layered model is the reason you can read from `/dev/sda` and `/dev/ttyS0` with the same `open/read` calls, and why adding a new device type requires only writing a new driver (layer 2) without touching the rest of the stack. The model also explains where bugs live: a missed interrupt (layer 1), a wrong command sequence (layer 2), a buffer overflow (layer 3), or an unhandled `errno` (layer 4).

## QnA Seeds

- Q: Name the four I/O software layers from bottom to top.
- Q: What is the role of the device-independent OS layer?
- Q: Why does user-space buffering (stdio) exist on top of kernel buffering?
