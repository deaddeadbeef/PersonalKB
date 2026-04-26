---
tags: [chunk, programming-languages, ocaml-jane-street]
source: "[[raw-pl-015]]"
---

# chunk-pl-088 OCaml at Jane Street and in Production

**Jane Street:** The largest OCaml user. Their entire trading infrastructure — millions of lines — is OCaml. Why: type safety catches bugs before they reach production (critical for financial systems), fast compilation enables rapid iteration, and the module system scales to very large codebases.

**Jane Street contributions:** Core (alternative standard library), Async (concurrency library), ppx_jane (compiler extensions), Incr_map (incremental computation). They effectively maintain a parallel OCaml ecosystem.

**Facebook/Meta Infer:** Static analysis tool for C, C++, Java, Objective-C. Written in OCaml. Uses abstract interpretation to find null dereferences, memory leaks, and concurrency bugs in mobile apps before release.

**Tezos:** Blockchain platform. Smart contract language (Michelson) and node implementation in OCaml. Chosen for formal verification properties.

**Why OCaml for these domains:**
- Type inference reduces annotation burden (fast to write)
- Pattern matching + exhaustiveness catches logic errors
- Module system enables large-scale code organization
- Fast compiler enables rapid iteration
- GC is fast for allocation-heavy functional code

**The ecosystem challenge:** OCaml's ecosystem is small compared to Rust/Python/JS. Libraries exist for core needs but coverage is spotty for niche domains. This is the main barrier to broader adoption.
