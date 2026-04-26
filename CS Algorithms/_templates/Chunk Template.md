---
id: tpl-csa-chunk
type: template
tags:
  - csa
  - template
  - chunk
---
# Chunk Template

> **Usage:** Duplicate for each atomic claim. Rename to `<Domain> - <claim summary>.md`.
> One claim per note. The claim should be a complete, standalone, falsifiable statement.

```yaml
---
id: chunk-csa-NNN
type: chunk
source: "[[raw note name]]"
source_loc: ""
topic: ""
claim: ""
confidence: ""
supports:
  - "[[wiki note name]]"
tags:
  - csa
  - chunk
up: "[[CS Algorithms]]"
---
```

Confidence values: `verified` · `plausible` · `fictional` · `policy` · `uncertain`

## Context

Where this claim comes from and what surrounds it in the source material.

## Why It Matters

How this fact or idea connects to the core themes of algorithm study — correctness, efficiency, problem tractability.

## QnA Seeds

Potential questions this chunk can answer:

- Q: ?
- Q: ?
