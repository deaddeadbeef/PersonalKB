---
tags: [chunk, nes-emulation, scripting]
source: "[[raw-nes-008]]"
up: "[[Lua Scripting Engine]]"
---

# Chunk NES 032 — Lua Callback System

The Lua API provides event-driven callbacks: emu.on_frame(fn) fires every frame before rendering, emu.on_scanline(n, fn) fires when scanline N begins, emu.on_read(addr, fn) triggers on CPU memory reads, emu.on_write(addr, fn) on writes, and emu.on_exec(addr, fn) when the CPU executes at an address. Display functions include emu.draw_text(), emu.draw_rect(), emu.draw_line() for overlays, and emu.screenshot(path) for captures. Multiple scripts can run simultaneously in separate Lua states, persisting across save state loads since script state is independent of emulation state.
