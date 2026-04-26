---
tags: [chunk, nes-emulation, crt]
source: "[[raw-nes-006]]"
up: "[[CRT Simulation Overview]]"
---

# Chunk NES 108 — CRT Pipeline Performance

The entire OxideNES CRT pipeline processes at better than 60 FPS on modern hardware using software rendering (no GPU shaders). Performance is achieved through pre-computed LUTs for gamma correction and shadow mask patterns, SIMD-friendly memory layouts with sequential pixel access, and early-exit optimizations skipping processing for fully black pixels. Each stage can be individually toggled via configuration, allowing users to trade visual fidelity for performance on weaker hardware. Profiling shows the CRT pipeline consumes 40-60% of total frame time with all effects enabled, making it the single largest performance cost in the emulator.
