---
tags: [nes, wiki]
up: "[[CPU — The 6502 Processor Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# 6502 Addressing Modes

> **The 13 ways the 6502 CPU locates data in memory, from simple register operations to complex indirect pointer lookups.**

## 🎯 Intuition
**The Core Idea:** Addressing modes are the CPU's vocabulary for describing *where* data lives — each mode is a different strategy for computing an effective memory address from the instruction bytes.
**Analogy:** Think of addressing modes as different ways to give someone directions: "it's in your hand" (Accumulator), "it's at house #42" (Absolute), "it's at the house 3 doors down from #42" (Indexed), or "look up the address written on the note at house #42, then go there" (Indirect).
**Why It Matters:** Every CPU instruction uses an addressing mode — your emulator's `get_operand_address()` function will be called millions of times per second, so getting all 13 modes correct (including edge cases like zero-page wrapping and the JMP indirect bug) is foundational.

---

## ⚙️ Core Mechanics
### How It Works
The CPU reads an opcode byte, which determines both the operation and the addressing mode. Depending on the mode, it then reads 0, 1, or 2 additional bytes to compute the effective address where the operand is found.

### Key Specifications

| Mode | Syntax | Bytes | Example | Description |
|------|--------|-------|---------|-------------|
| Implicit | - | 1 | CLC | Operand implied by opcode |
| Accumulator | A | 1 | ASL A | Operates on A register |
| Immediate | #nn | 2 | LDA #$42 | Operand is the next byte |
| Zero Page | nn | 2 | LDA $00 | Address in page zero (0x00-0xFF) |
| Zero Page,X | nn,X | 2 | LDA $00,X | Zero page + X (wraps within page) |
| Zero Page,Y | nn,Y | 2 | LDX $00,Y | Zero page + Y (wraps within page) |
| Relative | offset | 2 | BEQ $05 | PC + signed offset (branches only) |
| Absolute | nnnn | 3 | LDA $8000 | Full 16-bit address |
| Absolute,X | nnnn,X | 3 | LDA $8000,X | Base + X with page-cross penalty |
| Absolute,Y | nnnn,Y | 3 | LDA $8000,Y | Base + Y with page-cross penalty |
| Indirect | (nnnn) | 3 | JMP ($FFFE) | JMP only; reads address from pointer |
| Indirect,X | (nn,X) | 2 | LDA ($40,X) | Indexed indirect (pointer in ZP+X) |
| Indirect,Y | (nn),Y | 2 | LDA ($40),Y | Indirect indexed (pointer in ZP, +Y) |

### Key Facts
- Zero Page modes wrap within page zero (address & 0xFF) — they never cross into page 1
- Immediate mode means the operand IS the byte after the opcode, not an address
- Relative addressing is only used by branch instructions and uses a signed 8-bit offset (-128 to +127)
- Indirect addressing on the 6502 is only available to JMP

---

## 🔬 Deep Dive
### Hardware Behavior Details
**Page-Crossing Penalty:** When Absolute,X, Absolute,Y, or Indirect,Y addressing crosses a page boundary (high byte changes), an extra cycle is added. The check is `(base & 0xFF00) != (effective & 0xFF00)`. This penalty is critical for cycle-accurate emulation.

**The JMP Indirect Bug:** The 6502 has a famous hardware bug: `JMP ($xxFF)` wraps within the page instead of crossing it. If the pointer is at 0x02FF, the high byte is read from 0x0200, not 0x0300. This is not a quirk to ignore — it must be faithfully replicated.

**Zero-Page Wrapping:** Zero Page,X and Zero Page,Y wrap within the zero page. `LDA $FF,X` with X=1 reads from 0x0000, not 0x0100. Indirect,X also wraps: the pointer address calculation stays within the zero page.

### Common Emulation Pitfalls
1. **Forgetting zero-page wrapping** — If ZP+X overflows past 0xFF into page 1, games using ZP indexed modes will read wrong data and crash
2. **Missing the page-cross cycle penalty** — Cycle-sensitive games (especially those using sprite 0 hit timing) will glitch if Absolute,X reads don't cost the extra cycle when crossing pages
3. **Not replicating the JMP indirect bug** — Some games and test ROMs depend on this exact behavior; wrapping JMP ($xxFF) correctly is a common test of emulator accuracy

### Reference Implementations
The `get_operand_address()` method in OxideNES cpu.rs handles all 13 modes via an `AddressingMode` enum match. The page-crossing check compares `(base & 0xFF00) != (effective & 0xFF00)` and adds a cycle penalty when true. The JMP indirect bug is faithfully replicated.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. How many additional bytes does the CPU read for an Absolute,X instruction, and what are they used for?
2. Why do Zero Page addressing modes exist when Absolute modes can address the same locations?
3. What is the difference between Indirect,X (indexed indirect) and Indirect,Y (indirect indexed) in terms of when the index register is applied?

### Core Problems
1. **Implement `get_operand_address()`:** Write a function that takes an `AddressingMode` enum and the current CPU state, and returns the effective address plus a boolean indicating whether a page boundary was crossed.
2. **Page-cross detection:** Given base address 0x10FF and X register = 0x01, trace through the Absolute,X address calculation. What is the effective address? Does a page cross occur? How many extra cycles are added?

### Challenge
**The JMP Indirect Bug:** Write a test that sets memory[0x02FF] = 0x80 and memory[0x0200] = 0x40 (note: NOT memory[0x0300]). Execute `JMP ($02FF)`. Verify PC becomes 0x4080, not 0x??80 where ?? comes from 0x0300. Then explain why some games might actually rely on this bug.

---

*See also:* [[6502 Instruction Set]], [[6502 Registers and Status Flags]], [[CPU Cycle Accuracy and Timing]], [[CPU — The 6502 Processor Overview]]

## References
→ [[Sources Index]]
