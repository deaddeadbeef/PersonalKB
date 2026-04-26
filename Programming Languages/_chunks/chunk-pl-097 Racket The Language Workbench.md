---
tags: [chunk, programming-languages, racket]
source: "[[raw-pl-028]]"
---

# chunk-pl-097 Racket The Language Workbench

Racket (originally PLT Scheme): a platform for creating programming languages.

**Language-oriented programming:** Instead of writing programs in a general-purpose language, create a language tailored to your domain, then write programs in that.

**The macro system:** Racket's syntax transformers can define: new syntax, new binding forms, new module systems, new type systems. More powerful than Common Lisp macros because they integrate with the module system and IDE.

**Languages built in Racket:**
- **Typed Racket:** Static types added to Racket, with gradual typing
- **Datalog:** Logic programming as a Racket language
- **Scribble:** Documentation language
- **Slideshow:** Presentation language
- **Hackett:** Haskell-like language with Racket's macro system

**#lang directive:** Every Racket file starts with #lang specifying its language. #lang racket, #lang typed/racket, #lang datalog — different languages in the same ecosystem, sharing tooling.

**Educational impact:** Used at many universities for teaching programming languages. "How to Design Programs" uses Racket. DrRacket IDE designed for learners.

Racket demonstrates that Lisp's programmability extends to the language itself — you can redefine not just what programs do, but what programming looks like.
