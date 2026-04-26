---
tags: [pl, chunk, ffi, interop]
up: "[[Module Systems Overview]]"
---

# The C ABI as Universal Interop Layer

Nearly every programming language can call C functions, making the C ABI the de facto universal interface between languages.

## Why C Won the ABI War
1. **Simplicity:** C's calling convention is straightforward - pass values on stack/registers
2. **Ubiquity:** Every OS exposes its API as C functions
3. **No runtime:** C has no GC, no VM, no hidden state to manage
4. **Stability:** The C ABI hasn't changed in decades on any major platform

## FFI Overhead Spectrum

| Boundary | Overhead | Why |
|----------|----------|-----|
| Rust <-> C | ~0 | Same calling convention, no GC |
| Zig <-> C | ~0 | Zig can @cImport C headers directly |
| Swift <-> C | Low | Bridging header, minimal marshalling |
| Go <-> C (cgo) | Moderate | Stack switching |
| Python <-> C | Moderate | Object boxing/unboxing, GIL management |
| Java <-> C (JNI) | High | Object pinning, type marshalling |
| Java <-> C (Panama) | Low-moderate | New FFM API avoids JNI overhead |

## Key Insight
The C ABI is programming's universal connector. Language designers must decide: tight C interop (Rust, Zig) for systems use, or runtime isolation (Java, Erlang) for safety. This trade-off shapes what domains a language can serve.

## References
-> [[Sources Index]]
