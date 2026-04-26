---
tags:
  - csa
  - csa/analysis
confidence: verified
up: "[[Foundations and Analysis Overview]]"
tier-coverage: [intuition, core, deep-dive, practice]
---
# Algorithm Definition

> **One-line summary**: An algorithm is a finite, precisely specified sequence of steps that a computational device can execute to solve a well-defined problem.

## 🎯 Intuition
**The Core Idea:** An algorithm is a recipe that a computer can follow — every step unambiguous, every path terminating.
**Analogy:** Think of a recipe in a cookbook. A human recipe says "season to taste"; an algorithm says "add exactly 5 grams of salt." The computer is a literal-minded chef — it cannot improvise, so every instruction must be machine-precise.
**Why It Matters:** Every program you write is an algorithm. Understanding what qualifies a sequence of steps as an algorithm — finiteness, precision, effectiveness — is the prerequisite for analysing correctness and efficiency.

---

## ⚙️ Core Mechanics
### Definition / Formal Statement
An **algorithm** is a finite, precisely specified sequence of steps that a computational device can execute to solve a well-defined problem. It must satisfy four essential properties.

### Key Properties

| Property | Description |
|----------|-------------|
| **Finiteness** | Terminates after a finite number of steps |
| **Precision** | Each step is unambiguous — machine-executable, not human-interpretable |
| **Input / Output** | Takes zero or more inputs; produces at least one output |
| **Effectiveness** | Each basic step is feasible to carry out |

### Algorithm vs Everyday Procedure
A human "commute to work" procedure tolerates imprecision ("if traffic is bad, take the alternate route"). A computer algorithm cannot — "bad traffic" must be defined by a concrete measurable condition. This distinction is the first thing Cormen establishes in *Algorithms Unlocked*.

### What We Want From an Algorithm
1. **Correctness** — produces the right answer for every valid input (or a bounded approximation).
2. **Efficiency** — uses computational resources (primarily time, also memory) economically.

### Correctness Spectrum

| Type | Description | Example |
|------|-------------|---------|
| Exact | Always correct for every input | Binary search, merge sort |
| Probabilistic | Correct with high probability; error rate bounded | Miller-Rabin primality test |
| Approximation | Solution within factor α of optimal | TSP 2-approximation |

### Algorithms as Technology
Cormen's framing: algorithms are a *technology* on par with hardware and operating systems. GPS routing, web search ranking, public-key encryption, and data compression all depend on specific algorithm choices — and a better algorithm on slower hardware can outperform a worse algorithm on faster hardware once inputs are large enough.

### Worked Examples
**Example — Is "find the largest element" an algorithm?**
1. *Input*: an array A of n numbers.
2. *Steps*: Set max = A[1]. For i = 2 to n, if A[i] > max then max = A[i].
3. *Output*: max.
4. *Check*: Finite (n−1 comparisons), precise (each comparison is unambiguous), effective (comparison and assignment are basic operations), has input/output. ✅ Algorithm.

**Example — Is Bogosort an algorithm?**
Bogosort: randomly shuffle the array, check if sorted, repeat. The randomised version terminates with probability 1 but has no finite worst-case bound. The deterministic variant that enumerates all n! permutations *is* finite. Whether Bogosort qualifies depends on which variant — illustrating that finiteness is non-trivial.

### Key Facts
- An algorithm must terminate; an infinite loop is not an algorithm.
- Correctness and efficiency are the two primary desiderata.
- The RAM model underpins analysis by treating each basic operation as unit cost.

---

## 🔬 Deep Dive
### Formal Proof / Derivation
The four properties (finiteness, precision, input/output, effectiveness) trace back to Turing's 1936 formalisation. A procedure satisfying these properties can be simulated by a Turing machine, establishing equivalence between "algorithm" and "Turing-computable function." This connection underpins the Church-Turing thesis: anything we would intuitively call "computable" is computable by a Turing machine.

### Subtleties and Edge Cases
- **Non-terminating procedures**: A web server's event loop runs indefinitely — it is a *program*, not an algorithm in the strict sense. Each individual request handler may be an algorithm.
- **Randomised algorithms**: Algorithms like Miller-Rabin use randomness. They terminate in finite expected time and their correctness is probabilistic, not absolute. They are still algorithms.
- **Approximation vs heuristic**: An approximation algorithm has a *proven* bound (e.g., 2-approximation for metric TSP). A heuristic (e.g., simulated annealing) has no such guarantee.
- **The effectiveness trap**: "Compute the Kolmogorov complexity of string s" is precisely stated — but it is uncomputable, violating effectiveness at a deep level.

### Historical Context
The formal concept predates computers — al-Khwārizmī's 9th-century treatise on algebra gave the word its name. The modern formalisation came with Turing (1936) and Church (1936). Cormen's *Algorithms Unlocked* (2013), Chapter 1, frames algorithms as a technology, emphasising their practical importance alongside hardware advances.

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Which of the four essential properties does "search until you feel you've found a good result" violate?
2. Is a program that prints all prime numbers (never terminating) an algorithm? Why or why not?
3. Name one exact algorithm and one probabilistic algorithm.

### Core Problems
1. **Property check**: Given Bogosort (randomly shuffle, check sorted, repeat), identify which essential properties are satisfied and which are violated. Discuss the deterministic permutation-enumeration variant vs the randomised variant.

2. **Technology argument**: Algorithm X is $O(n²)$ on a 10⁹ ops/sec machine. Algorithm Y is $O(n \lg n)$ on a 10⁷ ops/sec machine. Find the crossover input size n where Y becomes faster than X.

### Challenge
1. Prove that for any decidable problem, there exist infinitely many distinct algorithms that solve it. *(Hint: consider padding with no-ops.)*

---

*See also:* [[Asymptotic Notation]] | [[Loop Invariant]] | **CS Data Structures:** [[Asymptotic Analysis and Big-O Notation]]

## Supporting Chunks

- [[Analysis - Algorithm correctness exists on a spectrum from exact to probabilistic to approximation]]
- [[Analysis - Algorithm choice matters as much as hardware at large n]]
- [[Analysis - The RAM model treats each basic operation as unit cost]]

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Sources Index]]. Chapter 1.
