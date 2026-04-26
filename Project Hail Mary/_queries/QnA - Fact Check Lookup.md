---
tags:
  - phm
  - query
up: "[[QnA System Roadmap]]"
---
# QnA — Fact Check Lookup

## Purpose

Look up the confidence level and source for a specific claim. Useful when you want to know whether a statement in the wiki is verified, plausible, or fictional.

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual search below.

```dataview
TABLE claim, confidence, source
FROM "Project Hail Mary/_chunks"
WHERE contains(claim, "radiation")
SORT confidence ASC
```

Replace `"radiation"` with your search term.

## Manual Search Fallback

Use Obsidian's built-in search (`Ctrl+Shift+F`):

**Search for a keyword across all chunks:**
```
path:"Project Hail Mary/_chunks" radiation
```

**Filter by confidence level:**
```
path:"Project Hail Mary/_chunks" confidence: verified
```
```
path:"Project Hail Mary/_chunks" confidence: uncertain
```

## Confidence Levels

| Level | Meaning |
|---|---|
| `verified` | Supported by peer-reviewed evidence or well-established science |
| `plausible` | Consistent with known science but not directly demonstrated |
| `fictional` | The novel's invention, not grounded in reality |
| `policy` | A normative or governance claim, not empirically verifiable |
| `uncertain` | Insufficient evidence to classify; more research needed |

## Tips

- Each chunk's `source` field links back to the raw material with full context.
- Follow the `supports` links to see which wiki notes depend on this evidence.
