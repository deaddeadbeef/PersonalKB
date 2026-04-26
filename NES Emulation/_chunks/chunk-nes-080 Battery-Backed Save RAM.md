---
tags: [chunk, nes-emulation, mapper]
source: "[[raw-nes-005]]"
up: "[[Cartridges and Mappers Overview]]"
---

# Chunk NES 080 — Battery-Backed Save RAM

Mappers supporting battery-backed SRAM expose an 8 KB window at - for persistent game saves. MMC1 and MMC3 are the most common mappers with this feature, used by games like Zelda, Final Fantasy, and Kirby's Adventure. OxideNES persists save RAM to disk at the config directory path ~/.nes-emulator/saves/<rom-crc32>.sav. The file is loaded when the ROM is opened and written on emulator exit. The PRG bank register can disable this RAM region, though most games leave it enabled throughout gameplay. Save RAM state is also included in save state snapshots.
