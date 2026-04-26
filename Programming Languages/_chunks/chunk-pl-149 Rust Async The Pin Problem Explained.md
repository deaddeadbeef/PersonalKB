---
tags: [pl, chunk, rust, async, pin]
up: "[[Concurrency Models Overview]]"
---

# Rust Async The Pin Problem Explained

Rust's async system is zero-cost but introduces Pin, one of the most confusing concepts in the language.

## Why Pin Exists

When Rust compiles sync fn, it creates a state machine struct. Consider:
`ust
async fn example() {
    let data = vec![1, 2, 3];
    let reference = &data;      // reference points to data
    some_async_op().await;      // state machine suspends here
    println!("{:?}", reference); // reference must still be valid after resume
}
`

The compiler generates something like:
`ust
enum ExampleFuture {
    State0 { data: Vec<i32> },
    State1 { data: Vec<i32>, reference: *const Vec<i32> },
    // reference is a pointer INTO the same struct!
    // If the struct moves in memory, reference becomes dangling
}
`

This is a **self-referential struct** — it contains a pointer to itself. If the struct is moved in memory, the internal pointer becomes invalid.

## What Pin Does

Pin<&mut T> is a wrapper that prevents the pointed-to value from being moved:
`ust
// A pinned future cannot be moved in memory
// This ensures self-references remain valid
let future = pin!(example());
// future.as_mut() gives Pin<&mut ExampleFuture>
// The future can be polled but not moved
`

## Why This Is Hard

1. **Self-referential structs** are unusual in most languages (GC handles this automatically)
2. **Pin is viral** — once you have Pin<&mut T>, many operations require Pin-aware APIs
3. **Unpin trait** — types that don't self-reference opt out via impl Unpin
4. **Most users never need Pin directly** — async/await sugar handles it

## Comparison with Other Languages

| Language | Async Mechanism | Self-Reference Problem |
|----------|----------------|----------------------|
| Rust | State machine + Pin | Explicit (developer handles) |
| JavaScript | Event loop + heap allocation | GC handles it (no issue) |
| Python | Coroutine objects on heap | GC handles it (no issue) |
| Go | Goroutine with stack | Runtime moves stacks (updates pointers) |
| C# | State machine + heap | GC handles it (no issue) |
| C++ | Coroutine frame (heap) | No self-reference guarantee |

## The Practical Reality

Most Rust async users never interact with Pin directly:
`ust
// This "just works" - the compiler handles Pin internally
async fn fetch_data(url: &str) -> Result<String, Error> {
    let response = reqwest::get(url).await?;
    Ok(response.text().await?)
}
`

Pin only surfaces when building custom Futures or interfacing with low-level async primitives.

## Key Insight
Pin is the price Rust pays for zero-cost async — no heap allocation, no GC, state machine fits in a struct. Every other language avoids Pin by putting coroutine state on the heap (and paying the allocation cost). It's a perfect example of Rust's philosophy: expose complexity to gain performance.

## References
→ [[Sources Index]]
