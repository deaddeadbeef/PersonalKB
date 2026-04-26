---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-005]]"
up: "[[Common Mappers]]"
---

# Chunk NES 113 — AxROM Mapper 7

AxROM (Mapper 7) switches a full 32 KB PRG bank at once and controls single-screen mirroring. Writing to - selects the 32 KB PRG bank (bits 0-2) and the nametable page (bit 4). Single-screen mirroring means all four logical nametables map to one physical nametable — either the lower or upper bank, selected by the mapper. This simplifies scrolling logic for games that only need one screen visible at a time. Used by Battletoads, Marble Madness, and Wizards and Warriors. The 32 KB granularity limits PRG size versus finer-grained mappers but simplifies the banking logic.
