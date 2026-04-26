---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-022]]"
up: "[[Advanced Mappers]]"
---

# Chunk NES 098 — MMC3 Mirroring and PRG RAM Control

MMC3 supports dynamic nametable mirroring: writing to $A000 selects horizontal (bit 0 clear) or vertical (bit 0 set) mirroring. This allows games to change scrolling direction dynamically — switching between horizontal and vertical scrolling segments mid-game. Writing to $A001 controls PRG RAM at $6000-$7FFF: enabling or disabling access, and optionally write-protecting it to prevent accidental corruption. These features combined with the scanline IRQ counter and fine-grained banking make MMC3 the most versatile common NES mapper, explaining its use in over 250 commercial games.
