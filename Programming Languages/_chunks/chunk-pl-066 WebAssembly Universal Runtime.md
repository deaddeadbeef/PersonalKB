---
tags: [chunk, programming-languages, wasm]
source: "[[raw-pl-025]]"
---

# chunk-pl-066 WebAssembly Universal Runtime

WebAssembly (Wasm): portable, sandboxed bytecode format with near-native performance. Originally for browsers, expanding to server-side (WASI), edge computing, and plugins.

**Key properties:** Binary format (compact, fast to decode). Stack-based VM. Linear memory model. Sandboxed execution (no access to host unless granted). Near-native speed for compiled languages.

**Compilation targets:** C/C++ (via Emscripten), Rust (via wasm-pack, wasm-bindgen), Go (native support), Zig, AssemblyScript (TypeScript subset), Kotlin/Wasm.

**WASI (WebAssembly System Interface):** Standard API for file, network, and system access. Makes Wasm run outside browsers. Cloudflare Workers, Fastly Compute, and Fermyon use Wasm for edge computing.

**The promise:** True "write once, run anywhere" — more portable than JVM (lighter, sandboxed, no JVM installation needed). Could become the universal plugin format, replacing language-specific extension mechanisms.

**Current limitations:** No GC (coming in Wasm GC proposal), no threads (coming in threads proposal), limited debugging tools, component model still maturing.
