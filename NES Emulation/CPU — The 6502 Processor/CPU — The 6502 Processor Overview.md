---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
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

## How To Read This Chapter

Read this chapter for 6502-compatible execution. NES emulation is less about isolated facts than about making several small timed machines agree on the same frame. The overview pages should give you the vocabulary first, then route you into the detailed pages where timing, registers, and test-ROM behavior matter.

A productive pass has three questions. First, what state does this subsystem own? Second, which reads or writes have side effects? Third, what timing relationship can break a game if it is off by even a few CPU or PPU cycles? Keep those questions nearby while reading the linked pages.

## Emulator Checkpoints

Use the deeper notes to turn the concept into implementation proof. The key checkpoints for this chapter are: addressing modes, status flags, page crossings, interrupt timing, stack behavior, and unofficial opcode policy. For each checkpoint, prefer a tiny deterministic test before a visual game test. A passing screenshot is useful, but a focused trace is better when the bug is cycle timing, flag behavior, mapper state, or register side effects.

The chapter is mastered when you can explain both the user-visible symptom and the internal cause of a failure. For example, audio pops, scrolling seams, wrong sprite priority, broken controller input, or a mapper crash should point back to a specific piece of state and a specific clock boundary.

## References

→ [[NES Emulation/Sources/Sources Index|Sources Index]]
