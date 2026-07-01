---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
---
# Emulator Architecture Overview

OxideNES is a cycle-accurate NES emulator written in Rust, designed for both accuracy and performance. The architecture follows a modular design with the Bus as central coordinator.

## Pages

- [[Main Loop and Cycle Ratios]] — The emulation timing core
- [[Save States and Rewind]] — State capture and time-travel mechanics
- [[Performance Optimization in OxideNES]] — Rust-specific techniques and measured results
- [[OxideNES Module Architecture]] — How the source code is organized

## Key Facts

- **Language:** Rust 2021 edition
- **~15,700 lines** of Rust across 15 source files
- **Dependencies:** minifb (window), cpal (audio), gilrs (gamepad), mlua (Lua), serde (config)
- **Release profile:** LTO enabled, single codegen unit, stripped binaries
- **Test suite:** 102 functional tests across all modules

## Design Principles

1. **Accuracy first** — Cycle-accurate PPU/CPU/APU synchronization
2. **Performance** — Strategic inlining, unsafe bounds elision, SWAR techniques
3. **Modularity** — Clean separation of CPU, PPU, APU, Bus, Mapper
4. **Zero-cost abstractions** — Enum dispatch instead of trait objects for mappers

## How To Read This Chapter

Read this chapter for whole-emulator structure. NES emulation is less about isolated facts than about making several small timed machines agree on the same frame. The overview pages should give you the vocabulary first, then route you into the detailed pages where timing, registers, and test-ROM behavior matter.

A productive pass has three questions. First, what state does this subsystem own? Second, which reads or writes have side effects? Third, what timing relationship can break a game if it is off by even a few CPU or PPU cycles? Keep those questions nearby while reading the linked pages.

## Emulator Checkpoints

Use the deeper notes to turn the concept into implementation proof. The key checkpoints for this chapter are: scheduler design, bus ownership, determinism, save states, testing hooks, and separation between core and frontend. For each checkpoint, prefer a tiny deterministic test before a visual game test. A passing screenshot is useful, but a focused trace is better when the bug is cycle timing, flag behavior, mapper state, or register side effects.

The chapter is mastered when you can explain both the user-visible symptom and the internal cause of a failure. For example, audio pops, scrolling seams, wrong sprite priority, broken controller input, or a mapper crash should point back to a specific piece of state and a specific clock boundary.

## References

→ [[NES Emulation/Sources/Sources Index|Sources Index]]
