---
tags: [pl, chunk, concurrency, green-threads]
up: "[[Concurrency Models Overview]]"
---

# Green Threads vs OS Threads The Runtime Trade-off

The choice between green threads (runtime-managed) and OS threads (kernel-managed) is one of the most impactful concurrency design decisions.

## OS Threads

The operating system kernel manages scheduling:
- **Memory:** 1-8MB stack per thread
- **Creation:** ~10-100µs
- **Context switch:** ~1-10µs (kernel mode transition)
- **Limit:** ~10,000 threads practical maximum

## Green Threads

The language runtime manages scheduling on fewer OS threads:
- **Memory:** As low as 2KB per green thread
- **Creation:** ~1µs or less
- **Context switch:** ~100-200ns (user-space only)
- **Limit:** Millions practical

| Implementation | Language | Multiplexing |
|---------------|----------|-------------|
| Goroutines | Go | M:N (many goroutines on few OS threads) |
| Virtual Threads | Java 21 | M:N (via Project Loom) |
| Erlang Processes | Erlang | M:N (BEAM scheduler) |

## Key Insight
Green threads are ideal for I/O-heavy workloads where you need millions of concurrent tasks.

## References
→ [[Sources Index]]
