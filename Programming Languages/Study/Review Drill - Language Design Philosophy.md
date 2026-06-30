---
tags: [pl, study, design-philosophy]
up: "[[Programming Languages Study Index]]"
confidence: policy
---
# Review Drill — Language Design Philosophy

## Quick Recall

1. What is the "explicit vs implicit" spectrum? Place Go, Python, Rust, and Haskell on it.
2. What does "zero-cost abstraction" mean? Which languages promise it?
3. Explain "correctness-first" vs "velocity-first" design. Give 2 languages for each.
4. What is "batteries included" vs "minimal core"? Compare Python and Go vs Rust and Haskell.
5. Name 3 languages designed by committee vs 3 designed by small teams. How do they differ?

## Deep Dive Questions

### Design Trade-offs
- Why did Go deliberately omit generics until 1.18? What does this reveal about language design priorities?
- How does Rust's steep learning curve relate to its "make illegal states unrepresentable" philosophy?
- Why does Python's "one obvious way to do it" sometimes conflict with its multi-paradigm nature?
- How does Zig's "no hidden control flow" philosophy compare to C++'s operator overloading?

### Language Character
- What makes a language "opinionated"? Compare Go's gofmt vs JavaScript's ecosystem of formatters.
- How does Ruby's "programmer happiness" manifest in its syntax and conventions?
- Why did Haskell choose purity as a default? What are the practical consequences?
- How does Erlang's telecom heritage shape its design differently from Java's enterprise heritage?

### Evolution and Convergence
- Are programming languages converging? What features are appearing in nearly all modern languages?
- How do languages balance backward compatibility with improvement? Compare Java, Python, and Rust.
- What happens when a language adds a feature that contradicts its original philosophy?
- Why do some languages succeed despite "worse" designs (JavaScript, PHP)?

### Trust and Safety
- Compare C's "trust the programmer" vs Rust's "trust but verify" vs Java's "protect the programmer."
- How does the safety spectrum affect adoption in different domains (systems, web, finance)?
- What is the relationship between type safety and memory safety?

## Mental Models

### The Design Space Compass
`
           Correctness

               |
    Haskell  Rust

               |
Explicit ------+------ Implicit

               |
      Go     Python

               |
           Velocity
`

### Language Philosophy Archetypes
- **The Purist**: Haskell — mathematical correctness above all
- **The Pragmatist**: OCaml, Kotlin — practical with principled foundations
- **The Minimalist**: Go, C — small language, big standard library
- **The Maximalist**: C++, Scala — every feature you could want
- **The Rebel**: Rust — rewrites the rules of systems programming

## Connections to Explore
- [[Programming Paradigms Overview]] — paradigm foundations
- [[Language Genealogy Overview]] — historical context
- [[Language Profiles Overview]] — per-language details

## References
→ [[Sources Index]]
