---
tags: [chunk, nes-emulation, pattern]
source: "[[raw-nes-018]]"
up: "[[Cartridges and Mappers Overview]]"
---

# Chunk NES 052 — CHR ROM vs CHR RAM

Pattern table data can be stored as CHR ROM (read-only tiles burned into the cartridge chip, bank-switched by the mapper) or CHR RAM (8 KB writable memory on the cartridge, populated by the CPU through PPU registers). Most NES games use CHR ROM for pre-designed tiles with mapper banking for animation. CHR RAM games (Mapper 2 titles like Mega Man, Castlevania) dynamically write tile data, enabling procedurally generated or modified graphics. OxideNES detects CHR type from the iNES header (CHR ROM size = 0 indicates CHR RAM) and allocates accordingly.
