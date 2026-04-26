---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-005]]"
up: "[[Common Mappers]]"
---

# Chunk NES 023 — UxROM Mapper 2

UxROM provides simple switchable PRG banking. Writing to - selects which 16 KB PRG bank appears at -; the last 16 KB bank is permanently fixed at -. CHR uses 8 KB of RAM (no ROM banking). This design is elegant in its simplicity — one write switches the entire lower bank. Games include Mega Man, Castlevania, and Contra. OxideNES stores the selected bank number and computes the ROM offset as bank_number * 0x4000 + (addr - 0x8000) for the switchable region.
