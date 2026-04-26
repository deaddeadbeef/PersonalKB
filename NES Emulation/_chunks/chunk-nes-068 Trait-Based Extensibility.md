---
tags: [chunk, nes-emulation, module]
source: "[[raw-nes-027]]"
up: "[[OxideNES Module Architecture]]"
---

# Chunk NES 068 — Trait-Based Extensibility

OxideNES uses Rust traits for modularity. The Mapper trait defines cpu_read/write and ppu_read/write methods implemented by all 20 mapper structs, enabling polymorphic cartridge handling. Serde Serialize/Deserialize traits on all state-holding structs enable save state serialization. The audio callback bridges emulation sample generation with cpals audio thread. Build configuration via Cargo.toml features includes no-audio (disabling cpal for CI), no-gui (disabling minifb for headless testing), and profile (enabling per-frame timing instrumentation). Rusts monomorphization eliminates virtual dispatch overhead for the Mapper trait in optimized builds.
