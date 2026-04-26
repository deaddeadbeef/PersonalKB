---
tags: [chunk, nes-emulation, input]
source: "[[raw-nes-016]]"
up: "[[Controller Features in OxideNES]]"
---

# Chunk NES 047 — Input System Architecture

Controller state is internally represented as an 8-bit bitmask matching NES hardware order: A (bit 0), B (bit 1), Select (bit 2), Start (bit 3), Up (bit 4), Down (bit 5), Left (bit 6), Right (bit 7). All input sources — keyboard, gamepad, Lua script overrides, and netplay — produce this same format. Default keyboard: arrows for D-pad, Z/X for A/B, Right Shift/Enter for Select/Start. The gilrs crate provides cross-platform gamepad support with auto-detection, configurable dead zones for analog-to-digital conversion, and hot-plugging. Turbo mode toggles A/B every other frame at 30 Hz.
