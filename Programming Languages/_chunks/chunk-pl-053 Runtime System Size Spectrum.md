---
tags: [chunk, programming-languages, runtime]
source: "[[raw-pl-007]]"
---

# chunk-pl-053 Runtime System Size Spectrum

**Minimal runtime (C, Zig):** C runtime: program startup, atexit, libc link. No GC, no type info. Zig can compile without libc - freestanding binaries for kernels and embedded.

**Moderate runtime (Go, OCaml):** Go: goroutine scheduler, GC, network poller, race detector (~10-20MB in binary). OCaml: generational GC, exception handling, module system. OCaml 5 adds multicore runtime.

**Heavy runtime (JVM, .NET, BEAM):** JVM: class loading, JIT compilation, multiple GC algorithms, monitoring, debugging. The most feature-rich. CLR (.NET): similar - JIT, GC, security. BEAM: process scheduler, per-process GC, distribution, hot code loading.

**Near-zero runtime (Rust):** No GC, no reflection, no green threads. Standard library has allocator and panic infrastructure. `#[no_std]` Rust runs on bare metal, in kernels, in WebAssembly.

Trade-off: larger runtimes provide more services (GC, profiling, hot code loading) at cost of memory and startup time. Smaller runtimes give control and predictability at cost of programmer responsibility.
