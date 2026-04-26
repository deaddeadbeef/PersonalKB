---
tags: [nes, hub]
up: "[[NES Emulation]]"
---

# CRT Simulation Overview

OxideNES features a comprehensive CRT simulation pipeline that transforms the raw 256x240 NES output into a convincing vintage television image. The CRT filter is the most performance-intensive part of the emulator, processing ~691K pixels per frame with multiple effect passes.

## Pages

- [[CRT Rendering Pipeline]] — The multi-stage post-processing chain
- [[Scanline and Phosphor Effects]] — Simulating the CRT electron beam
- [[Barrel Distortion and Shadow Mask]] — Screen curvature and pixel structure
- [[Glass Reflections and Chromatic Aberration]] — The final visual polish

## Key Facts

- **Multi-pass pipeline:** Bilinear upscale, phosphor warmth, scanlines, vignette, barrel distortion, shadow mask, glass reflections
- **Real-time adjustable:** All parameters tunable via in-game settings menu
- **SWAR optimization:** Packs R+B channels into single u32 for faster bilinear interpolation
- **Performance:** Optimized from 18.4ms to ~8ms per frame through multiple optimization passes

## OxideNES Implementation

CRT effects are implemented in main.rs (the largest file at 7,572 lines). Key optimizations documented in PPU_OPTIMIZATIONS.md include fused lookup tables, ghost buffer elimination, and SWAR bilinear interpolation.

## References

→ [[Sources Index]]
