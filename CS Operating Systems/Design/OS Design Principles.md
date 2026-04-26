---
tags:
  - csos
  - csos/design
confidence: verified
up: "[[Design Principles Overview]]"
tier-coverage: [intuition, core, deep-dive, practice]
---
# OS Design Principles

## 🎯 Intuition
**The Core Idea:** Building an OS is one of the most difficult software engineering tasks: it must be correct, performant, portable, secure, and extensible — often simultaneously. Tanenbaum identifies recurring design principles that guide good OS architecture.

**Analogy:** These principles are like the engineering rules behind a skyscraper. Without them, the structure may stand for a while, but every change makes collapse more likely.

**Why It Matters:** An OS without principles accumulates complexity and technical debt until every change becomes risky.

## ⚙️ Core Mechanics
### The Six Principles
#### Simplicity
Complex systems have more bugs. A kernel with fewer, well-understood mechanisms is easier to reason about, test, and maintain. Each mechanism should do one thing well (cf. UNIX philosophy). Avoid special cases: they multiply interactions and make behaviour unpredictable.

#### Correctness Over Performance
"First make it right, then make it fast — if you have to." Premature optimisation introduces bugs that are extremely hard to debug in an OS context (race conditions, heisenbugs). Measure before optimising; optimise the hot path, not imagined bottlenecks.

#### Portability
Writing the OS in C with a narrow Hardware Abstraction Layer (HAL or architecture-specific directory) keeps hardware dependencies contained. Linux's `arch/` tree and Windows' HAL embody this. The HAL should be as thin as possible — just enough to hide what is truly platform-specific.

#### Mechanism vs Policy
See dedicated note: [[Mechanism vs Policy]]. The most important single principle: mechanisms provide capability; policy decides when to use it. Keep them separate so policy can change without rewriting mechanisms.

#### Layering
Each layer should use only the services of the layer below it and export a clean interface upward. This makes each layer independently testable and replaceable. VFS is a canonical example: file-system drivers implement the VFS layer interface; upper layers never touch disk layouts.

#### Measurement
"If you didn't measure it, you don't know." OS performance is full of counter-intuitive results. Scheduler tuning, buffer size choices, and locking strategies all require profiling real workloads. Linux `perf`, DTrace, and eBPF exist precisely for this.

## 🔬 Deep Dive
### Portability in Real Systems
Linux's `arch/` tree shows how architecture-specific code can be isolated, while Windows uses a HAL for the same purpose. Both approaches contain machine-dependent details so the bulk of the kernel remains portable.

### Layering in Real Systems
VFS is a canonical example of layering: file-system drivers implement the VFS interface, and upper layers use that interface rather than touching device-specific disk layouts directly.

### Measurement Before Tuning
Because OS behaviour is often counter-intuitive, tools like Linux `perf`, DTrace, and eBPF are essential. They keep optimisation grounded in measured hot paths rather than guesses.

## 🏋️ Practice
### Warm-Up
1. Why is OS development one of the hardest software engineering tasks?
2. Which design principle warns against special cases and unnecessary complexity?
3. What does the phrase “If you didn't measure it, you don't know” mean in OS engineering?

### Core Problems
1. Why is premature optimisation especially dangerous in OS code?
2. How does Linux's `arch/` directory help achieve portability?
3. A kernel adds a special case for one workload that complicates several subsystems. Which principle does this violate, and why?

### Challenge
1. Compare portability through a narrow HAL with portability through an architecture-specific source tree. What do they have in common?
2. Explain how VFS demonstrates layering and why that matters for maintainability.
3. A developer argues that a new scheduler tweak should be merged because it “seems faster.” Use the design principles in this note to critique that argument.

## Supporting Chunks

- [[Design - OS design requires balancing conflicting goals across security performance and portability]]
- [[Design - Separating mechanism from policy lets policy evolve without rewriting mechanisms]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 12.
