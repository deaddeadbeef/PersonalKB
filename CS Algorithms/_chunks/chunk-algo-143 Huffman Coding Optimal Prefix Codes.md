---
id: chunk-csa-143
type: chunk
source: "[[Cormen 2022 - Greedy Algorithms]]"
source_loc: "Huffman Coding"
topic: "greedy"
claim: "Huffman coding builds optimal prefix-free binary codes in O(n log n) time by greedily merging the two lowest-frequency symbols"
confidence: verified
supports:
  - "[[Huffman Coding]]"
  - "[[Greedy Algorithms]]"
tags:
  - csa
  - csa/greedy
  - chunk
up: "[[CS Algorithms]]"
---
# Greedy — Huffman coding constructs optimal prefix codes in O(n log n)

## Context

Huffman coding constructs a full binary tree (every internal node has exactly two children) where leaves represent symbols and path lengths represent code lengths. The greedy strategy repeatedly extracts the two lowest-frequency nodes from a min-priority queue, merges them into a new internal node whose frequency is their sum, and inserts the result back. This minimizes the weighted external path length, producing the optimal prefix-free code. The O(n log n) time comes from n − 1 extract-min and insert operations on the priority queue.

## Why It Matters

Huffman coding is one of the most important practical applications of greedy algorithms, forming the basis of data compression in formats like DEFLATE (used in gzip, PNG, and ZIP).

## QnA Seeds

- Q: Why does Huffman coding always produce a full binary tree?
- Q: What data structure drives the O(n log n) complexity of Huffman coding?
- Q: What does Huffman coding minimize and why is that equivalent to optimal compression?
