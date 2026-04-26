---
tags: [chunk, programming-languages, safety-critical]
source: "[[raw-pl-029]]"
---

# chunk-pl-118 Languages for Safety-Critical Systems

When bugs can kill or cost billions:

**MISRA C/C++:** Subset of C/C++ with rules eliminating dangerous features. Used in automotive, medical, aerospace. No dynamic memory allocation, no recursion, restricted pointer arithmetic. Verified with static analysis tools.

**Ada/SPARK:** Designed for safety-critical systems (Boeing, Airbus, missile systems). SPARK subset has formal verification — mathematical proofs that code meets specification. The most rigorous approach to correctness.

**Rust for safety:** Memory safety without GC. Increasingly used in: Linux kernel, Android, automotive (Volvo, Volkswagen exploring). ferrocene — qualified Rust compiler for safety-critical ISO 26262 environments.

**Formal verification (Coq, Lean, Agda, Idris):** Write mathematical proofs that code satisfies specification. CompCert: verified C compiler (proved correct in Coq). seL4: verified microkernel. Extremely high assurance but very expensive to develop.

**The certification challenge:** Safety standards (DO-178C for aviation, ISO 26262 for automotive, IEC 62443 for industrial) require evidence of correctness. C/Ada have decades of certification history. Rust is building its certification story (ferrocene). Go, Python, Java are generally not used in hard safety-critical systems.
