---
tags: [chunk, programming-languages, design-philosophy]
source: "[[raw-pl-030]]"
---

# chunk-pl-027 Correctness-First vs Velocity-First

Languages optimize for different development phases:

**Correctness-first (Rust, Haskell, OCaml):** Spend more time upfront writing code that's correct from the start. Strong type systems catch errors at compile time. Slower initial development but fewer production bugs. Best for: payment systems, safety-critical software, infrastructure.

**Velocity-first (Python, Ruby, JavaScript):** Write code quickly, iterate rapidly, fix bugs as they appear. Dynamic types, minimal ceremony. Faster initial development but more runtime errors. Best for: prototyping, data science, startups finding product-market fit.

**Balanced (Kotlin, Swift, Go, TypeScript):** Moderate type safety with good ergonomics. Fast enough for rapid development, safe enough for production.

Neither is universally better. The choice depends on: cost of bugs (financial system vs personal script), team size (large teams need types as documentation), and lifecycle stage (prototype vs production).
