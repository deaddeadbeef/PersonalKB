---
tags: [nes, hub]
up: "[[NES Emulation]]"
---

# CPU — The 6502 Processor Overview

The Ricoh 2A03 is a modified MOS 6502 running at 1.789773 MHz (NTSC). It lacks the 6502's BCD (Binary Coded Decimal) mode but integrates the APU on the same die. The CPU is the heart of the NES, executing game logic and orchestrating all other subsystems.

## Pages

- [[6502 Registers and Status Flags]] — A, X, Y, SP, PC, and the P register
- [[6502 Addressing Modes]] — 13 modes from Immediate to Indirect Indexed
- [[6502 Instruction Set]] — All 56 official opcodes and common unofficial ones
- [[Interrupts — NMI, IRQ, and Reset]] — How the NES handles interrupts
- [[CPU Cycle Accuracy and Timing]] — Why every cycle matters for emulation

## Key Facts

- **56 official opcodes** with 151 valid opcode bytes (13 addressing modes)
- **3 registers** (A, X, Y) + Stack Pointer + Program Counter + Status
- **Fixed stack** at 0x0100-0x01FF (256 bytes)
- **Little-endian** byte ordering
- **1-7 cycles** per instruction

## OxideNES Implementation

cpu.rs (1,670 lines): Implements all official opcodes with cycle-accurate timing. Uses a large match statement for opcode dispatch. Strategic #[inline(always)] on flag operations and hot paths (see CPU_OPTIMIZATIONS.md).

## References

→ [[Sources Index]]
