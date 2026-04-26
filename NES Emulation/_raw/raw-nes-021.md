---
tags: [raw, nes-emulation, palette]
source: "NESdev palette reference + NTSC signal generation"
---

# Raw NES 021 — NES Color Palette and NTSC Signal

The NES doesn't generate RGB directly — it produces an NTSC composite video signal. The 64-entry color palette is defined in terms of NTSC signal parameters (hue and brightness), not RGB values.

## How NES Colors Work

The PPU generates composite NTSC video by outputting voltage levels that encode luma (brightness) and chroma (color) information. Each palette entry specifies: a hue (phase angle of the chroma signal, 12 possible hues in 30° increments) and a brightness level (4 levels: dark, normal, light, white). The TV's decoder converts this analog signal back into visible color.

## The 64-Entry Palette

Palette entries $00-$0F are the darkest row, $10-$1F normal, $20-$2F light, $30-$3F lightest. Within each row, entries $x0 is gray (no chroma), $x1-$xC are the 12 hues, and $xD is dark gray/black. Entries $xE and $xF are "blacker than black" (below the NTSC black level) — displaying them can cause issues on real TVs. Several entries produce identical or very similar colors, so the effective unique color count is around 52-54.

## RGB Approximation

Since modern displays use RGB, emulators must convert NES palette entries to RGB values. There is no single "correct" NES palette — the original hardware produced analog video that looked different on every TV. Common approaches:
- **Empirically measured palettes:** Captured from real NES hardware through various TVs. The "FCEUX" and "Nestopia" palettes are popular choices.
- **Generated palettes:** Mathematical models of the NTSC signal generation and decoding process. These are more accurate but complex. OxideNES uses a generated palette with configurable parameters.
- **Emphasis bits:** PPUMASK bits 5-7 tint the entire screen by attenuating R, G, or B components. This multiplies the palette by up to 8 emphasis combinations (64 × 8 = 512 effective colors). OxideNES applies emphasis as a post-process on the RGB output.

## Palette RAM

The PPU has 32 bytes of palette RAM at $3F00-$3F1F:
- $3F00: Universal background color (shared across all background palettes)
- $3F01-$3F03: Background palette 0, colors 1-3
- $3F05-$3F07: Background palette 1, colors 1-3
- $3F09-$3F0B: Background palette 2, colors 1-3
- $3F0D-$3F0F: Background palette 3, colors 1-3
- $3F10: Mirror of $3F00 (reading/writing $3F10 accesses $3F00)
- $3F11-$3F13: Sprite palette 0, colors 1-3
- $3F15-$3F17: Sprite palette 1, colors 1-3
- $3F19-$3F1B: Sprite palette 2, colors 1-3
- $3F1D-$3F1F: Sprite palette 3, colors 1-3

Addresses $3F04, $3F08, $3F0C (and their sprite mirrors) are technically writable but reading them returns the universal background color. This quirk must be emulated.

## Grayscale Mode

PPUMASK bit 0 enables grayscale mode, which ANDs all palette lookups with $30 — stripping the hue information and leaving only the brightness level. This produces a 4-shade grayscale image. Some games use this for visual effects (like screen fade to gray).
