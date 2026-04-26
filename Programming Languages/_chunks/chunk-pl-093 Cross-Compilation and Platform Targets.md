---
tags: [chunk, programming-languages, cross-compilation]
source: "[[raw-pl-007]]"
---

# chunk-pl-093 Cross-Compilation and Platform Targets

**Go:** Best cross-compilation story. GOOS=linux GOARCH=arm64 go build from any machine. No special toolchain needed. Built-in support for all major OS/arch combinations.

**Rust:** Cross-compilation via target triples. cargo build --target aarch64-unknown-linux-gnu. Requires target-specific linker. rustup manages target installation. Good but requires more setup than Go.

**Zig:** Cross-compilation as a first-class feature. Built-in libc headers for all targets. Can cross-compile C/C++ code too. zig build -Dtarget=aarch64-linux from any machine.

**C/C++:** Cross-compilation requires target-specific toolchain (cross-compiler, sysroot, headers). Complex setup. CMake toolchain files. Docker containers commonly used to simplify.

**WebAssembly as universal target:** Compile once to Wasm, run on any platform with a Wasm runtime. Rust (wasm-pack), Go (native), C/C++ (Emscripten), Zig all support Wasm output. Wasm Component Model for module interop.

**Kotlin Multiplatform:** Compile Kotlin to JVM bytecode, JavaScript, or native (via LLVM). Platform-specific code via expect/actual. Share business logic across Android, iOS, web, and desktop.
