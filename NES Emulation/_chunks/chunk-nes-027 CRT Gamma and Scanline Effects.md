---
tags: [chunk, nes-emulation, crt]
source: "[[raw-nes-006]]"
up: "[[Scanline and Phosphor Effects]]"
---

# Chunk NES 027 — CRT Gamma and Scanline Effects

A 256-entry gamma correction LUT simulates CRT phosphor non-linearity, pre-computed as (x/255)^gamma * 255 with default gamma 2.2. Horizontal scanlines darken every other pixel row by a configurable opacity (default 0.15). A vignette effect uses a radial distance function from screen center to darken edges, simulating reduced electron beam intensity at the periphery. Both scanline and vignette effects multiply existing pixel values, preserving color ratios while reducing brightness. The gamma LUT eliminates expensive per-pixel power function calls during rendering.
