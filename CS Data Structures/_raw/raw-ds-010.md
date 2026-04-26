---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Tries and String Indexing"
authors: [Robert Sedgewick]
year: 2011
up: "[[Sources Index]]"
---

# Tries and String Indexing

## Summary

Tries store strings character-by-character along tree edges enabling O(m) lookup independent of n. Compressed tries merge single-child chains reducing nodes from O(total chars) to O(n). Ternary search trees use three-way branching for trie speed with BST space. Suffix trees/arrays index all suffixes for O(m) substring search.

## Key Claims

1. Trie lookup is O(m) regardless of number of stored keys
2. Compressed tries reduce space from O(total chars) to O(n) nodes
3. TSTs achieve trie speed with BST-level space usage
4. Suffix trees enable O(m) substring search
5. Suffix arrays replace suffix trees with 3-5x less space

## Atomic Facts

1. Trie: from retrieval (Fredkin, 1960)
2. Patricia: Practical Algorithm To Retrieve Information Coded In Alphanumeric
3. TST: Bentley and Sedgewick, 1997
4. Suffix tree construction: O(n) via Ukkonen's algorithm
5. Suffix array space: 4n-8n bytes vs suffix tree ~20n bytes
6. SA-IS: O(n) suffix array construction

## Significance

String data structures enable efficient text processing that underpins search engines, genome analysis, and data compression.

## Chunks Extracted

*Pending*
