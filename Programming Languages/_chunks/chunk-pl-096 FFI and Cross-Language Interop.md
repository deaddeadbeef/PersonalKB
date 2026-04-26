---
tags: [chunk, programming-languages, ffi]
source: "[[raw-pl-007]]"
---

# chunk-pl-096 FFI and Cross-Language Interop

Foreign Function Interface (FFI): calling code across language boundaries. The C ABI is the universal bridge.

**Rust -> C:** xtern "C" fn with #[no_mangle]. cbindgen generates C headers from Rust. Rust libraries can expose C API while being written safely in Rust.

**Go -> C:** cgo wraps C functions. // #include <header.h> in Go comments. cgo has overhead (goroutine stack switch). Pure Go preferred when possible.

**Python -> C:** ctypes (call C shared libraries), cffi (higher-level), C extension API (fastest, most complex), pybind11 (C++ to Python), Cython (Python-like syntax compiled to C).

**Java -> C:** JNI (Java Native Interface) — verbose, error-prone. JNA (Java Native Access) — simpler, reflection-based. Panama (Java 22) — modern FFI without JNI boilerplate.

**OCaml -> C:** External declarations with C stubs. xternal add : int -> int -> int = "caml_add". Straightforward for simple functions, manual for complex data structures.

**Why C ABI wins:** No mangling, no exceptions, no GC, flat memory model. Simplest possible calling convention. Every language can implement it.
