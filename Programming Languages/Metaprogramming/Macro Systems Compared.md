---
tags: [programming-languages, metaprogramming, macros]
up: "[[Metaprogramming Overview]]"
tier-coverage: full
---

# Macro Systems Compared

## 🎯 Intuition

**The Core Idea:** Macros are compile-time code transformations — they take code as input and produce code as output before the compiler sees it.

**Analogy:** A macro system is like a ghostwriter who rewrites your rough draft into polished prose before anyone reads it. A C preprocessor ghostwriter does crude find-and-replace; a Lisp ghostwriter understands the story's structure and can rewrite entire plot arcs; a Rust ghostwriter works under strict editorial guidelines (hygiene) so the final text never contradicts itself.

**Why It Matters:** The design of a macro system is one of the most consequential decisions in language design. It determines how much a community can extend the language itself — from simple boilerplate reduction to embedding entirely new DSLs — and how much complexity that power inflicts on readers and tooling.

## ⚙️ Core Mechanics

### C Preprocessor: Text Substitution

The C preprocessor operates on text before parsing. `#define MAX(a,b) ((a)>(b)?(a):(b))` replaces text literally. Problems: no type checking, no hygiene (variables can clash), multiple evaluation (`MAX(i++, j++)` increments twice), and debugging shows preprocessed code, not what you wrote. Despite being primitive, the C preprocessor remains widely used because it's simple and universally available.

### Lisp Macros: Code as Data

Lisp's homoiconicity (code is represented as data structures — lists) makes macros natural. A Lisp macro is a function that receives code as a data structure, transforms it, and returns new code as a data structure. This is the most powerful macro system: macros can analyze their arguments, generate arbitrarily complex code, and implement entirely new language constructs.

Common Lisp macros are **unhygienic** — they can intentionally or accidentally capture variables from the call site. This is powerful (anaphoric macros) but dangerous (subtle naming collisions). The `gensym` function generates unique symbols to avoid captures.

Scheme's `syntax-rules` and `syntax-case` provide **hygienic macros** — the system automatically renames variables to prevent unintended capture. This trades some power for safety.

### Rust's Macro System

Rust provides two kinds of macros:

**Declarative macros (macro_rules!):** Pattern matching on token trees. You define patterns and their expansions. These are hygienic (can't capture ambient variables) and operate on Rust syntax tokens. Useful for reducing boilerplate: `vec![1, 2, 3]` is a macro that expands to allocation code.

**Procedural macros:** Rust functions that receive a TokenStream and return a TokenStream. Three types: derive macros (auto-implement traits), attribute macros (transform annotated items), and function-like macros. These are immensely powerful — `serde_derive`, `tokio::main`, and `sqlx::query!` are proc macros that generate complex code at compile time.

Rust's macro design philosophy: macros should be hygienic by default, type-checked after expansion, and clearly marked at call sites (the `!` suffix). Proc macros run arbitrary Rust code at compile time but are confined to separate crates for safety.

### Elixir Macros

Elixir inherits Lisp-style macros with Erlang's runtime. Macros operate on Elixir's AST (represented as tuples). The `quote`/`unquote` mechanism creates and splices AST fragments. Elixir macros power: the pipe operator, pattern matching in function heads, and the Phoenix web framework's routing DSL. Elixir's philosophy: macros should create clean DSLs, not obfuscate code.

### OCaml PPX (PreProcessor eXtensions)

OCaml uses PPX — compiler plugins that transform the AST at compile time. PPX extensions hook into special syntax (`[%name ...]` and `[@@name]`) to trigger transformations. Common uses: `ppx_deriving` (auto-derive functions like show, eq, compare), `ppx_jane` (Jane Street's production extensions), and test frameworks. PPX is less ad-hoc than Lisp macros but more powerful than simple decorators.

### Languages That Reject Macros

**Go** has no macros — `go generate` runs external tools. The philosophy: macros create non-obvious code; explicit code is always better.
**Java** has no macros — annotation processors generate new files but can't modify existing ones.
**Python** has no macros — metaclasses and decorators provide limited compile-time control.

## 🔬 Deep Dive

### Trade-offs

The central tension in macro design is **power vs. safety**:

| System | Input | Hygiene | Power | Typical Risk |
|---|---|---|---|---|
| C Preprocessor | Raw text | None | Low | Silent mis-expansion, double evaluation |
| Common Lisp | S-expressions (AST) | None (manual `gensym`) | Highest | Accidental variable capture |
| Scheme `syntax-rules` | S-expressions (AST) | Automatic | High | Reduced flexibility for intentional capture |
| Rust `macro_rules!` | Token trees | Automatic | Medium | Opaque error messages on mismatch |
| Rust proc macros | TokenStream | Manual care | High | Compile-time code execution in separate crate |
| Elixir | AST tuples | `quote`/`unquote` scoping | High | Overuse obscures control flow |
| OCaml PPX | Typed AST | Compiler-enforced | Medium–High | Tooling complexity, version coupling |

Hygiene prevents the most common macro bug — unintended variable capture — but unhygienic macros (Common Lisp) enable patterns like anaphoric macros (`aif`, `awhen`) that hygienic systems struggle to express cleanly.

### Historical Context

The C preprocessor (1972) set the floor: macros as textual find-and-replace, inherited from assembly. Lisp macros (1960s) set the ceiling: code-as-data transformations limited only by programmer imagination. Every subsequent macro system occupies a point between these poles. Scheme (1975) introduced hygiene. Rust (2015) combined hygiene with the proc-macro escape hatch for full generality. Languages that reject macros entirely (Go, Java) represent a deliberate bet that explicitness outweighs extensibility — a bet validated by Go's commercial success but contested by communities that value DSL-driven development.

## 🏋️ Practice

1. **C macro pitfall lab:** Write a C macro `SQUARE(x)` as `#define SQUARE(x) x*x`. Call it with `SQUARE(1+2)` and observe the incorrect result. Fix it with parentheses, then write a second version as a `static inline` function and compare the generated assembly.

2. **Rust declarative macro:** Implement a `hashmap!` macro using `macro_rules!` that accepts `hashmap!{ "a" => 1, "b" => 2 }` syntax and expands to a `HashMap` with those entries. Test that it works with different key/value types and empty input.

3. **Lisp vs Rust comparison:** In Common Lisp, write a `when-let` macro that binds a variable and executes a body only if the binding is non-nil. Then implement the same pattern in Rust using `macro_rules!`. Compare the two implementations for readability, hygiene, and error messages when misused.

## References

- [[Sources Index]]
