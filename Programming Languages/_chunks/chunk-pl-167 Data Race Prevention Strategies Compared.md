---
tags: [pl, chunk, concurrency, data-race]
up: "[[Threads and Locks]]"
---

# Data Race Prevention Strategies Compared

Data races (concurrent unsynchronized access to shared mutable data) are among the hardest bugs to find and fix. Languages take radically different approaches to preventing them.

## The Four Strategies

### 1. Prevent at Compile Time (Rust)
Rust's ownership system makes data races impossible:
```rust
// This won't compile - can't send non-Send type across threads
// This won't compile - can't share non-Sync type between threads
let data = vec![1, 2, 3];
let handle = thread::spawn(move || {
    // data is MOVED here - original thread can't access it
    println!("{:?}", data);
});
// println!("{:?}", data); // COMPILE ERROR: data was moved
```

The `Send` and `Sync` traits mark what can cross thread boundaries. The borrow checker ensures exclusive access.

### 2. Prevent by Design (Erlang, Go)
Eliminate shared mutable state entirely:
```erlang
%% Erlang: no shared memory, only message passing
Pid = spawn(fun() -> receive {data, D} -> process(D) end end),
Pid ! {data, MyData}.
%% MyData is COPIED to the other process - no sharing
```

### 3. Detect at Runtime (Go, Java)
```bash
# Go race detector
go test -race ./...
# Instruments memory accesses, reports races at runtime
```

### 4. Trust the Developer (C, C++)
```c
// C: no protection
// Developer must use mutexes, atomics correctly
// Misuse = undefined behavior, data corruption
```

## Comparison

| Strategy | Language | Guarantee | Cost |
|----------|---------|-----------|------|
| Compile-time prevention | Rust | No data races ever | Learning curve, borrow checker battles |
| No shared state | Erlang | No data races by design | Message copying overhead |
| Runtime detection | Go, Java | Finds races in tested paths | Only catches executed races |
| Manual synchronization | C, C++, Java | None (developer responsibility) | Bugs in production |

## Why Compile-Time Prevention Is Hard

Rust is the only mainstream language that prevents data races at compile time because:
1. It requires an ownership system (unique to Rust)
2. The borrow checker must track lifetimes across threads
3. Send/Sync traits must be implemented correctly for all types
4. The learning curve is steep for concurrent code

## Key Insight
Rust's data race prevention is arguably its most important contribution to programming language design. Before Rust, "concurrent + safe + fast" was considered impossible — you could pick two. Rust's ownership system proves you can have all three, at the cost of compiler complexity.

## References
→ [[Sources Index]]
