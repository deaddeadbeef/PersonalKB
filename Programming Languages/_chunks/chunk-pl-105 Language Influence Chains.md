---
tags: [chunk, programming-languages, generational]
source: "[[raw-pl-009]]"
---

# chunk-pl-105 Language Influence Chains

Tracing ideas through language genealogy:

**Type inference chain:** ML (1973) -> Standard ML -> OCaml -> Haskell -> Rust (local inference) -> Kotlin (local) -> Swift (local) -> Java 10 (var) -> Go (:=)

**Pattern matching chain:** ML -> Haskell -> OCaml -> Scala -> Rust -> Swift -> Kotlin -> Java 21 -> Python 3.10

**Null safety chain:** ML (option type, 1973) -> Haskell (Maybe) -> OCaml (option) -> Scala (Option) -> Kotlin (T?) -> Swift (Optional) -> Rust (Option<T>)

**GC chain:** Lisp (1958, invented GC) -> Smalltalk -> Java -> Go -> OCaml. Non-GC: C -> C++ (RAII) -> Rust (ownership) -> Zig (allocators)

**Concurrency chain:** CSP (Hoare, 1978) -> occam -> Go (goroutines + channels). Actor model: Hewitt (1973) -> Erlang -> Akka -> Swift actors.

**Closure chain:** Lisp (1958) -> Scheme (1975, lexical closures) -> ML -> JavaScript -> Ruby -> Python -> Java 8 -> C++11 -> Go

**The meta-pattern:** Ideas flow from research languages (ML, Haskell, Scheme) to pragmatic languages (OCaml, Erlang) to mainstream languages (Rust, Kotlin, Swift) to industrial languages (Java, C#, Python). Each step makes the idea more accessible but less pure.
