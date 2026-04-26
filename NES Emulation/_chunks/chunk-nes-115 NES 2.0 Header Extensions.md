---
tags: [chunk, nes-emulation, ines]
source: "[[raw-nes-019]]"
up: "[[iNES ROM Format]]"
---

# Chunk NES 115 — NES 2.0 Header Extensions

NES 2.0 extends the iNES header for modern needs. It provides a 12-bit mapper number (vs 8-bit), 4-bit submapper for mapper variants, extended PRG/CHR ROM sizes using exponent-plus-multiplier format for ROMs larger than 4 MB, separate fields for volatile and non-volatile PRG/CHR RAM sizes, and explicit CPU/PPU timing mode selection (NTSC, PAL, Multi-region, Dendy). Detection uses bits 2-3 of flags 7 equaling binary 10. OxideNES detects NES 2.0 and parses extended fields when present, falling back gracefully to iNES 1.0 interpretation for standard ROMs.
