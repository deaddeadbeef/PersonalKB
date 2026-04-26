---
tags: [chunk, programming-languages, effects]
source: "[[raw-pl-004]]"
---

# chunk-pl-049 Algebraic Effects The Next Frontier

Algebraic effects track which side effects a function performs — including errors, I/O, state mutation, concurrency. A function's type declares what effects it performs; the compiler ensures they're handled.

**OCaml 5 algebraic effects:** Effects are like resumable exceptions. The handler provides a value and execution continues at the effect site. This subsumes: exceptions, async/await, generators, and coroutines into one user-definable mechanism.

**Koka (Microsoft Research):** Designed around algebraic effects from the ground up. Every function's type lists its effects. The compiler tracks effect propagation.

**Java's checked exceptions — the cautionary tale:** Early, limited effect system. Failed due to: verbosity, poor generics/lambda interaction, and incentive to suppress. Lesson: effect tracking must compose with the rest of the language.

**Rust's implicit effect tracking:** No formal effect system, but types implicitly track: fallibility (Result), async (async fn), unsafe (unsafe), thread safety (Send/Sync). Ad-hoc effect markers, not unified.

The future: richer type-level effect tracking, user-definable effects, composable effect handling, and gradual adoption.
