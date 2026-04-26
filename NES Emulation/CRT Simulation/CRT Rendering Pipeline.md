---
tags: [nes, wiki]
up: "[[CRT Simulation Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# CRT Rendering Pipeline

> **A seven-stage pipeline transforms the 256×240 NES framebuffer into a stylized CRT image, and the stage order determines both fidelity and performance.**

## 🎯 Intuition
**The Core Idea:** Seven sequential stages transform the 256×240 NES framebuffer into a CRT display.
**Analogy:** Like an Instagram filter chain — order matters.
**Why It Matters:** This is the key to quality tuning and performance, and the `~18.4ms` → `~7.5ms` evolution shows how optimization improved the pipeline over time.

---

## ⚙️ Core Mechanics
### How It Works
The CRT simulation processes each frame through these stages in order:

1. **Bilinear Upscale (256x240 to 960x720):** The raw NES framebuffer is upscaled `3.75x` horizontally and `3x` vertically using bilinear interpolation. OxideNES uses SWAR (SIMD Within A Register) to pack R+B channels into a single `u32`, reducing multiply operations from `12` to `8` per pixel.
2. **Phosphor Warmth:** Shifts colors toward warm CRT phosphor tones. Applied as a per-pixel RGB adjustment blending toward a warm white point. Skipped entirely when parameter is zero (early exit optimization).
3. **Gamma, Brightness, and Contrast:** A fused lookup table (LUT) applies all three transformations in a single array lookup per color channel, eliminating a separate `691K`-pixel pass.
4. **Scanline and Vignette:** Precomputed `sv_table` combines scanline darkening (every other row dimmed) with vignette (edges darker than center) into a single multiply-shift per pixel. Table is rebuilt only when parameters change.
5. **Barrel Distortion:** Simulates CRT screen curvature by displacing pixels outward from center. Implemented via coordinate transformation with configurable curvature strength.
6. **Shadow Mask / Aperture Grille:** Simulates the physical pixel structure of CRT displays: shadow mask uses an RGB dot triad pattern, while aperture grille uses a vertical stripe pattern like Sony Trinitron.
7. **Glass Reflections:** Simulates light reflections on the CRT glass surface with chromatic aberration (RGB channel separation). Ghost buffer reads directly from CRT output buffer to eliminate a `2.7MB/frame` memcpy.

### Key Specifications

| Stage | Purpose | Key Implementation Detail |
|-------|---------|---------------------------|
| 1. Bilinear Upscale | Scale `256x240` to `960x720` | SWAR packs R+B into one `u32`, reducing multiplies from `12` to `8` per pixel |
| 2. Phosphor Warmth | Shift toward warm CRT tones | Early exit when parameter is zero |
| 3. Gamma, Brightness, and Contrast | Apply tonal corrections | Fused LUT eliminates a separate `691K`-pixel pass |
| 4. Scanline and Vignette | Darken rows and edges | Precomputed `sv_table`, rebuilt only when parameters change |
| 5. Barrel Distortion | Curve the screen image | Coordinate transformation with configurable curvature |
| 6. Shadow Mask / Aperture Grille | Simulate CRT pixel structure | RGB dot triads or Trinitron-style stripes |
| 7. Glass Reflections | Add reflections and RGB fringing | Direct ghost-buffer reads eliminate a `2.7MB/frame` memcpy |

### Key Facts
- The pipeline order is fixed and significant.
- The upscale stage converts `256x240` into `960x720`.
- SWAR optimization reduced bilinear multiply operations from `12` to `8` per pixel.
- The fused LUT removes an entire separate `691K`-pixel pass.
- `sv_table` combines scanline and vignette into one position-indexed lookup.
- Direct ghost-buffer reads eliminate a `2.7MB/frame` memcpy.

---

## 🔬 Deep Dive
### Performance Evolution

| Version | Frame Time | Key Optimization |
|---------|-----------|-----------------|
| 0.1.0 | ~18.4ms | Initial pipeline |
| 0.1.2 | ~14.7ms | Eliminated per-pixel divisions |
| 0.1.9 | ~10ms | Early exits, buffer elimination |
| 0.2.0 | ~8ms | SWAR bilinear, fused LUTs |
| 0.2.1 | ~7.5ms | Precomputed sv_table |

### Per-Stage Optimization Details
- **SWAR bilinear:** Packs R+B channels into a single `u32`, reducing multiply count during upscale.
- **Fused LUT:** Gamma, brightness, and contrast are merged into a single lookup per color channel, eliminating a separate `691K`-pixel pass.
- **`sv_table`:** Combines scanline darkening with vignette darkening into a precomputed table rebuilt only when parameters change.
- **Ghost buffer optimization:** Reads directly from the CRT output buffer, removing a `2.7MB/frame` memcpy.

### Reference Implementations
OxideNES implements the entire seven-stage pipeline in sequence: upscale, phosphor warmth, fused tonal LUT, `sv_table` scanline/vignette pass, barrel distortion, mask selection, and glass/reflection effects.

---

## 🏋️ Practice
### Warm-Up (5 min)
- Explain why the upscale stage should happen before scanlines.
- Calculate the horizontal scale factor from `256` to `960` and the vertical scale factor from `240` to `720`.
- Identify which optimization produced the biggest frame-time win in the version table.

### Core Problems
- Walk through how changing the order of scanlines and barrel distortion would affect the final image.
- Use the performance table to describe the pipeline's evolution from `0.1.0` to `0.2.1`.

### Challenge
- Argue which optimization matters most overall: SWAR bilinear, fused LUTs, `sv_table`, or the ghost-buffer memcpy elimination.

---

*See also:* [[Barrel Distortion and Shadow Mask]], [[Scanline and Phosphor Effects]], [[Glass Reflections and Chromatic Aberration]], [[CRT Simulation Overview]]

## References
→ [[Sources Index]]