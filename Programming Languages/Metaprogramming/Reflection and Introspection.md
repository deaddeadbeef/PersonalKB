---
tags: [programming-languages, metaprogramming, reflection]
up: "[[Metaprogramming Overview]]"
tier-coverage: full
---

# Reflection and Introspection

## 🎯 Intuition

**The Core Idea:** Reflection allows a program to examine and modify its own structure at runtime — inspecting types, methods, and fields, and creating or modifying objects dynamically.

**Analogy:** Reflection is like a building that can read its own blueprints while people are inside it. A fully reflective language (Java, Ruby) can knock down walls and add rooms at runtime; a minimally reflective one (Go) can only read the floor plan; a non-reflective one (C, Rust) shreds the blueprints after construction is complete.

**Why It Matters:** Runtime reflection powers the frameworks that dominate enterprise development — Spring, Rails, Django, Hibernate — making dependency injection, ORM mapping, and serialization possible with minimal boilerplate. Understanding when reflection helps and when it hurts is essential for choosing the right metaprogramming strategy.

## ⚙️ Core Mechanics

### Full Reflection: Java and C\#

**Java** provides the most complete reflection system among statically typed languages via `java.lang.reflect`. You can: discover a class's methods, fields, and constructors at runtime; invoke methods by name; create instances of unknown classes; access private fields (bypassing encapsulation); and create dynamic proxies.

Java reflection powers: serialization frameworks (Jackson, Gson), dependency injection (Spring), ORM systems (Hibernate), and test frameworks (JUnit). The trade-off: reflection bypasses type safety, incurs performance overhead, and makes code harder to reason about statically.

**C# (.NET)** provides similar reflection capabilities plus a powerful metadata system (attributes). C# also offers `System.Linq.Expressions` for building and compiling code at runtime — an expression tree API that's more structured than raw reflection.

### Dynamic Language Reflection: Python and Ruby

In dynamic languages, reflection is natural because types are runtime concepts:

**Python** has pervasive introspection: `type()`, `dir()`, `getattr()`/`setattr()`, `inspect` module, `__dict__` access. Classes can be created dynamically (`type('Name', (bases,), dict)`). Metaclasses control class creation itself. Python's `__dunder__` methods (magic methods) provide hooks into nearly every language operation.

**Ruby** takes reflection further: `method_missing` intercepts calls to undefined methods, `define_method` creates methods at runtime, `eval` executes strings as code, and open classes allow modifying any class (including built-ins) at runtime. ActiveRecord (Rails) uses `method_missing` to turn database columns into Ruby methods automatically.

### Minimal Reflection: Go

Go provides limited reflection via the `reflect` package. You can inspect types and values at runtime, but the API is deliberately restricted — Go's philosophy rejects the complexity of full reflection. `reflect` is used by encoding/json, fmt, and testing, but the Go community discourages its use in application code. "Clear is better than clever."

### No Reflection: Rust, Zig, C

**Rust** has no runtime reflection (some compile-time reflection via proc macros and the `Any` trait). Types are erased after compilation via monomorphization. This aligns with zero-cost abstraction — reflection would require runtime type information, adding overhead even when unused.

**Zig** has compile-time reflection via `@typeInfo`, which returns complete type information as a compile-time value. This enables writing generic code that inspects and generates based on types — all resolved before the binary is produced.

**C** has no reflection whatsoever. Type information doesn't exist at runtime. This is consistent with C's minimal runtime philosophy.

## 🔬 Deep Dive

### Trade-offs

Reflection enables powerful frameworks (Spring, Rails, Django) but comes with costs: performance overhead, bypassed type safety, difficult static analysis, and code that's hard to trace (method calls by name don't show up in IDE navigation). The trend in modern languages is toward compile-time metaprogramming (macros, comptime) rather than runtime reflection.

| Language | Reflection Level | Runtime Cost | Type Safety | Primary Use |
|---|---|---|---|---|
| Java | Full | Moderate | Bypassed | DI, ORM, serialization |
| C# | Full + expression trees | Moderate | Bypassed (mitigated by source generators) | Frameworks, LINQ |
| Python | Pervasive | Low (dynamic anyway) | N/A (dynamic typing) | Metaclasses, introspection |
| Ruby | Pervasive + open classes | Low (dynamic anyway) | N/A (dynamic typing) | ActiveRecord, DSLs |
| Go | Minimal | Low | Mostly preserved | encoding/json, fmt |
| Rust | None (runtime) | Zero | Fully preserved | Compile-time via proc macros |
| Zig | Compile-time only | Zero | Fully preserved | `@typeInfo` generic code |
| C | None | Zero | N/A | — |

The fundamental tension: reflection trades **static guarantees** for **dynamic flexibility**. Languages that reject reflection (Rust, Zig) achieve zero-cost abstractions but require more compile-time machinery. Languages that embrace reflection (Java, Ruby) enable rapid framework development but pay in performance, debuggability, and security surface area (reflection can bypass access control).

### Historical Context

Smalltalk (1970s) pioneered reflection as a core language feature — every object could answer questions about itself, and the entire development environment was built on this capability. Java adopted a more cautious version in Java 1.1 (1997) via `java.lang.reflect`, initially for JavaBeans tooling but quickly co-opted by the framework ecosystem. Ruby's reflection model (influenced by Smalltalk) powered Rails' "convention over configuration" revolution (2004). The backlash against reflection's costs drove the modern shift toward compile-time alternatives: Rust's proc macros, Zig's `@typeInfo`, and Java's own move toward annotation processors and GraalVM native-image (which struggles with reflection).

## 🏋️ Practice

1. **Java reflection explorer:** Write a Java program that takes a fully-qualified class name as a command-line argument, uses reflection to discover all public methods and fields, and prints a formatted summary. Then call a method by name via `Method.invoke()`. Measure the performance difference between reflective and direct invocation over 1 million calls.

2. **Python metaclass exercise:** Create a metaclass `AutoRepr` that automatically generates a `__repr__` method for any class listing all its `__init__` parameters and their current values. Apply it to three different classes and verify the output. Compare your approach to using `@dataclass`.

3. **Zig compile-time reflection:** Write a Zig function that takes a `comptime` type parameter, uses `@typeInfo` to iterate over all fields of a struct, and prints each field's name and type. Verify it works on multiple struct definitions and produces no runtime overhead.

## References

- [[Sources Index]]
