---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-005]]"
up: "[[Advanced Mappers]]"
---

# Chunk NES 101 — MMC5 Expansion Features

MMC5 (Mapper 5) is the most complex NES mapper, featuring: extended attribute mode allowing per-tile palette selection (bypassing the 2x2 attribute limitation), 1 KB of ExRAM for extra nametable data, 8x8-to-8x16 sprite mode switching, advanced PRG banking with 8 KB granularity up to 1 MB, and expansion audio with two extra pulse channels and a PCM channel. OxideNES implements the core MMC5 features including ExRAM modes and expansion audio. Used by Castlevania III (US), Laser Invasion, and Just Breed, though relatively few games used MMC5 due to its high cost.
