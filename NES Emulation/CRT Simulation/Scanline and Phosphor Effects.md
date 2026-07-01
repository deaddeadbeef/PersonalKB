---
tags: [nes, wiki]
up: "[[CRT Simulation Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Scanline and Phosphor Effects

> **Scanlines, phosphor warmth, bloom, and vignette recreate the glow, warmth, and edge falloff that make CRT images feel distinct.**

## 🎯 Intuition
**The Core Idea:** Scanlines, phosphor warmth, bloom, and vignette reproduce a CRT's characteristic glow and falloff.
**Analogy:** Candlelight vs LED — CRT phosphors have natural glow, fade, and color temperature.
**Why It Matters:** These are the most recognizable CRT visual signatures, and `sv_table` shows how to optimize them without sacrificing fidelity.

---

## ⚙️ Core Mechanics
### How It Works
#### Scanlines
Real CRT displays show visible dark lines between each row of pixels because the electron beam only illuminates alternating rows. OxideNES simulates this by:

1. Computing a scanline intensity based on vertical position (every `N`th row is dimmed)
2. Multiplying pixel brightness by scanline factor
3. Configurable intensity from `0%` (no scanlines) to `100%` (fully dark lines)

#### Phosphor Warmth
CRT phosphors emit slightly warm-tinted light compared to modern LCD white points. OxideNES shifts the color temperature by blending each pixel toward a warm reference point, controlled by an intensity slider.

#### Phosphor Bloom/Glow
Bright pixels bleed light into neighboring scanlines, simulating the phosphor glow effect:
- Vertical neighbor blending with configurable radius
- Skipped entirely when glow parameter is zero (early exit)
- Adds visual warmth at the cost of slight softening

#### Vignette
CRT screens are brighter at the center and darker at the edges due to electron gun geometry. OxideNES applies a radial darkening function based on distance from screen center.

### Key Specifications

| Effect | Mechanic | Key Detail |
|--------|----------|------------|
| Scanlines | Row-based darkening | Every `N`th row is dimmed; intensity ranges from `0%` to `100%` |
| Phosphor Warmth | Color-temperature shift | Pixels blend toward a warm reference point |
| Phosphor Bloom/Glow | Vertical neighbor blending | Configurable radius; skipped entirely when glow is zero |
| Vignette | Radial darkening | Darkening increases with distance from screen center |

### Key Facts
- Scanlines dim every `N`th row rather than uniformly darkening the whole image.
- Phosphor warmth shifts the image toward a warmer CRT-like white point.
- Bloom/glow uses vertical neighbor blending and softens bright regions slightly.
- Vignette darkens edges relative to the center.
- `sv_table` precomputes scanline and vignette values by pixel position.

---

## 🔬 Deep Dive
### The `sv_table` Optimization
Scanline and vignette effects are combined into a single precomputed lookup table (`sv_table`), indexed by pixel position.

### Why It Helps
This eliminates per-pixel multiply+shift operations in the hot loop, providing measurable frame time improvement.

### Rebuild Behavior
The table is rebuilt only when a related parameter changes, so the expensive setup work is avoided during steady-state rendering.

### Reference Implementations
In OxideNES, `sv_table` merges scanline darkening with vignette darkening into one position-based lookup. Phosphor warmth is applied as a color shift, and glow uses vertical neighbor blending with an early exit when the glow parameter is zero.

---

## 🏋️ Practice
### Warm-Up (5 min)
- Explain why dimming every `N`th row creates a scanline effect.
- Describe the visual tradeoff introduced by phosphor bloom/glow.
- Explain what `sv_table` stores and when it needs to be rebuilt.

### Core Problems
- Walk through how scanlines and vignette would combine for a bright pixel near the edge of the screen.
- Compare phosphor warmth and phosphor bloom: what changes does each one make to the image?

### Challenge
- Argue why precomputing `sv_table` is a better optimization than recalculating scanline and vignette factors per pixel every frame.

---

*See also:* [[CRT Rendering Pipeline]], [[Barrel Distortion and Shadow Mask]], [[Glass Reflections and Chromatic Aberration]], [[CRT Simulation Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]