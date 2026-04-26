---
tags: [raw, programming-languages, erlang-elixir]
source: "Programming Erlang (Armstrong), Elixir in Action (Juric), BEAM documentation"
created: 2025-07-25
---

# raw-pl-026: Erlang/Elixir and the BEAM Ecosystem

## The Telecom Origins

Erlang was designed at Ericsson in 1986 for telephone switches that needed: 99.999% uptime (five nines = ~5 minutes downtime per year), no scheduled maintenance windows, and handling millions of concurrent calls. These requirements produced a unique language and runtime.

## BEAM VM Architecture

The BEAM (Bogdan/Bjorn's Erlang Abstract Machine) is unlike any other VM:

**Lightweight processes:** 2KB initial heap, scheduled by the VM (not OS). A single BEAM node can run millions of processes. Each process has its own heap — garbage collection is per-process, so no global GC pauses. This is why Erlang achieves soft real-time guarantees.

**Preemptive scheduling:** BEAM tracks reduction counts (function calls) and preempts processes after a fixed number. This prevents any single process from monopolizing the scheduler — unlike Go's cooperative scheduling (before 1.14) where a tight loop could starve other goroutines.

**Distribution:** BEAM nodes can cluster. Processes send messages to processes on other nodes transparently. Erlang distribution is built into the runtime — not a library.

**Hot code swapping:** Load new module versions while the system runs. Old processes finish on the old code; new messages are handled by the new code. Essential for telecom: you can't take a phone switch down for a software update.

## The OTP Framework

OTP (Open Telecom Platform) provides patterns for building fault-tolerant systems:
- **GenServer:** Generic server pattern (receive messages, maintain state)
- **Supervisor:** Monitors child processes, restarts them on crash
- **Application:** Top-level supervision tree for an entire application
- **ETS:** In-memory term storage (like an embedded key-value store)

## Elixir's Additions

Jose Valim (2011) created Elixir to bring modern developer ergonomics to BEAM:
- Ruby-inspired syntax (cleaner than Erlang's Prolog-derived syntax)
- Hygienic macros (metaprogramming for DSLs)
- Pipe operator: data |> transform() |> filter() |> output()
- Mix build tool + Hex package manager
- Phoenix web framework (fastest in benchmarks)
- LiveView: real-time UI without JavaScript

## Real-World Usage

WhatsApp: 2 billion users, ~50 engineers, Erlang backend. Discord: Elixir for real-time message fanout. Heroku: Erlang for routing infrastructure. Pinterest: Elixir for notification systems. The BEAM excels where: massive concurrency, fault tolerance, and low latency matter more than single-thread throughput.
