---
tags: [cs-algorithms, raw]
source_type: textbook
source_title: "Randomized Algorithms"
authors: "Rajeev Motwani, Prabhakar Raghavan"
year: 1995
---

# Randomized Algorithms

## Summary
Randomized algorithms use random coin flips as part of their logic, achieving simplicity, efficiency, or both compared to deterministic counterparts. They fall into two categories: Las Vegas algorithms always produce the correct result but have random running time (e.g., randomized quicksort), and Monte Carlo algorithms run in deterministic time but may produce incorrect results with bounded probability (e.g., Miller-Rabin primality test). The analysis of randomized algorithms relies on probability theory—expectations, tail bounds, and probabilistic recurrences—to establish rigorous performance guarantees that hold with high probability.

## Key Claims
- Las Vegas algorithms guarantee correctness; their running time is a random variable with a bounded expectation (e.g., randomized quicksort runs in O(n log n) expected time for any input)
- Monte Carlo algorithms guarantee running time; their error probability is bounded and can be reduced by independent repetition (k repetitions reduce one-sided error from ε to εᵏ)
- Randomized quicksort selects a pivot uniformly at random, ensuring that the expected number of comparisons is 2n ln n ≈ 1.39n log₂ n for any input of size n, eliminating adversarial worst cases
- Karger's randomized min-cut algorithm contracts random edges until two vertices remain, finding a minimum cut with probability at least 2/(n(n−1)); repeating O(n² log n) times yields the min-cut with high probability in O(n⁴ log n), improved to O(n² log³ n) by Karger-Stein
- The Miller-Rabin primality test is a Monte Carlo algorithm that declares a composite number prime with probability at most 1/4 per witness; with k independent witnesses, the error probability is at most 4⁻ᵏ, giving effective certainty for k = 40 (error < 10⁻²⁴)

## Atomic Facts
1. Randomized quicksort's expected comparison count on any input of size n is exactly 2n·H_n − 4n + 2·H_n + 2 ≈ 2n ln n + O(n), where H_n is the nth harmonic number; the probability of exceeding 4n ln n comparisons is at most 1/n by Markov's inequality
2. Karger's contraction algorithm succeeds with probability ≥ 2/(n(n−1)); for n = 100, a single trial finds the min-cut with probability ≥ 0.02%, but n(n−1)/2 · ln n ≈ 22,800 repetitions find it with probability ≥ 1 − 1/n
3. Miller-Rabin with k = 40 witnesses runs in O(k · log² n · log log n · log log log n) time using fast multiplication; for a 2048-bit RSA prime candidate, this is approximately 10⁶ operations—negligible compared to key generation
4. Chernoff bounds state that for n independent Bernoulli trials with expected sum μ, P(X ≥ (1+δ)μ) ≤ (e^δ/(1+δ)^{1+δ})^μ; for δ = 1 (twice the mean), this gives P(X ≥ 2μ) ≤ (e/4)^μ ≈ 0.68^μ, exponentially small in μ
5. The randomized algorithm for approximate median finding (median of medians of random samples) uses a sample of size O(n^{3/4}) to find an element within rank n/2 ± √n with probability ≥ 1 − O(1/√n), enabling O(n) expected-time exact median via partitioning
6. Treaps (tree + heap) maintain BST order on keys and heap order on random priorities, achieving O(log n) expected height and O(log n) expected time for search, insert, and delete—providing a simple alternative to balanced BSTs with expected rather than worst-case bounds

## Significance
Randomized algorithms represent a fundamental paradigm shift in algorithm design, demonstrating that randomness is a powerful computational resource. Randomized quicksort is faster in practice than any deterministic O(n log n) sort due to its simplicity and cache behavior. Cryptography depends entirely on randomized primality testing (no deterministic polynomial-time test was known until AKS in 2002, and Miller-Rabin remains preferred in practice). Random sampling underpins load balancing (the power of two choices reduces maximum load from O(log n/log log n) to O(log log n)), hashing (universal and tabulation hashing), and machine learning (stochastic gradient descent). The theoretical tools developed for analyzing randomized algorithms—linearity of expectation, union bounds, Chernoff bounds, Lovász Local Lemma—form the backbone of modern probabilistic combinatorics.

## Chunks Extracted
*Pending*
