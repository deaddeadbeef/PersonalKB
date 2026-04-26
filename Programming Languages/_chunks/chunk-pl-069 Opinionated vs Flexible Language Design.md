---
tags: [chunk, programming-languages, opinionated]
source: "[[raw-pl-030]]"
---

# chunk-pl-069 Opinionated vs Flexible Language Design

**Opinionated (Go, Elm, Python):** One way to do things. gofmt: one formatting style, no config. Go: one error handling pattern (if err != nil). Elm: one architecture (Model-View-Update). Python: "one obvious way to do it."

Benefits: less bikeshedding, consistent codebases across teams, easier to onboard new developers, better tooling (one way to parse).

**Flexible (C++, Lisp, Scala):** Many ways to do things. C++: imperative, OOP, generic, functional — all first-class. Lisp: redefine the language with macros. Scala: full OOP + full FP, multiple syntax styles.

Benefits: powerful for experts, adaptable to diverse domains, enables domain-specific optimization. Costs: codebases vary wildly, hard to onboard, tooling must support many patterns.

**The middle ground:** Rust has opinions (ownership, error handling with Result) but flexibility within constraints (macros, trait system). Kotlin has opinions (null safety, immutability preferred) but allows escape hatches (!! for force-unwrap, var for mutability).

Go's radical opinion: simplicity itself. "Gofmt's style is no one's favorite, yet gofmt is everyone's favorite."
