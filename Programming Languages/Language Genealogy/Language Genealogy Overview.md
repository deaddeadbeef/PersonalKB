---
tags: [programming-languages, genealogy]
up: "[[Programming Languages]]"
---

# Language Genealogy Overview

Programming languages evolve through a process of inheritance, reaction, and synthesis. Each new language emerges from specific frustrations with existing tools and embodies a set of design beliefs about how programmers should work. Understanding this genealogy reveals why languages are designed the way they are.

## Major Language Families

### The ALGOL Family (Structured Programming)
ALGOL 60 (1960) established block structure, lexical scoping, and the BNF grammar notation. Nearly every mainstream language descends from ALGOL's structural ideas. Key descendants: Pascal, C, and through C, virtually all modern systems languages (C++, Java, C#, Go, Rust, Swift, Kotlin, Zig).

### The Lisp Family (Symbolic Computation)
Lisp (1958) introduced garbage collection, dynamic typing, first-class functions, and the radical idea of code-as-data (homoiconicity). The Lisp family includes Scheme (minimalist, lexical scoping), Common Lisp (pragmatic, multi-paradigm), Clojure (JVM, persistent data structures), and Racket (language-oriented programming). Lisp's influence extends far beyond its family — lambda expressions in Java/C++/Python/Ruby all trace back to Lisp.

### The ML Family (Type-Theoretic)
ML (1973) pioneered Hindley-Milner type inference, algebraic data types, and pattern matching. Its descendants include Standard ML, OCaml (adding OOP and modules), Haskell (adding purity and lazy evaluation), F# (.NET ML), and Elm (web frontend). Rust's type system borrows heavily from ML family innovations.

### The Smalltalk Family (Object-Oriented)
Smalltalk (1972) defined pure OOP: everything is an object, everything happens via message passing. It influenced Objective-C, Ruby, and the broader OOP movement in Java and C++. Smalltalk also pioneered the IDE, MVC architecture, and live-coding environments.

### The Erlang Family (Concurrent/Fault-Tolerant)
Erlang (1986) brought the actor model to practical systems programming with lightweight processes, message passing, and the "let it crash" philosophy. Elixir (2011) brought modern syntax and metaprogramming to the BEAM VM while preserving Erlang's concurrency model.

## Cross-Family Influence Patterns

- [[PL History and Eras]]
- [[Language Family Trees]]
- [[Influence Chains and Cross-Pollination]]
- [[The Rise of Multi-Paradigm Languages]]

## References

- [[Sources Index]]
