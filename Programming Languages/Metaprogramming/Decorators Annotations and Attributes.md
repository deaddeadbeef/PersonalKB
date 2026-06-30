---
tags: [programming-languages, metaprogramming, decorators]
up: "[[Metaprogramming Overview]]"
tier-coverage: full
confidence: plausible
---
# Decorators, Annotations, and Attributes

## 🎯 Intuition

**The Core Idea:** Attach lightweight metadata or behavior to code elements (functions, classes, fields) that the compiler, framework, or runtime can process — without the full weight of a macro system.

**Analogy:** Decorators and attributes are like sticky-note instructions on a package — "fragile," "this side up," "refrigerate on arrival." The package itself is unchanged, but every handler along the chain reads the notes and acts accordingly. Some notes merely inform (Java annotations); others actively rewrap the contents (Python decorators).

**Why It Matters:** They hit the sweet spot of metaprogramming for everyday work — powerful enough for serialization, routing, testing, and dependency injection, yet far safer and more readable than full macro systems. Most real-world framework "magic" (Spring, Rails, Angular, SwiftUI) runs on these mechanisms.

## ⚙️ Core Mechanics

### Python Decorators

Python decorators are syntactic sugar for higher-order functions. `@decorator` before a function definition passes the function to `decorator()` and replaces it with the result.

```python
@cache
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n-1) + fibonacci(n-2)
```

This is equivalent to `fibonacci = cache(fibonacci)`. Decorators can: add logging, memoize results, enforce access control, register routes (Flask/FastAPI), validate types, and transform function behavior arbitrarily. Stacking decorators applies them bottom-up.

Python's decorator philosophy: simple function transformation with a clean syntax. No special decorator language — decorators are just functions. This aligns with Python's "functions are first-class" principle.

### Java Annotations

Java annotations (`@Override`, `@Deprecated`, `@Autowired`) attach metadata to code elements. Annotations themselves have no behavior — they're processed by:
- **Compiler:** `@Override` triggers compile-time checking
- **Annotation processors:** Generate code at compile time (Lombok, Dagger, MapStruct)
- **Frameworks at runtime:** Via reflection (Spring, JUnit, Hibernate)

Java's annotation philosophy: annotations are metadata, not code transformation. They mark intent; tools decide what to do with them. This is deliberately less powerful than macros — you can't change what annotated code does, only attach information to it.

### C# Attributes

C# attributes (in `[brackets]`) are similar to Java annotations but more integrated:
- `[Serializable]` marks classes for serialization
- `[HttpGet]` marks ASP.NET controller methods
- `[Obsolete("Use NewMethod")]` generates compiler warnings
- Custom attributes can carry complex data and be queried via reflection

C# also provides source generators (C# 9) — compile-time code generation triggered by attributes, similar to Java annotation processors but with access to the Roslyn compiler API.

### Rust Attributes and Derive

Rust uses `#[attribute]` syntax for compiler directives and proc macro triggers:
- `#[derive(Debug, Clone, Serialize)]` auto-implements traits
- `#[test]` marks test functions
- `#[cfg(target_os = "linux")]` conditional compilation
- `#[tokio::main]` transforms main into an async runtime entry point

Rust's derive macros are the most common metaprogramming mechanism in the language. `serde_derive` alone (JSON/TOML/YAML serialization) is one of the most downloaded crates, demonstrating the power of attribute-triggered code generation.

### TypeScript Decorators

TypeScript decorators (Stage 3 proposal, legacy available with `experimentalDecorators`) modify classes and their members. Used heavily in Angular (`@Component`, `@Injectable`) and NestJS (`@Controller`, `@Get`). TypeScript decorators are functions that receive the target and descriptor, similar to Python decorators.

### Swift Property Wrappers

Swift's `@propertyWrapper` mechanism allows custom types to intercept property access. `@Published` (SwiftUI), `@State`, `@Binding`, and `@AppStorage` are all property wrappers that add behavior to simple property declarations. This is a structured form of metaprogramming specific to property access patterns.

## 🔬 Deep Dive

### Trade-offs

Across languages, decorators/annotations/attributes serve the same purpose: declare intent concisely and let tooling handle the implementation. They're the "right amount" of metaprogramming for most use cases — powerful enough for common patterns (serialization, routing, testing, DI) without the complexity of full macro systems.

The spectrum of power varies significantly:

| Mechanism | Phase | Transforms Code? | Typical Use |
|---|---|---|---|
| Java Annotations | Compile-time + runtime | No (metadata only) | DI, ORM, validation |
| C# Attributes | Compile-time + runtime | Via source generators | Serialization, MVC routing |
| Python Decorators | Runtime | Yes (function wrapping) | Caching, auth, routing |
| Rust `#[derive]` | Compile-time | Yes (proc macro expansion) | Trait implementation |
| TypeScript Decorators | Runtime | Yes (descriptor mutation) | Angular/NestJS DI |
| Swift Property Wrappers | Compile-time | Yes (accessor synthesis) | SwiftUI state management |

The key tension: **metadata-only** approaches (Java annotations) are safe but require external tooling to act, while **code-transforming** approaches (Python decorators, Rust proc macros) are more powerful but can obscure what actually executes at a given call site.

### Historical Context

Java introduced annotations in Java 5 (2004) explicitly as a safer alternative to code-generation tools and marker interfaces. Python borrowed decorator syntax from Java's annotations but gave decorators real transformative power (PEP 318, Python 2.4, 2004). C# attributes predated both, shipping with .NET 1.0 (2002), though source generators that could act on them didn't arrive until C# 9 (2020). Rust's derive macros evolved from compiler-internal `#[deriving]` to the user-extensible proc-macro system stabilized in Rust 1.30 (2018), becoming the ecosystem's dominant metaprogramming tool.

## 🏋️ Practice

1. **Python decorator chain:** Write three decorators — `@log_calls` (prints function name and args), `@retry(n=3)` (retries on exception), and `@validate_types` (checks argument types at runtime). Stack all three on a single function and verify the order-of-application produces the correct behavior.

2. **Rust custom derive macro:** Create a proc-macro crate that provides `#[derive(Describe)]`, which auto-generates a `describe()` method returning a string listing every field name and type of a struct. Test it on structs with varying field counts.

3. **Java vs Python comparison:** Implement the same "route registration" pattern in both Java (using a custom annotation + reflection to build a route table at startup) and Python (using a `@route("/path")` decorator). Compare the lines of code, the discoverability of registered routes, and the error you get when a route is misconfigured.

## References

- [[Sources Index]]
