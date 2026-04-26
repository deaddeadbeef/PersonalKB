---
tags: [chunk, programming-languages, memory-layout]
source: "[[raw-pl-002]]"
---

# chunk-pl-102 Memory Layout and Cache Performance

**Struct layout matters:** CPU caches work on cache lines (64 bytes). Data laid out contiguously in memory is fast. Pointer-chasing (following references to heap objects) causes cache misses.

**Array of Structs (AoS) vs Struct of Arrays (SoA):**
- AoS: [{x,y,z}, {x,y,z}, ...] — each entity's data together. Good when accessing all fields.
- SoA: {[x,x,...], [y,y,...], [z,z,...]} — each field in its own array. Good when accessing one field across many entities. Better SIMD vectorization.

**Language impact on layout:**
- **C/C++/Rust/Zig:** Programmer controls struct layout. #[repr(C)] in Rust for C-compatible layout. Padding and alignment explicit.
- **Java:** Objects always heap-allocated (until Valhalla). Pointer-chasing for every object access. Array of objects = array of pointers = cache misses.
- **Go:** Structs embedded inline (no pointer). Slices are contiguous arrays. Good cache performance for value types.
- **Swift:** Structs are value types (stack/inline). Classes are heap-allocated reference types.

**Why this matters:** In performance-critical code (games, HPC, databases), memory layout can be 10x more important than algorithmic complexity. Languages with value types and controlled layout (Rust, Zig, C) enable cache-friendly designs.
