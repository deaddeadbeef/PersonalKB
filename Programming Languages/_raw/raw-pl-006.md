---
tags: [raw, programming-languages, metaprogramming]
source: "Lisp in Small Pieces (Queinnec, 2003), The Rust Reference"
created: 2025-07-25
---

# raw-pl-006: Metaprogramming Mechanisms

## The Spectrum

Metaprogramming ranges from simple text substitution (C preprocessor) to full language-level AST transformation (Lisp macros). Each approach trades simplicity for power.

## C Preprocessor

Text replacement before parsing. #define, #include, #ifdef. No type checking, no hygiene, no awareness of language syntax. Dangerous but simple and universal. Most C and C++ codebases use the preprocessor extensively for conditional compilation and simple code generation.

## Lisp Macros — The Gold Standard

Lisp's homoiconicity means code IS data (lists). Macros receive code as data, transform it, return new code as data. No special macro language — macros use the full language. Common Lisp macros are unhygienic (can capture variables); Scheme macros are hygienic (automatic renaming prevents captures).

The power: you can implement any language feature as a macro. LOOP, ITERATE, CLOS method combination — all implemented via macros. The danger: overuse creates unreadable code with invisible semantics.

## Rust Macros (Declarative and Procedural)

Declarative macros (macro_rules!): Pattern matching on token trees. Hygienic. Used for: vec![], println!(), assert!().

Procedural macros: Rust functions that transform TokenStream to TokenStream. Three kinds:
1. Derive macros: #[derive(Debug, Serialize)] — auto-generate trait implementations
2. Attribute macros: #[tokio::main] — transform annotated items
3. Function-like macros: sqlx::query!() — custom syntax

Rust proc macros are extraordinarily powerful — serde, tokio, and sqlx all rely heavily on them. But they're complex to write and increase compile times.

## OCaml PPX

PPX (PreProcessor eXtensions) are compiler plugins that transform the AST. Extension points: [%name ...] and [@@name]. Common PPX: ppx_deriving (auto-derive), ppx_yojson (JSON), ppx_expect (inline expect tests). PPX provides structured metaprogramming without Lisp's full-power macro system.

## Zig Comptime

The most elegant approach: no separate macro language. Any Zig code can run at compile time with the comptime keyword. Types are first-class comptime values. Generic functions are just functions with comptime parameters. No macros needed because the language itself is the metaprogramming system.

## Reflection (Java, Python, Ruby)

Runtime introspection and modification. Java: java.lang.reflect (inspect classes, invoke methods by name). Python: getattr/setattr, __dict__, type(), metaclasses. Ruby: method_missing, define_method, open classes. Runtime metaprogramming is powerful but: bypasses type safety, hurts performance, makes code harder to analyze statically.

## Decorators/Annotations/Attributes

Lightweight metadata attachment: Python @decorator, Java @Annotation, Rust #[attribute], C# [Attribute]. Processed by compiler, framework, or runtime. Less powerful than macros but safer and more structured. The "right amount" of metaprogramming for most use cases.
