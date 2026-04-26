---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-005]]"
up: "[[Bank Switching Explained]]"
---

# Chunk NES 021 — Why Bank Switching Exists

The NES CPU can address only 32 KB of PRG ROM (-) and the PPU only 8 KB of CHR (-). Games exceeding these limits use mappers — custom hardware on the cartridge PCB that dynamically remaps different ROM sections into the address windows. This bank switching lets a 512 KB game expose different 16 KB or 32 KB chunks to the CPU as needed. OxideNES supports 20 mappers covering the vast majority of the commercial NES library, each implemented as a struct fulfilling the Mapper trait.
