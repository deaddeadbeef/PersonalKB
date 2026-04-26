---
tags: [chunk, programming-languages, interop]
source: "[[raw-pl-007]]"
---

# chunk-pl-114 Language Interop Strategies

How languages work together in polyglot systems:

**C ABI bridge:** Most common. Language A calls Language B through C calling conventions. Works for: Rust <-> Python (PyO3), Go <-> C (cgo), Java <-> C (JNI/Panama), OCaml <-> C (external). Universal but lowest common denominator.

**Shared runtime (JVM):** Kotlin, Scala, Clojure, Groovy call each other's code directly. No FFI overhead. Shared type system (objects, interfaces). Java libraries accessible from all JVM languages.

**Shared runtime (.NET):** C#, F#, VB.NET interop through CLR. Similar to JVM interop.

**WASM components:** Emerging standard. Languages compile to Wasm, interop through component model. Language-agnostic interface types. Still maturing.

**IPC/RPC:** Separate processes communicate via: gRPC (protobuf), REST/JSON, message queues. No language coupling. Overhead of serialization. Standard for microservices.

**Embedding:** Python embedded in C++ (pybind11), Lua embedded in C (game scripting), JavaScript embedded in Rust (deno_core). Host language controls lifecycle.

**Transpilation:** TypeScript to JavaScript, Kotlin to JavaScript (Kotlin/JS), ClojureScript to JavaScript. Source-to-source compilation targeting a common runtime.
