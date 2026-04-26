---
tags: [chunk, nes-emulation, tas]
source: "[[raw-nes-030]]"
up: "[[Input Recording and TAS]]"
---

# Chunk NES 114 — Frame Advance for TAS

Frame advance is the most critical TAS tool. Pressing the frame advance key (default: period) advances emulation by exactly one frame and pauses, allowing the TASer to examine each frame individually. Combined with save states, this enables systematic optimization: try an input, advance one frame, check the result, load state to retry if suboptimal. The on-screen input display shows a visual controller representation with active buttons highlighted. OxideNES does not support subframe input recording (changing controller state between  reads within a frame), consistent with most community emulator standards.
