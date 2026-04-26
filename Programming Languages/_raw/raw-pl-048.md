---
tags: [pl, raw, wasm, webassembly, cross-platform]
up: "[[Sources Index]]"
---

# Raw Note 048 – WebAssembly and Cross-Platform Targets

## WebAssembly Overview

WebAssembly (WASM) is a portable binary instruction format for a stack-based virtual machine, designed as a universal compilation target.

### WASM Properties
- **Sandboxed:** No direct access to host OS resources
- **Portable:** Same binary runs on any WASM runtime
- **Near-native speed:** AOT or JIT compiled to machine code
- **Language-agnostic:** Any language can target WASM

## Language Support for WASM

| Language | WASM Support | Maturity | Output Size |
|----------|-------------|----------|-------------|
| Rust | Excellent | Production | Small (wasm-pack) |
| C/C++ | Excellent | Production | Medium (Emscripten) |
| Go | Good | Production | Large (runtime included) |
| Zig | Excellent | Good | Very small |
| AssemblyScript | Native | Good | Small (TypeScript-like) |
| C# | Good | Production | Large (Blazor) |
| Kotlin | Good | Growing | Medium (Kotlin/Wasm) |
| Swift | Experimental | Early | Large |
| Python | Growing | Experimental | Large (Pyodide) |
| Haskell | Experimental | Early | Large (GHC WASM backend) |

### Why Rust Dominates WASM
1. No garbage collector → smaller binaries, no runtime overhead
2. Fine-grained control over memory layout
3. wasm-bindgen generates JS interop automatically
4. Excellent tooling: wasm-pack, trunk, leptos, yew

## WASI (WebAssembly System Interface)

WASI extends WASM beyond browsers with a capability-based system interface:
- File system access (sandboxed)
- Network sockets
- Clocks, random numbers
- Environment variables

### WASI Use Cases
- **Serverless/Edge:** Cloudflare Workers, Fastly Compute, Fermyon Spin
- **Plugin systems:** Envoy filters, Figma plugins, Zed extensions
- **Portable CLI tools:** Run anywhere with wasmtime run

## Component Model

The WASM Component Model (in development) enables:
- **Typed interfaces:** Define APIs with WIT (WASM Interface Type)
- **Cross-language composition:** Rust component calls Python component
- **Sandboxed plugins:** Host controls what guests can do

## Other Cross-Platform Targets

| Target | Languages | Use Case |
|--------|-----------|----------|
| LLVM IR | Rust, C/C++, Swift, Zig | Shared optimizer backend |
| JVM bytecode | Java, Kotlin, Scala, Clojure | JVM ecosystem |
| .NET IL | C#, F#, VB.NET | .NET ecosystem |
| BEAM bytecode | Erlang, Elixir, Gleam | BEAM VM |
| JavaScript | TypeScript, Elm, PureScript, Dart | Browser target |

## Key Insight
WASM is becoming the "write once, run anywhere" that Java promised but for all languages. Rust's zero-overhead model makes it the ideal WASM source language, but the Component Model will enable polyglot WASM applications where each component uses the best language for its task.

## References
→ [[Sources Index]]
