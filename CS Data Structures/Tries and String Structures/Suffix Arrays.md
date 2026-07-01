---
tags: [cs-ds, tries]
up: "[[Tries and String Structures Overview]]"
confidence: verified
freshness: stable
tier-coverage: [intuition, core, deep-dive, practice]
---
# Suffix Arrays

> **One-line summary**: A suffix array is the sorted array of all suffix starting positions of a string, providing a space-efficient alternative to suffix trees with $O(m \log n)$ substring search and $O(n)$ construction via algorithms like SA-IS.

## 🎯 Intuition
**The Core Idea:** Sort all suffix starting positions once, then answer substring queries by binary-searching that sorted order.
**Analogy:** Like a book's index sorted alphabetically — each entry points to a page (position) where a word starts, and you binary-search the index to find any word.
**Why It Matters:** Suffix arrays made suffix-based indexing practical by sharply reducing memory compared with suffix trees. With LCP arrays and compressed descendants like the FM-index, they underpin full-text search, compression, and large-scale bioinformatics workloads such as BWA and Bowtie.

---

## ⚙️ Core Mechanics
### How It Works
Given a string S of length n, its **suffix array** SA is an array of integers [0, n) sorted so that the suffix starting at position SA[0] is lexicographically smallest, SA[1] the next smallest, and so on. Concretely, SA is a permutation of {0, 1, ..., n - 1} such that S[SA[0]..] < S[SA[1]..] < ... < S[SA[n-1]..]. This compact representation requires only n integers (4n or 8n bytes depending on word size), a significant improvement over suffix trees' ~20n bytes.

Substring search for a pattern P of length m reduces to **binary search** over the suffix array: because suffixes are sorted, two binary searches locate the range of suffixes that begin with P, yielding $O(m \log n)$ time. The **LCP (Longest Common Prefix) array** -- where LCP[i] stores the length of the longest common prefix between SA[i] and SA[i - 1] -- accelerates this to $O(m + \log n)$ using Manber-Myers-style search, or even $O(m)$ with additional preprocessing. The LCP array also enables efficient computation of longest repeated substrings, longest common substrings, and the number of distinct substrings.

Construction algorithms have evolved from the original $O(n \log^{2} n)$ approach by Manber and Myers to $O(n \log n)$ methods using radix sort, and finally to **linear-time** algorithms: the **DC3/Skew algorithm** (Karkkäinen and Sanders, 2003) and **SA-IS** (Nong, Zhang, and Chan, 2009). SA-IS is considered the most practical $O(n)$ algorithm due to its simplicity and cache efficiency. Alternatively, a suffix array can be derived from a suffix tree in $O(n)$ time via DFS, though building the suffix tree first negates the space advantage.

Suffix arrays also connect directly to compression and succinct indexing. The Burrows-Wheeler Transform can be derived from the sorted suffix order, and FM-indexes layer rank/select structures on top to support compressed full-text search. In practice, the SA + LCP combination is the array-based workhorse for large texts, while enhanced suffix arrays add auxiliary tables to close much of the theoretical gap with suffix trees.

### Key Operations

| Operation                    | Time            | Notes                                |
|------------------------------|-----------------|--------------------------------------|
| Construction (SA-IS)         | $O(n)$            | Linear time, practical               |
| Construction (Manber-Myers)  | $O(n \log n)$      | Simpler to implement                 |
| Substring search             | $O(m \log n)$      | Two binary searches                  |
| Search with LCP acceleration | $O(m + \log n)$    | Using LCP array                      |
| Build LCP array (Kasai)      | $O(n)$            | Requires inverse suffix array        |
| Longest repeated substring   | $O(n)$            | Maximum value in LCP array           |
| Count distinct substrings    | $O(n)$            | n(n+1)/2 - sum of LCP[i]            |
| Space                        | $O(n)$            | 4n-8n bytes + optional LCP           |

### Key Facts
- Space: n integers -- 4n bytes (32-bit) or 8n bytes (64-bit), versus ~20n bytes for a suffix tree.
- Binary search for pattern of length m: $O(m \log n)$; with LCP array: $O(m + \log n)$.
- SA-IS constructs the suffix array in $O(n)$ time and $O(n)$ space; it is the standard in practice.
- The LCP array can be built in $O(n)$ from the suffix array using Kasai's algorithm.
- SA + LCP array together replace the suffix tree for nearly all applications with lower memory.
- Counting occurrences of a pattern: $O(m \log n)$ search to find the range, then range length gives the count.
- Enhanced suffix arrays (SA + LCP + additional tables) achieve $O(m + k)$ for listing k occurrences.
- Suffix arrays form the basis of the Burrows-Wheeler Transform used in bzip2 and FM-index for compressed full-text search.

---

## 🔬 Deep Dive
### Formal Properties
- SA is a permutation of {0, 1, ..., n - 1} ordered by lexicographic comparison of suffixes S[i..].
- Pattern matching works via a contiguous suffix-array interval: all suffixes beginning with a pattern P occupy one consecutive range in sorted order, which is why two binary searches suffice.
- LCP[i] stores the common-prefix length of suffixes at SA[i] and SA[i - 1], allowing repeated prefix comparisons to be reused across adjacent suffixes.
- The number of distinct substrings of a string of length n is n(n+1)/2 - sum of LCP[i].
- Kasai's algorithm builds the LCP array in $O(n)$ time using the inverse suffix array.

| Aspect              | Suffix Array             | Suffix Tree              |
|---------------------|--------------------------|--------------------------|
| Space               | 4n-8n bytes              | ~20n bytes               |
| Substring search    | $O(m \log n)$               | $O(m)$                     |
| Construction        | $O(n)$ SA-IS               | $O(n)$ Ukkonen             |
| Implementation      | Simpler (array-based)    | Complex (pointers)       |
| Online construction | No                       | Yes (Ukkonen)            |
| LCP computation     | Separate $O(n)$ step       | Implicit in tree depth   |

### Edge Cases and Pitfalls
- Off-by-one errors are common because SA positions are 0-based in many descriptions while suffix-tree literature often uses 1-based indexing.
- A naïve binary search that repeatedly compares long common prefixes can do unnecessary work unless LCP information is exploited carefully.
- Many linear-time constructions and BWT/FM-index pipelines assume a unique sentinel or endmarker; omitting it can break lexicographic assumptions.
- Suffix arrays are excellent for static texts but awkward for frequent updates, since inserting one character can invalidate much of the order.

### Real-World Usage
Suffix arrays are the practical indexing layer behind full-text search, compressed indexes, and large-scale sequence analysis. Their connection to the BWT and FM-index makes them central to compressed search systems, while tools such as BWA and Bowtie rely on suffix-array-derived indexing ideas to scale genome matching.

---

## 🏋️ Practice
### Warm-Up (5 min)
- Why do all suffixes that start with a pattern P appear in one contiguous interval of the suffix array?
- What extra power does the LCP array add beyond plain binary search on the suffix array?

### Core Problems
- **Build and Query a Suffix Array** — construct SA for a string and implement substring existence/count queries with binary search.
- **Kasai's LCP Array** — given a suffix array, derive the LCP array in linear time and use it to find the longest repeated substring.
- **Distinct Substring Counting** — compute the number of distinct substrings using SA + LCP rather than enumerating all substrings explicitly.

### Challenge
- **From SA to FM-Index Intuition** — explain how sorted suffix order leads to the Burrows-Wheeler Transform and why that enables compressed substring search.

---

*See also:* [[Suffix Trees]], [[Compressed Tries and Radix Trees]], [[Tries and Prefix Trees]], [[Ternary Search Trees]] | Cross-wiki links

## Supporting Chunks
### Supporting Chunks
- [[chunk-ds-014 Suffix arrays replace suffix trees with less space]]
- [[chunk-ds-033 Suffix arrays plus LCP match suffix tree power in less space]]
- [[chunk-ds-130 SA-IS builds suffix arrays in On time]]

## References
- [[CS Data Structures/Sources/Sources Index|Sources Index]]

## References

- [[CS Data Structures/Sources/Sources Index]]
- [[CS Data Structures/CS Data Structures Book Reading Spine]]
