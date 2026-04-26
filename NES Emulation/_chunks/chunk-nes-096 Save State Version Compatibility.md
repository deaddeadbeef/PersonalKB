---
tags: [chunk, nes-emulation, savestate]
source: "[[raw-nes-010]]"
up: "[[Save States and Rewind]]"
---

# Chunk NES 096 — Save State Version Compatibility

Save states encode an emulator version number derived from the semver crate. If the emulator version changes in a way that alters the serialization format, old save states are rejected with a version mismatch error rather than loading potentially corrupt state. The version check prevents subtle bugs from deserializing fields in the wrong order or missing new fields. State files use bincode format compressed with zstd for compact storage. Each ROM's states are organized in per-CRC32 directories under ~/.nes-emulator/states/ with numbered slot files (slot-0.state through slot-9.state).
