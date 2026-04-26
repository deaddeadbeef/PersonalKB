---
tags: [pl, chunk, paradigms, logic]
up: "[[Logic and Constraint Programming]]"
---

# Logic Programming Prolog and Its Hidden Influence

Logic programming, where you describe WHAT you want rather than HOW to compute it, has influenced SQL, pattern matching, and modern constraint solving.

## Prolog Fundamentals

`prolog
% Facts
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).

% Rules
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Query
?- grandparent(tom, ann).
% true - Prolog finds: tom->bob->ann

?- grandparent(tom, Who).
% Who = ann - Prolog solves for the variable
`

## Unification: The Core Mechanism

Prolog's power comes from unification — finding variable assignments that make two terms equal:
`prolog
?- f(X, b) = f(a, Y).
% X = a, Y = b (unification finds the solution)
`

This is the same mechanism behind:
- ML/Haskell/Rust pattern matching (one-way unification)
- TypeScript type inference (constraint solving)
- Database query optimization (predicate pushdown)

## Logic Programming's Hidden Influence

| Descendant | Origin | Example |
|-----------|--------|---------|
| SQL | Relational algebra + logic | SELECT * WHERE condition is a query, not a procedure |
| Pattern matching | Unification | Rust match, Haskell patterns |
| Type inference | Constraint solving | HM inference uses unification |
| Datalog | Restricted Prolog | Used in static analysis (Souffle, Datomic) |
| miniKanren | Embedded logic | Logic programming in Scheme, Python, Clojure |
| Regular expressions | Pattern matching | Backtracking, like Prolog search |

## Datalog: Logic Programming's Practical Descendant

Datalog is a restricted form of Prolog (no function symbols) that guarantees termination:
`datalog
// Static analysis example (points-to analysis)
pointsTo(x, h) :- assign(x, h).
pointsTo(x, h) :- assign(x, y), pointsTo(y, h).
`

Used in:
- **Souffle:** Static analysis for security vulnerabilities
- **Datomic:** Database query language
- **Differential Datalog:** Incremental computation

## Key Insight
Logic programming didn't become mainstream as a paradigm, but its ideas permeate modern computing. Pattern matching, type inference, SQL, and constraint solving all trace back to Prolog's unification. Understanding logic programming deepens understanding of ALL programming languages.

## References
→ [[Sources Index]]
