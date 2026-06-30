---
tags:
  - csa
  - csa/study
  - csa/strings
up: "[[Algorithms Study Index]]"
confidence: policy
---
# Strings — Review Drill

Active-recall drill covering dynamic programming on strings and linear-time string matching.

**Canon pages:** [[LCS - Longest Common Subsequence]] · [[Edit Distance]] · [[String Matching - KMP]]

---

## How to Use

Try to state the recurrence, complexity, and table-construction strategy for each algorithm before checking the canonical page. DP problems especially benefit from practising the sub-problem definition from scratch.

---

## Core Recall

**Longest Common Subsequence (LCS)**

Q: Define the LCS problem.
A: Given strings A (length m) and B (length n), find the longest subsequence common to both. A subsequence need not be contiguous — elements must appear in order but can skip characters.

Q: State the LCS sub-problem and recurrence.
A: Let LCS(i, j) = length of the LCS of A[1..i] and B[1..j].
- If i = 0 or j = 0: LCS(i, j) = 0.
- If A[i] = B[j]: LCS(i, j) = LCS(i−1, j−1) + 1.
- Otherwise: LCS(i, j) = max(LCS(i−1, j), LCS(i, j−1)).

Q: What is the time and space complexity of the LCS DP?
A: Time: $\Theta(mn)$ — fill an m × n table, each cell in $O(1)$. Space: $O(mn)$ for the full table; $O(min(m, n)$) if only the length is needed (two-row rolling array).

Q: Give a real-world application of LCS.
A: DNA sequence alignment — finding the longest stretch of shared genetic material between two sequences. Also used in diff tools (e.g., Unix `diff`) to identify unchanged lines between two files.

Q: How do you recover the actual LCS string (not just its length)?
A: Backtrack through the table: at cell (i, j), if A[i] = B[j], record A[i] and move to (i−1, j−1); else move toward the larger neighbour (up or left). Backtracking takes $O(m + n)$ time.

---

**Edit Distance (Levenshtein Distance)**

Q: Define the edit distance problem and its three allowed operations.
A: Given strings A and B, find the minimum number of single-character operations to transform A into B. Operations: **insert** a character, **delete** a character, **substitute** one character for another. Each operation has a cost (usually 1 for Levenshtein distance).

Q: State the edit distance recurrence.
A: Let D(i, j) = edit distance between A[1..i] and B[1..j].
- D(i, 0) = i (delete i characters).
- D(0, j) = j (insert j characters).
- If A[i] = B[j]: D(i, j) = D(i−1, j−1).
- Otherwise: D(i, j) = 1 + min(D(i−1, j), D(i, j−1), D(i−1, j−1)) — delete, insert, substitute.

Q: How does the edit distance recurrence generalise beyond equal operation costs?
A: Assign costs cᵢ (insert), cᵈ (delete), cₛ (substitute). The recurrence becomes:
- D(i, j) = min(D(i−1, j) + cᵈ, D(i, j−1) + cᵢ, D(i−1, j−1) + cₛ·[A[i] ≠ B[j]]).
This models biological sequence alignment with affine or custom gap penalties.

Q: What is the time and space complexity of edit distance DP?
A: Time: $\Theta(mn)$. Space: $O(mn)$ for the full table; $O(min(m, n)$) with a rolling-row approach.

Q: How is LCS related to edit distance?
A: If only insertions and deletions are allowed (no substitutions), edit distance = (m − LCS(A, B)) + (n − LCS(A, B)) = m + n − 2·LCS(A, B). Minimising edit distance then corresponds to maximising LCS.

---

**KMP String Matching**

Q: What problem does KMP solve, and what is its time complexity?
A: Pattern matching: find all occurrences of pattern P (length m) in text T (length n). Time: $\Theta(n + m)$ — $O(m)$ to build the failure function, $O(n)$ to scan the text.

Q: What is the KMP failure function (also called the prefix function)?
A: For pattern P, failure[i] = length of the longest proper prefix of P[1..i] that is also a suffix of P[1..i]. This tells the algorithm how far back to reset the pattern pointer on a mismatch — instead of restarting from the beginning.

Q: Why does the failure function depend only on the pattern, not the text?
A: The failure function encodes the self-similarity structure of the pattern. The same function applies to every text the pattern is searched against, so it can be precomputed once and reused across multiple texts.

Q: Describe the KMP matching process in one sentence.
A: Scan the text with a text pointer i and a pattern pointer j; on match, advance both; on mismatch, reset j to failure[j−1] (without moving i back) until either the whole pattern matches (output a hit) or j = 0 (advance i).

Q: What naive algorithm does KMP improve upon, and what is the naive algorithm's complexity?
A: Naïve brute-force string matching: try every starting position in T, compare P character by character. Worst case: $\Theta(nm)$ — e.g., T = "aaa…a" and P = "aa…ab". KMP avoids the text pointer ever moving backward.

Q: Give an example of a pattern where the failure function is non-trivial.
A: P = "abcabc". failure = [0, 0, 0, 1, 2, 3]. After matching "abcab" and then a mismatch on position 6, KMP resets j to failure[5] = 2, meaning it resumes matching from P[3] rather than P[1], exploiting the "abc" overlap.

---

## Compare and Contrast

**LCS vs Edit Distance**

| Aspect | LCS | Edit Distance |
|--------|-----|--------------|
| Problem | Longest common subsequence | Minimum operations to transform |
| Operations | Identify shared elements | Insert, delete, (substitute) |
| Recurrence shape | Max of sub-problems | Min of sub-problems + cost |
| Table size | m × n | m × n |
| Complexity | $\Theta(mn)$ | $\Theta(mn)$ |
| Application | Sequence alignment, diff | Spell-checking, DNA alignment with gaps |

**KMP vs Naïve String Matching**

| Aspect | Naïve | KMP |
|--------|-------|-----|
| Text pointer | Can move backward | Never moves backward |
| Pattern pointer | Resets to 0 on mismatch | Resets to failure[j−1] |
| Worst-case | $\Theta(nm)$ | $\Theta(n + m)$ |
| Precomputation | None | $O(m)$ failure function |
| Code complexity | Simple | Moderate |

**DP on Strings vs Sequence DP**

| | LCS | Edit Distance |
|--|-----|--------------|
| Sub-problem | Prefix of both strings | Prefix of both strings |
| Direction | Extend when chars match | Always advance; cost depends on match |
| Backtrack to recover solution | Yes (trace through table) | Yes (trace through table) |
| Optimal substructure | ✅ | ✅ |

---

## Common Mistakes

1. **LCS vs longest common substring** — LCS allows skipping characters (subsequence); longest common *substring* requires contiguous matching. Different recurrences and different applications.

2. **Edit distance with substitution vs without** — if substitution is not allowed, edit distance reduces to m + n − 2·LCS. If substitution *is* allowed but costs 2 (= 1 delete + 1 insert), the recurrence changes. Know which variant you are working with.

3. **KMP failure function off-by-one** — the failure function at position i is the length of the longest proper prefix of P[1..i] that equals a suffix. "Proper" means strictly shorter than the full string, so failure[i] < i always.

4. **KMP does not move i backward** — a common implementation mistake is to decrement the text pointer on mismatch. KMP never moves the text pointer backward; only the pattern pointer resets.

5. **LCS space optimisation** — if only the length is needed, a two-row rolling array reduces space from $O(mn)$ to $O(min(m, n)$). If you need to recover the actual sequence, you must keep the full table.

---

## Links Back

- [[LCS - Longest Common Subsequence]] — DP table, recurrence, backtracking, application
- [[Edit Distance]] — Levenshtein recurrence, generalised costs, relation to LCS
- [[String Matching - KMP]] — failure function construction, matching algorithm, $\Theta(n+m)$ analysis

## References
- [[CS Algorithms/Sources/Sources Index|CS Algorithms Sources Index]]
