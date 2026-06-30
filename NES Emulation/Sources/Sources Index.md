---
tags: [sources, nes-emulation]
up: "[[NES Emulation]]"
confidence: verified
---
# Sources Index — NES Emulation

## Primary Sources

| Source | Type | Description |
|--------|------|-------------|
| OxideNES Source Code | Codebase | Rust NES emulator at C:\Users\fpan1\nes-emulator (~15,700 lines) |
| NESdev Wiki | Reference | Community hardware documentation (nesdev.org) |
| nestest.nes | Test ROM | CPU validation ROM by kevtris |
| MOS 6502 Programming Manual | Manual | Original MOS Technology 6502 reference |
| Blargg's Test ROMs | Test Suite | PPU, APU, and mapper accuracy tests |

## Raw Notes

| Note | Topic | Key Content |
|------|-------|-------------|
| [[raw-nes-001]] | 6502 CPU Core | Registers, decoding, cycle accuracy, interrupts |
| [[raw-nes-002]] | PPU Rendering Pipeline | Scanline types, BG/sprite fetch, registers |
| [[raw-nes-003]] | APU Channels | Pulse, triangle, noise, DMC, frame sequencer, mixing |
| [[raw-nes-004]] | Bus and Memory Map | CPU/PPU address spaces, mirroring, DMA, timing |
| [[raw-nes-005]] | Mapper System | Bank switching, NROM, MMC1, UxROM, MMC3, advanced mappers |
| [[raw-nes-006]] | CRT Simulation | 7-stage pipeline: upscale, phosphor, gamma, scanlines, distortion |
| [[raw-nes-007]] | Netplay Protocol | UDP lockstep, input delay, desync detection |
| [[raw-nes-008]] | Lua Scripting | API surface, callbacks, sandboxing, use cases |
| [[raw-nes-009]] | Achievement System | JSON conditions, DNF evaluation, persistence |
| [[raw-nes-010]] | Save States and Rewind | Serde/bincode, slots, ring buffer rewind |
| [[raw-nes-011]] | 6502 Addressing Modes | All 13 modes, page crossing, JMP bug |
| [[raw-nes-012]] | PPU Scrolling | Loopy registers, t-to-v copies, split scrolling |
| [[raw-nes-013]] | 6502 Instruction Set | All official instructions by category |
| [[raw-nes-014]] | Sprite Rendering | OAM format, evaluation, overflow bug, sprite-0 hit |
| [[raw-nes-015]] | Performance Optimization | CPU/PPU optimizations, LUTs, zero allocation |
| [[raw-nes-016]] | Input System | Keyboard, gamepad, rebinding, turbo, recording |
| [[raw-nes-017]] | Nametables and Mirroring | Structure, mirroring modes, attribute table |
| [[raw-nes-018]] | Pattern Tables | Tile encoding, 2-bit planar, CHR ROM vs RAM |
| [[raw-nes-019]] | iNES ROM Format | Header format, flags, NES 2.0 extensions |
| [[raw-nes-020]] | Timing System | Master clock, dividers, frame timing, audio sync |
| [[raw-nes-021]] | Color Palette | NTSC signal, RGB approximation, emphasis, palette RAM |
| [[raw-nes-022]] | MMC3 Deep Dive | Bank registers, A12 IRQ, CHR/PRG modes |
| [[raw-nes-023]] | NES Hardware History | Timeline, design philosophy, regional differences |
| [[raw-nes-024]] | Expansion Audio | VRC6, VRC7, Namco 163, Sunsoft 5B, mixing |
| [[raw-nes-025]] | 8-bit Console Comparison | NES vs SMS, 7800, C64, emulation difficulty |
| [[raw-nes-026]] | MMC1 Deep Dive | Serial register, banking modes, edge cases |
| [[raw-nes-027]] | Module Architecture | Source layout, dependency graph, traits, build config |
| [[raw-nes-028]] | Test ROMs | nestest, PPU/APU tests, mapper tests, strategy |
| [[raw-nes-029]] | DMA Mechanisms | OAM DMA timing, DMC DMA stalls, interactions |
| [[raw-nes-030]] | TAS Support | Input recording, frame advance, determinism |

## References
- [[NES Emulation/Sources/Sources Index|NES Emulation Sources Index]]
