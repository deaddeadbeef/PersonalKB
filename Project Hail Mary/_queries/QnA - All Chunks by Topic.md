---
tags:
  - phm
  - query
up: "[[QnA System Roadmap]]"
---
# QnA — All Chunks by Topic

## Purpose

List all chunk notes grouped by topic. Useful for browsing the evidence base or checking coverage of a specific subject area.

## Dataview Query (Optional)

> [!info] Requires the Dataview plugin. If not installed, use the manual search below.

```dataview
TABLE claim, confidence, source
FROM "Project Hail Mary/_chunks"
SORT topic ASC, confidence ASC
```

## Manual Search Fallback

Use Obsidian's built-in search (`Ctrl+Shift+F`):

**All chunks:**
```
path:"Project Hail Mary/_chunks"
```

**Filter by topic** (replace `Propulsion` with your target):
```
path:"Project Hail Mary/_chunks" Propulsion
```

**Current topics in use:** Astrophage, Astronomy, Propulsion, Xenobiology, Xenolinguistics, Ethics.

## Tips

- Chunk filenames are prefixed by topic (e.g., `Propulsion - ...`), so even file-list browsing shows grouping.
- The `supports` field in each chunk links to the wiki note it provides evidence for.
