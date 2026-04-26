---
tags: [chunk, programming-languages, error-handling-comparison]
source: "[[raw-pl-004]]"
---

# chunk-pl-106 Error Handling Decision Tree

Choosing an error handling approach:

**Use Result/Option types when:**
- Errors are expected and recoverable (file not found, parse failure)
- You want type-safe error propagation
- The function signature should document failure modes
- Best: Rust (Result + ?), Haskell (Either + do), OCaml (result + let*)

**Use exceptions when:**
- Errors are rare and need to skip many stack frames
- Your language has mature exception support
- You need rich error information (stack traces, error chains)
- Best: Python (try/except), Java (try/catch), OCaml (fast exceptions)

**Use error codes when:**
- Working at FFI boundaries
- Maximum performance with no overhead
- Interfacing with OS APIs
- Best: C (errno), Zig (error unions -- type-safe error codes)

**Use panic/crash when:**
- Programmer bug detected (assertion failure)
- Invariant violated (impossible state reached)
- Recovery is not meaningful
- Best: Rust (panic!), Go (panic), Erlang (let it crash + supervisor restart)

**Use algebraic effects when:**
- You want composable effect handling
- You need user-definable control flow
- Available in: OCaml 5, Koka (research)
