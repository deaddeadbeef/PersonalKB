---
tags: [chunk, programming-languages, trust]
source: "[[raw-pl-030]]"
---

# chunk-pl-070 Trust vs Protection in Language Philosophy

**Trust the programmer (C, Zig):** Minimal guardrails. No bounds checking (C), no borrow checker (Zig). Maximum performance and flexibility. Bugs are the programmer's responsibility. C: "the programmer knows what they're doing." Zig: explicit about everything but trusts you to handle it.

**Protect the programmer (Rust, Haskell, Java):** Compiler catches mistakes. Type system prevents invalid states. Rust: ownership prevents memory errors. Haskell: purity prevents side effects. Java: GC prevents memory leaks. Cost: learning curve, compilation time, sometimes fighting the compiler.

**Rust's unique position:** Maximum protection AND maximum performance. The borrow checker is strict but produces zero-overhead code. "If it compiles, it works" is a Rust community saying. The price: the steepest learning curve of any mainstream language.

**Erlang's approach:** Don't prevent errors — make them recoverable. Let processes crash; supervisors restart them. Trust the system design, not the individual programmer.

**Python/Ruby:** Trust programmer conventions (_private prefix), not compiler enforcement. "We're all consenting adults here." Fast development at the cost of runtime safety.

The spectrum: Haskell (most protective) > Rust > Java > Go > Python > C > Assembly (most trusting).
