---
id: au-ch-08
type: book-chapter
chapter: 8
book: "Algorithms Unlocked"
author: "Thomas H. Cormen"
status: processed
chunk_count: 5
source: "[[Cormen 2013 - Algorithms Unlocked]]"
tags:
  - csa
  - book-chapter
up: "[[Chapter Index]]"
---
# AU — Chapter 08: Foundations of Cryptography

## Summary

Chapter 8 surveys cryptographic algorithms motivated by the practical problem of transmitting sensitive data over a public network. Simple substitution ciphers (such as Caesar's shift) are broken easily by frequency analysis — English character frequencies are non-uniform, so ciphertext letter distributions reveal the key. The **one-time pad** (XOR with a random key as long as the message) achieves perfect secrecy, but requires a secure channel to share a key as large as the data itself — impractical at scale. **Symmetric encryption** (both parties share one secret key) solves the efficiency problem but creates the key-distribution problem. **Public-key cryptography** solves key distribution: each party has a public key (freely shared) and a private key (secret); messages encrypted with the public key can only be decrypted with the private key. The **RSA cryptosystem** builds on number theory — choose large primes p and q, compute n = pq, choose public exponent e coprime to φ(n) = (p−1)(q−1), compute private exponent d via the Extended Euclidean Algorithm such that ed ≡ 1 (mod φ(n)). Encryption: c = mᵉ mod n; decryption: m = cᵈ mod n. Security rests on the hardness of factoring n. Modular exponentiation uses repeated squaring in $O(\lg e)$ multiplications. In practice, **hybrid encryption** uses RSA only to exchange a session key, then switches to fast symmetric encryption (AES) for bulk data. The chapter also covers the need for good randomness: cryptographic keys must be unpredictable, and a **pseudorandom bit generator (PRBG)** can expand a short secret seed into a keystream that serves as a practical substitute for a full-length one-time pad key.

## Key Concepts

| Concept | One-liner |
|---------|-----------|
| Caesar cipher | Letter substitution by fixed offset; broken by frequency analysis |
| One-time pad | XOR with random key; perfect secrecy; key-size = message-size |
| Symmetric encryption | Shared secret key; fast; key distribution problem |
| Public-key cryptography | Public key encrypts; only private key decrypts |
| RSA | Encrypt mᵉ mod n; decrypt cᵈ mod n; security = factoring hardness |
| Extended Euclidean Algorithm | Computes modular inverse d of e mod φ(n) |
| Repeated squaring | Computes mᵉ mod n in $O(\lg e)$ multiplications |
| Hybrid encryption | RSA for session-key exchange; AES for bulk payload |
| Pseudorandom bit generation | PRBG expands a short secret seed into a keystream; seed secrecy substitutes for a full-length one-time pad key |

## Chunk Candidates

- [x] [[Cryptography - Substitution ciphers are vulnerable to frequency analysis motivating stronger cryptography]]
- [x] [[Cryptography - The one-time pad achieves perfect secrecy but requires a key as long as the message]]
- [x] [[Cryptography - RSA security rests on the hardness of integer factorisation]]
- [x] [[Cryptography - Hybrid encryption combines public-key exchange with symmetric bulk encryption]]
- [x] [[Cryptography - Pseudorandom bit generation from a short seed approximates the security of a one-time pad]]

## Wiki Pages Seeded

- [[Cryptography Foundations]] — history, cipher types, symmetric vs asymmetric, hybrid
- [[RSA Algorithm]] — key generation, encrypt/decrypt, modular exponentiation
- [[Random Number Generation]] — pseudorandom bit generation, seed unpredictability, why poor randomness undermines security

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]].
