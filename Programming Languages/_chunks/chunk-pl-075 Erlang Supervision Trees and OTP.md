---
tags: [chunk, programming-languages, erlang-supervision]
source: "[[raw-pl-026]]"
---

# chunk-pl-075 Erlang Supervision Trees and OTP

OTP (Open Telecom Platform) provides patterns for fault-tolerant systems:

**GenServer:** Generic server pattern. Receive messages, maintain state, reply to callers. Handles: synchronous calls, asynchronous casts, info messages. The most common OTP behavior.

**Supervisor:** Monitors child processes. When a child crashes, the supervisor restarts it. Strategies:
- one_for_one: Restart only the crashed child
- one_for_all: Restart all children
- est_for_one: Restart crashed child and all children started after it

**Supervision trees:** Supervisors supervise other supervisors, forming a tree. Top-level crash restarts the subsystem. System-level crash restarts the application. This recursive fault isolation is unique to BEAM.

**Application:** Top-level OTP construct. Bundles a supervision tree with configuration. Start/stop applications at runtime.

**ETS (Erlang Term Storage):** In-memory key-value store shared between processes. Concurrent reads, controlled writes. No serialization needed — stores Erlang terms directly.

The philosophy: build systems that heal themselves. Individual components will fail; the system architecture ensures recovery. "Let it crash" is not carelessness — it's engineering for resilience.
