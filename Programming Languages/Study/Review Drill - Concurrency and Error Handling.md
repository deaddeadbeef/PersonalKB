---
tags: [pl, study, concurrency, error-handling]
up: "[[Programming Languages Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---
# Review Drill — Concurrency and Error Handling

## Quick Recall — Concurrency

1. Name the 4 main concurrency models and one language that champions each.
2. What is CSP? How do Go's goroutines and channels implement it?
3. Explain the Actor model. How does Erlang's "let it crash" philosophy work?
4. What is async/await? Compare implementations in Rust, Python, JS, and C#.
5. What is STM? Why is it only practical in Haskell?

## Deep Dive — Concurrency

### Shared State vs Message Passing
- Why does Rust allow shared mutable state but Erlang forbids it entirely?
- How does Go's "share memory by communicating" differ from Java's synchronized blocks?
- What makes Erlang's per-process heaps unique among concurrent runtimes?

### Async Models
- Why is Rust's async zero-cost but requires Pin and manual executor choice?
- How does JavaScript's single-threaded event loop handle concurrency without parallelism?
- Compare colored functions (JS, Python) vs Zig's approach to async.

### Advanced Patterns
- What are supervision trees? How does OTP use them for fault tolerance?
- Explain structured concurrency (Kotlin coroutines, Java Loom).
- How does Haskell's STM compose transactions that threads/locks cannot?

## Quick Recall — Error Handling

1. Name 4 error handling strategies and one language that uses each.
2. What is the Result/Option pattern? How does Rust's ? operator work?
3. How do exceptions work? Why did Go and Rust reject them?
4. What is panic vs recoverable error separation?
5. What are algebraic effects for error handling?

## Deep Dive — Error Handling

### Exception-Based
- Why do Java's checked exceptions exist? Why did Kotlin and C# drop them?
- How does Python's EAFP (Easier to Ask Forgiveness than Permission) work?
- What performance cost do exceptions have in the happy path vs error path?

### Result Types
- Trace the evolution: C error codes → Go multi-return → Rust Result<T,E> → Zig error unions.
- How does Haskell's Maybe/Either differ from Rust's Option/Result?
- Why is the ? operator in Rust considered a language design triumph?

### Design Philosophy
- Create a decision tree: when should a language use exceptions vs results vs panics?
- How does Swift combine optionals, throws, and Result for different error severities?
- Why does Erlang/Elixir embrace errors (let it crash) while Rust prevents them (make illegal states unrepresentable)?

## Connections to Explore
- [[Concurrency Models Overview]] — hub page
- [[Error Handling Overview]] — hub page
- [[Programming Languages/Concurrency Models/Async-Await and Event Loops|Async-Await Patterns]] — async deep dive
- [[Result and Option Types]] — result pattern

## References
→ [[Programming Languages/Sources/Sources Index|Sources Index]]
