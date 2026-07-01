---
tags: [moc, nes-emulation]
up: "[[Welcome]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# NES Emulation

A comprehensive knowledge base covering NES hardware theory and emulation practice, with OxideNES (a cycle-accurate Rust NES emulator) as the concrete implementation reference.

## Start Here

| Need | Open | Why |
|---|---|---|
| Read NES emulation like a book | [[NES Emulation/NES Emulation Book Reading Spine|NES Emulation Book Reading Spine]] | Curated reconstruction path through hardware, CPU, PPU, APU, memory, mappers, and architecture |
| Follow a guided course path | [[NES Emulation/NES Emulation — Learning Path|NES Emulation Learning Path]] | Progressive tour through the emulator domain |
| Debug or review implementation knowledge | [[NES Emulation/Study/NES Emulation Study Index|NES Emulation Study Index]] | Goal router from symptom to subsystem, review drills, and proof targets |
| Check provenance | [[NES Emulation/Sources/Sources Index|NES Emulation Sources Index]] | Source map for hardware and emulator references |
| Browse the catalog | This page below | Domain hubs, infrastructure, and references |

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

- [[NES Emulation/Sources/Sources Index|Sources Index]] — Primary sources and raw material catalog
- [[NES Emulation Study Index]] — Review drills and cheatsheets

## References

- [[Welcome]]
- [[NES Emulation/NES Emulation Book Reading Spine]]
- [[NES Emulation/Sources/Sources Index]]
