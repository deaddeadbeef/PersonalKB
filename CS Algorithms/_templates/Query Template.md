---
id: tpl-csa-query
type: template
tags:
  - csa
  - template
  - query
---
# Query Template

> **Usage:** Duplicate for each structured query. Rename to `QnA - <Question or View>.md`.
> Queries track coverage gaps, answer structured questions, and serve as Dataview dashboards.

```yaml
---
tags:
  - csa
  - query
up: "[[QnA System Roadmap]]"
---
```

## Purpose

What question or view this query answers.

## Dataview Query (Optional)

> [!info] Requires the Dataview community plugin. If not installed, use the manual search fallback below.

```dataview
TABLE claim, confidence, source
FROM "CS Algorithms/_chunks"
WHERE topic = "example"
SORT confidence ASC
```

## Manual Search Fallback

Use Obsidian's built-in search (`Ctrl+Shift+F`):

```
path:"CS Algorithms/_chunks" tag:#csa/example
```

## Notes

Any caveats or tips for interpreting the results.
