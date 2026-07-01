---
tags:
  - csa
  - csa/cryptography
confidence: verified
freshness: stable
up: "[[Cryptography Overview]]"
tier-coverage: [intuition, core, deep-dive, practice]
---
# Random Number Generation

> **Cryptographic security depends on unpredictable randomness — pseudorandom bit generators stretch a short secret seed into a long keystream that appears random.**

## 🎯 Intuition
**The Core Idea:** A pseudorandom bit generator (PRBG) takes a short, secret seed and deterministically expands it into a long bitstream indistinguishable from true randomness by any efficient observer.
**Analogy:** Random number generation is like the quality of a lock's combination — even the strongest safe is useless if the combination is "1234". Randomness is the entropy behind every cryptographic key.
**Why It Matters:** Every key, nonce, and initialisation vector in cryptography depends on high-quality randomness. Weak randomness is the single most common cause of real-world cryptographic failures.

---

## ⚙️ Core Mechanics
### How PRBGs Work
1. **Seed**: start with a short, high-entropy secret (e.g., 256 bits from a hardware entropy source).
2. **Stretch**: the PRBG deterministically expands the seed into a long pseudorandom bitstream.
3. **Use**: XOR the bitstream with plaintext (stream cipher mode), or use segments as keys, nonces, and IVs.
4. **Security guarantee**: no efficient algorithm can distinguish the output from truly random bits without knowing the seed.

### Pseudocode
N/A — conceptual page; PRBGs are implementation-specific (e.g., AES-CTR-DRBG, ChaCha20).

### Complexity

| Operation | Cost |
|-----------|------|
| Seed generation | Hardware-dependent (entropy collection) |
| PRBG expansion | $O(n)$ for n output bits (fast symmetric operations) |
| XOR with plaintext | $O(n)$ |

### Key Facts
- The one-time pad achieves perfect secrecy **only** with a truly random key as long as the message
- PRBGs resolve this by stretching a short seed into a long keystream — only the seed must be kept secret
- Seed secrecy is paramount: if the seed is compromised, the entire output stream is compromised
- The security of a cryptosystem depends as much on the quality of randomness as on the mathematical hardness of the algorithm
- PRBGs are complementary to hybrid encryption: PRBG stretches a secret, hybrid encryption exchanges a secret

---

## 🔬 Deep Dive
### Why Randomness Matters
The one-time pad achieves perfect secrecy **only** when the key is truly random — a uniformly distributed bitstring of the same length as the message. If an adversary can predict any part of the key, the information-theoretic guarantee collapses. The same principle extends to any cryptographic key material: a key that is biased or guessable reduces the effective search space an attacker must explore.

### Why Poor Randomness Undermines Security
If the seed is:
- **too short** — brute-force search over all possible seeds becomes feasible
- **biased or predictable** — the adversary narrows the search space dramatically
- **reused across sessions** — two ciphertexts XOR'd together cancel the keystream, directly exposing the plaintexts

A mathematically correct algorithm provides no practical security if its randomness source is weak.

### PRBG vs Hybrid Encryption
Two distinct mechanisms work together in practice:
- **PRBG**: takes a short secret *seed* and *stretches* it into a long pseudorandom bitstream. Resolves the one-time pad's impractical key-length requirement.
- **Hybrid encryption**: solves the *key-distribution* problem. RSA transmits a session key; AES encrypts the payload.

These are complementary: PRBG is about *stretching* a secret into a keystream; hybrid encryption is about *exchanging* a session key so both parties share it securely.

### Edge Cases and Pitfalls
- Using a timestamp as a seed: trivially predictable, reduces key space to seconds in a time window
- Using `rand()` from a standard library: not cryptographically secure — use `/dev/urandom` or `CryptGenRandom`
- Insufficient entropy at boot time: embedded devices and VMs may have weak entropy pools at startup
- Nonce reuse in stream ciphers: catastrophic — XOR of two ciphertexts reveals plaintext relationships

### Real-World Usage
- **TLS session keys**: generated from PRBG seeded by OS entropy
- **SSH key generation**: relies on high-quality randomness for key pair security
- **Cryptocurrency wallets**: private keys derived from random seeds — weak randomness = stolen funds
- **IV/nonce generation**: every AES-GCM encryption needs a unique, unpredictable nonce

---

## 🏋️ Practice
### Warm-Up (5 min)
1. Why can't you use `time()` as a cryptographic seed?
2. What happens if two messages are encrypted with the same keystream?

### Core Problems
1. **Seed entropy calculation**: If a PRBG seed is 40 bits, how many brute-force attempts are needed to recover it? Is this secure?
2. **Keystream reuse attack**: Given two ciphertexts C₁ = P₁ ⊕ K and C₂ = P₂ ⊕ K (same keystream K), show how to recover information about P₁ and P₂.
3. **PRBG vs true randomness**: Explain why a PRBG with a 256-bit seed provides computationally equivalent security to a 256-bit true random key for practical purposes.

### Challenge
**Distinguisher game**: Describe a formal experiment to test whether a PRBG is cryptographically secure (the distinguishing advantage game). What does it mean for the advantage to be negligible?

---

*See also:* [[Cryptography Foundations]], [[RSA Algorithm]], [[CS Data Structures]]

## Supporting Chunks

### Supporting Chunks

- [[Cryptography - Pseudorandom bit generation from a short seed approximates the security of a one-time pad]]
- [[Cryptography - PRNG security requires a high-entropy seed not a low-entropy value such as a timestamp]]

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Cormen 2013]], Chapter 8. See [[CS Algorithms/Sources/Sources Index#MIT OpenCourseWare 6.006|MIT OCW 6.006]], Lecture 14. See [[Cryptography Foundations]] for the broader cryptographic context and [[RSA Algorithm]] for the public-key mechanism used in hybrid encryption to exchange session keys.

## References

- [[CS Algorithms/Sources/Sources Index]]
- [[CS Algorithms/CS Algorithms Book Reading Spine]]
