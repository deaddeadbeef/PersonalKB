---
tags: [chunk, nes-emulation, instruction-set]
source: "[[raw-nes-013]]"
up: "[[6502 Instruction Set]]"
---

# Chunk NES 041 — Shift, Rotate, and Branch Instructions

ASL (arithmetic shift left) moves all bits left, placing bit 7 into Carry and inserting 0 at bit 0. LSR (logical shift right) moves bits right, placing bit 0 into Carry. ROL and ROR rotate through the Carry flag, creating a 9-bit rotation chain. All shift/rotate instructions operate on either the Accumulator or a memory location. Branch instructions use signed 8-bit relative offsets: BCC/BCS (carry), BEQ/BNE (zero), BMI/BPL (negative), BVC/BVS (overflow). Taken branches add 1 cycle; page-crossing branches add another. Branches are 2 bytes with 2-4 cycle cost.
