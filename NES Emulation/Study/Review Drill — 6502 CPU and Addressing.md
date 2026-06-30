---
tags: [study, nes-emulation, cpu]
up: "[[NES Emulation Study Index]]"
confidence: policy
---
# Review Drill — 6502 CPU and Addressing

Test your understanding of the MOS 6502 processor as implemented in the NES.

## Questions

**Q1:** Name all six 6502 registers and their sizes.
> A, X, Y (8-bit each), SP (8-bit, stack pointer into page -), PC (16-bit, program counter), P (8-bit, status flags: N V - B D I Z C)

**Q2:** What happens when a Zero Page,X address calculation overflows past 
> It wraps within the zero page.  +  =  (not ). Only the low byte is used — there is no carry into the high byte. This is a common source of emulation bugs.

**Q3:** Explain the JMP indirect bug at page boundaries.
> When JMP () is executed, the low byte of the target is read from , but the high byte wraps within the page — reading from  instead of 00. The 6502 only increments the low byte of the pointer address.

**Q4:** How does OxideNES detect page-crossing penalties efficiently?
> By checking (base AND ) + index >  — a single low-byte comparison without computing the full 16-bit address. Read instructions add 1 cycle on crossing; write instructions always take the penalty.

**Q5:** What is the difference between NMI and IRQ interrupt handling?
> NMI is edge-triggered (fires on signal transition) with highest priority, asserted by PPU at VBlank. IRQ is level-triggered and masked by the I flag. Both push PC and P to the stack (7 cycles) and load from their respective vectors ( for NMI,  for IRQ).

**Q6:** How does OxideNES achieve cycle-accurate CPU emulation?
> A remaining_cycles counter is set to the instruction's base cycle count. The bus calls cpu.tick() each master clock; the CPU only executes when the counter reaches zero. Page-cross and branch penalties are added dynamically.

**Q7:** Name four commonly-emulated unofficial opcodes and what they do.
> LAX (LDA + LDX combined), SAX (store A AND X), DCP (DEC + CMP), ISB (INC + SBC). Others: SLO (ASL + ORA), RLA (ROL + AND), SRE (LSR + EOR), RRA (ROR + ADC).

**Q8:** Why does the NES not implement BCD (decimal) mode despite the D flag existing?
> Ricoh disabled BCD arithmetic in the 2A03 to avoid patent royalties to MOS Technology. The D flag can be set/cleared but has no effect on ADC/SBC operations.

## References
- [[NES Emulation/Sources/Sources Index|NES Emulation Sources Index]]
