---
tags: [pl, chunk, concurrency, stm]
up: "[[Software Transactional Memory]]"
---

# STM Why Only Haskell Got It Right

Software Transactional Memory (STM) treats memory operations like database transactions. It's elegant in theory but only Haskell uses it successfully.

## How STM Works

\\\haskell
-- Haskell STM: atomic, composable transactions
transfer :: TVar Int -> TVar Int -> Int -> STM ()
transfer from to amount = do
    fromBal <- readTVar from
    when (fromBal < amount) retry  -- Block until condition is met
    writeTVar from (fromBal - amount)
    writeTVar to =<< ((+ amount) <\$> readTVar to)

-- Compose transactions!
atomically $ do
    transfer accountA accountB 100
    transfer accountB accountC 50
-- Either both transfers happen or neither does
\\\

## Why STM Requires Purity

STM works by optimistically executing a transaction and rolling back if there's a conflict. This REQUIRES that the transaction has no observable side effects:

- **Haskell:** The type system guarantees STM transactions are pure (can't do IO)
- **Clojure:** STM refs enforce transaction semantics but can't prevent all side effects
- **Other languages:** Can't guarantee purity, so STM is unreliable

\\\haskell
-- This is a TYPE ERROR in Haskell:
transfer from to amount = do
    putStrLn "Transferring..."  -- IO in STM? COMPILE ERROR
    -- Can't print in a transaction because it might be retried!
\\\

## STM Attempts in Other Languages

| Language | Implementation | Status |
|----------|---------------|--------|
| Haskell | Built-in (GHC.Conc) | Production-ready, widely used |
| Clojure | core (refs, dosync) | Works but less principled |
| Scala | ScalaSTM | Experimental, limited adoption |
| C++ | tm_atomic (proposal) | Never standardized |
| Java | Multiverse, DeuceSTM | Research only |
| Python | N/A | Not feasible (GIL, no purity) |

## The Composability Advantage

The killer feature of STM: transactions COMPOSE. With locks:
\\\
// Transfer with locks - DEADLOCK PRONE
lock(accountA);
lock(accountB);  // What if another thread locked B then A?
\\\

With STM: just combine transactions. The runtime handles conflicts.

## Why STM Didn't Go Mainstream

1. **Requires purity:** Most languages can't guarantee side-effect-free transactions
2. **Performance overhead:** Optimistic concurrency adds retry overhead
3. **Conceptual gap:** Developers understand locks better than transactions
4. **Alternatives exist:** Channels (Go), ownership (Rust), actors (Erlang) solve the same problems

## Key Insight
STM is the most elegant concurrency model in theory but requires language-level support for purity to work correctly. Haskell's type system (IO monad separation) makes it the only language where STM is reliable. For other languages, channels (Go) and ownership (Rust) provide practical alternatives without requiring purity.

## References
→ [[Sources Index]]
