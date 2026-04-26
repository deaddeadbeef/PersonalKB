---
tags: [pl, chunk, erlang, fault-tolerance]
up: "[[Erlang and Elixir – Language Profile]]"
---

# Erlang Let It Crash and Nine Nines

Erlang was designed at Ericsson for telephone switches that must never stop. Its approach to reliability is radically different from every other mainstream language.

## The Nine Nines Claim

AXD301 ATM switch achieved 99.9999999% uptime (nine nines = 31ms downtime/year). This wasn't through defensive programming – it was through acceptance of failure.

## Let It Crash Philosophy

Instead of preventing all crashes, Erlang assumes crashes will happen and builds recovery into the runtime:

```erlang
%% Supervisor restart strategy
init([]) ->
    {ok, {{one_for_one, 5, 10},
        [{worker1, {my_module, start_link, []}, permanent, 5000, worker, [my_module]},
         {worker2, {other_module, start_link, []}, permanent, 5000, worker, [other_module]}
        ]}}.
%% If worker1 crashes, only worker1 restarts
%% If it crashes 5 times in 10 seconds, the supervisor itself restarts
```

### Supervision Tree Structure
```
       Application

          |
    Top Supervisor
     /    |     \
  Sup1   Sup2   Worker3
  / \     |
W1  W2   W4
```

Each supervisor manages its children. If a child crashes, the supervisor decides: restart it, restart all siblings, or escalate to its own supervisor.

## Why This Works

### Process Isolation
Each Erlang process has:
- **Own heap:** No shared memory between processes
- **Own GC:** Garbage collection per process (no global GC pauses)
- **Own mailbox:** Communication only via message passing
- **Tiny overhead:** ~300 bytes per process, millions of processes possible

If one process crashes, no other process is affected – like having millions of microservices in one VM.

### Hot Code Loading
Erlang can update running code without stopping the system:
```erlang
%% Two versions of a module can run simultaneously
%% Old processes finish with old code
%% New processes start with new code
```

This enables zero-downtime deployments – critical for telecom switches.

## Real-World Scale
- **WhatsApp:** 2 million connections per server (Erlang/FreeBSD)
- **Discord:** Elixir handles millions of concurrent users
- **RabbitMQ:** Message broker handling billions of messages
- **Ericsson:** 50% of world's telecom traffic touches Erlang

## Key Insight
Erlang proves that the "make illegal states unrepresentable" approach (Rust, Haskell) isn't the only path to reliability. Erlang's approach: "crashes are inevitable, so build recovery into the system architecture." Both approaches work – for different problem domains.

## References
→ [[Sources Index]]
