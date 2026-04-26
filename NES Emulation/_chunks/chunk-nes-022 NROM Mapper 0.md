---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-005]]"
up: "[[Common Mappers]]"
---

# Chunk NES 022 — NROM Mapper 0

NROM is the simplest NES mapper with no bank switching. PRG ROM is either 16 KB (mirrored at  and ) or 32 KB (filling - directly). CHR is a fixed 8 KB bank. No registers, no switching logic. Games using NROM include Super Mario Bros., Donkey Kong, and Ice Climber. In OxideNES, the NROM mapper implementation is trivial: cpu_read returns prg_rom[addr - 0x8000] with a modulo for 16 KB mirroring, and ppu_read returns chr_rom[addr] directly. NROM represents the baseline NES hardware capability.
