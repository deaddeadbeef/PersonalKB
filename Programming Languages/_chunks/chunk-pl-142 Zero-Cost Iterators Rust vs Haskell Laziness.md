---
tags: [pl, chunk, iterators, lazy-evaluation]
up: "[[Programming Paradigms Overview]]"
---

# Zero-Cost Iterators Rust vs Haskell Laziness

Both Rust and Haskell achieve lazy computation but through fundamentally different mechanisms.

## Rust: Explicit Laziness via Iterators

`ust
// This allocates NOTHING until .collect()
let result: Vec<i32> = (0..1_000_000)
    .filter(|x| x % 2 == 0)
    .map(|x| x * x)
    .take(10)
    .collect();
`

The compiler monomorphizes each iterator adapter into a single fused loop — equivalent to:
`ust
let mut result = Vec::new();
for x in 0..1_000_000 {
    if x % 2 == 0 {
        result.push(x * x);
        if result.len() == 10 { break; }
    }
}
`

## Haskell: Implicit Laziness Everywhere

`haskell
-- This also computes lazily - ALL Haskell values are lazy
result = take 10 $ map (^2) $ filter even [0..999999]
`

In Haskell, laziness is the default — no special iterator protocol needed. Every value is a thunk (suspended computation) until forced.

## Trade-offs

| Property | Rust Iterators | Haskell Laziness |
|----------|---------------|-----------------|
| Default | Eager (opt-in lazy) | Lazy (opt-in strict) |
| Memory predictability | Excellent | Poor (thunk accumulation) |
| Space leaks | Impossible | Common pitfall |
| Performance | Predictable, inlined | Variable (thunk overhead) |
| Debugging | Straightforward | Harder (lazy evaluation order) |
| Composition | Method chaining | Function composition |
| Infinite structures | Iterators can be infinite | Lists are naturally infinite |

## The Space Leak Problem

Haskell's laziness can cause unexpected memory usage:
`haskell
-- This builds a huge chain of thunks before evaluating!
foldl (+) 0 [1..1000000]  -- BAD: O(n) memory
foldl' (+) 0 [1..1000000] -- GOOD: O(1) memory (strict fold)
`

Rust never has this problem because evaluation is always eager unless explicitly lazy.

## Key Insight
Rust's approach (eager by default, lazy iterators opt-in) is more practical for most programming. Haskell's approach (lazy by default) enables elegant infinite data structures but requires expertise to avoid space leaks. The industry trend is toward Rust's model.

## References
→ [[Sources Index]]
