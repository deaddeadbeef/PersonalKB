---
tags:
  - csa
  - csa/study
  - csa/compression
up: "[[Algorithms Study Index]]"
confidence: verified
freshness: stable
tier-coverage: [practice]
---
# Data Compression — Review Drill

Active-recall drill covering lossless compression algorithms: run-length encoding, Huffman coding, and LZW.

**Canon pages:** [[Data Compression Overview]] · [[Huffman Coding]] · [[Run-Length Encoding]] · [[LZW Compression]]

---

## How to Use

For each coding algorithm, try to describe the encode and decode procedures, state the complexity, and identify when it is effective vs ineffective before checking the canonical page.

---

## Core Recall

**Compression Fundamentals**

Q: What is the difference between lossless and lossy compression?
A: Lossless compression recovers the exact original data on decompression. Lossy compression discards some information, reducing file size at the cost of exactness. Lossless is required for text, executables, and data; lossy is used for images, audio, and video where minor quality loss is acceptable.

Q: What is a variable-length code?
A: A code where different symbols are assigned codewords of different lengths — shorter codewords for more frequent symbols, longer for rarer ones. Enables average-length compression below the fixed-length floor.

Q: What is a prefix-free code?
A: A code where no codeword is a prefix of another. This property enables unambiguous decoding without separators — scanning bits left to right, the first complete codeword boundary is unambiguous.

Q: What structure enables efficient decoding of prefix-free codes?
A: A binary trie (prefix tree): left branch = 0, right branch = 1. Each leaf is a symbol. Decoding: traverse the trie bit by bit; when you reach a leaf, emit the symbol and restart from the root.

---

**Run-Length Encoding (RLE)**

Q: Describe the RLE compression scheme.
A: Replace each run of consecutive identical symbols with a (count, symbol) pair. E.g., "AAAABBBBC" → "(4,A)(4,B)(1,C)".

Q: When is RLE most effective? When is it ineffective?
A: Effective: long runs of the same symbol (e.g., black-and-white fax images, sparse bitmaps, mostly-zero arrays). Ineffective: data with no or short runs — the output (count + symbol) may be *larger* than the input. The expected run length must exceed the overhead for RLE to be beneficial.

Q: What is RLE's compression ratio in the best and worst cases?
A: Best case: a single run of n identical symbols compresses to $O(1)$ tokens — ratio approaches n. Worst case: alternating distinct symbols (ABABABAB…) expands the data by a factor of 2 (each symbol becomes a 2-element pair).

---

**Huffman Coding**

Q: What does Huffman coding optimise?
A: Among all prefix-free codes, Huffman coding produces the one with minimum expected codeword length. It is optimal for symbol-by-symbol coding given a known symbol probability distribution.

Q: Describe the Huffman tree construction algorithm.
A: 1. Create a leaf node for each symbol with weight = frequency. 2. Insert all nodes into a min-heap. 3. Repeat n−1 times: extract the two minimum-weight nodes, create a parent node with weight = sum of children's weights, insert the parent. 4. The remaining node is the root. Left child = 0, right child = 1 (or vice versa). 

Q: What is the time complexity of building a Huffman tree?
A: $\Theta(n \lg n)$ — n−1 merge operations, each costing $O(\lg n)$ for the heap operations.

Q: What limitation means Huffman coding is not universally optimal?
A: Huffman is optimal for *symbol-by-symbol* codes — it assigns one codeword per input symbol. If the true entropy is non-integer (e.g., a symbol with probability 1/3 needs 1.58 bits), Huffman must round up to an integer number of bits. Arithmetic coding can approach the entropy limit more closely.

Q: What is adaptive Huffman coding and what problem does it solve?
A: Adaptive Huffman coding updates the Huffman tree as symbols are processed, without a pre-transmitted frequency table. This enables single-pass encoding (encoder and decoder build the same tree from the data stream in lock-step), at the cost of more complex update logic.

Q: Why does Huffman coding require a two-pass approach in the standard (non-adaptive) form?
A: Pass 1: scan the data to compute symbol frequencies. Pass 2: encode using the Huffman tree built from those frequencies. The frequency table (or the tree) must be transmitted with the compressed data so the decoder can reconstruct the same tree.

---

**LZW Compression**

Q: What does LZW stand for and what type of coding does it use?
A: Lempel-Ziv-Welch. LZW uses a *dictionary* (codebook) that maps variable-length input strings to fixed-length codewords, building the dictionary adaptively from the data stream.

Q: How does LZW compression work?
A: 1. Initialise the dictionary with all single-character strings. 2. Read input characters; find the longest dictionary match W. 3. Output the code for W. 4. Add the string W + (next character) to the dictionary. 5. Restart from the next character. The dictionary grows dynamically and is never transmitted.

Q: How does LZW decompression work without receiving the dictionary?
A: The decoder initialises the same single-character dictionary and reconstructs entries as it decodes: upon receiving a code, it decodes the string, then adds to its dictionary the previous decoded string + first character of the current decoded string. This mirrors the encoder's dictionary construction exactly.

Q: What is the significance of LZW's patent history for the PNG image format?
A: LZW was patented by Unisys. GIF images use LZW compression and required royalty payments. PNG was designed to use the DEFLATE algorithm (LZ77 + Huffman) instead, providing similar compression with no patent encumbrance. This illustrates how IP constraints can drive algorithm adoption decisions.

---

## Compare and Contrast

**RLE vs Huffman vs LZW**

| Property | RLE | Huffman | LZW |
|----------|-----|---------|-----|
| Technique | Run counting | Frequency-based VLC | Adaptive dictionary |
| Best for | Long runs (faxes, bitmaps) | Skewed symbol distribution | Natural language, general text |
| Worst case | Alternating symbols (expands) | Uniform distribution (no gain) | Short files (dictionary overhead) |
| Requires pre-scan | No | Yes (to build frequency table) | No (adaptive) |
| Transmitted codebook | No | Yes (or tree structure) | No |
| Adaptive | N/A | No (standard); Yes (adaptive Huffman) | Yes |
| Standard usage | Fax (CCITT), BMP | JPEG (DC coefficients), zlib | GIF, early PDF |

**Huffman vs Arithmetic Coding**

| Aspect | Huffman | Arithmetic Coding |
|--------|---------|------------------|
| Optimality | Optimal per-symbol | Approaches entropy limit |
| Handles fractional bits | No (rounds up) | Yes |
| Complexity | Simpler | More complex |
| Patent issues | No | Some implementations patented |

**LZW vs LZ77**

| | LZW | LZ77 |
|--|-----|------|
| Dictionary type | Growing explicit table | Sliding window (past data = implicit dict) |
| Patent history | Patented (Unisys) | Expired; used in DEFLATE (PNG, gzip) |
| Dictionary transmission | Not needed | Not needed |
| Typical use | GIF | gzip, PNG (DEFLATE) |

---

## Common Mistakes

1. **RLE on high-entropy data** — applying RLE to data with no repeated runs inflates the output. Always check expected run distribution before choosing RLE.

2. **Huffman optimality scope** — Huffman is optimal *among prefix-free symbol-by-symbol codes*. It is not universally optimal — arithmetic coding can do better by exploiting fractional bit allocations.

3. **LZW two-pass misconception** — LZW is single-pass in *both* encoder and decoder. Neither sends the dictionary. Students sometimes confuse this with Huffman's two-pass requirement.

4. **Adaptive Huffman complexity** — adaptive Huffman avoids the two-pass requirement but requires maintaining a valid Huffman tree dynamically. The tree-update algorithm (Vitter's algorithm) is non-trivial to implement correctly.

5. **Prefix-free vs uniquely decodable** — prefix-free codes are a strict subset of uniquely decodable codes. All prefix-free codes are uniquely decodable, but the converse is not true. In practice, prefix-free codes are preferred because they enable on-the-fly (streaming) decoding.

---

## Links Back

- [[Data Compression Overview]] — lossless vs lossy, variable-length codes, prefix-free codes
- [[Huffman Coding]] — greedy optimal prefix-free code construction, $\Theta(n \lg n)$ build time
- [[Run-Length Encoding]] — count-symbol pairs, when to use, worst-case expansion
- [[LZW Compression]] — adaptive dictionary, single-pass encoding/decoding, patent history

## References

- [[CS Algorithms/CS Algorithms]]
- [[CS Algorithms/Sources/Sources Index]]
