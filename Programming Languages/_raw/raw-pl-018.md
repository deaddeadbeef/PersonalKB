---
tags: [raw, programming-languages, pattern-matching]
source: "ML for the Working Programmer (Paulson), Rust by Example, Swift Documentation"
created: 2025-07-25
---

# raw-pl-018: Pattern Matching and Algebraic Data Types

## Algebraic Data Types (ADTs)

**Sum types** (tagged unions, variants): a value is ONE of several alternatives.
- OCaml: 	ype shape = Circle of float | Rectangle of float * float
- Rust: num Shape { Circle(f64), Rectangle(f64, f64) }
- Haskell: data Shape = Circle Double | Rectangle Double Double
- Kotlin: sealed class Shape { data class Circle(val r: Double): Shape() }
- Swift: num Shape { case circle(Double); case rectangle(Double, Double) }

**Product types** (records, tuples): a value has ALL of several fields.
- OCaml: 	ype point = { x: float; y: float }
- Rust: struct Point { x: f64, y: f64 }

Combined, sum types + product types can model any data structure. This is why they're called "algebraic" — sum types are addition (OR), product types are multiplication (AND).

## Pattern Matching

Destructure values and branch based on shape:

`
match shape with

| Circle r -> 3.14 * r * r
| Rectangle (w, h) -> w * h
`

The compiler checks exhaustiveness — if you forget a case, it warns. This is a killer feature for correctness: when you add a new variant, the compiler tells you every place that needs updating.

## Language Support

**Full ADT + pattern matching:** OCaml, Haskell, Rust, F#, Scala, Elm, Erlang/Elixir
**Sealed classes + when/switch:** Kotlin, Swift, Java 21+ (sealed classes + pattern matching)
**Limited pattern matching:** Python 3.10 (match/case, structural patterns)
**No ADTs:** Go, C, JavaScript (can be emulated with objects/TypeScript discriminated unions)

## The Power of Exhaustiveness

Exhaustiveness checking is the key benefit. When a variant is added to an enum/sealed class, every match/when expression that doesn't handle the new case becomes a compile error. This makes large-scale refactoring safe: the compiler is your checklist.

Languages without exhaustive pattern matching (Go, Python) rely on default cases or runtime errors, losing this safety.

## TypeScript Discriminated Unions

TypeScript achieves something similar to ADTs through discriminated unions:
`	ypescript
type Shape = { kind: "circle"; radius: number } | { kind: "rectangle"; w: number; h: number }
`
The kind field discriminates. TypeScript's narrowing in switch/if statements provides exhaustiveness checking via the 
ever type.

## The Visitor Pattern — OOP's Pattern Matching

In languages without ADTs (Java pre-17, C++), the Visitor pattern simulates pattern matching: define a Visitor interface with one method per variant, implement it for each operation. This is verbose but type-safe. Sealed classes + pattern matching (Java 21, Kotlin) eliminate the need for Visitors.
