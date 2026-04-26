---
id: chunk-csos-002
type: chunk
source: "[[Tanenbaum 2015 - Modern Operating Systems]]"
source_loc: "Chapter 1"
topic: "foundations"
claim: "The CPU hardware enforces a privilege boundary between kernel mode (full hardware access) and user mode (restricted), preventing user programs from corrupting OS state"
confidence: verified
supports:
  - "[[OS Fundamentals]]"
  - "[[System Calls]]"
tags:
  - csos
  - csos/foundations
  - chunk
up: "[[CS Operating Systems]]"
---
# Foundations — Kernel mode and user mode enforce the hardware privilege boundary

## Context

Modern CPUs implement at least two privilege levels. In kernel mode (ring 0 on x86), the CPU allows all instructions including those that control interrupts, access I/O ports, and modify memory protection registers. In user mode (ring 3), privileged instructions trap to the OS. This is a hardware mechanism — not a software convention — so user code cannot bypass it by clever tricks.

## Why It Matters

Without this boundary, any program could crash the OS, read another process's data, or disable interrupts. The boundary is the foundational mechanism enabling process isolation, OS protection, and the trusted computing base concept. All other OS security properties build on top of it.

## QnA Seeds

- Q: What is the difference between kernel mode and user mode?
- Q: Can user code execute privileged CPU instructions? What happens if it tries?
- Q: How does the CPU know which mode it is currently in?
