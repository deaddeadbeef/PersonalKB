---
tags: [study, nes-emulation, ppu]
up: "[[NES Emulation Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---
# Review Drill — PPU Rendering Pipeline

Test your understanding of the NES Picture Processing Unit.

## Questions

**Q1:** How many scanlines per NTSC frame, and how are they categorized?
> 262 total: pre-render (-1/261), visible (0-239), post-render (240), VBlank (241-260). Each scanline is 341 PPU cycles.

**Q2:** Describe the 4-step background tile fetch sequence.
> Every 8 PPU cycles: (1) nametable byte (tile index), (2) attribute byte (palette selection), (3) pattern table low byte (bit-plane 0), (4) pattern table high byte (bit-plane 1). Data feeds into 16-bit shift registers.

**Q3:** What are the four loopy scroll registers and their purposes?
> v (15-bit current VRAM address for rendering), t (15-bit temporary holding programmed scroll), x (3-bit fine horizontal scroll 0-7), w (1-bit write toggle for sequential / writes).

**Q4:** When do horizontal and vertical scroll components copy from t to v?
> Horizontal: cycle 257 of each visible scanline. Vertical: cycles 280-304 of the pre-render scanline only. This is why mid-frame horizontal scroll changes take effect immediately but vertical only at frame start.

**Q5:** Explain the sprite-0 hit flag conditions.
> Opaque sprite-0 pixel overlaps opaque background pixel, both BG and sprite rendering enabled, pixel not at X=255, and not in X=0-7 if left-side clipping is on. The exact PPU cycle depends on sprite X position.

**Q6:** Describe the sprite overflow hardware bug.
> After finding 8 sprites for a scanline, the PPU should check remaining sprites. Instead, it increments both sprite index AND byte offset simultaneously, reading wrong bytes as Y coordinates — missing some sprites and false-triggering on others.

**Q7:** What is the VBlank flag suppression quirk?
> Reading PPUSTATUS within 1-2 cycles of VBlank start (cycle 1, scanline 241) suppresses the VBlank flag and prevents NMI from firing. This race condition must be emulated at cycle precision.

**Q8:** How does the NES generate colors?
> The PPU outputs NTSC composite video with hue and brightness parameters, not RGB. Each palette entry specifies 1 of 12 hues and 4 brightness levels. Emulators approximate via lookup tables since no canonical RGB palette exists.

## References

- [[NES Emulation/Study/NES Emulation Study Index]]
- [[NES Emulation/Sources/Sources Index]]
- [[NES Emulation/NES Emulation Book Reading Spine]]
