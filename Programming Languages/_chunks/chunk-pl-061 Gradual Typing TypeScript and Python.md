---
tags: [chunk, programming-languages, gradual-typing]
source: "[[raw-pl-001]]"
---

# chunk-pl-061 Gradual Typing TypeScript and Python

Gradual typing lets you mix typed and untyped code in the same program.

**TypeScript:** Most successful gradual type system. ny escapes type checking. Strict mode enforces types. Structural typing — shape-based compatibility. All valid JavaScript is valid TypeScript. The type system adds information without restricting the language.

**Python type hints (PEP 484):** Optional annotations checked by external tools (mypy, pyright). No runtime enforcement by default. def greet(name: str) -> str. Growing adoption — major libraries now ship type stubs.

**Ruby Sorbet:** Gradual type checker from Stripe. sig annotations for methods. Adoption still limited compared to TypeScript/Python.

**The challenge:** Gradual types must interact safely with untyped code. At typed/untyped boundaries, runtime checks are needed to maintain safety. TypeScript handles this with ny as an explicit escape; Python relies on runtime behavior matching annotations.

The future: start dynamic for prototyping, add types where they matter, enforce in CI. The static/dynamic debate dissolves into a configuration choice.
