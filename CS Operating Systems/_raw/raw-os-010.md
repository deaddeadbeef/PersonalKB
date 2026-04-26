---
tags: [cs-os, raw]
source_type: textbook_chapter
source_title: "File System Interface"
authors: "Andrew S. Tanenbaum, Herbert Bos"
year: 2015
---

# File System Interface

## Summary
The file system interface provides the user-facing abstraction for persistent storage, defining operations on files (open, read, write, seek, close) and the directory structures that organize them. Files can be accessed sequentially, directly (randomly), or through indexed methods, with sequential access being the most common. Directory structures have evolved from flat single-level designs to hierarchical trees and DAG structures that support the organizational complexity of modern computing.

## Key Claims
- A file is the OS's abstraction of persistent, named data—it decouples the logical view of information from the physical details of disk block layout, enabling programs to work with data without knowing storage hardware specifics
- The open() system call is the gateway to file operations: it performs pathname resolution, checks permissions, allocates a file descriptor, and loads metadata into kernel memory—subsequent read/write operations use the file descriptor for efficiency
- Directory structures evolved from single-level (all files in one directory) to tree-structured hierarchies because flat namespaces become unmanageable beyond a few hundred files; the tree structure mirrors human organizational thinking
- A DAG (directed acyclic graph) directory structure extends the tree model by allowing files to appear in multiple directories through hard links or symbolic links, enabling shared access without duplication
- The file descriptor table (per-process), open file table (system-wide), and inode/vnode table (system-wide) form a three-level indirection that enables independent file positions per process while sharing underlying kernel structures

## Atomic Facts
1. The six fundamental file operations are: create (allocate space and directory entry), open (load metadata and return file descriptor), read (copy data from file position to buffer), write (copy data from buffer to file position), seek (reposition the file pointer for random access), and close (release the file descriptor and flush buffers)
2. Sequential access reads or writes file contents in order from beginning to end, advancing the file pointer automatically; this is the access pattern of compilers, text editors, and most data processing programs
3. Direct (random) access allows reading or writing any block of the file by specifying a block number or byte offset; databases rely on direct access to retrieve individual records without scanning the entire file
4. Hard links in Unix create multiple directory entries pointing to the same inode; the file's data is only deleted when the link count reaches zero, which is why "deleting" a file is actually called unlinking
5. Symbolic (soft) links are special files containing a pathname that the OS transparently follows during pathname resolution; unlike hard links, symbolic links can cross filesystem boundaries and can become dangling if the target is deleted
6. The POSIX standard defines a unified file system interface including open(), read(), write(), lseek(), close(), stat(), link(), unlink(), mkdir(), rmdir(), and opendir()/readdir()—this API has remained remarkably stable since its standardization in 1988

## Significance
The file system interface is one of the most enduring abstractions in computing—the open/read/write/close model has survived essentially unchanged for over 50 years. Unix's "everything is a file" philosophy extended this interface to devices, pipes, sockets, and even kernel data structures (/proc), demonstrating the power of a well-designed abstraction that separates interface from implementation.

## Chunks Extracted
*Pending*
