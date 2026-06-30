---
tags:
  - csa
  - csa/study
  - csa/cryptography
up: "[[Algorithms Study Index]]"
confidence: policy
---
# Cryptography — Review Drill

Active-recall drill covering classical ciphers, modern cryptographic primitives, RSA, and randomness security.

**Canon pages:** [[Cryptography Foundations]] · [[RSA Algorithm]] · [[Random Number Generation]]

---

## How to Use

Answer each question without consulting the canonical pages. For security definitions, try to state *why* the property holds before checking the proof or argument.

---

## Core Recall

**Historical Ciphers and One-Time Pad**

Q: What is a substitution cipher and what is its key weakness?
A: A substitution cipher replaces each letter with another (e.g., Caesar cipher shifts by a fixed amount; Vigenère uses a key word). Weakness: letter frequency is preserved. Statistical analysis of ciphertext letter frequencies reveals the substitution mapping — no computational effort needed for short keys.

Q: What is the one-time pad and why does it achieve perfect secrecy?
A: The key is a random string of the same length as the message; ciphertext = message XOR key. Perfect secrecy: every possible plaintext is equally likely given the ciphertext, because the key is uniformly random. An attacker gains zero information from the ciphertext alone.

Q: What practical limitation makes the one-time pad impractical?
A: The key must be: (1) as long as the message, (2) truly random, (3) used only once, and (4) securely transmitted to both parties. Securely transmitting a key as long as the message is at least as hard as securely transmitting the message itself.

---

**Symmetric vs Asymmetric Encryption**

Q: What is the key distribution problem in symmetric encryption?
A: Both parties must share the same secret key. Sharing the key securely over an untrusted channel requires an already-secure channel — a chicken-and-egg problem at scale.

Q: How does hybrid encryption solve the key distribution problem?
A: Use asymmetric (public-key) encryption to securely exchange a short session key, then use symmetric encryption for the bulk of the data. Hybrid encryption gets the security of public-key cryptography with the performance of symmetric encryption.

Q: Name one asymmetric (public-key) cryptosystem and state its security assumption.
A: RSA — security rests on the hardness of factoring large integers. Given the product of two large primes n = p·q, recovering p and q is believed to require super-polynomial time.

---

**RSA Algorithm**

Q: Describe the RSA key generation process.
A: 1. Choose two large primes p and q. 2. Compute n = p·q and φ(n) = (p−1)(q−1). 3. Choose public exponent e with 1 < e < φ(n) and gcd(e, φ(n)) = 1. 4. Compute private exponent d ≡ e⁻¹ (mod φ(n)). 5. Public key: (n, e). Private key: d (keep p, q, φ(n) secret).

Q: How does RSA encryption and decryption work?
A: Encrypt: C = Mᵉ mod n. Decrypt: M = Cᵈ mod n. Correctness follows from Euler's theorem: $M^{e·d}$ ≡ $M^{1 + k·φ(n}$) ≡ M (mod n) for gcd(M, n) = 1.

Q: What is RSA's security assumption, and what algorithm threatens it?
A: Security rests on the hardness of integer factorisation. Shor's algorithm (quantum) factors n in polynomial time — RSA would be broken by a large-scale quantum computer.

Q: What is modular exponentiation and why is it needed in RSA?
A: Computing Mᵉ mod n for large e by squaring and multiplying in modular arithmetic — $O(\lg e)$ multiplications rather than $O(e)$. Without this, RSA would be computationally infeasible for large exponents.

Q: How is primality testing used in RSA key generation?
A: Generating RSA keys requires finding two large primes p and q. Probabilistic primality tests (Miller-Rabin) efficiently certify that a candidate is prime with negligible error probability — deterministic testing of every divisor is infeasible.

---

**Random Number Generation**

Q: What is a Pseudorandom Bit Generator (PRBG)?
A: An algorithm that takes a short, secret, high-entropy seed and expands it into a long pseudorandom bit sequence. The output is computationally indistinguishable from truly random bits by any polynomial-time adversary.

Q: Why is the seed's entropy — not its length — the critical security parameter?
A: A seed generated from a low-entropy source (e.g., a timestamp with millisecond precision) can be exhaustively searched even if it is represented as a 128-bit number. An adversary who knows the seed generation process can enumerate likely seeds and predict the entire output. High entropy means the seed cannot be guessed or searched.

Q: Give a concrete example of how poor PRNG seeding can undermine cryptographic security.
A: Early implementations of SSL seeded the PRNG with the process ID and current time — both low-entropy values with small search spaces. Attackers could enumerate plausible seeds, regenerate the "random" session keys, and decrypt traffic. PRNG quality directly determines cryptographic security quality.

Q: What is the difference between a PRNG and a CSPRNG?
A: A PRNG (pseudorandom number generator) passes statistical tests but may be predictable from its state. A CSPRNG (cryptographically secure PRNG) additionally guarantees: (1) next-bit unpredictability — no polynomial-time adversary can predict the next bit better than chance given all previous bits; (2) state-compromise resistance — even if part of the state is revealed, past outputs remain secure.

---

## Compare and Contrast

**Symmetric vs Asymmetric Encryption**

| Property | Symmetric | Asymmetric (Public-key) |
|----------|-----------|------------------------|
| Keys | One shared key | Key pair: public + private |
| Speed | Fast | Slow (modular exponentiation) |
| Key distribution | Hard (pre-shared secret needed) | Easy (public key can be published) |
| Use case | Bulk data encryption | Key exchange, digital signatures |
| Examples | AES, 3DES | RSA, Diffie-Hellman, ECC |

**Classical Ciphers vs Modern Cryptography**

| | Classical (e.g., substitution) | Modern (e.g., RSA, AES) |
|--|-------------------------------|------------------------|
| Security basis | Obscurity | Computational hardness |
| Broken by | Frequency analysis | Quantum computers (RSA), brute force (AES-128 marginally) |
| Key length | Short (26 possibilities for Caesar) | 2048–4096 bits (RSA) |
| Provable security | No | Conditional on hardness assumptions |

**One-Time Pad vs Stream Cipher**

| | One-Time Pad | Stream Cipher (CSPRNG-based) |
|--|-------------|------------------------------|
| Security | Perfect (information-theoretic) | Computational (breaks if PRNG broken) |
| Key reuse | Never — breaks immediately | Depends; nonce management critical |
| Practicality | Impractical (key = message length) | Practical |
| Proof | Shannon's theorem | Under PRNG security assumption |

---

## Common Mistakes

1. **Key reuse with a one-time pad** — reusing a key reveals the XOR of two plaintexts, completely breaking perfect secrecy. The name "one-time" is definitional.

2. **RSA directly encrypting long messages** — RSA operates on integers modulo n; it can only encrypt messages smaller than n. In practice, RSA encrypts a symmetric session key, not the full message (hybrid encryption).

3. **PRNG seed quality** — using `srand(time(NULL))` or similar low-entropy sources in security-sensitive code is a classic vulnerability. Always use OS-provided entropy sources (`/dev/urandom`, `CryptGenRandom`) for cryptographic seeding.

4. **Confusing PRNG and CSPRNG** — `rand()` in most standard libraries is a PRNG suitable for simulation but not for cryptography. Security applications must use CSPRNGs.

5. **RSA's factorisation assumption** — RSA's security is *conditional* on factorisation being hard. It is widely believed but not proven to be NP-hard. A polynomial factorisation algorithm (classical or quantum at scale) would break RSA.

---

## Links Back

- [[Cryptography Foundations]] — substitution ciphers, one-time pad, symmetric vs asymmetric, hybrid encryption
- [[RSA Algorithm]] — key generation, encryption/decryption, modular exponentiation, primality testing
- [[Random Number Generation]] — PRBG definition, seed entropy, CSPRNG, why poor randomness breaks security

## References
- [[CS Algorithms/Sources/Sources Index|CS Algorithms Sources Index]]
