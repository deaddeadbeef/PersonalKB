---
tags: [chunk, programming-languages, compilation-speed]
source: "[[raw-pl-013]]"
---

# chunk-pl-077 Compilation Speed vs Optimization

Fast compilation enables rapid iteration. Heavy optimization enables peak performance.

**Go:** Compiles millions of lines in seconds. Custom compiler (not LLVM). Simple grammar, no circular dependencies. Developer experience is the priority. Moderate optimization.

**Rust:** Compiles in minutes for large projects. LLVM backend does heavy optimization. Monomorphization generates code per type. Incremental compilation helps but large projects are slow. Performance is the priority.

**C++:** Minutes to hours. Templates, includes, heavy optimization. Build systems (CMake) add complexity. Unity builds, precompiled headers, modules (C++20) attempt to help.

**Zig:** Fast with custom backend. LLVM available for release builds. Debug builds compile fast; release builds optimize thoroughly. Best of both worlds.

**OCaml:** Fast native compilation. Much faster than Rust/C++ for comparable codebases. The OCaml compiler prioritizes compilation speed alongside code quality.

**The debug/release split:** Rust uses cranelift (fast, less optimized) for debug, LLVM (slow, highly optimized) for release. This pattern is spreading: fast iteration during development, maximum optimization for production.
