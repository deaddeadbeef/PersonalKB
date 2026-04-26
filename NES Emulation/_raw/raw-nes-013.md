---
tags: [raw, nes-emulation, instruction-set]
source: "6502 reference + OxideNES cpu.rs"
---

# Raw NES 013 — 6502 Instruction Set Reference

The official MOS 6502 instruction set comprises 56 unique instructions encoded in 151 valid opcodes (the remaining 105 are unofficial). Instructions fall into several categories.

## Load/Store

- **LDA, LDX, LDY:** Load accumulator/X/Y from memory. Sets N and Z flags.
- **STA, STX, STY:** Store A/X/Y to memory. No flag changes.

## Arithmetic

- **ADC:** Add with carry: A = A + M + C. Sets N, V, Z, C. The NES ignores the decimal mode flag, so BCD mode never activates. Overflow (V) detection uses the formula: (A ^ result) & (M ^ result) & 0x80.
- **SBC:** Subtract with borrow: A = A - M - (1-C). Implemented as ADC with the operand complemented. Same flag behavior.
- **INC, INX, INY:** Increment memory/X/Y by 1. Sets N, Z.
- **DEC, DEX, DEY:** Decrement by 1. Sets N, Z.

## Compare

- **CMP, CPX, CPY:** Subtract register minus memory, setting N, Z, C flags but discarding the result. C is set if register >= memory (unsigned comparison).

## Logical

- **AND:** A = A & M. Sets N, Z.
- **ORA:** A = A | M. Sets N, Z.
- **EOR:** A = A ^ M (XOR). Sets N, Z.
- **BIT:** Performs A & M without storing result. Z is set from the result; N and V are set from bits 7 and 6 of the memory value (not the AND result).

## Shift/Rotate

- **ASL:** Arithmetic shift left. Bit 7 goes to C, 0 goes to bit 0. Operates on A or memory.
- **LSR:** Logical shift right. Bit 0 goes to C, 0 goes to bit 7.
- **ROL:** Rotate left through carry. Bit 7 goes to C, old C goes to bit 0.
- **ROR:** Rotate right through carry. Bit 0 goes to C, old C goes to bit 7.

## Branch

All branch instructions use relative addressing (signed 8-bit offset):
- **BCC/BCS:** Branch if carry clear/set
- **BEQ/BNE:** Branch if zero set/clear
- **BMI/BPL:** Branch if negative set/clear
- **BVC/BVS:** Branch if overflow clear/set

## Jump/Subroutine

- **JMP:** Unconditional jump (absolute or indirect)
- **JSR:** Jump to subroutine — pushes PC-1 to stack, then jumps
- **RTS:** Return from subroutine — pulls PC from stack, adds 1
- **RTI:** Return from interrupt — pulls P then PC from stack

## Stack

- **PHA/PLA:** Push/pull accumulator to/from stack
- **PHP/PLP:** Push/pull processor status to/from stack
- **TXS/TSX:** Transfer X to/from stack pointer

## System

- **BRK:** Software interrupt — pushes PC+2 and P with B flag set, loads IRQ vector
- **NOP:** No operation (2 cycles)
- **SEI/CLI:** Set/clear interrupt disable flag
- **SED/CLD:** Set/clear decimal flag (no effect on NES but state is tracked)
- **SEC/CLC:** Set/clear carry flag
- **CLV:** Clear overflow flag

## Unofficial Opcodes in OxideNES

OxideNES implements the most commonly used unofficial opcodes for game compatibility: LAX (LDA+LDX combined), SAX (store A&X), DCP (DEC+CMP), ISB/ISC (INC+SBC), SLO (ASL+ORA), RLA (ROL+AND), SRE (LSR+EOR), RRA (ROR+ADC). Unknown opcodes are treated as NOP with appropriate cycle counts.