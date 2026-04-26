---
tags: [cs-algorithms, raw]
source_type: textbook-chapter
source_title: "Fast Fourier Transform and Polynomial Multiplication"
authors: [Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein]
year: 2022
---

## Summary

The Fast Fourier Transform (FFT) computes the Discrete Fourier Transform (DFT) of a sequence of n values in O(n log n) time, down from the naive O(n²). The DFT evaluates a polynomial of degree n−1 at the n-th roots of unity (e^(2πik/n) for k = 0, …, n−1). FFT exploits the symmetry and periodicity of roots of unity through a divide-and-conquer strategy: split the polynomial into even-indexed and odd-indexed coefficients, recursively compute the DFT of each half, then combine results using the "butterfly" operation. The primary application is polynomial multiplication: to multiply two polynomials of degree n, (1) evaluate both at 2n points using FFT (O(n log n)), (2) multiply the point values element-wise (O(n)), and (3) interpolate back to coefficient form using inverse FFT (O(n log n)). This reduces polynomial multiplication from O(n²) to O(n log n). The inverse FFT is computed by the same algorithm with conjugated roots of unity and a 1/n scaling factor. The Number Theoretic Transform (NTT) replaces complex roots of unity with primitive roots modulo a prime, performing the entire computation in modular arithmetic without floating-point errors—essential for exact integer arithmetic and competitive programming. The Cooley-Tukey algorithm (1965) is the most common FFT variant, requiring n to be a power of 2 (achieved by zero-padding). Split-radix and mixed-radix variants handle other sizes. Applications extend far beyond polynomials: signal processing (frequency analysis, filtering), image processing (JPEG compression uses the related DCT), audio processing (spectral analysis), and big integer multiplication (Schönhage-Strassen algorithm achieves O(n log n log log n) for n-digit multiplication via FFT).

## Key Claims

1. FFT computes the DFT in O(n log n) time by exploiting the recursive structure of roots of unity, reducing the naive O(n²) matrix-vector multiplication.
2. Polynomial multiplication in O(n log n) via FFT is achieved by the evaluate-multiply-interpolate paradigm: forward FFT, pointwise multiplication, and inverse FFT.
3. The butterfly operation combines results from even and odd subproblems using the twiddle factor ω^k, exploiting the identity ω^(k+n/2) = −ω^k for n-th roots of unity.
4. NTT replaces complex arithmetic with modular arithmetic, eliminating floating-point precision issues while maintaining O(n log n) complexity for exact computation.
5. FFT-based multiplication underlies the fastest known algorithms for big integer arithmetic, including the Schönhage-Strassen O(n log n log log n) algorithm.

## Atomic Facts

1. The DFT of a sequence (a₀, …, a_{n−1}) produces (A₀, …, A_{n−1}) where Aₖ = Σⱼ aⱼ·ω^(jk) and ω = e^(2πi/n) is the principal n-th root of unity.
2. The Cooley-Tukey algorithm splits the DFT of size n into two DFTs of size n/2 using even/odd index decomposition: A(ω^k) = A_even(ω^(2k)) + ω^k·A_odd(ω^(2k)).
3. The inverse DFT uses the same structure with ω replaced by ω⁻¹ = e^(−2πi/n) and divides each output by n, since the DFT matrix is unitary up to scaling.
4. For NTT with prime p, a primitive n-th root of unity g satisfies g^n ≡ 1 (mod p) and g^k ≢ 1 (mod p) for 0 < k < n; common choices include p = 998244353 with g = 3.
5. Zero-padding to the next power of 2 ensures the input size is compatible with the radix-2 Cooley-Tukey algorithm; the result is valid up to the original degree.
6. The convolution theorem states that pointwise multiplication in the frequency domain corresponds to convolution in the time domain: DFT(a * b) = DFT(a) · DFT(b).

## Significance

The FFT is widely considered one of the most important algorithms of the 20th century (named as such by IEEE Computing). Its impact spans virtually every field of engineering and science: digital signal processing relies on it for spectral analysis and filtering; medical imaging uses it in CT and MRI reconstruction; telecommunications uses it in OFDM modulation (WiFi, 4G/5G); and scientific computing uses it for solving partial differential equations. In computer science, FFT-based polynomial multiplication is a foundational technique enabling faster algorithms for string matching (via convolution), big integer multiplication, and computational algebra. The NTT variant is essential in modern cryptography (lattice-based cryptosystems like Kyber/CRYSTALS-Dilithium used in post-quantum standards).

## Chunks Extracted

chunk-algo-193 through chunk-algo-196
