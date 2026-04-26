---
tags: [chunk, programming-languages, smart-pointers]
source: "[[raw-pl-010]]"
---

# chunk-pl-107 Smart Pointers and RAII Patterns

**C++ smart pointers:**
- unique_ptr<T>: Single owner. Moved, not copied. Freed when owner destroyed.
- shared_ptr<T>: Reference counted. Multiple owners. Freed when last owner destroyed.
- weak_ptr<T>: Non-owning reference to shared_ptr. Doesn't prevent destruction.

**Rust equivalents:**
- Box<T>: Heap allocation, single owner (like unique_ptr)
- Rc<T>: Reference counted, single thread (like shared_ptr)
- Arc<T>: Atomic reference counted, thread-safe
- Weak<T>: Non-owning reference (like weak_ptr)

**RAII pattern:** Acquire resource in constructor, release in destructor. Applied to: memory (smart pointers), files (File::open auto-closes on drop), locks (MutexGuard releases on drop), network connections.

**Rust's Drop trait:** Destructor. Implemented with Drop for MyType { fn drop(&mut self) { cleanup(); } }. Called automatically when value goes out of scope. Ordering: fields dropped in declaration order.

**Python context managers:** with open("file") as f: — __enter__ acquires, __exit__ releases. Similar goal to RAII but opt-in, not automatic.

**Go defer:** defer file.Close() — deferred until function returns. Simpler than RAII but less composable.
