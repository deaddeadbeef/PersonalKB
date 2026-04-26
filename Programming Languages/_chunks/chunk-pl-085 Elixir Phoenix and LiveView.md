---
tags: [chunk, programming-languages, elixir]
source: "[[raw-pl-026]]"
---

# chunk-pl-085 Elixir Phoenix and LiveView

Elixir (2011, Jose Valim): Modern syntax + powerful macros on BEAM VM.

**Pipe operator:** data |> transform() |> filter() |> output() — left-to-right data flow. Makes data transformation pipelines readable.

**Pattern matching everywhere:** Function heads match on arguments. No if/else chains for dispatch:
```elixir
def factorial(0), do: 1
def factorial(n), do: n * factorial(n - 1)
```

**Macros:** Hygienic, operating on Elixir AST (tuples). quote/unquote for AST manipulation. Powers Phoenix routing, Ecto queries, and test frameworks.

**Phoenix Framework:** High-performance web framework. Handles millions of connections per node. Channels for real-time WebSocket communication.

**LiveView:** Real-time, server-rendered UI without writing JavaScript. Server maintains state; diffs sent over WebSocket. Eliminates the SPA complexity for many use cases. Enables rich interactivity with Elixir-only code.

**Mix + Hex:** Build tool + package manager. Clean, well-designed. mix test, mix format, mix deps.get — consistent tooling.
