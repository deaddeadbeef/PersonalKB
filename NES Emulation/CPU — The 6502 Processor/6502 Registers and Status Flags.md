---
tags: [nes, wiki]
up: "[[CPU — The 6502 Processor Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# 6502 Registers and Status Flags

> **The 6502's six registers and 7-bit status word that form the complete internal state of the NES CPU.**

## 🎯 Intuition
**The Core Idea:** The registers are the CPU's tiny scratchpad — just 6 registers hold the entire working state, and the 8-bit status register encodes the outcome of every operation as a set of boolean flags.
**Analogy:** Registers are like the items the brain can hold in its hands at once: A is the main working hand (accumulator), X and Y are helper hands for counting and indexing, SP is a bookmark in a stack of papers, PC is a finger pointing at the current instruction, and P is a mood ring that changes color after every operation.
**Why It Matters:** Your CPU struct's core state is just these 6 fields. Every instruction reads or modifies them, and the flags register P drives all conditional branching — if you get flag behavior wrong, every game's control flow breaks.

---

## ⚙️ Core Mechanics
### How It Works
The CPU maintains six registers. The 8-bit status register P packs seven meaningful flags into a single byte, with bit 5 always set to 1 and bit 4 (B) only existing in the stack-pushed copy.

### Key Specifications

**Registers**

| Register | Size | Purpose |
|----------|------|---------|
| **A** (Accumulator) | 8-bit | Main arithmetic register |
| **X** (Index X) | 8-bit | Indexing, counting, memory transfer |
| **Y** (Index Y) | 8-bit | Indexing, counting |
| **SP** (Stack Pointer) | 8-bit | Points into stack page (0x0100-0x01FF) |
| **PC** (Program Counter) | 16-bit | Next instruction address |
| **P** (Status/Flags) | 8-bit | Condition flags (see below) |

**Status Flags (P Register)**

| Bit | Flag | Name | Set When |
|-----|------|------|----------|
| 7 | N | Negative | Result bit 7 is 1 |
| 6 | V | Overflow | Signed overflow in ADC/SBC |
| 5 | - | Unused | Always 1 |
| 4 | B | Break | BRK instruction (pushed only) |
| 3 | D | Decimal | BCD mode (disabled on NES/2A03) |
| 2 | I | Interrupt | IRQ disabled when set |
| 1 | Z | Zero | Result is zero |
| 0 | C | Carry | Unsigned overflow / borrow |

### Key Facts
- **Stack wraps around** within page 1 (0x01FF → 0x0100)
- **No BCD on NES** — the D flag exists but has no effect (Ricoh disabled it)
- **B flag** is not a real register bit — it only exists in the byte pushed to stack
- **SP initialized to 0xFD** after reset (not 0xFF — the reset sequence does 3 phantom pushes)

---

## 🔬 Deep Dive
### Hardware Behavior Details
**The B Flag Quirk:** B is not a physical flag in the P register. When P is pushed to the stack (by BRK, PHP, or interrupt), bit 4 is set to 1 for BRK/PHP and 0 for hardware interrupts (NMI/IRQ). When P is pulled from the stack (PLP, RTI), bit 4 is ignored. This distinction lets interrupt handlers detect whether they were triggered by BRK or a hardware interrupt.

**Bit 5 Always Set:** When reading P back from the stack (via PLP or RTI), bit 5 is always forced to 1. This is a hardware constant.

**SP After Reset:** The reset sequence performs three stack pushes (PC high, PC low, P) but with the R/W line held high (reads instead of writes), so nothing is actually written — SP just decrements from 0x00 to 0xFD.

### Common Emulation Pitfalls
1. **B flag handling on interrupts vs BRK** — If you always push B=1, interrupt handlers that check the B flag to distinguish BRK from IRQ will malfunction
2. **Forgetting bit 5 on PLP/RTI** — If PLP clears bit 5, flag checks will produce wrong results since bit 5 should always read as 1
3. **SP starting at 0xFF instead of 0xFD** — After reset, SP should be 0xFD due to the three phantom pushes; starting at 0xFF will cause the first real push to overwrite wrong memory

### Reference Implementations
The OxideNES `Cpu` struct stores each register as a field. Flags are stored as a single `u8` with bit manipulation via `get_flag()`/`set_flag()` methods, both marked `#[inline(always)]` since they are called ~1.79M times per second.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. After executing `LDA #$00`, which flags are set and which are cleared in the P register?
2. What happens to the stack pointer when you push a byte — does it increment or decrement, and what is the effective memory address?
3. Why can't you directly test the B flag with a branch instruction during normal execution?

### Core Problems
1. **Implement flag accessors:** Write `get_flag(flag: u8) -> bool` and `set_flag(flag: u8, value: bool)` using bitwise operations on a `u8` status register. Ensure bit 5 is always returned as 1.
2. **Reset sequence:** Implement the CPU reset: load PC from vector 0xFFFC-0xFFFD, set SP to 0xFD, set I flag, and ensure all other registers have correct initial values. What should A, X, Y be?

### Challenge
**BRK vs IRQ distinction:** Write a test where a BRK instruction and an IRQ interrupt both vector to the same handler at 0xFFFE. The handler must distinguish between the two by examining the pushed P register on the stack. Show the exact stack contents for each case and explain the bit 4 difference.

---

*See also:* [[6502 Instruction Set]], [[6502 Addressing Modes]], [[Interrupts — NMI, IRQ, and Reset]], [[CPU — The 6502 Processor Overview]]

## References
→ [[Sources Index]]
