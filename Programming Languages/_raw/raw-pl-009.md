---
tags: [raw, programming-languages, language-history]
source: "History of Programming Languages (Wexelblat, 1981), Concepts in Programming Languages (Mitchell, 2003)"
created: 2025-07-25
---

# raw-pl-009: Language History and Genealogy

## The Eras of Programming Languages

**1950s — Pioneers:** Fortran (1957, first compiler), LISP (1958, first functional language, invented GC), COBOL (1959, business computing).

**1960s — Structured Programming:** ALGOL 60 (influenced nearly every language's syntax), Simula 67 (invented objects, classes, inheritance), BASIC (1964, democratized programming).

**1970s — Systems and Theory:** C (1972, Unix), Smalltalk (1972, pure OOP), ML (1973, type inference, algebraic types), Prolog (1972, logic programming), Scheme (1975, lexical scope, continuations).

**1980s — Industrial Scale:** C++ (1985, C with classes), Erlang (1986, fault-tolerant concurrency), Objective-C (1984, C + Smalltalk), Miranda (1985, lazy functional, influenced Haskell).

**1990s — Internet Era:** Python (1991), Ruby (1995), Java (1995), JavaScript (1995), Haskell (1990), OCaml (1996), PHP (1995). The internet created demand for server-side and client-side languages.

**2000s — Modern Systems:** C# (2000), Scala (2004), D (2001), Go (2009), Clojure (2007). Response to Java complexity and C++ unsafety.

**2010s — Safety and Expressiveness:** Rust (2010/2015), Kotlin (2011/2016), Swift (2014), TypeScript (2012), Elixir (2011), Julia (2012), Zig (2016).

## Language Families

**C family (syntax):** C → C++ → Java → C# → Kotlin; C → JavaScript → TypeScript; C → Swift; C → Go; C → Rust (syntax only). Nearly every popular language uses C-derived syntax.

**ML family (type system):** ML → Standard ML → OCaml; ML → Haskell; ML → F#; ML → Rust (type system, pattern matching); ML → Swift (optionals, pattern matching).

**Lisp family:** Lisp → Scheme → Racket; Lisp → Common Lisp; Lisp → Clojure; Lisp → Emacs Lisp. Influenced JavaScript (closures, first-class functions).

**Smalltalk family (OOP):** Smalltalk → Objective-C → Swift; Smalltalk → Ruby; Smalltalk → Self → JavaScript (prototypes).

**Erlang family:** Erlang → Elixir (modern syntax on BEAM VM).

## Cross-Pollination Patterns

Every modern language is a synthesis:
- **Rust:** C++ (systems programming) + ML (type system) + Erlang (message passing influence) + Haskell (traits from type classes)
- **Kotlin:** Java (platform) + Scala (features) + C# (syntax ideas) + Groovy (pragmatism)
- **Swift:** Objective-C (platform) + Rust (value types, optionals) + Haskell (generics, protocols) + Python (clean syntax)
- **Go:** C (simplicity) + CSP (concurrency) + Pascal (packages) + Oberon (visibility rules)
