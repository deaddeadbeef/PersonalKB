---
id: chunk-csa-037
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 8"
topic: "cryptography"
claim: "Simple substitution ciphers such as Caesar's cipher are broken by frequency analysis because natural-language character distributions survive the substitution, motivating the development of stronger cryptography"
confidence: verified
supports:
  - "[[Cryptography Foundations]]"
tags:
  - csa
  - csa/cryptography
  - chunk
up: "[[CS Algorithms]]"
---
# Cryptography — Substitution ciphers are vulnerable to frequency analysis, motivating stronger cryptography

## Context

Cormen opens Chapter 8 by surveying the historical weakness of simple ciphers. A **Caesar cipher** shifts every letter by a fixed offset (e.g., A→D, B→E). A general **substitution cipher** maps each letter to a fixed but arbitrary other letter. Both share a critical flaw: the substitution is letter-by-letter, so the *frequency distribution* of characters is preserved in the ciphertext. English uses 'e' roughly 13% of the time and 'z' roughly 0.07%; an attacker can count ciphertext character frequencies to recover the substitution mapping without knowing the key.

This attack — **frequency analysis** — requires no computational power beyond counting letters and matching distributions. It exposes the fundamental weakness of any system where each plaintext symbol maps deterministically to the same ciphertext symbol.

## Why It Matters

The failure of substitution ciphers provides the motivating contrast for the rest of Chapter 8: the one-time pad randomises the mapping per bit, modern symmetric ciphers mix characters across the entire message block, and public-key cryptography solves key distribution entirely. Understanding why frequency analysis works explains why security must come from genuine randomness and mathematical hardness rather than obscured character mappings.

## QnA Seeds

- Q: Why does frequency analysis break a Caesar cipher even without knowing the shift value?
- Q: What property of substitution ciphers makes them vulnerable to frequency analysis?
- Q: How did the failure of substitution ciphers motivate the design of the one-time pad?
