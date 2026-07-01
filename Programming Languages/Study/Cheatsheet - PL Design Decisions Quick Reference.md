---
tags: [pl, study, cheatsheet]
up: "[[Programming Languages Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---
# Cheatsheet — PL Design Decisions Quick Reference

> **One-line summary:** A compact comparison sheet for programming-language design choices across type systems, memory management, concurrency, errors, modules, runtimes, and paradigms.

## Type System Quick Compare

| Language | Static/Dynamic | Inference | Generics | Null Safety |
|----------|---------------|-----------|----------|-------------|
| C | Static (weak) | None | None (void*) | No |
| C++ | Static | Auto/decltype | Templates + Concepts | No |
| Java | Static | Limited (var) | Erasure | Optional class |
| Python | Dynamic | N/A | Type hints (gradual) | No |
| JS/TS | Dynamic/Gradual | TS infers | TS generics | TS strict mode |
| Go | Static | := shorthand | Go 1.18+ | No |
| Rust | Static | Full HM-based | Monomorphized | Option type |
| OCaml | Static | Full HM | Parametric | Option type |
| Haskell | Static | Full HM | Parametric + HKT | Maybe type |
| Erlang | Dynamic | N/A | N/A | No |
| Lisp | Dynamic | N/A | N/A | No |
| Swift | Static | Good | Protocols + Associated Types | Optionals |
| Kotlin | Static | Good | Reified + Declaration-site variance | Built-in null safety |
| Ruby | Dynamic | N/A | N/A (RBS type hints) | No |
| Zig | Static | Limited | Comptime generics | Optional type |

## Memory Model Quick Compare

| Language | Strategy | GC Type | Manual Control | Safety Level |
|----------|----------|---------|----------------|-------------|
| C | Manual | None | Full | Unsafe |
| C++ | RAII + Manual | None | Full | Unsafe (safe subset) |
| Java | GC | Generational (G1/ZGC) | None | Safe |
| Python | GC + RC | Reference counting + cycle collector | None | Safe |
| Go | GC | Concurrent tri-color | None | Safe |
| Rust | Ownership | None | Unsafe blocks | Safe by default |
| OCaml | GC | Generational | None | Safe |
| Haskell | GC | Generational | None | Safe |
| Erlang | GC | Per-process | None | Safe |
| Swift | ARC | Reference counting | Unowned/weak | Safe |
| Zig | Manual | None | Full (allocator API) | Unsafe (safety checks) |

## Concurrency Model Quick Compare

| Language | Primary Model | Mechanism | Data Race Prevention |
|----------|--------------|-----------|---------------------|
| C | Threads | pthreads | None (programmer responsibility) |
| C++ | Threads + Virtual | std::thread + async | Atomic types, mutexes |
| Java | Threads + Virtual | synchronized, Loom | Monitors, volatile |
| Python | Async | asyncio + GIL | GIL prevents true parallelism |
| Go | CSP | Goroutines + channels | Race detector (runtime) |
| Rust | Multi-model | Send/Sync + async | Compile-time (ownership) |
| Haskell | STM | STM + forkIO | Type system (IO monad) |
| Erlang | Actors | Processes + messages | No shared state |
| Swift | Actors | Swift actors + async/await | Actor isolation |
| Kotlin | Coroutines | Structured concurrency | Coroutine scope |

## Error Handling Quick Compare

| Language | Primary Strategy | Types | Philosophy |
|----------|-----------------|-------|-----------|
| C | Error codes | int return values | Check yourself |
| C++ | Exceptions | try/catch/throw | Don't pay for what you don't use |
| Java | Checked + unchecked exceptions | Exception hierarchy | Enforce handling |
| Python | Exceptions | try/except | EAFP |
| Go | Multi-return | error interface | Explicit, verbose |
| Rust | Result + Option | Result<T,E>, Option<T> | Make illegal states unrepresentable |
| Haskell | Maybe + Either | Maybe a, Either e a | Compose with monads |
| Erlang | Let it crash | exit/throw/error | Supervisors recover |
| Swift | Throws + Optionals | throws, Optional, Result | Tiered severity |
| Kotlin | Exceptions + nullability | Nothing type, ?. operator | Pragmatic safety |
| Zig | Error unions | error!type | Explicit with payload |

## Philosophy One-Liners

| Language | Core Philosophy |
|----------|----------------|
| C | Trust the programmer, stay close to hardware |
| C++ | Zero-cost abstractions, you don't pay for what you don't use |
| Java | Write once, run anywhere, safety through the JVM |
| Python | Readability counts, one obvious way to do it |
| JavaScript | The language of the web, everything is an object |
| Go | Simplicity is complicated, less is exponentially more |
| Rust | Safety without sacrifice, fearless concurrency |
| OCaml | Practical rigor, real-world functional programming |
| Haskell | Avoid success at all costs, purity enables reasoning |
| Erlang | Let it crash, the system must never stop |
| Lisp | Code is data, programmable programming language |
| Swift | Safe, fast, and expressive for Apple platforms |
| Kotlin | Modern Java done right, pragmatic and concise |
| Ruby | Optimized for programmer happiness |
| Zig | No hidden control flow, simple is better |

## References
→ [[Programming Languages/Sources/Sources Index|Sources Index]]
