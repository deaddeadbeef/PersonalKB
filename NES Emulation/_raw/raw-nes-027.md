---
tags: [raw, nes-emulation, module-architecture]
source: "OxideNES source code architecture analysis"
---

# Raw NES 027 — OxideNES Module Architecture

OxideNES is structured as a monolithic Rust application with clear module boundaries. Understanding the source layout is essential for navigating the codebase and making modifications.

## Source Files and Responsibilities

| File | Lines | Responsibility |
|------|-------|----------------|
| main.rs | ~7,572 | Entry point, window management, input, CRT pipeline, netplay, Lua, achievements, config |
| cpu.rs | ~1,670 | 6502 CPU emulation (registers, decode, execute, interrupts) |
| ppu.rs | ~781 | PPU emulation (rendering, scrolling, register I/O) |
| apu.rs | ~973 | APU emulation (all 5 channels, frame sequencer, mixing) |
| bus.rs | ~351 | System bus (address decode, timing, DMA) |
| mapper.rs | ~3,213 | All 20 mapper implementations |
| lib.rs | ~100 | Library root, module declarations |
| audio.rs | ~200 | Audio output (cpal integration, ring buffer) |
| input.rs | ~180 | Input handling (keyboard, gamepad via gilrs) |
| config.rs | ~150 | Configuration file handling (TOML) |
| savestate.rs | ~120 | Save state serialization/deserialization |
| rewind.rs | ~100 | Rewind ring buffer management |
| netplay.rs | ~250 | UDP networking (socket, protocol, sync) |
| lua_api.rs | ~300 | Lua scripting API registration and callbacks |
| achievement.rs | ~200 | Achievement condition evaluation and persistence |

## Dependency Graph

\\\
main.rs
  +-> bus.rs (owns all subsystems)

  |     +-> cpu.rs
  |     +-> ppu.rs
  |     +-> apu.rs
  |     +-> mapper.rs (via Cartridge)
  +-> input.rs (keyboard + gamepad)
  +-> audio.rs (cpal output)
  +-> config.rs (TOML settings)
  +-> savestate.rs (serde serialization)
  +-> rewind.rs (ring buffer)
  +-> netplay.rs (UDP protocol)
  +-> lua_api.rs (mlua scripting)
  +-> achievement.rs (condition eval)
\\\

## The Bus as Central Coordinator

The Bus struct owns the CPU, PPU, APU, and Cartridge (with its mapper). All memory access flows through the bus:
- CPU reads/writes call us.read(addr) / us.write(addr, val)
- Bus decodes the address and routes to the appropriate subsystem
- PPU VRAM access goes through the cartridge mapper for nametable mirroring and CHR bank switching
- The bus's clock() method maintains the 3:1 PPU:CPU timing ratio

## Main.rs as the "Shell"

main.rs is the largest file because it handles everything above the emulation core: window creation (minifb), the CRT rendering pipeline, input polling, audio output management, save state I/O, the rewind system, netplay protocol, Lua script loading/execution, achievement evaluation, and the config file. It essentially wraps the pure emulation (bus+cpu+ppu+apu+mapper) with all the features that make OxideNES a full emulator application.

## Trait-Based Extensibility

Key traits enable modularity:
- Mapper trait: All mappers implement this for cpu_read/write and ppu_read/write
- Serialize/Deserialize (serde): All state-holding structs implement these for save states
- Audio callback trait: Bridges the emulation's sample generation with cpal's audio thread

## Build Configuration

\Cargo.toml\ features:
- Default: all features enabled
- \
o-audio\: Disables cpal dependency (for CI/testing)
- \
o-gui\: Disables minifb (for headless testing/benchmarking)
- \profile\: Enables per-frame timing instrumentation
