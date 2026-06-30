---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: plausible
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

## References

→ [[Sources Index]]
