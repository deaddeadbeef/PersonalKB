---
tags: [pl, chunk, type-systems, null-safety]
up: "[[Error Handling Overview]]"
---

# Null Safety The Billion Dollar Mistake Fixed

Tony Hoare called null references his "billion-dollar mistake." Modern languages have found different solutions.

## The Problem

Null-related crashes are the #1 runtime error in Java, C#, and JavaScript. Nothing in traditional type systems warns you about null.

## Solution 1: Optional Types (Rust, Haskell, OCaml)

Remove null entirely. Use an explicit Option/Maybe type:
- Impossible to get a null pointer exception
- Compiler forces you to handle both Some and None cases

## Solution 2: Nullable Types (Kotlin, Swift, TypeScript strict)

Distinguish nullable from non-nullable in the type system:
- \al name: String\ cannot be null
- \al maybe: String?\ explicitly nullable
- Backward compatible with existing null-using code

## Solution 3: Flow-Sensitive Narrowing (TypeScript, C# 8+)

The compiler tracks nullability through control flow.

## Solution 4: Nullable Reference Types (C# 8+)

Opt-in null safety annotations.

## Key Insight
The industry consensus is clear: null safety should be built into the type system. Kotlin proved it can be added to existing languages. Rust proved you can eliminate null entirely.

## References
→ [[Sources Index]]
