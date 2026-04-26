---
tags: [chunk, programming-languages, error-handling]
source: "[[raw-pl-004]]"
---

# chunk-pl-013 Panic vs Recoverable Error Separation

Languages that separate unrecoverable errors (bugs) from recoverable errors (expected failures):

**Rust:** Result<T, E> for recoverable errors. panic!() for bugs/invariant violations. catch_unwind() exists but is strongly discouraged for control flow.

**Go:** Error values for expected failures. panic() for unrecoverable situations. ecover() catches panics in deferred functions. Convention: libraries never panic across API boundaries.

**Erlang:** "Let it crash" — processes crash on any error; supervisors restart them. Eliminates the recoverable/unrecoverable distinction within a process.

**Java:** Exception (recoverable) vs Error (JVM-level, shouldn't catch). RuntimeException (unchecked, programmer bugs) vs checked exceptions.

Languages separating panic from error (Rust, Go) enforce clearer thinking about failure modes. Languages unifying them (Python, Java) are simpler but blur the distinction.
