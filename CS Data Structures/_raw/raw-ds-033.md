---
tags: [cs-ds, raw]
id: raw-ds-033
source: "Open Data Structures (Morin, Ch. 8)"
up: "[[CS Data Structures]]"
---

# Scapegoat Trees and Weight-Balanced Trees

## Key Ideas
- Scapegoat tree: rebalance by rebuilding subtree around the scapegoat node
- No extra balance info stored per node (unlike AVL or RB)
- Alpha-balanced: every subtree has size ratio between alpha and 1-alpha
- On insert: if tree becomes unbalanced, walk up to find scapegoat, rebuild subtree
- Rebuild: flatten to sorted array, rebuild perfect BST — O(size of subtree)
- Amortized O(log n) insert/delete via potential function argument
- Worst-case single insert: O(n) — but amortized O(log n)
- Weight-balanced trees (BB[alpha]): explicit size fields, rebalance when ratio violated
- Adams' weight-balanced tree: used in Haskell Data.Map and Data.Set
- Advantage: simple invariant, no colors/balance-factors, efficient split/join
- Disadvantage: amortized not worst-case, occasional expensive rebuilds

## When to Choose
- Good for memory-constrained systems (no extra per-node metadata)
- Not suitable for real-time systems requiring worst-case guarantees
- Excellent for functional/persistent implementations
