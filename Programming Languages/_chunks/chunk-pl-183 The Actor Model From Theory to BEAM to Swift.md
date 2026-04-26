---
tags: [pl, chunk, concurrency, actor-erlang]
up: "[[The Actor Model]]"
---

# The Actor Model From Theory to BEAM to Swift

The Actor model, proposed by Carl Hewitt in 1973, has found its most successful implementation in Erlang/BEAM and is now being adopted by Swift and Kotlin.

## Actor Model Fundamentals

An actor is a computational entity that:
1. **Receives messages** from a mailbox
2. **Processes one message at a time** (no concurrent access to state)
3. **Can create new actors**
4. **Can send messages to other actors**
5. **Can modify its own state**

No shared memory. No locks. No data races.

## Erlang: The Reference Implementation

\\\rlang
%% Define an actor (process)
counter(Count) ->
    receive
        increment -> counter(Count + 1);
        {get, Caller} -> Caller ! {count, Count}, counter(Count);
        stop -> ok
    end.

%% Spawn and interact
Pid = spawn(fun() -> counter(0) end),
Pid ! increment,
Pid ! increment,
Pid ! {get, self()},
receive {count, N} -> io:format("Count: ~p~n", [N]) end.
\\\

## Swift Actors (Swift 5.5+)

Swift added actors as a first-class language feature:
\\\swift
actor BankAccount {
    var balance: Double = 0
    
    func deposit(_ amount: Double) {
        balance += amount  // Safe: actor-isolated
    }
    
    func getBalance() -> Double {
        return balance
    }
}

// External access is async (enforced by compiler)
let account = BankAccount()
await account.deposit(100)  // Must await - crosses actor boundary
\\\

## Comparison

| Property | Erlang Processes | Swift Actors | Akka Actors (Scala) |
|----------|-----------------|-------------|-------------------|
| Isolation | Complete (own heap) | Compiler-enforced | Convention-based |
| Mailbox | Unbounded, selective receive | Compiler manages | Configurable |
| Distribution | Built-in (nodes) | Not built-in | Akka Cluster |
| Supervision | OTP supervisors | Not built-in | Actor hierarchy |
| Performance | Lightweight (300 bytes) | Lightweight | Moderate |

## The Supervision Advantage

Erlang's killer feature isn't just actors – it's supervision:
\\\
Supervisor (restarts failed children)

   |
   +-- Worker1 (if it crashes, supervisor restarts it)
   +-- Worker2 (independent from Worker1)
   +-- SubSupervisor
        +-- Worker3
        +-- Worker4
\\\

Swift and Kotlin actors lack this – they provide concurrency safety but not fault tolerance.

## Key Insight
The actor model is experiencing a renaissance. Erlang proved it works for decades. Swift made it type-safe. The actor model's advantage over locks: you cannot have a data race because state is never shared. The trade-off: you must design around message passing, which requires a different architectural mindset.

## References
→ [[Sources Index]]
