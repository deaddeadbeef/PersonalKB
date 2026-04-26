---
tags: [pl, chunk, gc, latency]
up: "[[Garbage Collection Strategies]]"
---

# GC Pause Time Engineering Low-Latency Collectors

Modern garbage collectors have dramatically reduced pause times, changing the calculus of "GC vs manual" memory management.

## Pause Time Evolution

| Collector | Language | Max Pause | Target |
|-----------|---------|-----------|--------|
| Go GC | Go | < 500µs | Web services |
| ZGC | Java 15+ | < 1ms | Large heaps |
| Shenandoah | Java | < 10ms | Low-latency |
| G1GC | Java (default) | ~200ms target | General purpose |
| Erlang per-process GC | Erlang | < 1ms per process | Soft real-time |
| Python GC | Python | Unpredictable | N/A |

## Key Insight
GC technology has advanced to the point where pause times are negligible for most applications.

## References
→ [[Sources Index]]
