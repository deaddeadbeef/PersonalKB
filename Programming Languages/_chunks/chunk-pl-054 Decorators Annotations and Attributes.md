---
tags: [chunk, programming-languages, decorators]
source: "[[raw-pl-006]]"
---

# chunk-pl-054 Decorators Annotations and Attributes

Lightweight metaprogramming: attach metadata to code elements for processing.

**Python decorators:** Syntactic sugar for higher-order functions. `@cache` wraps function. `@app.route("/")` registers routes. Stacking applies bottom-up. Simple - decorators are just functions.

**Java annotations:** `@Override`, `@Autowired`, `@Deprecated`. No behavior - metadata processed by: compiler, annotation processors (Lombok, Dagger), or runtime (Spring, JUnit via reflection).

**Rust attributes:** `#[derive(Debug, Serialize)]` auto-implements traits. `#[test]` marks tests. `#[cfg(target_os)]` conditional compilation. `#[tokio::main]` transforms main. Derive macros are the most common Rust metaprogramming.

**TypeScript decorators:** `@Component`, `@Injectable` (Angular). Functions receiving target and descriptor. Stage 3 proposal.

**Swift property wrappers:** `@Published`, `@State`, `@Binding`. Custom types intercepting property access. Powers SwiftUI reactivity.

Pattern across all: declare intent concisely, let tooling handle implementation. The "right amount" of metaprogramming for common patterns.
