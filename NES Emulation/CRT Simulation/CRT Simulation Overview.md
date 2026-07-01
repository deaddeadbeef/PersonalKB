---
tags: [nes, hub]
up: "[[NES Emulation]]"
confidence: established
freshness: stable
tier-coverage: [intuition, core, deep-dive]
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

## How To Read This Chapter

Read this chapter for display feel beyond raw pixels. NES emulation is less about isolated facts than about making several small timed machines agree on the same frame. The overview pages should give you the vocabulary first, then route you into the detailed pages where timing, registers, and test-ROM behavior matter.

A productive pass has three questions. First, what state does this subsystem own? Second, which reads or writes have side effects? Third, what timing relationship can break a game if it is off by even a few CPU or PPU cycles? Keep those questions nearby while reading the linked pages.

## Emulator Checkpoints

Use the deeper notes to turn the concept into implementation proof. The key checkpoints for this chapter are: scanline structure, color emphasis, NTSC artifacting, phosphor persistence, scaling, and latency budget. For each checkpoint, prefer a tiny deterministic test before a visual game test. A passing screenshot is useful, but a focused trace is better when the bug is cycle timing, flag behavior, mapper state, or register side effects.

The chapter is mastered when you can explain both the user-visible symptom and the internal cause of a failure. For example, audio pops, scrolling seams, wrong sprite priority, broken controller input, or a mapper crash should point back to a specific piece of state and a specific clock boundary.

## References

→ [[NES Emulation/Sources/Sources Index|Sources Index]]
