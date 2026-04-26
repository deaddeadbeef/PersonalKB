---
tags: [pl, raw, effect-systems, algebraic-effects]
up: "[[Sources Index]]"
---

# Raw Note 039 — Effect Systems and Algebraic Effects

## The Problem: Tracking Side Effects

Pure functions are easy to reason about, but real programs need I/O, state, exceptions, and concurrency. How do languages track and control these effects?

## Approaches to Effect Management

### 1. No Effect Tracking (Most Languages)
- **C, Python, Java, Go, JavaScript:** Any function can do anything
- Pro: Simple, no overhead
- Con: No compiler help distinguishing pure from impure code

### 2. IO Monad (Haskell)
Haskell uses the type system to separate pure and effectful code:

`haskell
-- Pure function: no IO in type
add :: Int -> Int -> Int
add x y = x + y

-- Effectful function: IO in return type
readAndPrint :: IO ()
readAndPrint = do
    line <- getLine
    putStrLn ("You said: " ++ line)
`

- Pro: Total separation of pure and impure
- Con: Monad transformer stacks become complex; composition is awkward

### 3. Algebraic Effects (Emerging)
A more flexible approach where effects are declared and handlers can be swapped:

**Koka** (Microsoft Research):

`koka
effect ask
  fun ask() : string

fun greet() : ask string
  "Hello, " ++ ask()

// Handler provides the implementation
fun main()
  with handler
    fun ask() "World"
  println(greet())
`

**OCaml 5.0:** First mainstream language with algebraic effects (for concurrency):

`ocaml
(* Effect declaration *)
type _ Effect.t += Ask : string Effect.t

(* Handler *)
let run f =
  Effect.Deep.try_with f ()
    { effc = fun (type a) (e : a Effect.t) ->
      match e with

      | Ask -> Some (fun (k : (a, _) continuation) ->
          continue k "World")

      | _ -> None }
`

**Unison:** Effects are a core language feature, enable distributed computing.

### 4. Checked Exceptions (Java)
A limited form of effect tracking:

`java
// Caller must handle or propagate
void readFile() throws IOException { ... }
`

- Widely considered a failure — too coarse, too much ceremony

### 5. Capability-Based (Emerging)
**Scala 3 (experimental):** CanThrow capability:

`scala
def readFile()(using CanThrow[IOException]): String = ...
`

## Algebraic Effects vs Monads

| Property | Monads (Haskell) | Algebraic Effects (Koka/OCaml) |
|----------|------------------|--------------------------------|
| Composition | Transformer stacks (awkward) | Natural composition |
| Polymorphism | Higher-kinded types needed | Effect rows |
| Performance | Overhead from wrapping/unwrapping | Can compile to direct style |
| Adoption | Well-established theory | Newer, less tooling |
| Handler swapping | Requires monad morphisms | Built-in — swap handlers freely |

## Languages Exploring Effects

| Language | Status | Approach |
|----------|--------|----------|
| Koka | Research | Full algebraic effects with evidence passing |
| OCaml 5 | Stable | Effects for multicore concurrency |
| Eff | Research | First language designed around algebraic effects |
| Unison | Growing | Effects for distributed computing |
| Scala 3 | Experimental | Capture checking, CanThrow |
| Haskell | Libraries | effect systems (polysemy, effectful, cleff) |
| Rust | Discussion | Effect generics RFC (in-progress) |

## Key Insight
Algebraic effects solve the "monad transformer problem" elegantly and may represent the next major advance in practical programming language design. OCaml 5's adoption gives them their first mainstream test.

## References
→ [[Sources Index]]
