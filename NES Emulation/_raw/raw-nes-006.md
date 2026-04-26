---
tags: [raw, nes-emulation, crt]
source: "OxideNES main.rs CRT pipeline"
---

# Raw NES 006 — CRT Simulation Pipeline

OxideNES implements a multi-stage CRT simulation pipeline in main.rs that transforms the raw 256×240 NES framebuffer into a convincing retro display. The pipeline runs entirely on the CPU using software rendering.

## Stage 1: Bilinear Upscale

The raw 256×240 framebuffer is upscaled to the window resolution using bilinear interpolation. This provides smooth sub-pixel positioning for subsequent effects. The upscale uses pre-computed weights to minimize per-pixel math, operating on the RGBA buffer directly.

## Stage 2: Phosphor Persistence

Simulates CRT phosphor decay by blending the current frame with the previous frame. A configurable persistence factor (0.0-1.0) controls how much of the previous frame bleeds through. At 0.3 (default), fast-moving objects leave subtle trails just like a real CRT. Implementation stores the previous frame buffer and performs per-pixel linear interpolation.

## Stage 3: Gamma Correction

A 256-entry lookup table (LUT) applies gamma correction to simulate CRT phosphor non-linearity. The LUT is pre-computed at startup using (x/255)^gamma * 255 for each value 0-255. Default gamma is 2.2 (standard CRT). This step ensures brightness levels match the non-linear response curve of real CRT phosphors.

## Stage 4: Scanlines and Vignette

Horizontal scanlines darken every other row by a configurable factor (default 0.15 opacity). The vignette effect darkens the edges of the screen using a radial distance function from the center, simulating the electron beam's reduced intensity at screen edges. Both effects multiply the existing pixel values.

## Stage 5: Barrel Distortion

Simulates the curvature of a CRT screen by applying barrel distortion. Each output pixel's coordinates are remapped through a radial distortion function: ' = r * (1 + k * r^2) where k controls curvature strength. Pixels outside the distorted boundary are set to black, naturally creating the curved-edge look. The distortion amount is configurable (default k=0.15).

## Stage 6: Shadow Mask

Applies an RGB sub-pixel pattern simulating the shadow mask or aperture grille of a CRT. Each pixel's R, G, B channels are modulated based on horizontal position: at column mod 3 == 0, R is boosted and G/B reduced; at mod 1, G is boosted; at mod 2, B is boosted. This creates the characteristic RGB stripe pattern visible when zooming into a real CRT screen. Intensity is configurable.

## Stage 7: Glass Reflections and Chromatic Aberration

The final stage simulates the glass surface of a CRT monitor. A subtle specular highlight is placed at a configurable position (default upper-left area), using a Gaussian falloff function. Chromatic aberration shifts R and B channels by ±1-2 pixels at screen edges, simulating light dispersion through the curved glass. Both effects are subtle but add significant realism to the final image.

## Performance

The entire CRT pipeline processes at better than 60 FPS on modern hardware. Each stage is optimized with pre-computed LUTs, SIMD-friendly memory layouts, and early-exit optimizations for black pixels. Stages can be individually toggled via configuration.
