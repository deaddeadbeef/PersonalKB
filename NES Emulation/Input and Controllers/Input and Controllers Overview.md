---
tags: [nes, hub]
up: "[[NES Emulation]]"
---

# Input and Controllers Overview

The NES controller is a simple but elegant input device with a D-pad, two action buttons (A, B), and two meta buttons (Start, Select). The console communicates with controllers via a serial shift register protocol.

## Pages

- [[NES Joypad Protocol]] — The serial interface for reading button state
- [[Controller Features in OxideNES]] — Turbo buttons, input remapping, gamepad support

## Key Facts

- **8 buttons** per controller: A, B, Select, Start, Up, Down, Left, Right
- **Serial protocol:** Strobe latch + 8-bit shift register
- **Two controller ports** addressed at CPU 0x4016 and 0x4017
- **Turbo buttons** implemented in OxideNES (toggle at 30 Hz)

## OxideNES Implementation

joypad.rs (86 lines): Minimal and clean implementation of the NES serial protocol. Main.rs handles keyboard/gamepad input mapping via configurable bindings.

## References

→ [[Sources Index]]
