---
tags: [chunk, nes-emulation, tas]
source: "[[raw-nes-030]]"
up: "[[Input Recording and TAS]]"
---

# Chunk NES 073 — TAS Input Recording Format

OxideNES records TAS inputs in a compact binary format. The 16-byte header contains format version (2 bytes), ROM CRC32 (4 bytes), total frame count (4 bytes), re-record count (4 bytes), and flags (2 bytes). Per-frame data is 2 bytes: player 1 input plus player 2 input. A typical 5-minute TAS at 60 FPS produces approximately 36 KB. When loading a save state during recording, the input log truncates to that frame number and the re-record counter increments. Competitive TAS typically involves thousands of re-records as each section is optimized for frame-perfect execution.
