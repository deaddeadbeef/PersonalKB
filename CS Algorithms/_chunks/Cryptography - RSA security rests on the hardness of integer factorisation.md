---
id: chunk-csa-017
type: chunk
source: "[[Cormen 2013 - Algorithms Unlocked]]"
source_loc: "Chapter 8"
topic: "cryptography"
claim: "RSA security rests on the hardness of factoring a large semiprime n=pq — easy to multiply, infeasible to factor at key sizes"
confidence: verified
supports:
  - "[[RSA Algorithm]]"
  - "[[Cryptography Foundations]]"
tags:
  - csa
  - csa/cryptography
  - chunk
up: "[[CS Algorithms]]"
---
# Cryptography — RSA security rests on the hardness of integer factorisation

## Context

RSA: choose large primes p and q; n = pq. The public key (n, e) is broadcast; the private key (n, d) is kept secret, where d is the modular inverse of e mod φ(n) = (p−1)(q−1). Encryption: c = mᵉ mod n. Decryption: m = cᵈ mod n. An attacker who can factor n recovers p, q, hence φ(n), hence d. For a 500-digit n, even testing 2500 candidate divisors per second for the lifetime of the universe would not find the factors. Modern RSA uses 2048-bit (roughly 617-digit) moduli. Note: quantum algorithms (Shor's algorithm) would break RSA — motivation for post-quantum cryptography.

## Why It Matters

RSA is the most widely deployed public-key cryptosystem and the basis of HTTPS certificate exchange. Understanding *why* it is secure (and the caveats) is essential for practitioners. The factoring hardness assumption is also a vivid example of asymmetric computational difficulty — multiplication is fast (O(n²) digit-wise); factoring is believed exponential.

## QnA Seeds

- Q: What mathematical problem is RSA's security based on?
- Q: How does an attacker break RSA if they can factor n?
- Q: Why are quantum computers a threat to RSA?
