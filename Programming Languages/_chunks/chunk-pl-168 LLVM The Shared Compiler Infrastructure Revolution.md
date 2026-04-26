---
tags: [pl, chunk, compilation, llvm]
up: "[[Compilation Pipeline Stages]]"
---

# LLVM The Shared Compiler Infrastructure Revolution

LLVM transformed compiler development by providing a shared optimization and code generation backend, enabling new languages to get production-quality compilation for free.

## Before LLVM

Each compiler was a monolith:
```
GCC: C source -> GCC frontend -> GCC optimizer -> GCC codegen -> binary
Javac: Java source -> Javac -> JVM bytecode
```

New languages had to build everything from scratch, including architecture-specific code generation for x86, ARM, etc.

## After LLVM

```
Rust source  -> rustc frontend  -+
C source     -> Clang frontend   |-> LLVM IR -> LLVM optimizer -> LLVM codegen -> binary
Swift source -> Swift frontend   |     (shared)    (shared)         (shared)
Zig source   -> Zig frontend    -+
```

## Languages Using LLVM

| Language | Frontend | Why LLVM |
|----------|----------|----------|
| Rust | rustc | Production-quality codegen from day one |
| Swift | Swift compiler | Apple invested heavily in LLVM |
| Zig | Zig compiler | Also works as C compiler via LLVM |
| Julia | Julia JIT | Scientific computing performance |
| Crystal | Crystal compiler | Ruby-like syntax, native performance |
| Nim | Nim compiler (optional) | Alternative to C codegen |
| Haskell | GHC (optional LLVM backend) | Better optimization for some patterns |

## LLVM IR (Intermediate Representation)

LLVM IR is a typed, SSA-based assembly language:
```llvm
define i32 @add(i32 %a, i32 %b) {
    %result = add i32 %a, %b
    ret i32 %result
}
```

This IR is:
- **Typed:** Catches bugs that raw assembly wouldn't
- **SSA (Static Single Assignment):** Each variable assigned exactly once
- **Target-independent:** Same IR compiles to any supported architecture

## LLVM's Impact

1. **Lowered the barrier to new languages:** Rust, Swift, Zig all exist partly because LLVM handles code generation
2. **Shared optimizations:** Every language benefits from LLVM's optimizer improvements
3. **Cross-compilation:** LLVM supports dozens of targets (x86, ARM, WASM, RISC-V, etc.)
4. **Clang/LLVM replaced GCC:** For many projects, Clang produces better code with better diagnostics
5. **Enabled LSP:** Clang's modular design led to clangd (C++ LSP) and inspired rust-analyzer

## Limitations

- **Compile time:** LLVM optimization passes are slow (contributes to Rust's compile times)
- **Binary size:** LLVM is large (~100MB), making it hard to distribute
- **Not optimal for all:** GHC's own codegen can beat LLVM for some Haskell patterns
- **Cranelift alternative:** Rust is developing Cranelift as a faster (but less optimizing) backend

## Key Insight
LLVM is one of the most important infrastructure projects in programming language history. Without it, the 2010s language renaissance (Rust, Swift, Zig, Julia) might not have happened. It proved that shared infrastructure can accelerate innovation.

## References
→ [[Sources Index]]
