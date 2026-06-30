---
tags: [programming-languages, compilation, linking]
up: "[[Compilation and Runtime Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Linking and Loading

> Linking and loading bridge the gap between compiled object files and a running program — how a language handles linking affects binary size, deployment, versioning, and cross-language interoperability.

---

## 🎯 Intuition

### Core Idea

Linking resolves symbolic references between separately compiled code units and produces a runnable artifact. Loading maps that artifact into memory so the OS can execute it. The choices made at this stage — static vs dynamic, mangled vs flat symbols — ripple through every downstream concern from deployment to security patching.

### Analogy

Linking is like assembling a car from parts made in different factories. **Static linking** ships the car with all spare parts welded into the trunk — heavy, but you'll never be stranded. **Dynamic linking** assumes a parts store is nearby — the car is lighter, but you're stuck if the store closes or stocks the wrong version.

### Why It Matters

- **Deployment simplicity vs resource efficiency** — a single static binary is trivial to ship; shared libraries save disk and memory across processes.
- **Versioning and compatibility** — dynamic linking introduces "DLL hell"; static linking sidesteps it at the cost of manual updates.
- **Cross-language interop** — the linking model determines how (and whether) code written in different languages can call each other.

---

## ⚙️ Core Mechanics

### How It Works

**Static linking** copies all required library code into the final executable at build time. The result is a single self-contained binary with no external dependencies at runtime.

**Dynamic linking** defers symbol resolution to program startup or runtime. Shared libraries (`.so` on Linux, `.dll` on Windows, `.dylib` on macOS) are loaded by the operating system's dynamic linker/loader.

### Key Concepts

| Dimension | Static Linking | Dynamic Linking |
|---|---|---|
| When resolved | Build time | Load time or runtime |
| Binary size | Larger (all code embedded) | Smaller (references shared libs) |
| Deployment | Single file, copy-and-run | Must ship or ensure shared libs |
| Library updates | Requires rebuild | Swap `.so`/`.dll` in place |
| Memory sharing | No deduplication across processes | Shared pages for common libraries |
| Versioning risk | None (self-contained) | Version conflicts ("DLL hell") |
| Startup cost | Minimal | Symbol resolution overhead |
| Reproducibility | High | Depends on host environment |

### Language Examples

**Languages that favor static linking:**
- **Go:** Statically linked by default. A Go binary is a single file with no external dependencies — the entire Go runtime, standard library, and all packages are embedded. This makes deployment trivially simple: copy the binary.
- **Rust:** Statically links the Rust standard library by default. External C libraries can be statically or dynamically linked.
- **Zig:** Statically links by default, including libc. Can produce truly dependency-free binaries for any target.

**Languages that favor dynamic linking:**
- **C/C++:** The traditional model. Programs link against libc, libm, OpenSSL, etc. at runtime.
- **Java:** Classes loaded dynamically by the class loader; JARs are not linked in the C sense.
- **Python:** Extension modules (`.so`/`.pyd`) are dynamically loaded. The Python runtime itself is a shared library.

### Key Facts

**Name Mangling.** Compiled languages encode function signatures into symbol names to support function overloading:
- **C:** No mangling — function names are symbol names (why C is the lingua franca for FFI).
- **C++:** Mangles names with parameter types (varies by compiler — no standard ABI).
- **Rust:** Mangles names with module path, crate hash, and types (no stable ABI).
- **Go:** Uses package path as prefix (internal, not standardized).

**FFI (Foreign Function Interface).** The mechanism for calling code across language boundaries. The C ABI is the universal bridge:
- **Rust:** `extern "C"` functions with `#[no_mangle]`.
- **Go:** cgo wraps C functions.
- **Python:** ctypes, cffi, or C extension API.
- **Java:** JNI (Java Native Interface) or JNA.
- **OCaml:** C stubs with `external` declarations.

The C ABI's simplicity (no exceptions, no GC, no name mangling, flat memory model) makes it the lowest common denominator for language interop.

**Link-Time Optimization (LTO).** LTO defers some compiler optimizations to the linking stage, when the compiler can see all code units together. This enables cross-module inlining, dead code elimination, and global optimization. Rust, C, and C++ support LTO; Go does its own whole-program optimization during compilation.

---

## 🔬 Deep Dive

### Formal Foundations — ABI Stability

An Application Binary Interface (ABI) defines calling conventions, register usage, struct layout, and name-mangling rules at the binary level. A **stable ABI** means compiled libraries remain compatible across compiler versions without recompilation.

- **C** has a de-facto stable ABI on each platform (System V AMD64 on Linux, Microsoft x64 on Windows). This is why virtually every language provides C FFI support.
- **C++** has no cross-compiler stable ABI — Itanium ABI is widely adopted on Unix but is not a guarantee.
- **Rust** and **Go** intentionally provide no stable ABI, reserving the right to change layouts between compiler releases. Libraries must be recompiled with each compiler version.

The lack of a stable ABI in Rust and Go means libraries must be recompiled with each compiler version. C's stable ABI is why virtually every language has C FFI support.

### Trade-offs and Design Decisions

| Decision | Favors Static | Favors Dynamic |
|---|---|---|
| Containerized / embedded deploy | ✔ single binary, minimal image | |
| Shared server with many services | | ✔ memory savings via shared pages |
| Security patching at scale | | ✔ update one `.so`, all consumers patched |
| Reproducible builds / hermetic CI | ✔ no host dependency variance | |
| Plugin / extension architectures | | ✔ load at runtime without recompile |
| Cross-compilation simplicity | ✔ (Go, Zig excel here) | |

### Historical Context

Early Unix systems used only static linking (`ar` archives → `ld`). Dynamic linking appeared in SunOS 4 (1988) and became mainstream with ELF shared objects in System V Release 4. Windows introduced DLLs with Windows 1.0 (1985) but the approach matured in Win32. "DLL hell" drove innovations like Windows Side-by-Side assemblies, Linux `soname` versioning, and eventually the modern trend back toward static linking in Go, Rust, and container-native workflows.

---

## 🏋️ Practice

### Warm-Up

1. You run `ldd` on a Go binary and get "not a dynamic executable." Explain why, and name one scenario where a Go binary *would* show dynamic dependencies.
2. A C++ library compiled with GCC fails to link against a binary compiled with MSVC on Windows. What is the most likely cause, and how would you fix it?
3. Why does Rust require `#[no_mangle]` and `extern "C"` to expose a function to other languages?

### Core Problems

4. You maintain a Python extension module (`.pyd`) that wraps a Rust library via C FFI. After upgrading the Rust compiler, the extension segfaults on load. Outline a systematic debugging approach, identifying which linking-related properties could have changed.
5. Design a deployment strategy for a microservice fleet where some services are written in Go (static) and others in C++ (dynamic). Address binary size, security patching, and shared-library consistency across hosts.

### Challenge

6. Propose a scheme that gives Rust a stable ABI for a subset of types (e.g., `#[repr(C)]` structs, `extern "C"` functions) without constraining the compiler's freedom to optimize internal representations. What trade-offs does your scheme introduce compared to the current "recompile everything" model?

---

*See also:* [[Compilation and Runtime Overview]]

---

## Supporting Chunks / References

- [[Sources Index]]

## References
- [[Programming Languages/Sources/Sources Index|Programming Languages Sources Index]]
