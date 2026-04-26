---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Trie Data Structure and Prefix Trees"
authors: [Robert Sedgewick, Kevin Wayne]
year: 2011
---

## Summary

A trie (from "retrieval," pronounced "try") is a tree-based data structure for storing and searching strings, where each node represents a single character and paths from root to nodes spell out prefixes. For an alphabet of size R, each node contains up to R children (one per character) and a value marking whether the node represents the end of a stored key. Insert and search operations both run in O(m) time where m is the length of the key—independent of the number of keys stored—making tries superior to hash tables for prefix-based operations. The key advantage of tries over other data structures is support for prefix queries: finding all keys with a given prefix requires only traversing to the prefix node and collecting all descendants, an operation hash tables cannot perform efficiently. Applications include autocomplete systems (search engines, IDEs), spell checkers (checking if a word exists or suggesting corrections by exploring nearby trie paths), IP routing tables (longest prefix matching), and dictionary implementations in word games. Standard R-way tries can be memory-intensive: each node allocates R pointers regardless of actual children. Compressed tries (Patricia trees, radix trees) address this by collapsing chains of single-child nodes into single edges labeled with substrings, reducing node count dramatically for sparse key sets. A ternary search trie (TST) uses three pointers per node (less, equal, greater) instead of R, providing O(m + log n) search time with much less memory than R-way tries. Space optimization techniques include alphabet reduction, hash-mapped children, and array-of-children compaction. For large-scale string sets, tries enable operations impossible with flat data structures: prefix counting, lexicographic ordering, and longest common prefix computation all become natural tree traversals.

## Key Claims

1. Tries provide O(m) insert and search where m is the key length, with no dependence on the number of stored keys—unlike balanced BSTs which require O(m log n) string comparisons.
2. Prefix queries (find all keys sharing a prefix) are a natural O(p + k) operation in tries (p = prefix length, k = matches), impossible to achieve efficiently with hash tables.
3. Compressed tries (Patricia/radix trees) collapse single-child chains into multi-character edges, reducing space from O(n·R·m) to O(n·m) for n keys of average length m.
4. Ternary search tries balance the memory efficiency of BSTs with the time efficiency of R-way tries, achieving O(m + log n) search with three pointers per node.
5. In IP routing, longest prefix matching on tries determines the most specific route for a destination address, a critical operation in network routers.

## Atomic Facts

1. In an R-way trie with alphabet size R, each node stores an array of R child pointers and optionally a value; null pointers indicate absent characters.
2. Search follows child pointers character by character; reaching a null pointer means the key is absent; reaching the end of the key checks for a stored value.
3. Patricia trees (Practical Algorithm to Retrieve Information Coded in Alphanumeric) were invented by Morrison in 1968 for IP address lookup.
4. Autocomplete works by traversing the trie to the prefix node, then performing DFS/BFS to collect all complete keys in the subtrie, optionally ranked by frequency.
5. The double-array trie implementation uses two arrays (base and check) to represent the trie compactly, achieving the speed of array-based tries with compressed space.
6. Burst tries combine tries with container nodes (small sorted arrays or BSTs at the leaves), adapting their structure to the data distribution for improved cache performance.

## Significance

Tries are the go-to data structure for string-centric problems, offering unique capabilities that no other structure provides as efficiently. Their importance spans from theoretical foundations (compact representations of string sets, connections to automata theory) to critical systems applications (DNS lookup, IP routing, search engine autocomplete, T9 predictive text). Compressed trie variants power text indexing in information retrieval systems, and trie-based structures underlie the implementation of finite automata for regular expression matching. Understanding tries is essential for any engineer working with string processing, networking, or search systems.

## Chunks Extracted

chunk-algo-161 through chunk-algo-164
