---
tags: [nes, wiki]
up: "[[CRT Simulation Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---
# Glass Reflections and Chromatic Aberration

> **Glass reflections add ambient ghosting on the CRT surface, and chromatic aberration adds subtle RGB fringing near the edges.**

## 🎯 Intuition
**The Core Idea:** Glass reflections are ambient light bouncing off the CRT surface; chromatic aberration is RGB separation at the edges.
**Analogy:** A TV in a bright room — a ghost reflection plus color fringing at curved edges.
**Why It Matters:** These effects sell the illusion of a physical TV, and the ghost-buffer optimization saves `2.7MB/frame`.

---

## ⚙️ Core Mechanics
### How It Works
#### Glass Reflection Algorithm
The CRT glass surface reflects ambient light, adding a subtle translucent layer over the game image:

1. A ghost image is computed from the current frame
2. The ghost is offset and faded to simulate reflection angle
3. Blended over the final image at configurable intensity
4. **Optimization:** Ghost pixels read directly from CRT output buffer, eliminating a `2.7MB/frame` memcpy (added in `v0.2.0`)

#### Chromatic Aberration
The glass surface refracts light slightly differently for each color channel, causing RGB separation at the edges:

1. Red, green, and blue channels are sampled at slightly different positions
2. Offset increases toward screen edges (center is aligned)
3. Creates a subtle rainbow fringing effect on high-contrast edges
4. Configurable intensity from off to extreme

#### TV Bezel
OxideNES renders a silver CRT TV frame around the game screen.

### Key Specifications

| Bezel Element | Detail |
|---------------|--------|
| Speaker grille | Horizontal slots |
| RCA jacks | Composite video aesthetic |
| Controls | Physical buttons and badge |
| Screen coverage | Game screen fills `~80%` of TV face |
| Render size | Integer `3x` NES vertical scale at `960x720` |

### Key Facts
- Glass reflections are blended over the final image as a translucent layer.
- Chromatic aberration samples `R`, `G`, and `B` at slightly different positions.
- Edge separation increases away from the center, where the channels remain aligned.
- Ghost pixels were changed in `v0.2.0` to read directly from the CRT output buffer.
- The silver bezel includes a speaker grille, RCA jacks, physical buttons, and a badge.
- The bezel was redesigned in `v0.1.4-0.1.7` for authentic vintage proportions.

---

## 🔬 Deep Dive
### Ghost Buffer Optimization (`v0.2.0`)
The reflection system originally required copying ghost data, but `v0.2.0` changed ghost-pixel reads to come directly from the CRT output buffer, eliminating a `2.7MB/frame` memcpy.

### Bezel Redesign History (`v0.1.4-0.1.7`)
The TV bezel was redesigned in `v0.1.4-0.1.7` to produce more authentic vintage proportions while keeping the game screen at roughly `80%` of the TV face.

### Chromatic Aberration Edge Calculation
Chromatic aberration is weakest at the center because the channels are aligned there. As distance from center increases, the per-channel sample offsets grow, creating a subtle rainbow fringing effect on high-contrast edges.

### Reference Implementations
In OxideNES, the reflection pass computes a ghost image from the current frame, offsets and fades it, then blends it at configurable intensity. The chromatic-aberration pass samples `R`, `G`, and `B` at different positions, and the rendered image sits within a silver CRT bezel at `960x720`.

---

## 🏋️ Practice
### Warm-Up (5 min)
- Explain why chromatic aberration becomes stronger toward the edges.
- Describe the `2.7MB/frame` ghost-buffer optimization in one sentence.
- State the approximate screen-to-TV-face ratio used by the bezel design.

### Core Problems
- Trace the 4 reflection steps from current frame to blended final image.
- Compare the center and edge behavior of chromatic aberration sampling.

### Challenge
- Use the `960x720` display and `~80%` screen-fill fact to explain how OxideNES balances gameplay visibility with a convincing TV bezel.

---

*See also:* [[CRT Rendering Pipeline]], [[Barrel Distortion and Shadow Mask]], [[Scanline and Phosphor Effects]], [[CRT Simulation Overview]]

## References
→ [[Sources Index]]