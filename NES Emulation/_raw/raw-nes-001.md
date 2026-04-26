---
tags: [raw, nes-emulation, cpu]
source: "OxideNES cpu.rs + 6502 reference"
---

# Raw NES 001 — 6502 CPU Core Implementation

The MOS 6502 CPU in OxideNES is implemented as a cycle-accurate state machine in cpu.rs (~1,670 lines). The CPU struct holds registers A, X, Y, SP (stack pointer), PC (program counter), and the P status register with flags N (negative), V (overflow), B (break), D (decimal, unused on NES), I (interrupt disable), Z (zero), and C (carry).

## Instruction Decoding

Each opcode is decoded via a match statement mapping all 256 possible byte values. Official opcodes execute documented behavior; unofficial opcodes implement the most commonly used ones (LAX, SAX, DCP, ISB, SLO, RLA, SRE, RRA) while others map to NOP or KIL. The decode step consumes 1 cycle for the opcode fetch.

## Addressing Modes

The CPU implements 13 addressing modes: Implicit, Accumulator, Immediate, Zero Page, Zero Page X/Y, Absolute, Absolute X/Y, Indirect, Indexed Indirect (X), Indirect Indexed (Y), and Relative. Each mode has a dedicated method that computes the effective address and tracks whether a page boundary was crossed (adding an extra cycle for read instructions on page crosses).

## Cycle Accuracy

OxideNES achieves cycle accuracy through a emaining_cycles counter. When an instruction begins execution, it sets emaining_cycles to the instruction's base cycle count. The bus calls cpu.tick() each master clock cycle; the CPU only executes when emaining_cycles reaches zero. Page-crossing penalties and branch-taken penalties are added dynamically. This approach produces correct timing without needing a full per-cycle pipeline simulation.

## Interrupt Handling

Three interrupt vectors are supported: NMI (0xFFFA), RESET (0xFFFC), and IRQ/BRK (0xFFFE). NMI is edge-triggered and has highest priority — the PPU asserts it at the start of vertical blank (scanline 241). IRQ is level-triggered and masked by the I flag. The interrupt sequence pushes PC and P to the stack (7 cycles total), sets the I flag, and loads PC from the vector. OxideNES polls for pending interrupts between instructions, matching real hardware behavior.

## Key Design Decisions

- All memory access goes through the Bus trait, enabling memory-mapped I/O
- The decimal mode flag exists but BCD arithmetic is not implemented (NES disabled it)
- Unofficial opcodes are implemented for compatibility with games that use them
- The CPU exposes cycle_count for synchronization with PPU and APU
