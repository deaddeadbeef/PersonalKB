---
tags: [cs-algorithms, raw]
source_type: textbook
source_title: "String Matching Algorithms"
authors: "Donald Knuth, James Morris, Vaughan Pratt; Michael Rabin, Richard Karp"
year: 1977
---

# String Matching Algorithms

## Summary
String matching algorithms find all occurrences of a pattern string of length m in a text string of length n. The naive algorithm runs in O(nm) worst-case time, but three landmark algorithms achieve significantly better bounds. Rabin-Karp uses rolling hash functions for O(n + m) expected time with O(nm) worst case. The Knuth-Morris-Pratt (KMP) algorithm preprocesses the pattern to build a failure function in O(m) time, then matches in O(n) time, achieving O(n + m) worst-case guaranteed. Boyer-Moore achieves sublinear expected time in practice by scanning the pattern right-to-left and skipping large sections of text.

## Key Claims
- The naive string matching algorithm performs at most (n − m + 1) × m character comparisons in the worst case, giving O(nm); this worst case is achieved by patterns like aaa...ab in text aaa...aaa
- KMP constructs a failure function π[i] = length of the longest proper prefix of pattern[0..i] that is also a suffix, in O(m) time; during matching, the text pointer never retreats, guaranteeing O(n) scanning
- Rabin-Karp computes a rolling hash over m-character windows in O(1) per shift using h(s+1) = (d · (h(s) − T[s] · d^{m−1}) + T[s+m]) mod q, achieving O(n + m) expected time with a prime q reducing spurious matches to O(n/q)
- Boyer-Moore combines the bad-character rule (shift pattern to align the mismatched text character) and the good-suffix rule (shift pattern to align a matching suffix), achieving O(n/m) best-case time for long patterns
- Aho-Corasick builds a finite automaton from k patterns of total length m in O(m) time, then searches text in O(n + z) time where z is the number of matches, making it optimal for multi-pattern matching

## Atomic Facts
1. KMP's failure function for pattern "abcabd" is π = [0, 0, 0, 1, 2, 0]; upon mismatch at position 5 (d≠c), the pattern shifts to align position 2 (c) with the current text position, avoiding re-scanning "ab"
2. Rabin-Karp with a prime q ≈ 10⁹ has a false positive probability of approximately m/q per window; for n = 10⁶ and m = 100, the expected number of false positives is about 10⁻¹, making verification negligible
3. Boyer-Moore in its best case compares only n/m characters: for a pattern of length m = 100 in text of length n = 1,000,000, it makes approximately 10,000 comparisons—a 100× speedup over linear scanning
4. The Aho-Corasick automaton has at most m + 1 states and is constructed with a BFS-based failure link computation; for a dictionary of 10,000 patterns totaling 500,000 characters, the automaton fits in approximately 4 MB
5. The Z-algorithm computes the Z-array in O(n) time, where Z[i] = length of the longest substring starting at position i that matches a prefix of the string; this solves pattern matching by concatenating P$T and finding Z[i] = m
6. Suffix arrays sort all n suffixes in O(n) time (SA-IS algorithm) and enable O(m log n) pattern matching via binary search; combined with the LCP array, they provide O(m + log n) matching and support for counting all k occurrences in O(m + log n + k)

## Significance
String matching is fundamental to text editors (find/replace), search engines (inverted index construction), bioinformatics (DNA sequence alignment and motif finding), network security (deep packet inspection uses Aho-Corasick), and compilers (lexical analysis). KMP's failure function is a beautiful example of amortized analysis—though individual shifts may vary, the total text pointer advances at most 2n times. Rabin-Karp's use of hashing for pattern matching pioneered fingerprinting techniques in algorithms, influencing plagiarism detection (document fingerprinting) and file synchronization (rsync). The progression from naive O(nm) to optimal O(n + m) illustrates how preprocessing the pattern can eliminate redundant comparisons.

## Chunks Extracted
*Pending*
