---
id: chunk-csa-016
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 7"
topic: "strings"
claim: "KMP precomputes a failure function in Theta(m) so that pattern mismatches shift to the longest matching proper prefix-suffix, enabling Theta(n+m) total matching"
confidence: verified
supports:
  - "[[String Matching - KMP]]"
tags:
  - csa
  - csa/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Strings — KMP failure function enables Theta(n+m) string matching

## Context

The failure function π[k] = length of the longest proper prefix of P[1..k] that is also a suffix of P[1..k]. Computing π takes Θ(m) time. During matching: maintain position j in pattern P alongside position i in text T. When P[j+1] ≠ T[i], instead of resetting j to 0 (naïve), set j = π[j], preserving all partial matches. This ensures we never re-examine text characters, giving Θ(n) for the matching phase. Total Θ(n+m). The naïve algorithm is Θ(nm) in the worst case (e.g., text = "aaa…a", pattern = "aaa…b").

## Why It Matters

KMP is the archetypal linear-time string matching algorithm. Its insight — that partial matches encode useful information that should not be discarded — is a principle that recurs in other efficient pattern matching algorithms (Rabin-Karp, Boyer-Moore, Aho-Corasick). Understanding the failure function is the key prerequisite.

## QnA Seeds

- Q: What does the failure function π[k] represent?
- Q: How does KMP avoid re-examining text characters?
- Q: What is the worst-case input for naïve string matching?
