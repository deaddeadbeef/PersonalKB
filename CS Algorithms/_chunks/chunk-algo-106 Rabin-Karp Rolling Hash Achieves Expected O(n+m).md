---
id: chunk-algo-106
type: chunk
source: "[[raw-algo-017]]"
source_loc: "String Matching Algorithms - Key Claims"
topic: "strings"
claim: "Rabin-Karp computes a rolling hash over m-character windows in O(1) per shift using modular arithmetic, achieving O(n+m) expected time with a prime modulus q reducing false positive rate to approximately m/q per window."
confidence: verified
supports:
  - "[[String Matching - Rabin-Karp]]"
tags:
  - cs-algorithms
  - cs-algorithms/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Rabin-Karp Rolling Hash Achieves Expected O(n+m)

## Context

The rolling hash recurrence updates in O(1) by removing the leftmost character's contribution and adding the rightmost. With prime q ~ 10^9, false positive probability per window is about m/q. For n=10^6 and m=100, expected false positives are ~0.1, making verification negligible. The O(nm) worst case occurs only with pathological hash collisions. Rabin-Karp extends naturally to multi-pattern and 2D pattern matching.

## Why It Matters

Rabin-Karp pioneered the fingerprinting technique in algorithms, influencing plagiarism detection, file synchronization (rsync), and multi-pattern search. Its expected-time guarantee and extensibility make it a versatile complement to KMP.

## QnA Seeds

- Q: How does Rabin-Karp update its hash in O(1) per shift?
- Q: What is the false positive probability with prime q ~ 10^9?
- Q: When does Rabin-Karp's worst case O(nm) actually occur?