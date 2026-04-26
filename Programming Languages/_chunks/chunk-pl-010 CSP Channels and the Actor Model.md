---
tags: [chunk, programming-languages, concurrency]
source: "[[raw-pl-003]]"
---

# chunk-pl-010 CSP Channels and the Actor Model

**CSP (Communicating Sequential Processes):** Independent processes communicate via typed channels. No shared memory.

**Go:** Goroutines (4KB green threads, M:N scheduled) + channels + select. Go's concurrency model is its strongest feature. Millions of goroutines per program.

**Rust:** std::sync::mpsc channels. Sending transfers ownership — sender can't use the value after sending. Tokio provides async channels.

**Actor Model:** Actors have private state, communicate via async messages, process one message at a time (no internal concurrency).

**Erlang/Elixir:** BEAM processes ARE actors. Millions per node. Supervision trees for fault tolerance. "Let it crash" philosophy.

**Swift 5.5+:** Actors as language-level construct. Actor methods are async. Compiler prevents direct access to actor state from outside.

**Async/await (JS, Python, Rust, C#, Kotlin):** Cooperative multitasking. Functions yield at await points. JavaScript: single-threaded event loop eliminates data races by construction. Rust async: zero-cost futures compiled to state machines.
