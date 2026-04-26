---
tags: [chunk, programming-languages, type-level]
source: "[[raw-pl-029]]"
---

# chunk-pl-115 Type-Level Programming

Advanced type systems enable computation at the type level:

**Haskell type-level programming:**
- Type families: functions at the type level. 	ype family Add (a :: Nat) (b :: Nat) :: Nat
- GADTs: constructors can refine the type. data Vec (n :: Nat) a where VNil :: Vec 0 a; VCons :: a -> Vec n a -> Vec (n+1) a
- DataKinds: promote value constructors to type constructors. Natural numbers become types.

**TypeScript type-level programming:**
- Conditional types: 	ype IsString<T> = T extends string ? true : false
- Template literal types: 	ype EventName = "on"
- Mapped types: 	ype Readonly<T> = { readonly [K in keyof T]: T[K] }
- TypeScript's type system is Turing-complete (proved by implementing a Turing machine in types)

**Rust type-level (limited):**
- Const generics: struct Array<T, const N: usize>
- Associated types: output types determined by input types
- Trait bounds for compile-time constraints
- No higher-kinded types (major limitation)

**C++ template metaprogramming:** Turing-complete type-level computation via template specialization. Powerful but notorious for error messages and compile times.

Use cases: dimension-checked arithmetic, protocol state machines, database schema validation, compile-time configuration validation.
