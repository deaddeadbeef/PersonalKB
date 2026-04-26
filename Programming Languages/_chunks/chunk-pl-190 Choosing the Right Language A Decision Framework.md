---
tags: [pl, chunk, design, language-choice]
up: "[[Programming Languages]]"
---

# Choosing the Right Language A Decision Framework

The most important programming language skill isn't mastering any single language – it's knowing which language fits which problem.

## Decision Matrix

| Requirement | Best Fit | Why |
|-------------|----------|-----|
| Maximum performance | Rust, C, C++ | No GC, zero-cost abstractions |
| Web API server | Go, Java, C# | Great concurrency, mature frameworks |
| Data science / ML | Python | NumPy/PyTorch ecosystem |
| iOS app | Swift | Apple platform SDK |
| Android app | Kotlin | Google-endorsed, Jetpack Compose |
| Cross-platform mobile | Kotlin Multiplatform, Flutter/Dart | Shared business logic |
| Frontend web | TypeScript + React/Vue/Svelte | Browser monopoly + type safety |
| CLI tools | Rust, Go | Fast startup, single binary |
| Distributed systems | Erlang/Elixir | Fault tolerance, message passing |
| Financial systems | OCaml, Rust, Haskell | Type safety, correctness |
| Embedded systems | C, Rust, Zig | No runtime, hardware access |
| Game engine | C++, Rust | Performance, low-level control |
| Game scripting | Lua, C# (Unity) | Embedding, productivity |
| DevOps / scripting | Python, Go, Bash | Quick automation |
| Blockchain | Rust, Solidity | Safety, determinism |
| Compiler writing | OCaml, Rust, Haskell | ADTs, pattern matching |

## The Wrong Question

"Which is the best programming language?" is the wrong question.
The right question: "Which language has the best **ecosystem** for my **problem domain** and **team**?"

## Team Factors

| Factor | Impact |
|--------|--------|
| Team size | Large teams benefit from Go's simplicity |
| Experience level | Junior-heavy teams need simpler languages |
| Hiring pool | JavaScript and Python have the largest talent pools |
| Existing codebase | Interop requirements constrain choices |
| Domain expertise | ML teams know Python; systems teams know C++ or Rust |

## The Multi-Language Reality

Most modern projects use multiple languages:
\\\
Frontend: TypeScript
Backend API: Go or Java
ML pipeline: Python
Infrastructure: Terraform (HCL) + Go
CLI tools: Rust
Scripts: Python or Bash
\\\

The key skill is knowing which language to use where.

## Key Insight
Language choice is a systems engineering decision, not a religious one. Consider: ecosystem quality, hiring pool, team experience, interop requirements, performance needs, and maintenance cost. The "best" language is the one that minimizes total cost of ownership for your specific situation.

## References
→ [[Sources Index]]
