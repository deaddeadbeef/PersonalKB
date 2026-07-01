---
tags: [cs-ds, study]
up: "[[CS Data Structures]]"
confidence: verified
freshness: stable
---

# CS Data Structures Study Index

## Start Here By Goal

Use this page as a selection router first and a drill catalog second.

| Goal | Start with | Then use | Proof you should leave behind |
|---|---|---|---|
| Read data structures as a book | [[CS Data Structures/CS Data Structures Book Reading Spine|CS Data Structures Book Reading Spine]] | [[CS Data Structures/Foundational Concepts/Data Structure Comparison and Selection|Data Structure Comparison and Selection]], [[CS Data Structures/Foundational Concepts/Memory Layout and Cache Performance|Memory Layout and Cache Performance]] | A mental map from workload shape to storage shape |
| Pick the right structure for code | [[DS Cheatsheet — Operation Complexities]] | [[CS Data Structures/Foundational Concepts/Data Structure Comparison and Selection|Data Structure Comparison and Selection]], [[CS Data Structures/Linear Structures/Linear Structures Overview|Linear Structures Overview]], [[CS Data Structures/Trees/Trees Overview|Trees Overview]] | A decision row with operations, constraints, memory behavior, and rejected alternatives |
| Understand indexing and lookup | [[CS Data Structures/Hash-Based Structures/Hash-Based Structures Overview|Hash-Based Structures Overview]] | [[CS Data Structures/Tries and String Structures/Tries and String Structures Overview|Tries and String Structures Overview]], [[CS Data Structures/Graphs/Graphs Overview|Graphs Overview]] | A lookup-path explanation that names collisions, branching, locality, or compression |
| Prepare for recall | [[DS Review — Linear Structures]] | The family drill that matches the weak area | A corrected cost table plus one implementation invariant |

## Review Drills

- [[DS Review — Linear Structures]]
- [[DS Review — Trees and Balancing]]
- [[DS Review — Hash Tables]]
- [[DS Review — Advanced Structures]]

## Cheatsheets

- [[DS Cheatsheet — Operation Complexities]]

## Suggested Pass Order

1. Start with [[DS Cheatsheet — Operation Complexities]] for the big-picture cost model.
2. Drill one family at a time: [[DS Review — Linear Structures]], [[DS Review — Hash Tables]], then [[DS Review — Trees and Balancing]].
3. When a prompt feels shaky, jump back to the matching canonical hub instead of memorizing the table in isolation.

## How to Use

1. Read canonical pages for deep understanding
2. Use review drills to test recall
3. Reference cheatsheet for quick lookup
4. Explore chunks for atomic facts and QnA seeds

## Navigation

- Foundations: [[Asymptotic Analysis and Big-O Notation]], [[Amortized Analysis]], [[Memory Layout and Cache Performance]]
- Core families: [[Linear Structures Overview]], [[Hash-Based Structures Overview]], [[Trees Overview]]
- Selection help: [[Data Structure Comparison and Selection]]

## Study Loop

Use this page as a retrieval-practice hub, not as another article to passively read. Each session should start with one data-structure family, one concrete operation table, and one implementation trade-off. For example, compare array-backed stacks with linked stacks, then explain where the asymptotic cost hides cache or allocation costs. The point is to move from name recognition to selection judgment.

A good pass through the study set has three outputs: a cost table you can reproduce from memory, a short explanation of the invariant that keeps the structure correct, and one scenario where the obvious structure is not the right choice. If the answer depends on workload shape, say so explicitly: read-heavy, write-heavy, ordered, unordered, bounded memory, streaming, or concurrent.

## Evidence of Mastery

You are ready to leave this index when you can choose between arrays, linked lists, hash tables, balanced trees, heaps, tries, union-find, and graph-adjacent structures without looking up the table. The proof is not memorizing Big-O alone; it is explaining the operational consequence of each choice under realistic constraints such as memory locality, resizing, collision behavior, rebalancing, and iterator invalidation.

When a review drill exposes a weak area, go back to the canonical hub first, then return to the drill. The intended motion is article -> recall -> correction -> second recall. Avoid collecting more pages until the existing pages can change your design choices in code.

## References

- [[CS Data Structures]]
- [[CS Data Structures/Sources/Sources Index|Sources Index]]
- [[Data Structure Comparison and Selection]]
