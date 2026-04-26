---
tags: [pl, chunk, functional, algebraic-data-types]
up: "[[Functional Programming Principles]]"
---

# Algebraic Data Types The Foundation of Modern Type Systems

Algebraic Data Types (ADTs) — sum types (enums) and product types (structs/records) — are the most important type system feature to emerge from functional programming.

## Sum Types (Tagged Unions)

A value that is ONE of several variants:

```rust
// Rust
enum Shape {
    Circle(f64),
    Rectangle(f64, f64),
    Triangle(f64, f64),
}
```

```haskell
-- Haskell
data Shape = Circle Double | Rectangle Double Double | Triangle Double Double
```

```ocaml
(* OCaml *)
type shape = Circle of float | Rectangle of float * float | Triangle of float * float
```

## Product Types (Records/Structs)

A value that has ALL of several fields:
```rust
struct Point { x: f64, y: f64 }  // x AND y
```

## Why "Algebraic"?

It's literal algebra:
- **Sum type:** `|variants|` = sum of variant counts (OR)
- **Product type:** `|fields|` = product of field counts (AND)
- `Bool` = True + False = 2 values
- `(Bool, Bool)` = 2 * 2 = 4 values
- `Option<Bool>` = None + Some(Bool) = 1 + 2 = 3 values

## Adoption Across Languages

| Language | Sum Types | Product Types | Exhaustive Match |
|----------|-----------|---------------|------------------|
| Haskell | data (1990) | data/record | Yes |
| OCaml | variant types | records | Yes |
| Rust | enum (2010s) | struct | Yes |
| Scala | sealed trait + case class | case class | Yes (sealed) |
| Swift | enum with associated values | struct | Yes |
| Kotlin | sealed class/interface | data class | Yes (sealed) |
| TypeScript | Discriminated unions | Interfaces/types | Partial |
| Java 21 | Sealed classes + records | Records | Yes (sealed) |
| C# | Not native (unions proposed) | Records | Partial |
| Python | Not native (match is structural) | dataclass | No |
| Go | Not native (interfaces) | struct | No |

## The Missing Feature in Go and C

Go and C lack sum types, forcing workarounds. This means the compiler can't check if you handled all cases, leading to bugs.

## Key Insight
ADTs + pattern matching + exhaustiveness checking form a trinity that eliminates entire categories of bugs. They're why Rust code "just works" after compilation more often than Go or C code. The trend is clear: every modern language is adding ADTs.

## References
→ [[Sources Index]]
