---
id: au-ch-07
type: book-chapter
chapter: 7
book: "Algorithms Unlocked"
author: "Thomas H. Cormen"
status: processed
chunk_count: 4
source: "[[Cormen 2013 - Algorithms Unlocked]]"
tags:
  - csa
  - book-chapter
up: "[[CS Algorithms/Books/Algorithms Unlocked/Chapter Index|Chapter Index]]"
confidence: established
freshness: stable
tier-coverage: [core]
---
# AU — Chapter 07: Algorithms on Strings

## Summary

Chapter 7 covers three classical string problems. **Longest Common Subsequence (LCS)**: a subsequence preserves relative character order but need not be contiguous. Naïve enumeration over all 2ᵐ subsequences is exponential; dynamic programming defines l[i,j] as the LCS length of the first i characters of X and the first j of Y. The recurrence either matches the last characters (l[i,j] = l[i−1,j−1]+1) or takes the better of skipping one (max of l[i−1,j] and l[i,j−1]). The m×n table fills in $\Theta(mn)$; the actual subsequence is reconstructed by backtracking. Applied to DNA strand comparison. **Edit distance**: minimum-cost transformation of string X to string Y via operations (copy, replace, delete, insert). Another DP table over prefixes; generalises Levenshtein distance; central to diff tools and sequence alignment. **KMP string matching**: given text T (length n) and pattern P (length m), find all occurrences. Naïve search is $\Theta(nm)$ worst case. KMP preprocesses P in $\Theta(m)$ to compute a *failure function* π, where π[k] is the length of the longest proper prefix of P[1..k] that is also a suffix. On a mismatch at position k in P, shift to position π[k−1] instead of 1, preserving all partial matches. Matching runs in $\Theta(n)$; total time $\Theta(n+m)$.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Subsequence | Characters in order, non-contiguous (vs substring which is contiguous) |
| LCS | Longest sequence that is a subsequence of both input strings |
| LCS recurrence | l[i,j] = l[i-1,j-1]+1 if match; max(l[i-1,j], l[i,j-1]) otherwise |
| Edit distance | Min cost to transform X into Y via copy/replace/delete/insert |
| KMP failure function π | Longest proper prefix-suffix for each prefix of P |
| KMP total time | $\Theta(m)$ preprocessing + $\Theta(n)$ matching = $\Theta(n+m)$ |

## Chunk Candidates

- [x] [[Strings - LCS dynamic programming fills an m by n table in Theta(mn)]]
- [x] [[Strings - KMP failure function enables Theta(n+m) string matching]]
- [x] [[Strings - Edit Distance recurrence computes minimum-cost alignment via DP over prefixes]]
- [x] [[Strings - Edit Distance DP table fills in Theta(mn) time and O(mn) space]]

## Wiki Pages Seeded

- [[LCS - Longest Common Subsequence]] — DP recurrence and reconstruction
- [[Edit Distance]] — operations, recurrence, applications
- [[String Matching - KMP]] — failure function, matching algorithm

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]].
