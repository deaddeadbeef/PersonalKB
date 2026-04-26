---
tags: [pl, chunk, type-systems, phantom]
up: "[[Type Systems Overview]]"
---

# Phantom Types Type-Level Tags Without Runtime Cost

Phantom types are type parameters that appear in the type signature but not in the runtime representation. They enable compile-time checks with zero runtime overhead.

## How Phantom Types Work

`ust
use std::marker::PhantomData;

struct Distance<Unit> {
    value: f64,
    _unit: PhantomData<Unit>,
}

struct Meters;
struct Feet;

impl Distance<Meters> {
    fn to_feet(self) -> Distance<Feet> {
        Distance { value: self.value * 3.28084, _unit: PhantomData }
    }
}

let d1 = Distance::<Meters> { value: 100.0, _unit: PhantomData };
let d2 = Distance::<Feet> { value: 328.0, _unit: PhantomData };
// d1 + d2; // COMPILE ERROR: can't add Meters to Feet!
`

## Use Cases

### Unit Safety (Preventing the Mars Orbiter Bug)
The Mars Climate Orbiter was lost because one module used pounds-force and another used newtons. Phantom types prevent this at compile time.

### State Machines
`ust
struct File<State> { handle: RawFd, _state: PhantomData<State> }
struct Open;
struct Closed;

impl File<Open> {
    fn read(&self) -> Vec<u8> { /* ... */ }
    fn close(self) -> File<Closed> { /* ... */ }
}
// file.read() only works if file is Open
// After close(), the type changes to File<Closed>
`

### Permission Levels
`ust
struct Query<Permission> { sql: String, _perm: PhantomData<Permission> }
struct ReadOnly;
struct ReadWrite;

impl Query<ReadWrite> {
    fn execute_write(&self) { /* ... */ }
}
// Read-only queries cannot call execute_write
`

## Languages Supporting Phantom Types

| Language | Syntax | Common Usage |
|----------|--------|-------------|
| Rust | PhantomData<T> | Units, state machines, permissions |
| Haskell | Type parameter (natural) | Tagged types, proofs |
| OCaml | Phantom type parameter | Typed IDs, safety tags |
| TypeScript | Branded types (approximation) | Nominal typing hack |
| Scala | Type parameter | Tagged types |

## Key Insight
Phantom types demonstrate the power of types as documentation that the compiler enforces. They cost nothing at runtime but prevent entire categories of bugs (unit mismatches, invalid state transitions, permission violations). They're an underused feature in every language that supports them.

## References
→ [[Sources Index]]
