---
tags: [raw, nes-emulation, performance]
source: "OxideNES CPU_OPTIMIZATIONS.md + PPU_OPTIMIZATIONS.md"
---

# Raw NES 015 — Performance Optimization Strategies

OxideNES implements several optimization techniques documented in its internal CPU_OPTIMIZATIONS.md and PPU_OPTIMIZATIONS.md files. These balance accuracy with performance to maintain 60 FPS on modern hardware.

## CPU Optimizations

**Instruction Fusion:** Commonly paired instructions are detected and executed as single operations where semantically equivalent. For example, `LDA #imm / STA zp` sequences can be detected but OxideNES opts to keep instructions separate for accuracy.

**Branch Prediction Hints:** The CPU emulation uses Rust's `likely()`/`unlikely()` hints (via compiler intrinsics) for hot paths in the decode loop. Since most opcodes are taken branches, loads, and stores, these paths are marked likely.

**Lookup Tables:** Instruction cycle counts, addressing mode handlers, and flag calculations use pre-computed lookup tables indexed by opcode. This eliminates branching in the decode stage. The NZ flag table (256 entries mapping byte values to N and Z flag states) is particularly impactful.

**Page-Cross Detection:** Instead of comparing full 16-bit addresses, page crosses are detected by checking if `(base & 0xFF) + offset > 0xFF` — a single comparison on the low byte.

## PPU Optimizations

**Dirty Tile Tracking:** Rather than re-rendering the entire nametable background each frame, OxideNES tracks which nametable entries changed since the last frame. Only dirty tiles are re-rendered. This dramatically reduces work for games with mostly static backgrounds (typical for NES games).

**Sprite Evaluation Cache:** The per-scanline sprite evaluation is cached when sprite positions haven't changed between frames. If OAM hasn't been written to since the last frame (detected via a dirty flag on 0x4014 writes), the sprite evaluation from the previous frame is reused.

**Shift Register Optimization:** The PPU's 16-bit background shift registers use native integer shifts rather than bit-by-bit simulation. Each pixel output uses `(shift_reg >> (15 - fine_x)) & 1` for each bitplane, compiled to efficient single-cycle instructions.

**Scanline Skipping:** When both background and sprite rendering are disabled (PPUMASK bits 3-4 clear), the PPU skips all rendering logic for that scanline, only updating timing and VBlank state. Many games disable rendering for the top/bottom scanlines.

**Frame Buffer Layout:** The pixel buffer uses a flat RGBA array with stride matching the display width. This ensures cache-friendly sequential writes during rendering and efficient blitting to the display surface.

## Memory Allocation

OxideNES pre-allocates all large buffers (frame buffer, rewind ring buffer, audio buffer) at startup. No heap allocation occurs during emulation frames, preventing GC-like pauses. Rust's ownership model ensures this is enforced at compile time.

## Profiling

The emulator can be compiled with a `profile` feature flag that instruments the main loop, measuring CPU/PPU/APU/render time per frame. This data helped identify the CRT pipeline as the largest time consumer (40-60% of frame time with all effects enabled), leading to the per-stage LUT optimizations.
