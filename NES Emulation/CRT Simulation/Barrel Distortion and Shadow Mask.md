---
tags: [nes, wiki]
up: "[[CRT Simulation Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Barrel Distortion and Shadow Mask

> **Barrel distortion curves the image like CRT glass, while shadow mask patterns recreate the visible phosphor structure.**

## 🎯 Intuition
**The Core Idea:** Barrel distortion simulates curved CRT glass; shadow mask reproduces the RGB phosphor dot pattern.
**Analogy:** Looking through a fishbowl at a mosaic.
**Why It Matters:** These two effects most define the CRT look.

---

## ⚙️ Core Mechanics
### How It Works
#### Barrel Distortion Algorithm
CRT screens are slightly curved, causing straight lines to bow outward at the edges. OxideNES simulates this with a coordinate transformation:

1. Normalize pixel coordinates to [-1, 1] range
2. Apply distortion: `distorted = coord * (1 + k * r^2)` where `r` is distance from center
3. Sample the source image at the distorted coordinates
4. Edge pixels that map outside the source are rendered black

#### Shadow Mask Pattern
The physical pixel structure of a CRT is visible as a repeating pattern of colored phosphor dots. Traditional CRT design uses triangular dot triads. Each pixel position has an RGB emphasis pattern that repeats every 3 horizontal pixels, simulating the physical shadow mask that directs electron beams to specific phosphor colors.

#### Aperture Grille Pattern
Sony Trinitron-style vertical stripe pattern. Simpler than shadow mask: alternating R, G, B vertical columns with thin dark gaps between.

### Key Specifications
OxideNES supports both modes, selectable in the CRT settings menu.

### Key Facts
- The curvature parameter `k` is adjustable from `0` (flat) to high values (pronounced curve).
- Coordinates are normalized to `[-1, 1]` before distortion is applied.
- Pixels mapped outside the source image are rendered black.
- Shadow mask emphasizes repeating RGB dot triads every 3 horizontal pixels.
- Aperture grille uses vertical R, G, B stripes with thin dark gaps between columns.

---

## 🔬 Deep Dive
### Curvature Parameter
The curvature parameter `k` controls how strongly the image bows outward. At `k = 0`, the screen is effectively flat. Higher values produce a more pronounced CRT-style curve.

### Coordinate Normalization Math
The distortion operates in normalized coordinates rather than raw pixel positions. Pixel coordinates are first mapped into the `[-1, 1]` range, then transformed with `distorted = coord * (1 + k * r^2)`, where `r` is the distance from the screen center.

### CRT Settings Menu
OxideNES exposes both shadow mask and aperture grille as selectable CRT settings so the visible pixel structure can be tuned for different CRT styles.

### Reference Implementations
In OxideNES, the barrel distortion pass performs coordinate remapping, while the mask stage applies either the shadow mask RGB dot-triad look or the aperture grille stripe look as part of the CRT settings pipeline.

---

## 🏋️ Practice
### Warm-Up (5 min)
- Trace what happens to a corner pixel during barrel distortion.
- Explain the visual difference between a shadow mask and an aperture grille.
- Describe what the output looks like when `k = 0`.

### Core Problems
- Walk through the 4 barrel distortion steps for a pixel near the edge of the screen.
- Compare how a repeating 3-pixel RGB emphasis pattern differs from vertical RGB stripe columns.

### Challenge
- Explain why barrel distortion and phosphor-mask simulation together do more to sell the CRT look than either effect used alone.

---

*See also:* [[CRT Rendering Pipeline]], [[Scanline and Phosphor Effects]], [[Glass Reflections and Chromatic Aberration]], [[CRT Simulation Overview]]

## References
→ [[Sources Index]]