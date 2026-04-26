---
tags:
  - <topic-tag>
  - query
up: "[[QnA System Roadmap]]"
---
# {{Query Title}}

## Purpose

What question or view this query answers.

## Dataview Query (Optional)

> [!info] Requires the Dataview community plugin. If Dataview is not installed, use the manual search fallback below.

```dataview
TABLE claim, confidence, source
FROM "<TOPIC_ROOT>/_chunks"
WHERE topic = "example"
SORT confidence ASC
```

## Manual Search Fallback

Use Obsidian's built-in search (`Ctrl+Shift+F`):

```
path:"<TOPIC_ROOT>/_chunks" tag:#example
```

Adjust the search terms to match your needs.

## Notes

Any caveats or tips for interpreting the results.
