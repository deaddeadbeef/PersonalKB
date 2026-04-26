---
id: chunk-csa-018
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 8"
topic: "cryptography"
claim: "Hybrid encryption uses public-key cryptography only to exchange a symmetric session key, then switches to fast symmetric encryption for bulk data"
confidence: verified
supports:
  - "[[Cryptography Foundations]]"
  - "[[RSA Algorithm]]"
tags:
  - csa
  - csa/cryptography
  - chunk
up: "[[CS Algorithms]]"
---
# Cryptography — Hybrid encryption combines public-key exchange with symmetric bulk encryption

## Context

Public-key encryption (RSA) is slow — modular exponentiation on large integers. Symmetric encryption (AES) is fast but requires both parties to share a secret key beforehand. Hybrid encryption combines the best of both: use RSA (or Diffie-Hellman) to securely transmit a randomly generated symmetric session key; then use that session key with AES for all actual data. This is exactly what HTTPS/TLS does. Each session gets a fresh key, limiting exposure if a key is compromised.

## Why It Matters

Hybrid encryption is the real-world deployment pattern for every major secure communication system. Understanding this architecture explains why both RSA and AES are covered in a cryptography curriculum — neither alone solves the practical problem. It also explains forward secrecy: each session's key is independent, so compromising one session key doesn't expose others.

## QnA Seeds

- Q: Why don't we just use RSA to encrypt all data directly?
- Q: What is the role of RSA versus AES in HTTPS?
- Q: What is forward secrecy and how does it relate to hybrid encryption?
