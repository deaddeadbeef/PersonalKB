---
tags: [pl, chunk, ocaml, ml-family]
up: "[[OCaml – Language Profile]]"
---

# OCaml The Pragmatic ML

OCaml occupies a unique position: a language with one of the strongest type systems in practical use, chosen by organizations that need both correctness and performance.

## OCaml in Production

### Jane Street (Finance)
- **Millions of lines** of OCaml powering electronic trading
- Performance-critical: nanosecond-level latency requirements
- OCaml's type system catches bugs that would cause financial losses
- Developed the Core library, Async framework, and ppx macros

### Meta (formerly Facebook)
- **Flow:** JavaScript type checker written in OCaml
- **Hack:** PHP successor's type checker in OCaml
- **Pyre:** Python type checker (originally OCaml, now Rust)
- **Infer:** Static analysis tool for C, Java, ObjC

### Tezos (Blockchain)
- Smart contract language (Michelson) and node implementation in OCaml
- Type safety critical for financial smart contracts

### MirageOS (Unikernels)
- Operating system library written entirely in OCaml
- Compiles to unikernels – minimal VMs running single applications

## What Makes OCaml Special

### Type Inference + Modules
OCaml combines Hindley-Milner type inference with the most powerful module system in any mainstream language:
```ocaml
(* Functor: a module that takes a module as argument *)
module MakeSet (Ord : OrderedType) : Set with type elt = Ord.t = struct
  type elt = Ord.t
  type t = elt list
  let empty = []
  let add x s = if List.mem x s then s else x :: s
end

module StringSet = MakeSet(String)
```

### OCaml 5.0: Multicore + Effects
The biggest change in OCaml's history:
- **Multicore support:** Parallel domains (like threads)
- **Algebraic effects:** First mainstream language with effect handlers
- **Backward compatible:** Existing code runs unchanged

### Performance
OCaml compiles to efficient native code:
- Typically within 2x of C for most workloads
- Excellent for symbolic computation, compilers, and analysis tools
- Unboxed floats and optimized pattern matching

## OCaml's Influence on Rust

Rust's type system borrowed heavily from OCaml:
- **Algebraic data types** (enums with data)
- **Pattern matching** (exhaustive, with guards)
- **Trait system** (influenced by OCaml's modules and type classes)
- **Type inference** (HM-based)
- **Option/Result types** (from ML's option type)

Graydon Hoare, Rust's creator, has acknowledged OCaml as a primary influence.

## Key Insight
OCaml is the "hidden gem" of programming languages – a 28-year-old language with a type system that modern languages are still catching up to. Its influence on Rust, F#, Haskell, and Swift is enormous relative to its user base. OCaml 5's algebraic effects may start a new wave of adoption.

## References
→ [[Sources Index]]
