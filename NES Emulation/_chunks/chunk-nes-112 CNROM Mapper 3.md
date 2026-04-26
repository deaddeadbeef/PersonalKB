---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-005]]"
up: "[[Common Mappers]]"
---

# Chunk NES 112 — CNROM Mapper 3

CNROM (Mapper 3) provides simple CHR bank switching with fixed PRG. PRG ROM is either 16 KB or 32 KB with no switching (like NROM). Writing to - selects which 8 KB CHR bank is mapped to the PPU pattern tables at -. This allows games to have multiple sets of pre-designed tiles and swap them instantly — useful for level-specific graphics, animation frames, or cutscene images. Games include Solomon's Key, Gradius, and Paperboy. In OxideNES, the CNROM mapper stores a single bank register and multiplies by 8192 for the CHR offset calculation.
