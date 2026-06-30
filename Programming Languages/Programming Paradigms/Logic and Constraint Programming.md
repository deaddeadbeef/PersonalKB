---
tags: [programming-languages, paradigms, logic]
up: "[[Programming Paradigms Overview]]"
confidence: verified
tier-coverage: [intuition, core, deep-dive, practice]
---

# Logic and Constraint Programming

> Logic programming is the most fundamentally different paradigm from mainstream imperative/OOP/functional programming — instead of telling the computer *how* to compute, you declare what relationships hold true and let the system figure out the answer.

---

## 🎯 Intuition

### Core Idea

In logic programming, a program is a set of logical facts and rules. Computation is the process of querying these rules to find values that satisfy constraints. The programmer describes the problem; the runtime solves it.

### Analogy

Logic programming is like **describing what a finished puzzle looks like and letting the system assemble the pieces**, rather than placing each piece yourself. You state the shape of the solution — which edges connect, which colours match — and the engine searches, backtracks, and unifies until every piece fits.

### Why It Matters

Logic programming's declarative philosophy increasingly influences mainstream languages through pattern matching, query languages, and constraint-based systems. Understanding it unlocks a fundamentally different way of thinking about computation — one where you specify *what* you want, not *how* to get it.

---

## ⚙️ Core Mechanics

### How It Works

**The Declarative Philosophy.** A program is a set of logical facts and rules. Computation is the process of querying these rules to find values that satisfy constraints.

**Unification.** Pattern matching on steroids — the engine finds substitutions that make two terms identical, driving the entire resolution process.

**Backtracking.** When a path fails, the engine systematically reverses to the most recent choice point and tries the next possibility, performing an exhaustive search through the solution space.

### Key Concepts

| Concept | Description |
|---|---|
| Fact | A ground truth asserted in the knowledge base (e.g. `parent(tom, bob).`) |
| Rule | An implication deriving new facts from existing ones (e.g. `grandparent(X,Z) :- parent(X,Y), parent(Y,Z).`) |
| Query | A question posed to the engine that triggers search and unification |
| Unification | Algorithm that finds variable bindings making two terms identical |
| Backtracking | Systematic search that reverses on failure to explore alternatives |
| Constraint | A relationship between variables that the solver must satisfy |

### Language Examples

**Prolog — The Flagship.** Prolog (1972, Alain Colmerauer) is the most well-known logic language. Programs consist of facts (data), rules (implications), and queries (questions). Prolog's execution model uses unification and backtracking.

Example — defining and querying family relationships:
```prolog
parent(tom, bob).
parent(bob, ann).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
?- grandparent(tom, ann).  % true
?- grandparent(tom, Who).  % Who = ann
```

Prolog excels at: natural language processing, expert systems, symbolic AI, theorem proving, and constraint satisfaction. It struggles with: numerical computation, systems programming, and problems requiring fine-grained control over execution order.

**Datalog — Logic for Databases.** A restricted subset of Prolog designed for database queries. Unlike Prolog, Datalog always terminates (no recursion through function symbols). It's used in program analysis (Facebook's Doop analyzer), access control policies, and network configuration. Datalog is experiencing a renaissance — tools like Soufflé and Differential Datalog bring logic programming to modern infrastructure.

**miniKanren — Embedded Logic.** A minimal logic programming system (from "The Reasoned Schemer") embeddable in other languages. Implementations exist for Scheme, Clojure, Python, Ruby, and many others. It demonstrates that logic programming can be a library rather than a separate language.

**Constraint Logic Programming (CLP).** Constraint programming generalizes logic programming: define variables, define constraints (relationships between variables), and let a solver find valid assignments. Applications include scheduling, resource allocation, puzzle solving, and configuration. CLP extends Prolog with constraint domains — CLP(FD) for finite domain integers, CLP(R) for real numbers, CLP(B) for booleans. The solver uses specialized algorithms (arc consistency, propagation) rather than naive backtracking.

### Key Facts — Influence on Modern Computing

Logic programming's ideas appear throughout modern computing:

| Modern Technology | Logic Programming Connection |
|---|---|
| SQL | Essentially logic programming over tables — declare what data you want, not how to retrieve it |
| Type inference (Hindley-Milner) | Uses unification — the same algorithm as Prolog |
| Pattern matching (ML/Haskell/Rust) | A restricted form of unification |
| GraphQL | Applies declarative querying to APIs |
| Terraform / declarative infrastructure | Describes desired state rather than steps to reach it |

---

## 🔬 Deep Dive

### Formal Foundations

**Unification** is the core computational primitive. Given two terms, the unification algorithm finds the most general substitution (if one exists) that makes them syntactically identical. Robinson's unification algorithm (1965) runs in near-linear time with optimisations and underpins Prolog's SLD-resolution.

**Hindley-Milner Connection.** The type inference algorithm used by ML, Haskell, and Rust relies on the same unification procedure. Type variables are unified with concrete types during inference — making type checking a specialised form of logic programming.

### Trade-offs and Design Decisions — Why Logic Programming Remains Niche

Despite its elegance, logic programming hasn't gone mainstream because:

1. **Performance unpredictability** — Search-based execution makes performance hard to reason about
2. **Debugging difficulty** — Backtracking makes execution flow hard to follow
3. **Limited ecosystem** — Few libraries and frameworks compared to imperative languages
4. **Paradigm mismatch** — Most programmers think imperatively; logic requires a mental model shift

### Historical Context

Prolog emerged in 1972 from Alain Colmerauer's work on natural language processing at the University of Marseille. Japan's Fifth Generation Computer Project (1982–1992) attempted to build an entire computing platform around logic programming, investing billions before the project was ultimately shelved. Despite that commercial setback, logic programming's core ideas — unification, declarative querying, constraint solving — diffused broadly into mainstream languages and tools (SQL, type inference, pattern matching, declarative infrastructure).

---

## 🏋️ Practice

### Warm-Up

1. In your own words, explain the difference between *unification* and ordinary pattern matching. When does unification do more work?
2. Given the Prolog facts `parent(tom, bob)` and `parent(bob, ann)`, trace the execution of the query `?- grandparent(tom, ann).` step by step, identifying each unification and any backtracking that occurs.
3. Why does Datalog guarantee termination while full Prolog does not? What feature does Datalog restrict to achieve this?

### Core Problems

4. Design a small Prolog knowledge base for a directed graph of five nodes. Write rules for `path(X, Y)` that succeeds when there is a path of any length from X to Y. Identify the risk of infinite loops and explain how to mitigate it.
5. A scheduling problem has four meetings, three rooms, and constraints on which meetings conflict. Sketch how you would model this in CLP(FD) — define the variables, domains, and constraints. What does the solver do that a brute-force loop does not?

### Challenge

6. Implement a miniKanren (or Prolog) program that acts as a simple type-checker for a tiny expression language with integers, booleans, and `if` expressions. The program should *infer* the type of an expression via unification rather than checking a provided annotation.

---

*See also:* [[Programming Paradigms Overview]] · Functional Programming · Declarative Programming

---

## Supporting Chunks / References

- [[Sources Index]]

## References
- [[Programming Languages/Sources/Sources Index|Programming Languages Sources Index]]
