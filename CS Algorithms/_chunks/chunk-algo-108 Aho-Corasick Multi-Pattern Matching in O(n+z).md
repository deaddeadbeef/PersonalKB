---
id: chunk-algo-108
type: chunk
source: "[[raw-algo-017]]"
source_loc: "String Matching Algorithms - Key Claims"
topic: "strings"
claim: "Aho-Corasick builds a finite automaton from k patterns of total length m in O(m) time, then searches text of length n in O(n+z) time where z is the number of matches, providing optimal multi-pattern matching."
confidence: verified
supports:
  - "[[String Matching - Aho-Corasick]]"
tags:
  - cs-algorithms
  - cs-algorithms/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Aho-Corasick Multi-Pattern Matching in O(n+z)

## Context

The automaton has at most m+1 states, constructed via a trie augmented with BFS-based failure links analogous to KMP's failure function. Each text character triggers a single state transition in O(1), and output links report all matching patterns. For 10,000 patterns totaling 500,000 characters, the automaton fits in approximately 4 MB. The O(n+z) time is optimal—every character must be read and every match reported.

## Why It Matters

Aho-Corasick is the standard algorithm for simultaneous multi-pattern search, used in antivirus scanners, network intrusion detection (deep packet inspection), and the Unix fgrep command.

## QnA Seeds

- Q: How does Aho-Corasick achieve O(n+z) multi-pattern matching?
- Q: What is the maximum state count for patterns of total length m?
- Q: How are Aho-Corasick failure links analogous to KMP's failure function?