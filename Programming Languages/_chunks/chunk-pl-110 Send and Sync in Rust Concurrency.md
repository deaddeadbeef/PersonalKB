---
tags: [chunk, programming-languages, concurrency-safety]
source: "[[raw-pl-019]]"
---

# chunk-pl-110 Send and Sync in Rust Concurrency

Rust prevents data races through two marker traits:

**Send:** A type can be transferred between threads. Most types are Send. Notable exceptions: Rc<T> (not thread-safe reference counting), raw pointers.

**Sync:** A type can be referenced from multiple threads. T is Sync if &T is Send. Mutex<T> is Sync (provides synchronized access). Cell<T> is NOT Sync (interior mutability without synchronization).

**How it works:** When you spawn a thread or send data through a channel, the compiler checks Send/Sync bounds. std::thread::spawn requires the closure to be Send. This is checked at compile time — not a runtime check.

**Common patterns:**
- Arc<Mutex<T>>: Thread-safe shared mutable state. Arc provides shared ownership; Mutex provides synchronized access.
- Arc<RwLock<T>>: Many readers OR one writer, thread-safe.
- mpsc::channel: Send values between threads (ownership transfer).

**Why this is unique:** No other language prevents data races at compile time. Java uses happens-before rules (enforced by programmer). Go uses the race detector (runtime). Erlang prevents sharing (no shared memory). Only Rust proves absence of data races statically.
