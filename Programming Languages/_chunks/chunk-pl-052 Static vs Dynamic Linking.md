---
tags: [chunk, programming-languages, linking]
source: "[[raw-pl-007]]"
---

# chunk-pl-052 Static vs Dynamic Linking

**Static linking:** Copy all library code into the executable. Single self-contained binary.
- Go: static by default. Single binary, no dependencies. Deployment = copy file.
- Rust: static for Rust stdlib. External C libraries configurable.
- Zig: static by default, including libc. Truly dependency-free binaries.
Trade-offs: larger binaries, no shared library deduplication, rebuild for library updates. But: simpler deployment, no DLL hell, reproducible.

**Dynamic linking:** Defer symbol resolution to startup/runtime. Shared libraries (.so/.dll/.dylib).
- C/C++: traditional model. Link against libc, OpenSSL, etc.
- Java: classes loaded dynamically by class loader.
- Python: extension modules (.so/.pyd) dynamically loaded.
Trade-offs: smaller binaries, shared memory, update libraries without rebuilding. But: dependency management complexity, DLL hell.

**Name mangling:** C (none - why C is FFI lingua franca), C++ (compiler-specific), Rust (crate hash + types, no stable ABI).

**The C ABI as universal bridge:** Every language's FFI calls through C conventions because C has: no mangling, no exceptions, no GC, flat memory model.
