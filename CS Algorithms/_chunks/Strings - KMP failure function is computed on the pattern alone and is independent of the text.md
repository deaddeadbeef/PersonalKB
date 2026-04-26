---
id: chunk-csa-047
type: chunk
source: "[[CP Algorithms - Online Reference]]"
source_loc: "KMP String Matching article"
topic: "strings"
claim: "KMP's failure function (prefix function) is computed entirely from the pattern and requires no knowledge of the text, separating pattern preprocessing from text scanning"
confidence: verified
supports:
  - "[[String Matching - KMP]]"
tags:
  - csa
  - csa/strings
  - chunk
up: "[[CS Algorithms]]"
---
# Strings — KMP failure function is computed on the pattern alone and is independent of the text

## Context

KMP preprocessing computes the **failure function** π[1..m] purely from the pattern P — the text T is not consulted during this phase. π[k] is the length of the longest proper prefix of P[1..k] that is also a suffix of P[1..k]. The computation runs in Θ(m) time, independent of the text length n.

**Why this separation matters**:
1. **Reuse**: for a fixed pattern P, the failure function is computed once and can then be applied to any number of texts. The Θ(m) preprocessing cost is amortised over all texts searched.
2. **Streaming**: since the text is scanned strictly left-to-right (never revisiting a character), KMP can operate on a data stream — useful when the text is too large to fit in memory.
3. **Clarity of the time bound**: the total Θ(n+m) bound decomposes cleanly — Θ(m) for pattern preprocessing, Θ(n) for the text scan. The text scan never re-examines any character because the failure function encodes exactly how much of the partial match can be retained on a mismatch.

**Contrast with naïve search**: naïve matching restarts the pattern comparison from scratch on every mismatch, potentially re-examining text characters. KMP's failure function pre-computes the longest safe restart position, so each text character is examined at most twice overall.

## Why It Matters

Understanding that the failure function depends only on the pattern — not the text — is essential for correctly implementing KMP and for understanding its time complexity. It is also the conceptual key to extending KMP to other problems, such as finding all occurrences of a pattern in a circular string or computing the period of a string.

## QnA Seeds

- Q: Why can KMP's failure function be computed without looking at the text?
- Q: How does the separation of preprocessing and matching phases give KMP its Θ(n+m) bound?
- Q: Why can KMP operate on a data stream but naïve string matching cannot?
- Q: What does π[k] encode, and how is it used during the matching phase?
