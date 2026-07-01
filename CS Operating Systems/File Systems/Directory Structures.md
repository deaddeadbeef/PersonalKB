---
tags:
  - csos
  - csos/filesystems
confidence: verified
freshness: stable
up: "[[File Systems Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Directory Structures

## 🎯 Intuition
**The Core Idea:** A **directory** is a special file that maps names to metadata or inode numbers, letting the OS organise a flat inode namespace into a usable hierarchy.
**Analogy:** A directory is like a library card catalog that maps book titles to shelf locations, so users look up names instead of memorising storage identifiers.
**Why It Matters:** Without directories, users and programs would need to remember inode numbers directly, making storage management and navigation impractical.

## ⚙️ Core Mechanics
### Hierarchical Directories
UNIX introduced the rooted directory tree in 1969. Every file has a **path** from the root (`/`) through zero or more directory levels to the file name.

```
/
├── etc/
│   ├── passwd
│   └── fstab
├── home/
│   └── alice/
│       └── notes.txt
└── var/
    └── log/
        └── syslog
```

### Directory Entries
In ext4, a directory entry records:
- **inode number** — index into the inode table
- **name** — variable-length filename
- **file type** — stored with features such as `dir_index`

The inode stores the main metadata; the directory entry stores the name-to-inode mapping.

### Special Directories
- `.` — current directory
- `..` — parent directory
- A **mount point** grafts another file system's root onto a directory in the current tree

## 🔬 Deep Dive
### Hard Links
A hard link is a second directory entry pointing to the same inode. The inode keeps a **reference count**. Each `unlink()` decrements that count, and the inode is freed only when the count reaches zero. Hard links cannot span file systems and cannot point to directories, which helps prevent cycles in the directory graph.

### Symbolic Links
A symbolic link is a special file containing a path string. When the OS resolves the symlink, it redirects to that target path. Symlinks can span file systems, can point to directories, and can become **dangling** if the target is deleted.

### Why the Distinction Matters
Hard links create another name for the same inode, while symlinks create an indirection through a stored path. That difference explains why hard links affect reference counts and survive renames within the same file system, whereas symlinks are more flexible but easier to break.

## 🏋️ Practice
### Warm-Up
File X has link count = 3. What happens after two `unlink()` calls?

### Core Problems
Why can't hard links point to directories?

### Challenge
Suppose `link` is a symlink to `/home/alice/data`, and Alice deletes `data`. What happens when a program later reads through `link`?

## Supporting Chunks

- [[File Systems - Directory trees impose hierarchy on flat storage via name-to-inode mappings]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 4.