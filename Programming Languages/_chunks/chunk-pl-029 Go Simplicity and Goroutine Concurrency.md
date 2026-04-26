---
tags: [chunk, programming-languages, go]
source: "[[raw-pl-022]]"
---

# chunk-pl-029 Go Simplicity and Goroutine Concurrency

Go's philosophy: "Less is exponentially more" (Rob Pike). Designed at Google to solve Google-scale problems.

**Fast compilation:** Millions of lines in seconds. No circular dependencies, simple grammar, custom compiler (not LLVM).

**Goroutines:** go doSomething() launches a green thread (4KB stack). M:N scheduling onto OS threads. Millions per program. Channels for typed communication. Select for multiplexing.

**Structural interfaces:** Satisfied implicitly — if a type has the right methods, it satisfies the interface. No implements keyword. Consumer-defined: the caller decides what it needs.

**Error values:** esult, err := doSomething() + if err != nil { return err }. Explicit, verbose, intentional. Every error decision visible.

**Static binary:** Single file, no dependencies. Copy and run. Transformative for deployment.

**Trade-offs:** Limited expressiveness (20 lines where Rust needs 5), no sum types, no immutability enforcement, verbose error handling. Go's simplicity is both its superpower and its limitation.
