---
tags: [pl, chunk, wasm, component-model]
up: "[[Compilation and Runtime Overview]]"
---

# WASM Component Model Polyglot Future

The WebAssembly Component Model aims to enable cross-language composition — components written in different languages interacting through typed interfaces.

## The Vision

`
+------------------+     +------------------+     +------------------+

| Rust Component   |<--->| Python Component  |<--->| Go Component     |
| (image resize)   |     | (ML inference)    |     | (HTTP server)    |
+------------------+     +------------------+     +------------------+
        All running in the same WASM runtime, with typed interfaces
`

## WIT (WebAssembly Interface Types)

WIT defines typed interfaces between components:
`wit
package myapp:image-processor;

interface resize {
    record dimensions {
        width: u32,
        height: u32,
    }

    resize-image: func(image: list<u8>, target: dimensions) -> list<u8>;
}

world image-service {
    export resize;
}
`

## Current State (2025)

| Feature | Status | Used By |
|---------|--------|---------|
| Core WASM | Stable | All WASM runtimes |
| WASI preview 2 | Stable | wasmtime, wasmer |
| Component Model | Stabilizing | wasmtime, Spin, jco |
| WIT tooling | Growing | wit-bindgen, componentize-py |
| Language support | Variable | Rust (excellent), Go/Python/JS (growing) |

## Use Cases Already Working

1. **Fermyon Spin:** Build microservices as WASM components, mix languages per endpoint
2. **Wasmtime:** Run components with capability-based security
3. **jco:** Run WASM components in Node.js
4. **Zed editor:** Extensions are WASM components (any language)
5. **Envoy proxy:** WASM filters for request processing

## Why This Matters

The Component Model solves the polyglot microservice problem without network overhead:
- **Today:** Microservices communicate via HTTP/gRPC (serialization + network latency)
- **Future:** Components call each other directly (typed function calls, zero serialization)

## Key Insight
The WASM Component Model could be the next major shift in software architecture — enabling polyglot applications without the overhead of microservices, with the safety of sandboxing, and the portability of WASM. Rust's first-class support positions it as the primary component language.

## References
→ [[Sources Index]]
