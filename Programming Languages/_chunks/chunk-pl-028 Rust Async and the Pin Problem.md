---
tags: [chunk, programming-languages, rust]
source: "[[raw-pl-021]]"
---

# chunk-pl-028 Rust Async and the Pin Problem

Rust async/await: sync fn returns a Future. .await suspends until complete. Futures are lazy — do nothing until polled.

**Zero-cost:** Futures compile to state machines. No heap allocation for the future itself. This makes Rust async competitive with C for network services.

**The complexity:** Async interacts with ownership and lifetimes. A self-referential struct (future holding a reference to its own data) can't be moved — this is why Pin exists. Pin prevents moving a value, allowing self-references to remain valid.

**Ecosystem split:** tokio vs async-std as runtime. tokio won. Async traits (stabilized 2023) required years of design.

**Error handling in async:** sync fn read() -> Result<Data, Error> — same Result pattern, but error types must be Send for cross-thread futures.

Despite complexity, Rust async powers: Cloudflare Workers, Discord's infrastructure, and Tokio-based microservices handling millions of connections.
