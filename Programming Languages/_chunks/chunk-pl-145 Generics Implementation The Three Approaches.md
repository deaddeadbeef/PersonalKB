---
tags: [pl, chunk, generics, monomorphization]
up: "[[Type Systems Overview]]"
---

# Generics Implementation The Three Approaches

How a language implements generics affects performance, binary size, and type information at runtime.

## 1. Monomorphization (Rust, C++)

The compiler generates specialized code for each concrete type:
`ust
fn max<T: Ord>(a: T, b: T) -> T {
    if a > b { a } else { b }
}
// Calling max(1i32, 2i32) generates max_i32
// Calling max("a", "b") generates max_str
`

**Pros:** Zero runtime overhead, full optimization per type
**Cons:** Binary size bloat (N types = N copies), slower compilation

### C++ Templates
`cpp
template<typename T>
T max(T a, T b) { return a > b ? a : b; }
// Same monomorphization, but with famously terrible error messages
// C++20 Concepts improve this significantly
`

## 2. Type Erasure (Java)

Generic type information is erased at compile time:
`java
List<String> names = new ArrayList<>();
// At runtime, this is just ArrayList<Object>
// The compiler inserts casts at usage sites
`

**Pros:** No binary size increase, backward compatible (Java 5 added generics without changing JVM)
**Cons:** No runtime type info (instanceof List<String> is illegal), boxing overhead for primitives

### The Boxing Problem
`java
List<int> // ILLEGAL - must use List<Integer> (boxed)
// Each Integer is a heap allocation instead of a stack value
// Valhalla project aims to fix this with value types
`

## 3. Reification (C#)

Generic types exist at runtime with full type information:
`csharp
List<int> list = new List<int>();
list.GetType().GetGenericArguments() // [System.Int32]
// CLR generates specialized code for value types
// Reference types share one implementation with casts
`

**Pros:** Full runtime type info, no boxing for value types
**Cons:** More complex runtime, some binary size increase

## Comparison

| Property | Monomorphization | Erasure | Reification |
|----------|-----------------|---------|-------------|
| Runtime overhead | Zero | Boxing, casts | Minimal |
| Binary size | Large | Small | Medium |
| Runtime type info | No (types gone) | No (types gone) | Yes |
| Compile time | Slow (many copies) | Fast | Fast |
| Value type support | Full | Boxed only | Full |
| Language | Rust, C++ | Java, Kotlin/JVM | C#, .NET |

## Other Approaches
- **Go (1.18+):** GC shape stenciling — hybrid between monomorphization and dictionary passing
- **Haskell:** Dictionary passing — type class methods passed as runtime arguments
- **Swift:** Witness tables — similar to dictionary passing with specialization optimization
- **Zig:** Comptime generics — generics are just compile-time code execution

## Key Insight
Each approach reflects the language's priorities: Rust/C++ choose monomorphization for zero-cost abstractions (performance over compile time). Java chose erasure for backward compatibility. C# chose reification for runtime flexibility. There's no universally superior approach.

## References
→ [[Sources Index]]
