---
tags: [chunk, nes-emulation, crt]
source: "[[raw-nes-006]]"
up: "[[CRT Rendering Pipeline]]"
---

# Chunk NES 026 — CRT Bilinear Upscale and Phosphor Persistence

The CRT pipeline begins by upscaling the raw 256x240 framebuffer to window resolution using bilinear interpolation with pre-computed weights. Next, phosphor persistence blends the current frame with the previous frame using a configurable factor (default 0.3) — fast-moving objects leave subtle trails matching real CRT behavior. The implementation stores the previous frame buffer and performs per-pixel linear interpolation. These two stages establish the base image quality before post-processing effects are applied. Both stages use optimized memory-sequential access patterns.
