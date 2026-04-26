---
tags: [pl, chunk, design, teaching]
up: "[[Language Genealogy Overview]]"
---

# Programming Languages for Teaching CS Education Choices

The choice of first programming language shapes how students think about computation.

## Historical Teaching Languages

| Era | Language | Why Chosen |
|-----|----------|------------|
| 1960s-70s | BASIC, Fortran | Accessible, mathematical |
| 1970s-80s | Pascal | Structured programming, clear types |
| 1980s-90s | C | Systems understanding, widespread |
| 1990s-2000s | Java | OOP teaching, industry demand |
| 2000s-10s | Python | Readability, low barrier |
| 2010s-20s | Python, Racket, Haskell | CS concepts over syntax |

## Current Dominant Choices

### Python (Most Popular)
- **Harvard CS50:** Starts with C, transitions to Python
- **MIT 6.001:** Switched from Scheme to Python (2009)
- **AP CS Principles:** Python
- Why: Low syntax overhead, immediate feedback, REPL

### Racket/Scheme (CS Theory)
- **How to Design Programs (HtDP):** Racket
- **SICP:** Originally Scheme (MIT switched away)
- Why: Teaches computational thinking without syntactic baggage

### Haskell (Functional Thinking)
- **University of Edinburgh, Stanford:** Haskell for FP courses
- Why: Forces pure thinking, strong type system as teaching tool

### Rust (Systems + Safety)
- **Growing adoption** in systems programming courses
- Why: Teaches memory management concepts without segfaults

### Java (Still Widespread)
- **AP CS A:** Java (unchanged since 2003)
- Why: Industry demand, OOP teaching, static types

## The Pedagogical Trade-off

| Priority | Best Language | Why |
|----------|--------------|-----|
| Lowest barrier | Python, Scratch | Start coding immediately |
| CS fundamentals | Racket, Scheme | Focus on concepts, not syntax |
| Type thinking | Haskell, OCaml | Types as design tool |
| Systems understanding | C, Rust | Memory, hardware awareness |
| Industry preparation | Python, Java, JS | Job market alignment |

## Key Insight
There's no single best teaching language because the goal varies. Python dominates because it minimizes friction for beginners. Racket is best for teaching computational thinking. Haskell is best for teaching type-driven design. The trend is toward Python first, then branching into domain-specific languages for advanced courses.

## References
→ [[Sources Index]]
