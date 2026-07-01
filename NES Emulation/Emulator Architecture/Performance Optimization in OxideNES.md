---
tags: [nes, wiki]
up: "[[Emulator Architecture Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Performance Optimization in OxideNES

> **OxideNES reaches real-time speed by optimizing the hottest paths while preserving cycle-accurate behavior.**

## 🎯 Intuition
**The Core Idea:** The emulator stays accurate first, then tunes only the parts that run often enough to matter.
**Analogy:** Like tuning a race car: you optimize the engine, aerodynamics, and weight separately instead of randomly changing everything.
**Why It Matters:** A cycle-accurate emulator still has to hit about 60 fps, so hot-path work must be cheap enough to keep pace with real hardware timing.

---

## ⚙️ Core Mechanics
### How It Works
OxideNES prioritizes accuracy but applies targeted optimizations to hot paths without sacrificing correctness. The work is split across CPU execution, PPU rendering, and CRT post-processing, because those areas dominate runtime cost for different reasons.

### Key Specifications

| Technique | Target | Impact |
|-----------|--------|--------|
| `#[inline(always)]` | get_flag/set_flag | ~1.79M calls/sec |
| `#[inline]` | Stack ops, addressing modes | Medium frequency |
| `#[inline]` | Arithmetic helpers (ADC, SBC) | Per-instruction |
| Enum dispatch | Opcode matching | Zero-cost vs vtable |

| Technique | Target | Impact |
|-----------|--------|--------|
| 11 inline annotations | tick, read, write, scroll | 5.37M ticks/sec |
| Unsafe pixel writes | Bounds check elimination | 61,440 checks/frame |
| Direct palette access | 32-element lookup | Avoids address decode |
| OAM dirty tracking | Future sprite caching | Infrastructure |

| Technique | Target | Impact |
|-----------|--------|--------|
| SWAR bilinear | R+B channel packing | 12→8 multiplies/pixel |
| Fused gamma LUT | Gamma+brightness+contrast | Eliminates 691K pass |
| Merged multiply stage | Phosphor+scanline+vignette | 6 ops/pixel saved |
| Ghost buffer elim | Glass reflections | 2.7MB/frame saved |
| sv_table precompute | Scanline+vignette combo | Rebuilt only on change |
| Early exits | Zero-param effects | Skip entire passes |

### Key Facts
- CPU helpers such as flag accessors, stack operations, addressing modes, ADC, and SBC are inlined because they occur constantly.
- PPU work is especially sensitive because it runs at 5.37M ticks/sec.
- CRT post-processing is optimized as a separate stage with math and memory reductions.
- Accuracy remains the priority; the optimizations are targeted rather than architectural shortcuts.

---

## 🔬 Deep Dive
### CPU Hot Path
The CPU side focuses on tiny functions that sit inside the instruction loop. `#[inline(always)]` on `get_flag` and `set_flag` targets helpers called about 1.79 million times per second. Other medium-frequency helpers, including stack operations and addressing modes, use `#[inline]`, as do arithmetic helpers such as ADC and SBC. Enum dispatch is used for opcode matching so the code stays concrete and avoids vtable overhead.

### PPU Hot Path
The PPU is even more frequency-sensitive because it advances at 5.37 million ticks per second. Eleven inline annotations cover `tick`, `read`, `write`, and scroll-related paths. Unsafe pixel writes eliminate bounds checks, avoiding 61,440 checks per frame. Direct palette access reduces decode overhead for a fixed 32-element lookup. OAM dirty tracking exists as infrastructure for future sprite caching work.

### CRT Pipeline
CRT effects in `main.rs` are treated as a numerical throughput problem. SWAR bilinear filtering packs R+B channels and cuts multiplies from 12 to 8 per pixel. A fused gamma LUT combines gamma, brightness, and contrast so a separate 691K-pass stage disappears. A merged multiply stage combines phosphor, scanline, and vignette work, saving 6 operations per pixel. Eliminating the ghost buffer saves 2.7 MB per frame for glass reflections. `sv_table` precomputes the scanline+vignette combination and is rebuilt only when parameters change. Early exits skip whole passes when effects are zeroed out.

### Rust-Specific Techniques
- **Release profile:** `LTO=true`, `codegen-units=1` for maximum optimization
- **Enum dispatch:** `MapperEnum` avoids dynamic dispatch overhead
- **Bounds check elision:** `unsafe` where index validity is provable
- **Iterator patterns:** `chunks_exact` enables auto-vectorization

### Reference Implementations
In OxideNES, the reference pattern is not "optimize everything." It is: keep the model accurate, identify the hottest loops, then apply Rust-friendly low-level techniques such as LTO, single codegen-unit release builds, enum dispatch, provable bounds-check elision, and iterator forms like `chunks_exact` that help the compiler generate efficient code.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why might `#[inline(always)]` help in a helper called millions of times per second but hurt if used everywhere?
2. What does "zero-cost vs vtable" mean in the opcode or mapper-dispatch context?
3. Why is the PPU especially sensitive to per-call overhead?

### Core Problems
1. Estimate the cumulative effect of saving 4 multiplies per pixel in a 256×240 frame and explain why SWAR-style optimization matters.
2. Describe the tradeoff of using `unsafe` pixel writes to remove bounds checks when index validity is already provable.

### Challenge
Choose one optimization from the CPU table, one from the PPU table, and one from the CRT table, then argue which of the three is most likely to matter most for sustaining real-time performance.

---

*See also:* [[Main Loop and Cycle Ratios]], [[OxideNES Module Architecture]], [[Emulator Architecture Overview]]

## References
→ [[NES Emulation/Sources/Sources Index|Sources Index]]
