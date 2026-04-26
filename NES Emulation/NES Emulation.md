---
tags: [moc, nes-emulation]
---

# NES Emulation

A comprehensive knowledge base covering NES hardware theory and emulation practice, with OxideNES (a cycle-accurate Rust NES emulator) as the concrete implementation reference.

> 📚 **New here?** Start with the [[NES Emulation — Learning Path|Learning Path]] for a guided, progressive tour.

## Wiki Statistics

| Metric | Count |
|--------|-------|
| Domain Pages | 50 |
| Raw Notes | 30 |
| Chunks | 120 |
| Study Files | 6 |
| Total Files | ~213 |

## Domain Hubs

### Hardware
- [[NES Hardware Overview]] — Console architecture, specs, history, comparisons
- [[CPU — The 6502 Processor Overview]] — Registers, addressing, instruction set, interrupts, timing
- [[PPU — Picture Processing Unit Overview]] — Rendering pipeline, backgrounds, sprites, scrolling, registers
- [[APU — Audio Processing Unit Overview]] — Pulse, triangle, noise, DMC, frame sequencer

### System
- [[Memory Map and Bus Overview]] — CPU/PPU address spaces, OAM DMA
- [[Cartridges and Mappers Overview]] — iNES format, bank switching, NROM through MMC5
- [[Input and Controllers Overview]] — Joypad protocol, OxideNES controller features

### Emulation
- [[CRT Simulation Overview]] — 7-stage rendering pipeline for authentic retro display
- [[Emulator Architecture Overview]] — Main loop, save states, rewind, performance
- [[Extended Features Overview]] — Netplay, Lua scripting, achievements, TAS support

## Infrastructure

- [[Sources Index]] — Primary sources and raw material catalog
- [[NES Emulation Study Index]] — Review drills and cheatsheets
