---
tags: [chunk, programming-languages, erlang-elixir]
source: "[[raw-pl-026]]"
---

# chunk-pl-034 BEAM VM and Let It Crash Philosophy

**BEAM architecture:** Lightweight processes (2KB heap), preemptive scheduling (by reduction count), per-process GC (no global pauses), built-in distribution, hot code swapping.

**Let it crash:** Instead of defensive error handling, let processes crash. Supervisors restart them with clean state. Simplifies code: processes handle happy path, supervisors handle failure.

**OTP patterns:** GenServer (generic server), Supervisor (monitors + restarts children), Application (top-level supervision tree), ETS (in-memory term storage).

**Elixir additions:** Modern Ruby-like syntax, hygienic macros, pipe operator (|>), Mix/Hex tooling, Phoenix web framework, LiveView (real-time UI without JavaScript).

**Scale proof:** WhatsApp — 2 billion users, ~50 engineers, Erlang backend. Discord — Elixir for real-time message fanout.

BEAM excels where: massive concurrency + fault tolerance + low latency matter more than single-thread throughput. The design trades peak single-process performance for unmatched system-level resilience.
