---
tags: [pl, raw, ffi, interop]
up: "[[Sources Index]]"
---

# Raw Note 032 — Language Interoperability and FFI

## Foreign Function Interface (FFI) Patterns

### C ABI as Universal Lingua Franca
Nearly every language can call C functions, making the C ABI the universal interop layer:
- **Python:** ctypes, cffi, Cython
- **Rust:** xtern "C" blocks, bindgen for auto-generation
- **Go:** cgo (with significant overhead)
- **Java:** JNI (verbose), Panama/FFM API (modern, Java 22+)
- **Haskell:** FFI pragma with explicit marshalling
- **OCaml:** C stubs with CAMLparam/CAMLreturn macros
- **Zig:** @cImport directly includes C headers
- **Swift:** C/Objective-C bridging header

### Platform-Specific Interop
- **JVM languages** (Java, Kotlin, Scala, Clojure) — seamless interop via bytecode
- **.NET languages** (C#, F#, VB.NET) — seamless interop via CLR
- **BEAM languages** (Erlang, Elixir) — seamless interop via BEAM VM
- **JavaScript/TypeScript** — TypeScript compiles to JS, seamless

### WebAssembly as New Universal Target
WASM enables cross-language interop in browsers and server-side:
- Rust, C, C++, Go, Zig compile to WASM natively
- WASI extends WASM beyond browsers
- Component Model (preview) enables typed cross-language calls

### Embedding Strategies
- **Lua** — designed to be embedded in C/C++ applications (game scripting)
- **Python** — CPython embedding API, used in Blender, Maya, etc.
- **JavaScript** — V8/SpiderMonkey embedding for Node.js, Deno, Bun
- **Wren** — small embeddable scripting language

## Performance Costs

| Boundary | Overhead | Example |
|----------|----------|---------|
| Same VM | Near zero | Java ↔ Kotlin |
| C FFI | Low (marshalling) | Rust → C |
| cgo | Moderate (goroutine stack switch) | Go → C |
| JNI | High (boxing, GC pinning) | Java → C |
| Process boundary | Very high (serialization) | Any → Any via gRPC |

## Design Patterns for Interop
1. **Thin C wrapper** — expose C ABI from any language, consume from any other
2. **Code generation** — protobuf/flatbuffers generate types in multiple languages
3. **Shared nothing** — microservices with language-agnostic protocols (HTTP, gRPC)
4. **Polyglot runtime** — GraalVM runs Java, JS, Python, Ruby, R in one VM

## References
→ [[Sources Index]]
