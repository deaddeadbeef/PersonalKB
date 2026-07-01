---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
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

## How To Read This Chapter

Read this chapter for controller protocol and input latency. NES emulation is less about isolated facts than about making several small timed machines agree on the same frame. The overview pages should give you the vocabulary first, then route you into the detailed pages where timing, registers, and test-ROM behavior matter.

A productive pass has three questions. First, what state does this subsystem own? Second, which reads or writes have side effects? Third, what timing relationship can break a game if it is off by even a few CPU or PPU cycles? Keep those questions nearby while reading the linked pages.

## Emulator Checkpoints

Use the deeper notes to turn the concept into implementation proof. The key checkpoints for this chapter are: shift-register polling, strobe semantics, zapper timing, expansion devices, and frontend event mapping. For each checkpoint, prefer a tiny deterministic test before a visual game test. A passing screenshot is useful, but a focused trace is better when the bug is cycle timing, flag behavior, mapper state, or register side effects.

The chapter is mastered when you can explain both the user-visible symptom and the internal cause of a failure. For example, audio pops, scrolling seams, wrong sprite priority, broken controller input, or a mapper crash should point back to a specific piece of state and a specific clock boundary.

## References

→ [[NES Emulation/Sources/Sources Index|Sources Index]]
