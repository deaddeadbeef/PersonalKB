---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-005]]"
up: "[[Common Mappers]]"
---

# Chunk NES 102 — MMC2 Latch-Triggered CHR Switching

MMC2 (Mapper 9) and MMC4 (Mapper 10) feature a unique latch-triggered CHR bank switching mechanism designed specifically for Punch-Out!! The PPU pattern table fetches are monitored for specific tile indices. When tiles  or  are fetched, the mapper automatically swaps CHR banks — enabling smooth animation of large sprites without CPU involvement. OxideNES tracks PPU tile fetches and triggers bank switches at the exact cycle of the latch tile read. This mapper is only used by a few games but demonstrates the creative possibilities of the NES mapper architecture.
