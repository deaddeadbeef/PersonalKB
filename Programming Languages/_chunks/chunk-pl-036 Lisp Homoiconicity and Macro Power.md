---
tags: [chunk, programming-languages, lisp]
source: "[[raw-pl-028]]"
---

# chunk-pl-036 Lisp Homoiconicity and Macro Power

**Homoiconicity:** Lisp code is represented as lists — the same data structure the language manipulates. (+ 1 2) is both a function call AND a list of three elements. Macros transform code-as-data as naturally as functions transform data.

**Common Lisp:** Feature-rich. CLOS (most flexible OOP ever), conditions/restarts (restartable exceptions — more powerful than any other error handling), LOOP macro (iteration DSL implemented via macros).

**Scheme:** Minimalist. Lexical scope, tail call optimization, hygienic macros, continuations. SICP used Scheme to teach CS at MIT.

**Clojure (2007):** Modern JVM Lisp. Rich Hickey's thesis: "state is the root of all evil." Immutable persistent data structures, controlled mutation (atoms, refs, agents), JVM interop.

**Racket:** Language workbench. Macro system can define entirely new languages with custom syntax and semantics.

**Lisp's influence today:** Every language with closures owes Lisp. JavaScript's first-class functions from Scheme. Immutable data structures from Clojure. The concept of macros-as-code-transformation from Lisp. Lisp invented GC, dynamic typing, REPL, higher-order functions, and conditional expressions.
