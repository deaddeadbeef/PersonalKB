---
tags:
  - csos
  - csos/security
confidence: verified
up: "[[Security Overview]]"
tier-coverage:
  - intuition
  - core
  - deep-dive
  - practice
---
# Authentication and Protection

**Authentication** is the process of verifying that a claimed identity is genuine — establishing *who* is making a request — before access control policies decide *what* they can do.

## 🎯 Intuition
**The Core Idea:** Authentication answers "who are you?" before authorisation and access control answer "what can you do?"

**Analogy:** It is like showing your passport at customs before being told which areas you are allowed to enter. First identity is checked; then permissions are applied.

**Why It Matters:** All access control is meaningless if identity can be faked. Strong protection therefore depends on both correct authentication and correct execution domains.

## ⚙️ Core Mechanics
### Authentication Factors

| Factor | Type | Example |
|--------|------|---------|
| Something you know | Knowledge | Password, PIN, security question |
| Something you have | Possession | Hardware token (YubiKey), TOTP app, smart card |
| Something you are | Inherence | Fingerprint, face, iris, voice |

**Multi-factor authentication (MFA)** requires two or more factors from different categories, significantly raising the cost of compromise.

### Password Security
Storing passwords in plaintext is catastrophic on database breach. Best practice:
1. Generate a random **salt** (per-user random value).
2. Hash: `digest = H(salt || password)` using a slow hash (bcrypt, scrypt, Argon2).
3. Store `(salt, digest)`.

On login, recompute the hash with the stored salt and compare. Salts prevent rainbow table attacks; slow hashes raise the cost of brute-force.

### Protection Domains
A **protection domain** is a set of (object, rights) pairs that defines the access environment of a running process. On UNIX, UID + GID determine the domain.

## 🔬 Deep Dive
### Kerberos
A ticket-based authentication protocol for distributed systems:
1. The user authenticates to the **Authentication Server (AS)** and gets a Ticket-Granting Ticket (TGT) encrypted with the user's key.
2. The user presents the TGT to the **Ticket-Granting Server (TGS)** to get a service ticket.
3. The user presents the service ticket to the service — no password travels the network after step 1.

Kerberos is used in Windows Active Directory and Kerberos-enabled UNIX environments.

### Password Storage Design
The stored pair is `(salt, digest)`, not the plaintext password. The salt makes precomputed rainbow tables ineffective, and a slow hash such as bcrypt, scrypt, or Argon2 increases the attacker's cost for each guess.

### Protection Domains and `setuid`
`setuid` binaries run in the file owner's domain. The OS switches domains on `exec()` of a setuid program. This is useful for controlled privilege elevation, but it also means bugs in setuid programs can execute with higher rights than the invoking user normally has.

## 🏋️ Practice
### Warm-Up
- What question does authentication answer, and what separate question does access control answer?
- List the three authentication factor categories and give one example of each.
- Why is MFA stronger than using two methods from the same factor category?

### Core Problems
- Why is a salt necessary even when the system already uses a strong hash function?
- A database stores `(salt, digest)` for each user. Explain how login verification works without storing the plaintext password.
- Trace the Kerberos flow when a user accesses a file server. Identify where the AS, TGS, TGT, and service ticket appear.

### Challenge
- A setuid-root program has a buffer overflow. What is the security impact, and why is it more dangerous than the same bug in an unprivileged program?
- Compare a password-only login system with an MFA system that uses a password plus hardware token. Explain how the threat model changes.
- Suppose an attacker steals a password database hashed with fast unsalted hashes. Explain how salts and slow hashes would have changed the attacker's options.

## Supporting Chunks

- [[Security - Authentication verifies identity before granting access using passwords biometrics or tokens]]

## References

See [[CS Operating Systems/Sources/Sources Index#Tanenbaum 2015|Sources Index]]. Chapter 9.
