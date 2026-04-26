---
tags: [pl, chunk, effects, algebraic-effects]
up: "[[Error Handling Overview]]"
---

# Algebraic Effects The Post-Monad Revolution

Algebraic effects offer a cleaner alternative to monad transformers for managing side effects in functional programming.

## The Problem They Solve

In Haskell, combining multiple effects requires monad transformer stacks:
-- Want logging + state + IO? Stack transformers:
type App a = LoggingT (StateT AppState IO) a
-- Order matters! And composition gets awkward quickly.

Algebraic effects let you declare and compose effects freely.

## Real-World Implementations

### OCaml 5 (2022) - First Mainstream Adoption
OCaml uses algebraic effects for multicore concurrency:
- Effects replace the need for colored functions (async/sync split)
- Handlers enable different concurrency strategies
- Used by Eio (effects-based I/O library)

### Koka (Microsoft Research)
The reference implementation for algebraic effects:
- Evidence-passing translation for performance
- Effect rows track all effects precisely
- Handlers can be swapped (e.g., replace real I/O with mock)

### Unison
Uses abilities (algebraic effects) as a core language feature:
- Enables transparent distributed computing
- Code can be moved between machines with effects rebound

### Haskell Effect Libraries
Multiple libraries bring effect-system patterns to Haskell:
- **effectful:** Fast, based on IORef and ReaderT
- **polysemy:** Ergonomic but slower
- **cleff:** Balance of speed and ergonomics

## Effects vs Other Approaches

| Approach | Composition | Performance | Clarity |
|----------|-------------|-------------|---------|
| Monad transformers | Awkward (ordering, lifting) | Moderate overhead | Complex types |
| Free monads | Natural | Slow (interpretation) | Clear separation |
| Algebraic effects | Natural | Good (compiled away) | Clear + flexible |
| No tracking | N/A (implicit) | Zero overhead | No compiler help |

## Key Insight
Algebraic effects may be the most important PL innovation of the 2020s. OCaml 5's adoption proves they work in practice. They solve the "what color is your function" problem (no async/sync split needed) and compose more naturally than monads.

## References
-> [[Sources Index]]
