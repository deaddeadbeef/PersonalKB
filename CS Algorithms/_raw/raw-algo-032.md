---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Suffix Arrays, Suffix Trees, and String Indexing"
authors: [Dan Gusfield]
year: 1997
---

## Summary

Suffix trees and suffix arrays are powerful data structures for indexing all suffixes of a text string, enabling a wide range of efficient string operations. A suffix tree for a string of length n is a compressed trie of all n suffixes, built in O(n) time using Ukkonen's online algorithm (1995). Each leaf represents a suffix, each edge is labeled with a substring, and no two edges from the same node start with the same character. The key property is that any substring of the text corresponds to a path prefix from the root, enabling O(m) substring search (where m is the pattern length) by simply walking down the tree. Suffix trees also solve the longest common substring (LCS) problem in O(n + m) for two strings by building a generalized suffix tree and finding the deepest internal node with leaves from both strings. A suffix array is a space-efficient alternative: it stores the starting positions of all suffixes sorted lexicographically. Construction takes O(n log n) with the prefix-doubling algorithm (Kärkkäinen-Sanders DC3 achieves O(n)) and requires only O(n) space versus the suffix tree's O(n) pointers with large constants. The LCP (Longest Common Prefix) array, storing the length of the longest common prefix between consecutive suffixes in sorted order, is built in O(n) using Kasai's algorithm and restores much of the suffix tree's functionality. Together, the suffix array and LCP array enable O(m log n) pattern matching (improved to O(m + log n) with additional structures), longest repeated substring, and many other string queries. Applications span bioinformatics (genome assembly, sequence alignment), data compression (BWT for bzip2), plagiarism detection, and information retrieval.

## Key Claims

1. Suffix trees enable O(m) substring search in a text of length n after O(n) construction time, making them the theoretically optimal indexing structure for exact pattern matching.
2. Ukkonen's algorithm constructs suffix trees online (left to right) in O(n) time using three key tricks: implicit extensions, suffix links, and the observation that "once a leaf, always a leaf."
3. Suffix arrays provide equivalent functionality to suffix trees with significantly less memory (4–8 bytes per character vs 20+ for suffix trees), making them practical for large texts.
4. The LCP array combined with a suffix array enables O(m + log n) pattern matching via binary search enhanced with LCP information, approaching suffix tree query performance.
5. The Burrows-Wheeler Transform (BWT), derivable from the suffix array, is the foundation of modern compressed text indexes (FM-index) that support pattern matching in space close to the text's entropy.

## Atomic Facts

1. A suffix tree for a string of length n has exactly n leaves and at most n−1 internal nodes, with each edge labeled by a substring represented as a (start, end) index pair.
2. Ukkonen's algorithm extends the suffix tree one character at a time; suffix links connect internal nodes to enable O(1) amortized transitions between extension points.
3. The DC3 (Difference Cover modulo 3) algorithm constructs suffix arrays in O(n) time by recursively sorting ⅔ of the suffixes and merging with the remaining ⅓.
4. Kasai's algorithm computes the LCP array in O(n) time by exploiting the property that LCP values for lexicographically adjacent suffixes decrease by at most 1 when moving to the next text position.
5. The BWT permutes the text such that characters with similar contexts are clustered, enabling run-length encoding and move-to-front coding for compression.
6. Generalized suffix trees index multiple strings simultaneously, enabling multi-string queries like finding the longest substring common to k out of n strings.

## Significance

Suffix trees and arrays are among the most powerful string processing tools in computer science. In bioinformatics, they underpin genome assembly tools (handling billions of base pairs), sequence alignment (finding homologous regions), and repeat detection. In data compression, the BWT derived from suffix arrays is the basis of bzip2 and forms the core of compressed full-text indexes used in bioinformatics tools like Bowtie and BWA for read mapping. In search engines and text editors, suffix-based structures enable near-instant substring search across massive document collections. The theoretical elegance of O(n) construction and O(m) query, combined with practical importance, makes suffix structures a pinnacle of algorithm engineering.

## Chunks Extracted

chunk-algo-165 through chunk-algo-168
