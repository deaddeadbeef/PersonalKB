---
tags: [cs-ds, raw]
source_type: textbook_chapter
source_title: "Hash Tables Theory and Practice"
authors: [Pat Morin]
year: 2013
up: "[[Sources Index]]"
---

# Hash Tables — Theory and Practice

## Summary

Hash tables map keys to indices via hash functions achieving expected O(1) operations. Chaining uses linked lists per slot. Open addressing probes for empty slots. Load factor alpha determines performance. Resizing maintains amortized O(1).

## Key Claims

1. Hash tables achieve expected O(1) for search, insert, and delete
2. Load factor alpha directly determines collision frequency
3. Chaining supports arbitrary load factors; open addressing degrades above 70-80%
4. Linear probing causes clustering but has excellent cache behavior
5. Resizing rehashes all entries in O(n), amortized to O(1)

## Atomic Facts

1. Division method: h(k) = k mod m; m should be prime
2. Multiplication method: h(k) = floor(m * (k*A mod 1))
3. Python dict uses open addressing with perturbation
4. Java HashMap uses chaining with tree conversion at bucket size 8
5. Robin Hood hashing reduces probe length variance
6. Tombstones needed for deletion in open addressing

## Significance

Hash tables provide the fastest average-case access of any general-purpose data structure and are the most widely used structure in practice.

## Chunks Extracted

*Pending*
