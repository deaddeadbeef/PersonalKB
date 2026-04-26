---
tags: [chunk, programming-languages, metaprogramming]
source: "[[raw-pl-006]]"
---

# chunk-pl-017 Macro Systems Across Languages

**C preprocessor:** Text substitution. No type checking, no hygiene. Simple but dangerous.

**Lisp macros:** Code IS data (homoiconicity). Macros transform ASTs as naturally as functions transform data. Most powerful macro system. Common Lisp: unhygienic (can capture variables). Scheme: hygienic (automatic renaming).

**Rust macros:** Declarative (macro_rules! — pattern matching on tokens, hygienic) and procedural (Rust functions transforming TokenStream). Proc macros power: serde, tokio, sqlx. Extremely powerful but complex and slow to compile.

**OCaml PPX:** Compiler plugins transforming AST at extension points. Structured metaprogramming.

**Zig comptime:** No separate macro language. Normal code executes at compile time. The most elegant approach.

**Languages rejecting macros:** Go (go generate — external tools), Java (annotation processors), Python (no macros — metaclasses and decorators instead). Philosophy: macros create non-obvious code.
