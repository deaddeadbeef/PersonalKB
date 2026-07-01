---
tags: [nes, wiki]
up: "[[CPU — The 6502 Processor Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# 6502 Instruction Set

> **The complete set of 56 official opcodes (plus undocumented extras) that drive the NES CPU, organized by function.**

## 🎯 Intuition
**The Core Idea:** The instruction set is the CPU's complete repertoire of actions — every game ever made for the NES is expressed entirely through these ~56 operations combined with addressing modes.
**Analogy:** If the CPU is the brain, the instruction set is its vocabulary. Load/Store are "pick up" and "put down," arithmetic is mental math, branches are decisions ("if this, go there"), and JSR/RTS are "call someone to do a subtask, then come back."
**Why It Matters:** Your emulator must correctly execute every one of the 256 possible opcode bytes (including ~105 unofficial opcodes), with correct flag behavior and cycle timing — one wrong flag bit and game logic breaks.

---

## ⚙️ Core Mechanics
### How It Works
The CPU reads an opcode byte (0x00-0xFF), decodes it to determine the operation and addressing mode, executes the operation, updates status flags, and advances the program counter. Each opcode has a fixed base cycle cost that may increase for page crosses or taken branches.

### Key Specifications

**Load/Store**

| Opcode | Description | Flags |
|--------|-------------|-------|
| LDA | Load Accumulator | N, Z |
| LDX | Load X Register | N, Z |
| LDY | Load Y Register | N, Z |
| STA | Store Accumulator | - |
| STX | Store X Register | - |
| STY | Store Y Register | - |

**Arithmetic**

| Opcode | Description | Flags |
|--------|-------------|-------|
| ADC | Add with Carry | N, V, Z, C |
| SBC | Subtract with Carry | N, V, Z, C |
| CMP | Compare A | N, Z, C |
| CPX | Compare X | N, Z, C |
| CPY | Compare Y | N, Z, C |

### Key Facts
- **Increment/Decrement:** INC, INX, INY, DEC, DEX, DEY — each sets N and Z flags
- **Logical:** AND, ORA, EOR, BIT — bitwise operations on A register
- **Shift/Rotate:** ASL, LSR, ROL, ROR — shift operations on A or memory; sets N, Z, C
- **Branch:** BCC, BCS, BEQ, BNE, BMI, BPL, BVC, BVS — conditional branch using relative addressing; +1 cycle if taken, +1 more if page crossed
- **Jump/Call:** JMP, JSR, RTS, RTI — flow control and subroutine management
- **Stack:** PHA, PLA, PHP, PLP — push/pull A or flags to/from stack
- **Flags:** CLC, SEC, CLI, SEI, CLV, CLD, SED — explicit flag manipulation
- **System:** BRK (software interrupt), NOP (no operation)

---

## 🔬 Deep Dive
### Hardware Behavior Details
**Unofficial Opcodes:** The 6502 has undocumented opcodes that some NES games use. Common ones include:
- **LAX** — LDA + LDX simultaneously
- **SAX** — Store A & X to memory
- **DCP** — DEC + CMP in one instruction
- **ISC** — INC + SBC in one instruction

These arise from the 6502's PLA (Programmable Logic Array) decoding — unused opcode patterns still trigger partial combinations of micro-operations.

**ADC/SBC and the Carry Flag:** ADC always adds the carry bit; SBC always subtracts the inverse of carry. Forgetting to set carry before subtraction (SEC then SBC) or clear it before addition (CLC then ADC) is a common 6502 programming error — and your emulator must faithfully reproduce the wrong result.

**BCD Mode Disabled:** The NES's Ricoh 2A03 disables BCD (Binary-Coded Decimal) mode. The D flag can be set/cleared but ADC/SBC always operate in binary mode.

### Common Emulation Pitfalls
1. **Wrong V (overflow) flag on ADC/SBC** — The overflow flag detects signed overflow, not unsigned. The formula is: `V = (A ^ result) & (operand ^ result) & 0x80`. Getting this wrong breaks games that use signed arithmetic
2. **Unofficial opcodes treated as NOP** — Games like Bionic Commando and Battletoads use unofficial opcodes; treating them as NOP will crash these games
3. **Branch cycle counting** — A taken branch costs +1 cycle; a taken branch that crosses a page costs +2 total extra cycles. Miss this and raster-timed games glitch

### Reference Implementations
OxideNES cpu.rs uses a massive match statement on the opcode byte (0x00-0xFF) in the `clock()` method. Each arm sets the addressing mode, executes the operation, and assigns the cycle count. The most common unofficial opcodes are handled.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Which flag is affected by almost every arithmetic and load operation? (Hint: two flags, actually)
2. What is the difference between CMP and SBC in terms of flags set and register modification?
3. Why does BRK push PC+2 to the stack (skipping a byte) even though it's a 1-byte instruction?

### Core Problems
1. **Implement ADC with correct flag handling:** Write the ADC operation that correctly sets N, V, Z, and C flags. Test with: A=0x50, operand=0x50, C=0 (should set V because 80+80=overflow in signed).
2. **Opcode decoder:** Design a data structure to map all 256 opcode bytes to their operation, addressing mode, base cycle count, and whether they have a page-cross penalty.

### Challenge
**Unofficial opcode accuracy:** Implement LAX (opcode 0xA7, 0xB7, 0xAF, 0xBF, 0xA3, 0xB3) which performs LDA and LDX simultaneously. What flags should be set? Test with a ROM that uses LAX and verify it matches hardware behavior. Then explain why LAX exists at the hardware level (hint: the 6502's internal data bus).

---

*See also:* [[6502 Addressing Modes]], [[6502 Registers and Status Flags]], [[CPU Cycle Accuracy and Timing]], [[Interrupts — NMI, IRQ, and Reset]], [[CPU — The 6502 Processor Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
