---
tags: [chunk, nes-emulation, cpu]
source: "[[raw-nes-011]]"
up: "[[6502 Addressing Modes]]"
---

# Chunk NES 093 — JMP Indirect Page Boundary Bug

The JMP indirect instruction has a famous hardware bug. When the pointer address ends in  (e.g., JMP ()), the low byte of the target is read from  correctly, but the high byte wraps within the page — reading from  instead of . This occurs because the 6502 increments only the low byte of the pointer address without carrying into the high byte. OxideNES emulates this bug faithfully: the indirect address fetch masks the increment to the low byte. While only JMP uses indirect addressing on the 6502, this bug affected real NES games and must be replicated.
