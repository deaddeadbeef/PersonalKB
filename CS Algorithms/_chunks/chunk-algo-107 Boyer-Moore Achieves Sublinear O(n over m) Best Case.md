---
id: chunk-algo-107
type: chunk
source: "[[raw-algo-017]]"
source_loc: "String Matching Algorithms - Key Claims"
topic: "strings"
claim: "Boyer-Moore scans the pattern right-to-left and combines the bad-character and good-suffix rules, achieving O(n/m) best-case time—for m=100 in n=1,000,000 text, roughly 10,000 comparisons, a 100x speedup over linear scanning."
confidence: verified
supports:
  - "[[String Matching - Boyer-Moore]]"
tags:
  - cs-algorithms
  - cs-algorithms/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Boyer-Moore Achieves Sublinear O(n over m) Best Case

## Context

The bad-character rule shifts the pattern to align the mismatched text character with its rightmost occurrence in the pattern. The good-suffix rule aligns a matching suffix with another occurrence within the pattern. Together these allow skipping up to m characters per mismatch, yielding sublinear O(n/m) best-case comparisons. In practice Boyer-Moore is the fastest single-pattern matcher for natural language text with large alphabets.

## Why It Matters

Boyer-Moore is the most practical string matching algorithm for text editors and grep-like tools. Its sublinear best case demonstrates that not all characters need examination—a counterintuitive result exploiting right-to-left scanning.

## QnA Seeds

- Q: How does Boyer-Moore achieve sublinear O(n/m) matching?
- Q: What are the bad-character and good-suffix rules?
- Q: How many comparisons for m=100, n=1,000,000 in best case?