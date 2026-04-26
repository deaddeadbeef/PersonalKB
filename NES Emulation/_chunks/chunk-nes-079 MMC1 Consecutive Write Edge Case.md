---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-026]]"
up: "[[Common Mappers]]"
---

# Chunk NES 079 — MMC1 Consecutive Write Edge Case

MMC1 has an important edge case: consecutive writes to the serial register on consecutive CPU cycles should be ignored — the second write is eaten by the shift register logic. OxideNES tracks the last write cycle to detect and discard these back-to-back writes. This behavior matters for a small number of games that intentionally or accidentally perform consecutive writes to the mapper address range. The bit-7 reset also has precise timing requirements: writing with bit 7 set immediately resets the shift register and forces PRG mode 3 (fixed last bank) regardless of shift register state.
