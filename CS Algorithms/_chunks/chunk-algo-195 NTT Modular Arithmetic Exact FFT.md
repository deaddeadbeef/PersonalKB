---
id: chunk-csa-195
type: chunk
source: "[[Cormen 2022 - Fast Fourier Transform]]"
source_loc: "NTT"
topic: "transforms"
claim: "NTT replaces complex roots of unity with primitive roots modulo a prime, performing exact O(n log n) computation without floating-point errors"
confidence: verified
supports:
  - "[[NTT]]"
  - "[[FFT]]"
tags:
  - csa
  - csa/transforms
  - chunk
up: "[[CS Algorithms]]"
---
# Transforms — NTT uses modular arithmetic for exact FFT computation

## Context

The Number Theoretic Transform (NTT) replaces complex roots of unity e^(2*pi*i/n) with primitive n-th roots of unity g modulo a prime p, where g^n = 1 (mod p) and g^k != 1 for 0 < k < n. Common choice: p = 998244353, g = 3. The entire FFT computation proceeds in modular arithmetic, eliminating floating-point precision issues. NTT is essential for exact integer arithmetic in competitive programming and underlies modern post-quantum cryptography (lattice-based schemes like Kyber/CRYSTALS-Dilithium).

## Why It Matters

NTT solves the critical practical problem of floating-point errors in FFT, making it essential for exact computation in competitive programming, big integer arithmetic, and post-quantum cryptography.

## QnA Seeds

- Q: What problem does NTT solve that standard FFT has?
- Q: What are common NTT prime and primitive root choices?
- Q: How is NTT used in post-quantum cryptography?
