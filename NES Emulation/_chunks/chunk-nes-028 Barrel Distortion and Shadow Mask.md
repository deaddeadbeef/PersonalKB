---
tags: [chunk, nes-emulation, crt]
source: "[[raw-nes-006]]"
up: "[[Barrel Distortion and Shadow Mask]]"
---

# Chunk NES 028 — Barrel Distortion and Shadow Mask

Barrel distortion simulates CRT screen curvature by remapping each output pixel through a radial function: r_prime = r * (1 + k * r^2) where k controls curvature strength (default 0.15). Pixels outside the distorted boundary render as black, creating natural curved edges. The shadow mask applies an RGB sub-pixel pattern: at column mod 3 positions, one of R, G, or B is boosted while others are reduced, replicating the characteristic RGB stripe pattern visible on real CRT screens when viewed closely. Both effects have configurable intensity parameters.
