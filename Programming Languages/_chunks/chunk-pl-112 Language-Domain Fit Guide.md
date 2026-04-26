---
tags: [chunk, programming-languages, domain-fit]
source: "[[raw-pl-013]]"
---

# chunk-pl-112 Language-Domain Fit Guide

Matching languages to problem domains:

**Systems programming (OS, drivers, embedded):** Rust (safe), C (legacy), C++ (performance + abstraction), Zig (simple + C interop).

**Web backend:** Go (simple, concurrent), Java/Kotlin (enterprise), Python (rapid development), Elixir (real-time), Rust (performance-critical).

**Web frontend:** TypeScript (dominant), JavaScript (universal), Elm (correctness), Dart (Flutter).

**Data science/ML:** Python (ecosystem), R (statistics), Julia (performance), SQL (data).

**Mobile:** Kotlin (Android), Swift (iOS), Dart/Flutter (cross-platform), Kotlin Multiplatform.

**Financial systems:** OCaml (Jane Street), Haskell (correctness), Java (enterprise), C++ (low-latency trading).

**Compilers and language tools:** OCaml (tradition), Rust (modern), Haskell (research), C++ (legacy like GCC, LLVM).

**Cloud infrastructure:** Go (Docker, K8s, Terraform). The one domain where Go has near-monopoly.

**Real-time messaging:** Erlang/Elixir (WhatsApp, Discord). BEAM's concurrency model is unmatched.

**Game engines:** C++ (Unreal), Rust (emerging), Zig (emerging). Performance and memory control are critical.

Key insight: the "best" language depends on the domain, team, and constraints. No language is universally best.
