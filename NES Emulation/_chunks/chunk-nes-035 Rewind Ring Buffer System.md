---
tags: [chunk, nes-emulation, savestate]
source: "[[raw-nes-010]]"
up: "[[Save States and Rewind]]"
---

# Chunk NES 035 — Rewind Ring Buffer System

The rewind system automatically saves compressed state snapshots every 2 frames into a ring buffer (default 300 entries, providing about 10 seconds of rewind at 60 FPS). When the user holds the rewind key, states are popped from the buffer and restored in reverse, rendering each frame backwards. The ring buffer uses the ringbuf crate for efficient circular operations. Total memory usage is approximately 300 x 12 KB = 3.6 MB. Rewind is disabled during netplay to prevent desync. The snapshot interval and buffer size are configurable in emulator settings.
