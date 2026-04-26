---
tags: [chunk, nes-emulation, savestate]
source: "[[raw-nes-010]]"
up: "[[Save States and Rewind]]"
---

# Chunk NES 034 — Save State Serialization

Save states capture the complete emulation state via serde with bincode format: CPU registers and cycle counter, PPU VRAM/OAM/palette/scroll registers and timing position, APU channel states and frame sequencer, bus RAM and DMA state, mapper bank registers and IRQ counters, and cartridge battery RAM. Typical size is 10-15 KB compressed with zstd. Ten slots (F1-F10 to load, Shift+F1-F10 to save) are stored per ROM CRC32. States include a version number checked on load to reject incompatible formats. Edge cases like mid-DMA state and mid-scanline PPU position are fully preserved.
