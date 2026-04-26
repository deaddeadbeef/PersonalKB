---
tags:
  - csa
  - moc
up: "[[CS Algorithms]]"
---
# Cryptography Overview

Cryptographic algorithms secure communication and data by exploiting mathematical hardness. This domain covers classical ciphers, the one-time pad, public-key cryptography (RSA), pseudorandom generation, and the hybrid encryption model used in practice.

---

## Learn in This Order

1. [[Cryptography Foundations]] — substitution ciphers, frequency analysis, one-time pad, perfect secrecy, symmetric vs asymmetric, hybrid encryption
2. [[Random Number Generation]] — entropy, pseudorandom generators (PRNGs), seed unpredictability, why poor randomness breaks security
3. [[RSA Algorithm]] — public-key cryptosystem, modular exponentiation, primality testing, key generation

---

## In This Domain

| Page | One-line summary |
|------|-----------------|
| [[Cryptography Foundations]] | Classical ciphers; OTP; symmetric vs asymmetric; hybrid encryption model |
| [[Random Number Generation]] | PRNG construction; seed entropy; security implications of weak randomness |
| [[RSA Algorithm]] | Public-key system; factoring hardness; modular arithmetic; primality |

---

## Common Distinctions

| Question | Answer |
|----------|--------|
| Symmetric vs asymmetric? | Symmetric uses one shared secret key (fast). Asymmetric uses a key pair (slow but enables key exchange without a pre-shared secret). Hybrid encryption uses asymmetric to exchange a symmetric session key. |
| PRNG vs true RNG? | True RNGs harvest physical entropy (thermal noise, etc.). PRNGs use a short seed and a deterministic algorithm — secure only if the seed is unpredictable and the generator is cryptographically strong. |
| Perfect secrecy vs semantic security? | Perfect secrecy (OTP): ciphertext leaks zero information. Semantic security: computationally infeasible to distinguish encryptions. Modern systems aim for semantic security. |
| RSA encryption vs signing? | RSA encryption: encrypt with public key, decrypt with private key. Signing: sign with private key, verify with public key. Same mathematical operation, opposite key usage. |

---

## How to Navigate

- **Building intuition first?** Start at [[Cryptography Foundations]] — it explains why naive ciphers fail before introducing the OTP and public-key idea.
- **Understanding RSA?** Read [[Cryptography Foundations]] first, then [[RSA Algorithm]].
- **Security of random numbers?** [[Random Number Generation]] explains why seed quality is the most common practical failure point.

---

## Related Domains

- **[[Complexity Theory Overview]]** — RSA's security rests on the hardness of integer factorisation (an NP-intermediate problem). The P vs NP and NP-hardness discussions underpin all public-key cryptographic assumptions.
- **[[Foundations and Analysis Overview]]** — Modular exponentiation uses fast exponentiation (repeated squaring); asymptotic analysis applies to key-generation and primality-testing algorithms.
