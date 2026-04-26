---
id: chunk-csa-030
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 8"
topic: "cryptography"
claim: "The one-time pad achieves information-theoretic (perfect) secrecy by XOR-ing plaintext with a random key of equal length, but this key-length requirement makes it impractical at scale"
confidence: verified
supports:
  - "[[Cryptography Foundations]]"
tags:
  - csa
  - csa/cryptography
  - chunk
up: "[[CS Algorithms]]"
---
# Cryptography — The one-time pad achieves perfect secrecy but requires a key as long as the message

## Context

XOR each bit of the plaintext with the corresponding bit of a truly random, never-reused key of the same length. The ciphertext is statistically independent of the plaintext: for any ciphertext, every possible plaintext of the same length is equally likely. An adversary with unlimited computational power gains zero information about the plaintext from the ciphertext alone — this is **perfect secrecy** (Shannon, 1949).

Constraints that must all hold simultaneously:
1. The key must be **truly random** (not pseudo-random).
2. The key must be **as long as the message**.
3. The key must be **used only once** — reuse leaks the XOR of the plaintexts.
4. The key must be **kept secret** and transmitted via a secure channel.

Constraint (4) is the fatal practical problem: securely transmitting a key as long as the message requires a secure channel with the same bandwidth as the data — at which point you could just send the message securely directly.

## Why It Matters

The one-time pad establishes a theoretical ceiling: perfect secrecy is achievable. It also clarifies why real cryptography does not achieve it — practical schemes (AES, RSA) sacrifice information-theoretic security for computational hardness. Understanding this gap separates provable from assumed security.

## QnA Seeds

- Q: What makes the one-time pad "perfectly" secure, and what does that mean precisely?
- Q: Why does reusing the key break the one-time pad's security?
- Q: What is the key distribution problem and why does it make the one-time pad impractical?
