---
tags: [pl, chunk, error-handling, let-it-crash]
up: "[[Panic and Recovery]]"
---

# Let It Crash vs Make Illegal States Unrepresentable

Two opposing philosophies for building reliable software – both successful in different domains.

## Make Illegal States Unrepresentable (Rust, Haskell, OCaml)

Prevent bugs by making them impossible to express:
\\\ust
// State machine where invalid transitions don't compile
enum ConnectionState {
    Disconnected,
    Connecting { attempt: u32 },
    Connected { session: Session },
}

// Can only send data in Connected state
impl ConnectionState {
    fn send(&self, data: &[u8]) -> Result<(), Error> {
        match self {
            Connected { session } => session.write(data),
            _ => Err(Error::NotConnected),
            // Or better: use typestate to prevent this at compile time
        }
    }
}
\\\

**Philosophy:** If the program compiles, it's probably correct.
**Best for:** Systems programming, financial software, safety-critical systems.

## Let It Crash (Erlang, Elixir)

Accept that crashes will happen and build recovery into the architecture:
\\\rlang
%% Worker that might crash
handle_call({process, Data}, _From, State) ->
    Result = dangerous_operation(Data),  % Might crash!
    {reply, Result, State}.

%% Supervisor that recovers
init([]) ->
    {ok, {{one_for_one, 5, 60},
        [{worker, {my_worker, start_link, []}, permanent, 5000, worker, []}]}}.
%% If worker crashes, supervisor restarts it within 5 seconds
%% If it crashes 5 times in 60 seconds, escalate
\\\

**Philosophy:** Crashes are inevitable; design for recovery, not prevention.
**Best for:** Distributed systems, messaging, telecom, long-running services.

## Comparison

| Property | Illegal States | Let It Crash |
|----------|---------------|-------------|
| Bug prevention | At compile time | At runtime (supervision) |
| Recovery | Not needed if states are impossible | Built into architecture |
| Complexity | In the type system | In the supervision tree |
| Failure mode | Won't compile | Crashes and recovers |
| Learning curve | Types and proofs | Architecture patterns |
| Domain fit | Correctness-critical | Availability-critical |

## Can You Combine Them?

Yes! The best systems use both:
- **Rust + supervision:** Use types to prevent most bugs, but add supervision for the ones that slip through (network failures, hardware errors)
- **Elixir + types:** Elixir is adding gradual types to catch some bugs at compile time while maintaining let-it-crash for runtime resilience

## Key Insight
These aren't competing philosophies – they address different failure modes. Type safety prevents logic bugs. Supervision handles environmental failures (network, disk, OOM). The safest systems use both: Rust's type system for correctness + a supervisor/orchestrator for resilience.

## References
→ [[Sources Index]]
