---
id: tpl-csos-query
type: template
tags:
  - csos
  - template
  - query
---
# Query Template

> **Usage:** Duplicate for each analytical question about KB coverage or content.
> Rename to `QnA - <topic>.md`. Keep under `_queries/`.

```yaml
---
tags:
  - csos
  - query
up: "[[QnA System Roadmap]]"
---
```

## Purpose

What question does this query answer? What decision does it support?

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual approach below.

```dataview
TABLE field1, field2
FROM "CS Operating Systems/_chunks"
WHERE type = "chunk"
SORT topic ASC
```

## Manual Search Fallback

Obsidian built-in search (`Ctrl+Shift+F`):

```
path:"CS Operating Systems/_chunks" topic: <domain>
```

## Current Status

Manual table maintained here until Dataview is installed.

| Item | Status |
|------|--------|
| Example | pending |
