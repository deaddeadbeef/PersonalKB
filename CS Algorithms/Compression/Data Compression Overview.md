---
tags:
  - csa
  - csa/compression
confidence: verified
freshness: stable
up: "[[CS Algorithms]]"
---
# Data Compression Overview

Data compression reduces the number of bits needed to represent information. This page covers lossless compression only — perfect reconstruction guaranteed.

---

## Why Compression Is Possible

Digital data is often redundant:

1. **Structural redundancy**: ASCII uses 8 bits per character but standard text characters only need 7 (the high bit is always 0).
2. **Statistical redundancy**: in English text, 'e' appears ~13% of the time; 'z' ~0.07%. A fixed-length code (e.g., 8 bits for every character) wastes bits on rare characters.

Variable-length codes assign short bit-strings to frequent characters and long bit-strings to rare characters, reducing average bits per character.

---

## Lossless vs Lossy

| Type | Property | Examples |
|------|----------|---------|
| **Lossless** | Perfect reconstruction | Huffman (text), LZW (GIF), DEFLATE (gzip, ZIP) |
| **Lossy** | Some fidelity lost | MP3 (audio), JPEG (image), H.264 (video) |

This page covers lossless only.

---

## Prefix-Free Codes

For variable-length codes to be **uniquely decodable**, no codeword may be a prefix of another — the **prefix-free** property.

Represented as a **binary tree**: leaves = symbols; root-to-leaf path = codeword (0 = left branch, 1 = right branch).

**Cost of a code** = Σ fᵢ · lᵢ, where fᵢ = frequency of symbol i, lᵢ = codeword length. This is the expected number of bits per symbol.

The optimal prefix-free code for a given frequency distribution is produced by [[Huffman Coding]].

---

## Run-Length Encoding (Fax Compression)

Black-and-white document images consist of long runs of the same colour. Instead of encoding each pixel, encode `(colour, run-length)` pairs. The ITU fax standard uses specific codes tuned to typical document statistics. Highly effective for documents; poor on photographs with frequent colour changes.

---

## LZW Compression

LZW (Lempel-Ziv-Welch) is a **dictionary-based** scheme that builds a shared codebook on the fly:

1. Both encoder and decoder start with the same initial dictionary (e.g., all single characters).
2. The encoder repeatedly finds the longest current-dictionary match in the input, outputs its code, and adds the match extended by one character to the dictionary.
3. The decoder, receiving codes, reconstructs the same dictionary updates — no explicit dictionary transmission needed.

Effective on repetitive data (source code, genomic sequences). Used in GIF images and the Unix `compress` utility. Roughly linear time.

See [[Compression - LZW builds a shared codebook dynamically requiring no transmitted dictionary]].

---

## Comparison of Approaches

| Method | Approach | Best for |
|--------|----------|---------|
| Huffman | Statistical; fixed frequency table | Known-distribution text |
| LZW | Adaptive dictionary; single pass | Repetitive streams |
| RLE | Run-length pairs | Binary images, long runs |
| DEFLATE | LZ77 + Huffman | General-purpose (gzip, ZIP, PNG) |

---

## Supporting Chunks

- [[Compression - Huffman coding builds the optimal prefix-free code with a greedy merge]]
- [[Compression - LZW builds a shared codebook dynamically requiring no transmitted dictionary]]
- [[Compression - Run-length encoding encodes same-symbol runs as count-symbol pairs]]

## References

See [[CS Algorithms/Sources/Sources Index#Cormen 2013|Sources Index]]. Chapter 9. See [[Huffman Coding]] for the full algorithm. See [[Run-Length Encoding]] for the run-based scheme. See [[LZW Compression]] for the dictionary-based approach.
