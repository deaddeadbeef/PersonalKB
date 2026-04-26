---
tags:
  - cs-ds
  - hub
up: "[[CS Data Structures]]"
---

# Tries and String Structures Overview

Strings are the most common non-numeric data type, yet general-purpose search trees and hash tables ignore the internal structure of their keys. **Tries** and related string-specialised structures exploit the fact that strings are sequences of characters, enabling prefix queries, autocomplete, and substring search that would be awkward or impossible with generic containers. This hub covers the family of tree structures designed expressly for string and text operations.

## Tries and Prefix Trees

A **trie** (from "re*trie*val") stores each character of a key along an edge, so that all keys sharing a common prefix share the corresponding path from the root. Lookup, insertion, and deletion run in $O(L)$ time where L is the key length — independent of the number of stored keys. Tries naturally support prefix enumeration ("give me every word starting with *pre-*"), making them ideal for dictionaries, autocomplete engines, and IP routing tables.

## Compressed and Space-Efficient Variants

Standard tries can waste space when long chains of single-child nodes appear. **Compressed tries (Patricia / radix trees)** collapse such chains into single edges labelled with substrings, dramatically reducing node count while preserving $O(L)$ operations. **Ternary search trees** offer a different compromise: each node holds a character and three children (less-than, equal, greater-than), combining the time efficiency of tries with the space economy closer to balanced BSTs.

## Suffix Structures

When the task shifts from prefix lookup to arbitrary substring search, **suffix trees** and **suffix arrays** take centre stage. A suffix tree indexes every suffix of a text in $O(n)$ space and time, enabling $O(L)$ substring queries, longest repeated substring detection, and many bioinformatics applications. Suffix arrays achieve comparable functionality with less overhead and better cache behaviour, often paired with LCP arrays for enhanced queries.

## Mutable String Structures

For applications that require frequent insertions, deletions, and concatenations within large strings — text editors, collaborative editing, and rendering engines — the **rope** data structure replaces flat arrays with balanced binary trees of string fragments, delivering $O(\log n)$ edits without copying entire buffers.

## Pages in This Hub

- [[Tries and Prefix Trees]]
- [[Compressed Tries and Radix Trees]]
- [[Suffix Trees]]
- [[Suffix Arrays]]
- [[Ternary Search Trees]]
- [[Rope Data Structure]]

## Related Hubs

- [[Trees Overview]] — general tree concepts and balancing strategies
- [[Hash-Based Structures Overview]] — hash-based alternatives for string key lookup
- [[Foundational Concepts Overview]] — complexity and memory considerations for string structures