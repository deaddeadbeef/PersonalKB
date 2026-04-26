---
tags: [chunk, programming-languages, metaprogramming-comparison]
source: "[[raw-pl-006]]"
---

# chunk-pl-109 Metaprogramming Power Ranking

From least to most powerful:

**Level 1 — Annotations/Decorators:** Metadata attachment. Python decorators, Java annotations, Rust attributes. Processed by tools. Can't change semantics.

**Level 2 — Code generation:** External tools produce source code. Go generate, protobuf, OpenAPI generators. Powerful but separate build step.

**Level 3 — Reflection:** Runtime introspection. Java reflect, Python getattr, Ruby method_missing. Can inspect and modify at runtime. Bypasses type safety.

**Level 4 — Template metaprogramming:** Compile-time code generation via type system. C++ templates, D templates. Turing-complete but hard to read/debug.

**Level 5 — Compile-time execution:** Normal code runs at compile time. Zig comptime, C++ constexpr, Rust const fn. Same language for meta and regular code.

**Level 6 — Hygienic macros:** AST transformation with variable hygiene. Rust proc macros, Scheme syntax-rules, Elixir macros. Powerful with safety.

**Level 7 — Unhygienic macros + homoiconicity:** Full AST manipulation in the language's own data types. Common Lisp macros, Racket. Can redefine the language itself.

**The trade-off:** More metaprogramming power = more abstraction ability = more potential for confusion. Go chose Level 2 (external tools). Rust chose Level 6 (hygienic macros). Lisp chose Level 7 (unlimited power).
