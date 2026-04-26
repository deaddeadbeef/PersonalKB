---
tags: [chunk, nes-emulation, performance]
source: "[[raw-nes-015]]"
up: "[[Performance Optimization in OxideNES]]"
---

# Chunk NES 097 — Zero-Allocation Frame Loop

OxideNES pre-allocates all large buffers at startup: the frame buffer (256x240x4 RGBA bytes), rewind ring buffer (300 state snapshots), and audio ring buffer. No heap allocation occurs during emulation frames, preventing garbage-collection-like pauses. Rust's ownership model enforces this at compile time. The emulator can be compiled with a profile feature flag that instruments the main loop, measuring CPU, PPU, APU, and render time per frame. Profiling revealed the CRT pipeline consumes 40-60% of frame time with all effects enabled, leading to the pre-computed LUT optimizations for gamma, scanlines, and shadow mask stages.
