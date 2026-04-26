---
tags: [pl, chunk, concurrency, structured]
up: "[[Concurrency Models Overview]]"
---

# Structured Concurrency The Next Concurrency Paradigm

Structured concurrency ensures that concurrent tasks have clear lifetimes and ownership, preventing orphaned tasks and resource leaks.

## The Problem with Unstructured Concurrency

Traditional concurrency is "goto for tasks":
`python
# Unstructured: who owns this task? When does it end?
asyncio.create_task(background_work())
# If this function returns, the task might still be running
# If the task fails, nobody might notice
`

## Structured Concurrency Principle

Every concurrent task must be scoped to a parent — like structured programming scoped goto to blocks:

`
Unstructured:  spawn task → task floats freely → ???
Structured:    scope { spawn task → task must complete before scope exits }
`

## Language Implementations

### Kotlin Coroutines (pioneer in mainstream)
`kotlin
coroutineScope {
    val result1 = async { fetchUser() }
    val result2 = async { fetchOrders() }
    // Both MUST complete (or fail) before scope exits
    process(result1.await(), result2.await())
}
// If either fails, the other is automatically cancelled
`

### Java (Project Loom, JDK 21+)
`java
try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    Subtask<User> user = scope.fork(() -> fetchUser());
    Subtask<List<Order>> orders = scope.fork(() -> fetchOrders());
    scope.join().throwIfFailed();
    return new Response(user.get(), orders.get());
}
`

### Swift (async let)
`swift
async let user = fetchUser()
async let orders = fetchOrders()
// Both bound to the enclosing scope
let response = try await Response(user: user, orders: orders)
`

### Python (trio / anyio)
`python
async with anyio.create_task_group() as tg:
    tg.start_soon(fetch_user)
    tg.start_soon(fetch_orders)
# Both complete before exiting the async with block
`

## What Structured Concurrency Prevents

| Bug | Unstructured | Structured |
|-----|-------------|------------|
| Orphaned tasks | Common | Impossible |
| Leaked resources | Easy | Prevented by scope |
| Unhandled errors | Silent | Propagated to parent |
| Cancellation | Manual | Automatic on scope exit |
| Reasoning about lifetimes | Hard | Clear (matches code structure) |

## Languages Without Structured Concurrency
- **Go:** Goroutines are unstructured (though errgroup adds partial structure)
- **Erlang:** Supervision trees provide a different (but effective) structure
- **Rust:** tokio tasks are unstructured; structured concurrency is an active discussion

## Key Insight
Structured concurrency is to concurrent programming what structured programming was to goto: it constrains a powerful primitive to make it predictable and safe. Kotlin, Swift, and Java are leading the adoption. Rust's ownership model should make it a natural fit, but the design is still evolving.

## References
→ [[Sources Index]]
