---
tags: [nes, wiki]
up: "[[Emulator Architecture Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# OxideNES Module Architecture

> **OxideNES is organized around a central Bus that coordinates core chip emulators and optional plugin-style subsystems.**

## 🎯 Intuition
**The Core Idea:** A single Bus coordinates CPU, PPU, APU, cartridge logic, and controller input while optional subsystems plug into the application layer around that core.
**Analogy:** Like a PC motherboard connecting processors, memory, and expansion slots: the board is the hub, and everything meaningful routes through it.
**Why It Matters:** This structure is the fastest way to navigate a 15,000+ line codebase, because it tells you which modules own hardware behavior and which ones are peripheral systems.

---

## ⚙️ Core Mechanics
### How It Works
`main.rs` owns the application layer and constructs the emulator's top-level systems. The Bus in `bus.rs` is the central coordinator. The CPU reads and writes through the Bus, the PPU reads CHR data through the Cartridge, the APU performs DMC reads through the Bus, and optional subsystems such as netplay, scripting, achievements, recording, ROM database lookup, and updating sit alongside the core hardware path.

### Key Specifications

| File | Lines | Responsibility |
|------|-------|---------------|
| main.rs | 7,572 | Application, UI, CRT, input, menus |
| mapper.rs | 3,213 | 20 mapper implementations |
| cpu.rs | 1,670 | 6502 CPU emulation |
| apu.rs | 973 | Audio processing (5 channels) |
| ppu.rs | 781 | Picture processing unit |
| netplay.rs | 491 | UDP multiplayer |
| achievements.rs | 482 | Achievement system |
| recording.rs | 372 | Input recording/playback |
| bus.rs | 351 | Memory bus arbitration |
| scripting.rs | 174 | Lua scripting engine |
| cartridge.rs | 171 | ROM loading and parsing |
| romdb.rs | 114 | ROM database |
| joypad.rs | 86 | Controller input |
| updater.rs | 80 | Auto-update checker |
| lib.rs | 14 | Module exports |

```
main.rs
  └── Bus (bus.rs) — central coordinator
        ├── Cpu (cpu.rs) — reads/writes through Bus
        ├── Ppu (ppu.rs) — reads CHR via Cartridge
        ├── Apu (apu.rs) — DMC reads through Bus
        ├── Cartridge (cartridge.rs)
        │     └── MapperEnum (mapper.rs)
        └── Joypad x2 (joypad.rs)
  └── Plugins (optional subsystems)
        ├── NetplaySession (netplay.rs)
        ├── ScriptEngine (scripting.rs)
        ├── AchievementEngine (achievements.rs)
        ├── InputRecording (recording.rs)
        ├── RomDatabase (romdb.rs)
        └── Updater (updater.rs)
```

| Crate | Purpose |
|-------|---------|
| minifb | Window creation and framebuffer display |
| cpal | Cross-platform audio output |
| gilrs | Gamepad/controller input |
| mlua | Lua 5.4 scripting (vendored) |
| serde/serde_json | Configuration serialization |
| socket2 | UDP networking for netplay |
| ringbuf | Lock-free ring buffer for audio |
| blip_buf | Band-limited audio synthesis |
| crc32fast | ROM identification |
| ureq | HTTP client for auto-updater |
| semver | Version comparison |

### Key Facts
- `bus.rs` is the memory arbitration layer at the center of the emulator.
- `mapper.rs` is one of the largest files because cartridge hardware variation is substantial.
- `main.rs` contains the application, UI, CRT, input, and menu integration work.
- Optional subsystems are kept outside the strict chip-emulation core.

---

## 🔬 Deep Dive
### Dependency Relationships
The dependency graph is intentionally centered on the Bus. The CPU does not directly own the rest of the machine; instead, it accesses memory through Bus reads and writes. The PPU reaches CHR data through the cartridge path, which means mapper logic can affect graphics fetches as well as CPU-visible PRG access. The APU's DMC channel also depends on Bus-mediated reads, so audio timing still touches the shared memory fabric.

### Module Responsibilities
The large top-level files map cleanly onto emulator concerns. `cpu.rs`, `ppu.rs`, and `apu.rs` model the three major hardware domains. `cartridge.rs` parses ROMs and exposes cartridge state, while `mapper.rs` implements the board-specific logic behind that abstraction. `joypad.rs` handles controller state. `main.rs` is deliberately broad because it hosts windowing, menus, CRT presentation, and integration of optional features such as recording, netplay, scripting, achievements, ROM metadata, and updates.

### Reference Implementations
OxideNES uses `Bus` as the central coordinator, `MapperEnum` in `mapper.rs` to represent mapper variants, and `cpal` as the crate providing cross-platform `audio_output`. This keeps the hot path on concrete enum dispatch rather than per-access dynamic dispatch, while still letting the cartridge layer expose many mapper implementations behind one interface shape.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. If the CPU performs a memory read from cartridge PRG space, which modules are involved in servicing that request?
2. Which external crate is responsible for cross-platform audio output?
3. Why is `mapper.rs` larger than `cartridge.rs` in a multi-mapper emulator?

### Core Problems
1. Trace a CPU read from the Bus to cartridge PRG data and explain where mapper-specific behavior enters the path.
2. Explain why an enum-based mapper dispatch design can be attractive in Rust compared with a vtable-based trait-object design.

### Challenge
Propose how you would add a new optional subsystem without violating the current architecture's separation between core hardware emulation and plugins.

---

*See also:* [[Main Loop and Cycle Ratios]], [[Performance Optimization in OxideNES]], [[Save States and Rewind]], [[Emulator Architecture Overview]]

## References
→ [[Sources Index]]
