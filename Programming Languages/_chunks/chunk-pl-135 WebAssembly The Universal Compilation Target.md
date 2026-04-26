---
tags: [pl, chunk, wasm, cross-platform]
up: "[[Compilation and Runtime Overview]]"
---

# WebAssembly The Universal Compilation Target

WebAssembly is becoming what the JVM promised — a universal runtime, but language-agnostic and with near-native performance.

## WASM vs JVM vs CLR

| Property | WASM | JVM | CLR |
|----------|------|-----|-----|
| Language support | Any (C, Rust, Go, etc.) | JVM languages | .NET languages |
| GC | Optional (GC proposal) | Built-in | Built-in |
| Startup | Near-instant (AOT) | Slow (class loading) | Moderate |
| Size | Small (Rust: < 100KB) | Large (JRE) | Large (.NET runtime) |
| Sandboxing | By design | SecurityManager (deprecated) | CAS (limited) |
| Portability | Browser + server + edge | Server + desktop | Server + desktop |

## Why Rust Dominates WASM

Rust produces the smallest, fastest WASM binaries because:
1. **No GC:** No garbage collector runtime to include
2. **No runtime:** Minimal startup code
3. **LLVM backend:** Mature WASM code generation
4. **wasm-bindgen:** Generates JS interop glue automatically
5. **wasm-pack:** One command from Rust source to npm package

Typical binary sizes (hello world):
- Rust: ~20KB (with wasm-opt)
- Go: ~2MB (includes Go runtime)
- C# (Blazor): ~5MB (includes .NET runtime)
- Python (Pyodide): ~15MB (includes CPython)

## WASM Use Cases in 2025

| Use Case | Example | Why WASM |
|----------|---------|----------|
| Edge computing | Cloudflare Workers | Instant cold start, sandboxed |
| Plugin systems | Figma, Zed editor | Safe third-party code execution |
| Blockchain | Solana, Polkadot | Deterministic, auditable |
| AI inference | ONNX Runtime Web | Near-native performance in browser |
| Desktop apps | Wasm-based portable tools | Cross-platform without recompilation |

## The Component Model Future
WASM Component Model enables:
- Typed interfaces between components (WIT format)
- Cross-language function calls with zero serialization
- Hot-swappable components in running systems

## Key Insight
WASM's killer feature isn't raw performance — it's the combination of sandboxing, portability, and near-native speed. This makes it ideal for plugin systems, edge computing, and any scenario where you need to run untrusted code safely.

## References
→ [[Sources Index]]
