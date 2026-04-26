---
tags: [raw, nes-emulation, testing]
source: "OxideNES testing approach + NES test ROMs"
---

# Raw NES 028 — NES Test ROMs and Validation

Validating an NES emulator requires running specialized test ROMs that exercise specific hardware behaviors. The NES homebrew and emulation community has created extensive test suites that OxideNES uses for accuracy verification.

## nestest.nes — CPU Validation

The most important CPU test ROM. Originally by kevtris, it runs through every official and many unofficial opcodes, testing:
- All addressing modes
- All flag behaviors (N, V, Z, C for every instruction)
- Page-crossing cycle behavior
- Stack operations
- BRK/RTI behavior

nestest produces a log of every instruction executed with expected vs actual register states. OxideNES can run in headless mode, comparing its execution log against the golden reference log. Any deviation indicates a CPU bug. OxideNES passes nestest completely for all official opcodes.

## PPU Test ROMs

**sprite_hit_tests (blargg):** Tests sprite-0 hit detection under various conditions — different X/Y positions, background/sprite enabling combinations, left-side clipping, timing accuracy. Tests include edge cases like hit at X=255 (should not trigger) and hit with rendering disabled.

**vbl_nmi_timing (blargg):** Tests the exact cycle when VBlank begins, when NMI fires, and interactions between PPUSTATUS reads and VBlank suppression. The NES has a quirk where reading PPUSTATUS within 1-2 cycles of VBlank start suppresses the VBlank flag — this must be emulated precisely.

**scroll_tests:** Various tests for PPU scroll register behavior — PPUSCROLL/PPUADDR write interleaving, mid-frame scroll changes, and the loopy register mechanics.

**sprite_overflow_tests:** Tests the sprite overflow flag, including the hardware bug in the overflow detection logic.

## APU Test ROMs

**apu_test (blargg):** Tests each APU channel's behavior — period, duty cycle, length counter, envelope, sweep. Verifies timing of the frame sequencer in both 4-step and 5-step modes.

**dmc_tests:** Tests DMC channel behavior — sample playback, IRQ generation, and the CPU stall behavior during DMA reads.

## Mapper-Specific Tests

**MMC3 tests:** Specifically test the scanline counter (A12 detection, counter reload behavior, IRQ timing). These are critical because many games depend on cycle-accurate MMC3 IRQs for visual effects.

**holy_mapperel:** A comprehensive mapper test ROM that exercises bank switching for various mapper types.

## OxideNES Testing Strategy

1. **Automated regression:** A test script runs nestest and compares logs on every build
2. **Visual comparison:** PPU test ROMs produce specific screen patterns — screenshots are compared against reference images
3. **Game compatibility:** A list of ~100 reference games is periodically tested for regressions
4. **Cycle comparison:** For timing-critical tests, OxideNES can log PPU cycle/scanline positions alongside CPU execution for manual verification

## Known Limitations

OxideNES intentionally does not pass every obscure test ROM. Some tests exercise behaviors that no commercial game relies on (e.g., reading PPU status during specific mid-sprite-evaluation cycles). The development philosophy prioritizes game compatibility over passing every edge-case test.
