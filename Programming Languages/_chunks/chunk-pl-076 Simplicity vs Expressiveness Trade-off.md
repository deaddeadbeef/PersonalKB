---
tags: [chunk, programming-languages, simplicity-expressiveness]
source: "[[raw-pl-013]]"
---

# chunk-pl-076 Simplicity vs Expressiveness Trade-off

**Simple languages (Go, C):** Easy to learn (days to weeks). Every programmer can read every codebase. Limited abstraction — verbose for complex patterns. Go: no generics until 1.18, no exceptions, no inheritance. C: functions, structs, pointers — that's it.

**Expressive languages (Haskell, Rust, C++, Scala):** Enable concise, powerful abstractions. Expert code is remarkably compact. Steep learning curves (weeks to years). Feature interactions create complexity.

**Haskell example:** sort :: Ord a => [a] -> [a] — polymorphic sort in one line. But understanding requires: type classes, parametric polymorphism, constraints. Expert writes in minutes; beginner puzzles for hours.

**Go example:** Same sort requires explicit comparison function or type assertion. More verbose but immediately readable by any Go programmer.

**The Go bet:** Simplicity wins at scale. Google has thousands of engineers and high turnover. A language any engineer can learn in a week is more valuable than one that enables elegant abstractions.

**The Rust bet:** Expressiveness + safety wins for correctness-critical code. The learning investment pays off in fewer bugs and fearless refactoring.
