---
tags: [chunk, nes-emulation, addressing]
source: "[[raw-nes-011]]"
up: "[[6502 Addressing Modes]]"
---

# Chunk NES 036 — Zero Page and Immediate Addressing

Immediate addressing (#nn) uses the byte following the opcode as the literal operand — 2 bytes, 2 cycles. Zero Page addressing () uses a single byte to address -, the first 256 bytes of memory. Zero page instructions are shorter (2 bytes vs 3) and faster (3 cycles vs 4) than absolute equivalents. NES games heavily use zero page for frequently accessed variables like player position, counters, and temporary values. Zero Page,X and Zero Page,Y add the index register with wrap-around within zero page — + wraps to , not . This wrapping is a common source of emulation bugs.
