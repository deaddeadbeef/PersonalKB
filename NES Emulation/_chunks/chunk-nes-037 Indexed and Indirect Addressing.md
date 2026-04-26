---
tags: [chunk, nes-emulation, addressing]
source: "[[raw-nes-011]]"
up: "[[6502 Addressing Modes]]"
---

# Chunk NES 037 — Indexed and Indirect Addressing

Absolute,X/Y addressing adds an index register to a 16-bit base address. Read instructions gain an extra cycle only on page boundary crossings; write instructions always take the penalty due to a dummy read at the incorrect address. Indexed Indirect ((,X)) computes a zero-page pointer location then reads the 16-bit effective address from there — used for array-of-pointer patterns (6 cycles). Indirect Indexed ((),Y) reads a base pointer from zero page then adds Y — the most common mode for data structure and screen buffer access (5+ cycles with page-cross penalty). The JMP indirect bug at page boundaries ( wraps within page) must be emulated.
