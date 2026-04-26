---
tags: [raw, nes-emulation, addressing]
source: "6502 reference manual + OxideNES cpu.rs"
---

# Raw NES 011 — 6502 Addressing Modes Deep Dive

The MOS 6502 processor uses 13 addressing modes that determine how the operand for each instruction is located. Understanding these modes is essential for NES programming and emulation accuracy.

## Immediate (#nn)

The operand is the byte immediately following the opcode. Example: LDA #$42 loads the literal value 0x42 into A. In OxideNES, this simply reads self.read(self.pc + 1). 2 bytes, 2 cycles.

## Zero Page ($nn)

The operand address is a single byte, addressing the first 256 bytes of memory ($0000-$00FF). Example: LDA $42 loads from address $0042. The zero page was designed as a fast-access area — instructions are shorter (2 bytes vs 3) and faster (3 cycles vs 4) than absolute addressing. NES games heavily use zero page for frequently accessed variables.

## Zero Page,X and Zero Page,Y ($nn,X / $nn,Y)

Like zero page but the index register is added to the address, wrapping within the zero page (no carry into high byte). LDA $80,X with X=3 loads from $0083. If X=0x90 and base is $80, the address wraps to $0010 (not $0110). This wrapping is a common source of emulation bugs. 2 bytes, 4 cycles.

## Absolute ($nnnn)

A full 16-bit address follows the opcode in little-endian format. LDA $1234 loads from address $1234. 3 bytes, 4 cycles. This is the general-purpose mode for accessing any address.

## Absolute,X and Absolute,Y ($nnnn,X / $nnnn,Y)

The 16-bit address is added to the index register. If the addition crosses a page boundary (high byte changes), an extra cycle is added for read instructions. Write instructions always take the extra cycle because the CPU does a dummy read of the wrong address first. LDA $1200,X with X=0xFF reads from $12FF (no penalty) or $1300 (with penalty if crossed). 3 bytes, 4+ cycles.

## Indirect ($nnnn)

Only used by JMP. The 16-bit address points to a location containing the actual jump target (little-endian). JMP ($1234) reads the low byte from $1234 and high byte from $1235 to form the target PC. Bug: if the pointer is at a page boundary ($xxFF), the high byte wraps within the page — JMP ($10FF) reads low from $10FF and high from $1000, NOT $1100. This hardware bug must be emulated. 3 bytes, 5 cycles.

## Indexed Indirect (($nn,X))

A zero page address + X gives a pointer location (wrapping in zero page). The 16-bit address at that location is the effective address. LDA ($20,X) with X=4 reads the pointer from $0024/$0025. Used for array-of-pointers patterns. 2 bytes, 6 cycles.

## Indirect Indexed (($nn),Y)

A zero page address gives a base pointer. The 16-bit address at that location + Y is the effective address. LDA ($20),Y reads the pointer from $0020/$0021, adds Y. Page-cross penalty applies for reads. This is the most common addressing mode for accessing data structures and screen buffers. 2 bytes, 5+ cycles.

## Relative (for branches)

Branch instructions use a signed 8-bit offset from the instruction following the branch. Range is -128 to +127 bytes. If the branch is taken, 1 extra cycle. If the branch crosses a page boundary, 1 more extra cycle. Branches are 2 bytes, 2/3/4 cycles depending on taken/page-cross.