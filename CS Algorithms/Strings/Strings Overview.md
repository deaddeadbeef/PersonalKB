---
tags:
  - csa
  - moc
up: "[[CS Algorithms]]"
confidence: verified
---
# Strings Overview

String algorithms compute relationships between sequences — exact matches, longest common parts, and minimum-cost transformations. All three algorithms in this domain are built on dynamic programming or failure-function preprocessing.

---

## Learn in This Order

1. [[String Matching - KMP]] — failure function; avoiding re-comparison; $\Theta(n+m)$ exact matching
2. [[LCS - Longest Common Subsequence]] — $\Theta(mn)$ DP table; backtracking the alignment; DNA comparison
3. [[Edit Distance]] — minimum-cost insert/delete/replace; Levenshtein generalisation; $\Theta(mn)$ DP

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[String Matching - KMP]] | KMP failure function; linear-time exact pattern matching |
| [[LCS - Longest Common Subsequence]] | DP alignment table; longest common subsequence; DNA diff |
| [[Edit Distance]] | Levenshtein distance; minimum operations to transform one string into another |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Exact matching vs approximate? | KMP does *exact* pattern matching in $\Theta(n+m)$. Edit distance measures *approximate* similarity by counting operations. |
| Subsequence vs substring? | Subsequence = characters in order but not necessarily contiguous (LCS). Substring = contiguous portion. |
| LCS vs Edit Distance? | LCS finds the longest shared subsequence; edit distance counts the cheapest way to make two strings identical. Both use $\Theta(mn)$ DP tables with different recurrences. |
| When to prefer KMP over naive? | KMP pays $\Theta(m)$ preprocessing cost to guarantee $\Theta(n)$ search time; worth it whenever m is non-trivial and you search multiple texts. |

---

## How to Navigate

- **Pattern matching problem?** → [[String Matching - KMP]]
- **Sequence alignment / similarity?** → [[LCS - Longest Common Subsequence]]
- **Minimum edit operations between two strings?** → [[Edit Distance]]

---

## Related Domains

- **[[Foundations and Analysis Overview]]** — all three algorithms rely on dynamic programming (see [[Dynamic Programming]]) and asymptotic analysis. The KMP failure function is analysed with amortised reasoning.
- **[[Graphs Overview]]** — sequence alignment generalises to DAG shortest paths; edit distance DP is equivalent to a shortest path on a grid DAG.

## References
- [[CS Algorithms/Sources/Sources Index|CS Algorithms Sources Index]]
