---
tags: [cs-algorithms, raw]
source_type: textbook
source_title: "Hash Tables: Theory and Practice"
authors: "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein"
year: 2009
---

# Hash Tables

## Summary
Hash tables provide expected O(1) time for insert, delete, and lookup operations by mapping keys to array indices via a hash function. The two primary collision resolution strategies are chaining (linked lists at each bucket) and open addressing (probing sequences within the table). Performance depends critically on the load factor α = n/m (items/slots) and the quality of the hash function, with universal hashing providing provable worst-case expected guarantees independent of the input distribution.

## Key Claims
- Under simple uniform hashing assumption with chaining, the expected time for a successful search is Θ(1 + α/2) and for an unsuccessful search is Θ(1 + α), where α is the load factor
- Universal hashing families guarantee that for any pair of distinct keys, the probability of collision is at most 1/m, eliminating adversarial worst-case inputs without requiring randomness in the data
- Open addressing with linear probing suffers from primary clustering but achieves excellent cache performance; with load factor α < 0.75, the expected number of probes is at most 1/(1 − α) ≈ 4 for unsuccessful search
- Perfect hashing achieves O(1) worst-case lookup for static sets using a two-level scheme with O(n) total space, where the second level uses m_j = n_j² slots for n_j keys mapping to slot j
- Cuckoo hashing provides O(1) worst-case lookup and O(1) amortized expected insertion using two hash functions and two tables, with insertion failing (requiring rehash) with probability O(1/n)

## Atomic Facts
1. The birthday paradox implies that with m slots and n insertions, the first collision is expected after approximately √(πm/2) insertions; for m = 365, this is about 23—the classic birthday problem
2. The Carter-Wegman universal hash family h_{a,b}(k) = ((ak + b) mod p) mod m, where p is prime and a ∈ {1,...,p−1}, b ∈ {0,...,p−1}, achieves collision probability exactly ⌈p/m⌉/p ≤ 1/m + 1/p
3. When a hash table's load factor exceeds a threshold (typically 0.75), resizing doubles the table to 2m slots and rehashes all n elements in O(n) time; amortized over n insertions, this adds O(1) per insertion
4. Robin Hood hashing (a variant of linear probing) bounds the maximum probe length to O(log n) with high probability by displacing keys with shorter probe distances, reducing variance in search times
5. MurmurHash3 and xxHash are non-cryptographic hash functions achieving throughput exceeding 5 GB/s on modern CPUs, with 128-bit variants providing collision probability less than 2⁻⁶⁴ for practical input sizes
6. Hopscotch hashing constrains each key to be within H positions of its home bucket (typically H = 32), achieving O(1) worst-case lookup in practice while maintaining high load factors up to 0.9 with neighborhood-based displacement

## Significance
Hash tables are the most widely used data structure in software engineering, underlying dictionaries in Python, HashMap in Java, unordered_map in C++, and objects in JavaScript. The theoretical study of hashing connects probability theory, number theory (universal families), and amortized analysis (dynamic resizing). Perfect hashing demonstrates that O(1) worst-case lookup is achievable, while cuckoo hashing bridges theory and practice with simple, analyzable guarantees. The choice between chaining and open addressing remains a practical engineering decision driven by cache behavior, memory allocation patterns, and expected load factors.

## Chunks Extracted
*Pending*
