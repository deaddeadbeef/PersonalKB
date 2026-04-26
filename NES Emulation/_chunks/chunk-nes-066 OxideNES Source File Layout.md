---
tags: [chunk, nes-emulation, module]
source: "[[raw-nes-027]]"
up: "[[OxideNES Module Architecture]]"
---

# Chunk NES 066 — OxideNES Source File Layout

OxideNES consists of approximately 15,700 lines across 15 Rust source files. The largest files are main.rs (7,572 lines — window, CRT, input, netplay, Lua, achievements), mapper.rs (3,213 lines — all 20 mappers), cpu.rs (1,670 lines — 6502 emulation), apu.rs (973 lines — audio channels and mixing), and ppu.rs (781 lines — rendering pipeline). Supporting modules include bus.rs (351 lines), netplay.rs (250 lines), lua_api.rs (300 lines), audio.rs (200 lines), input.rs (180 lines), config.rs (150 lines), savestate.rs (120 lines), rewind.rs (100 lines), achievement.rs (200 lines), and lib.rs (100 lines).
