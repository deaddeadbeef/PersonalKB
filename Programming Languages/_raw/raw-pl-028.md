---
tags: [raw, programming-languages, lisp-scheme]
source: "SICP (Abelson & Sussman), Lisp in Small Pieces (Queinnec), The Racket Guide"
created: 2025-07-25
---

# raw-pl-028: Lisp Family — The Programmable Programming Language

## Why Lisp Matters

Lisp (1958) is the most influential programming language in history relative to its market share. Lisp invented: garbage collection, dynamic typing, higher-order functions, recursion as the primary iteration mechanism, REPL-driven development, macros (code as data), and conditional expressions. Every programming language innovation can be traced back to Lisp ideas.

## Homoiconicity: The Key Insight

Lisp code is represented as lists — the same data structure the language manipulates. (+ 1 2) is both: a function call (+ applied to 1 and 2) and a list of three elements (+, 1, 2). This means macros can manipulate code exactly as functions manipulate data.

Other languages have macros, but none achieve Lisp's naturalness: Rust proc macros operate on token streams (strings, essentially); C macros operate on text; Lisp macros operate on the actual AST represented as the language's native data type.

## Macro Power and Danger

Common Lisp macros can implement entirely new language features:
- LOOP: A complete iteration facility, as a macro
- CLOS: The object system, partially implemented via macros
- WITH-OPEN-FILE: Resource management (like Python's with)

The danger: macros can make code look like a different language. A heavily macro'd Lisp codebase is a custom language — powerful for the author, impenetrable for newcomers.

## Scheme vs Common Lisp

**Scheme:** Minimalist. Lexical scope, tail call optimization, hygienic macros, continuations. Designed for teaching and research. SICP (Structure and Interpretation of Computer Programs) used Scheme to teach CS fundamentals at MIT for decades.

**Common Lisp:** Industrial. Rich standard library, CLOS (most flexible OOP system), conditions and restarts (restartable exceptions — more powerful than any other error handling mechanism), multiple values, format directives. Designed for building real systems.

## Clojure: Lisp for the Modern JVM

Rich Hickey (2007) designed Clojure with a specific thesis: **state is the root of all evil.** Clojure provides:
- Immutable persistent data structures (hash maps, vectors, sets — all immutable, structural sharing for efficiency)
- Controlled mutation via: atoms (single value), refs (coordinated, transactional), agents (asynchronous)
- JVM interop (use any Java library)
- ClojureScript (compile to JavaScript)
- REPL-driven development (the defining workflow)

## Racket: The Language Workbench

Racket (originally PLT Scheme) is designed for creating new programming languages. Its macro system supports: defining new syntax, new semantics, new type systems, and complete DSLs. Racket languages include: Typed Racket (static types), Datalog, Scribble (documentation), and Slideshow (presentations). Racket demonstrates that Lisp's programmability can extend to the language itself.

## Lisp's Influence Today

Every language with closures owes a debt to Lisp (via Scheme). JavaScript's first-class functions and closures come directly from Scheme. Ruby's blocks are Lisp-influenced. Rust's pattern matching and iterators echo Lisp's list processing philosophy. Clojure's immutable data structures influenced Immutable.js and ClojureScript.
