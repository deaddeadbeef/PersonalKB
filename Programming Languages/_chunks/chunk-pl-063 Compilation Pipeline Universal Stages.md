---
tags: [chunk, programming-languages, compilation-pipeline]
source: "[[raw-pl-007]]"
---

# chunk-pl-063 Compilation Pipeline Universal Stages

Every compiler follows the same fundamental pipeline:

**Lexing:** Characters -> tokens. Keywords, identifiers, literals, operators become discrete units. Most languages use regex-based lexers; Python needs context-sensitive (significant whitespace).

**Parsing:** Tokens -> AST. Recursive descent (most modern compilers — better error messages) or parser generators (yacc, ANTLR).

**Semantic analysis:** Type checking, name resolution, overload resolution. Where most language complexity lives. Haskell's type inference, Rust's borrow checking, C++'s template instantiation — all happen here.

**IR generation:** AST -> intermediate representation. Simpler than source, closer to machine code. Multiple IRs common: Rust: HIR -> MIR -> LLVM IR.

**Optimization:** Transform IR to faster/smaller equivalent. Dead code elimination, constant folding, inlining, vectorization. LLVM provides shared optimization infrastructure.

**Code generation:** IR -> machine code (x86, ARM) or bytecode (JVM, Wasm). Backend-specific optimizations.

**Linking:** Combine object files into executable. Static (copy into binary) or dynamic (resolve at load time).
