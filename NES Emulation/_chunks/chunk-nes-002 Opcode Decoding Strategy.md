---
tags: [chunk, nes-emulation, cpu]
source: "[[raw-nes-001]]"
up: "[[6502 Instruction Set]]"
---

# Chunk NES 002 — Opcode Decoding Strategy

OxideNES decodes all 256 possible opcode bytes via a Rust match statement. Official opcodes execute documented 6502 behavior. The most commonly used unofficial opcodes are implemented for game compatibility: LAX (LDA+LDX), SAX (store A AND X), DCP (DEC+CMP), ISB (INC+SBC), SLO (ASL+ORA), RLA (ROL+AND), SRE (LSR+EOR), and RRA (ROR+ADC). Remaining undefined opcodes map to NOP with appropriate cycle counts, or KIL which halts the CPU. The decode step itself consumes 1 cycle for the opcode fetch from memory.
