---
tags: [chunk, programming-languages, compilation]
source: "[[raw-pl-007]]"
---

# chunk-pl-045 LLVM and the Shared Compiler Backend

LLVM provides shared compiler infrastructure: optimization passes and code generation for multiple architectures (x86, ARM, RISC-V, WebAssembly).

**How it works:** Language frontends emit LLVM IR (a typed, SSA-form intermediate representation). LLVM optimizes the IR, then generates target-specific machine code. Write a frontend for your language, get world-class optimization for free.

**Users:** Rust (rustc), Swift (swiftc), Clang (C/C++/ObjC), Julia, Zig (optional backend), Kotlin/Native. LLVM is the most important compiler infrastructure project.

**Trade-off:** LLVM optimization is thorough but slow. Rust and C++ compile slowly partly because LLVM does heavy optimization. Go chose its own compiler for fast compilation at the cost of slightly less optimized output.

**Cranelift:** Alternative backend (used by Rust for debug builds). Faster compilation than LLVM, less optimization. The debug-build/release-build split: fast compilation for development, maximum optimization for production.
