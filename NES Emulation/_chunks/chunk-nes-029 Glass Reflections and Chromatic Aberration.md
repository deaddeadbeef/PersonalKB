---
tags: [chunk, nes-emulation, crt]
source: "[[raw-nes-006]]"
up: "[[Glass Reflections and Chromatic Aberration]]"
---

# Chunk NES 029 — Glass Reflections and Chromatic Aberration

The final CRT pipeline stage simulates the glass surface of a CRT monitor. A specular highlight with Gaussian falloff is placed at a configurable position (default upper-left), creating a subtle bright spot mimicking ambient light reflection. Chromatic aberration shifts the R and B color channels by 1-2 pixels in opposite directions at screen edges, simulating light dispersion through curved glass. Both effects are intentionally subtle but add significant realism. All CRT stages can be individually toggled and the full pipeline maintains better than 60 FPS on modern hardware.
