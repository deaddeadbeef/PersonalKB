---
tags: [chunk, nes-emulation, cpu]
source: "[[raw-nes-001]]"
up: "[[CPU — The 6502 Processor Overview]]"
---

# Chunk NES 001 — 6502 Register Set

The MOS 6502 has six registers: the 8-bit Accumulator (A) used for arithmetic and logic, two 8-bit Index Registers (X and Y) for addressing and counting, an 8-bit Stack Pointer (SP) pointing into page 1 (-), a 16-bit Program Counter (PC) tracking the current instruction, and an 8-bit Processor Status register (P) containing flags: Negative (N), Overflow (V), Break (B), Decimal (D, unused on NES), Interrupt Disable (I), Zero (Z), and Carry (C). OxideNES stores these as individual fields in the CPU struct for direct access.
